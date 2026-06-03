import os
import re
import shutil
from pathlib import Path
from typing import List, Tuple, Dict


class ChemistryRAGProcessor:
    """
    Chemistry-Note RAG Processor
    
    Functions:
    1. Extract images to @/images/chapter_name/
    2. Generate three-level markdown aggregation
       - Level 1: Global aggregation into a single file
       - Level 2: Aggregation by chapter (11 files)
       - Level 3: File-level expansion, flat without subdirectories
    """

    def __init__(self, source_dir: str, output_dir: str):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.images_dir = self.output_dir / "images"
        self.markdown_dir = self.output_dir / "markdown"

    def run(self):
        """Execute the complete processing workflow"""
        print(f"[START] Processing Chemistry-Note RAG")
        print(f"   Source: {self.source_dir}")
        print(f"   Output: {self.output_dir}")

        # Create output directories
        self._ensure_dirs()

        # Scan chapter structure
        chapters = self._scan_chapters()
        print(f"   Found {len(chapters)} chapters")

        # 1. Process images
        self._process_images(chapters)

        # 2. Process Level 1: Global aggregation
        self._process_level1(chapters)

        # 3. Process Level 2: Aggregation by chapter
        self._process_level2(chapters)

        # 4. Process Level 3: File-level expansion
        self._process_level3(chapters)

        print(f"[DONE] Processing completed!")

    def _ensure_dirs(self):
        """Ensure output directories exist"""
        self.images_dir.mkdir(parents=True, exist_ok=True)
        self.markdown_dir.mkdir(parents=True, exist_ok=True)
        (self.markdown_dir / "level1").mkdir(exist_ok=True)
        (self.markdown_dir / "level2").mkdir(exist_ok=True)
        (self.markdown_dir / "level3").mkdir(exist_ok=True)

    def _scan_chapters(self) -> List[Dict]:
        """
        Scan chapter structure
        Match format: "XX ChapterName" folders
        Return: [{number, name, path, files}, ...]
        """
        chapters = []
        chapter_pattern = re.compile(r'^(\d{2})\s+(.+)$')

        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory does not exist: {self.source_dir}")

        for item in sorted(self.source_dir.iterdir()):
            if item.is_dir():
                match = chapter_pattern.match(item.name)
                if match:
                    number = match.group(1)
                    name = match.group(2)
                    md_files, image_dirs = self._scan_folder_files(item)

                    chapters.append({
                        'number': number,
                        'name': name,
                        'folder_name': item.name,
                        'path': item,
                        'md_files': md_files,
                        'image_dirs': image_dirs
                    })

        # Sort by number
        chapters.sort(key=lambda x: x['number'])
        return chapters

    def _scan_folder_files(self, folder: Path) -> Tuple[List[Path], List[Path]]:
        """
        Scan markdown files and image directories within a folder
        """
        md_files = []
        image_dirs = []

        for item in folder.iterdir():
            if item.is_file() and item.suffix.lower() == '.md':
                md_files.append(item)
            elif item.is_dir():
                # Check if it's an image directory (images or image)
                if item.name.lower() in ['images', 'image']:
                    image_dirs.append(item)

        # Sort by filename
        md_files.sort(key=lambda x: x.name)
        return md_files, image_dirs

    def _process_images(self, chapters: List[Dict]):
        """Process image copying"""
        print(f"\n[IMAGES] Processing images...")

        for chapter in chapters:
            # Target directory: images/XX ChapterName/
            target_chapter_dir = self.images_dir / chapter['folder_name']
            target_chapter_dir.mkdir(parents=True, exist_ok=True)

            for img_dir in chapter['image_dirs']:
                for img_file in img_dir.iterdir():
                    if img_file.is_file() and self._is_image(img_file):
                        target_path = target_chapter_dir / img_file.name
                        shutil.copy2(img_file, target_path)
                        print(f"   Copy: {img_file.name}")

        print(f"   [OK] Images processed")

    def _is_image(self, path: Path) -> bool:
        """Check if file is an image"""
        image_exts = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg'}
        return path.suffix.lower() in image_exts

    def _process_level1(self, chapters: List[Dict]):
        """
        Level 1: Global aggregation into a single file"""
        print(f"\n[LEVEL 1] Global aggregation...")

        output_file = self.markdown_dir / "level1" / "000_all_chemistry.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Chemistry Note - Full Summary\n\n")
            f.write("---\n\n")

            for chapter in chapters:
                # Add chapter separator
                f.write(f"# Chapter {chapter['number']} {chapter['name']}\n\n")
                f.write(f"Source directory: `{chapter['folder_name']}`\n\n")

                # Merge all markdown files in this chapter
                for md_file in chapter['md_files']:
                    content = self._read_md_file(md_file)
                    f.write(f"## Original file: {md_file.name}\n\n")
                    f.write(content)
                    f.write("\n\n---\n\n")

                f.write("\n\n")

        print(f"   [OK] Output: {output_file}")

        # Extra copy for RAG convenience
        extra_copy = self.markdown_dir / "Anyayay_Chemistry_Note.md"
        shutil.copy2(output_file, extra_copy)
        print(f"   [OK] Extra copy: {extra_copy}")

    def _process_level2(self, chapters: List[Dict]):
        """
        Level 2: Aggregation by chapter"""
        print(f"\n[LEVEL 2] Aggregation by chapter...")

        for chapter in chapters:
            # Filename: {number}_{name}.md
            safe_name = self._sanitize_filename(chapter['name'])
            output_file = self.markdown_dir / "level2" / f"{chapter['number']}_{safe_name}.md"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Chapter {chapter['number']} {chapter['name']}\n\n")
                f.write(f"Source directory: `{chapter['folder_name']}`\n\n")
                f.write("---\n\n")

                for md_file in chapter['md_files']:
                    content = self._read_md_file(md_file)
                    f.write(f"## {md_file.stem}\n\n")
                    f.write(content)
                    f.write("\n\n---\n\n")

            print(f"   [OK] {output_file.name}")

    def _process_level3(self, chapters: List[Dict]):
        """
        Level 3: File-level expansion (flat without subdirectories)"""
        print(f"\n[LEVEL 3] File-level expansion...")

        total_files = 0
        for chapter in chapters:
            for md_file in chapter['md_files']:
                # Naming rule: {number}_{name}_{original_filename}.md
                safe_name = self._sanitize_filename(chapter['name'])
                original_name = self._sanitize_filename(md_file.stem)
                output_name = f"{chapter['number']}_{safe_name}_{original_name}.md"
                output_file = self.markdown_dir / "level3" / output_name

                content = self._read_md_file(md_file)

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"# {md_file.stem}\n\n")
                    f.write(f"Source chapter: Chapter {chapter['number']} {chapter['name']}\n\n")
                    f.write(f"Original file: `{md_file.name}`\n\n")
                    f.write("---\n\n")
                    f.write(content)

                total_files += 1

        print(f"   [OK] Expanded {total_files} files")

    def _read_md_file(self, path: Path) -> str:
        """Read markdown file content"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Try other encodings
            with open(path, 'r', encoding='gbk') as f:
                return f.read()

    def _sanitize_filename(self, name: str) -> str:
        """Replace special characters in filename with underscores"""
        # Replace disallowed characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            name = name.replace(char, '_')
        return name.strip()


def main():
    """Main function - supports command line arguments"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Chemistry-Note RAG processing script"
    )
    parser.add_argument(
        "--source", "-s",
        default="./Chemistry-Note",
        help="Source directory path (default: ./Chemistry-Note)"
    )
    parser.add_argument(
        "--output", "-o",
        default=".",
        help="Output directory path (default: current directory)"
    )

    args = parser.parse_args()

    processor = ChemistryRAGProcessor(args.source, args.output)
    processor.run()


if __name__ == "__main__":
    main()
