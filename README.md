# Chemistry-Note-RAG

自动同步 [AnyayayPlus/Chemistry-Note](https://github.com/AnyayayPlus/Chemistry-Note) 并生成三级聚合的 Markdown 和图片资源，用于 RAG（Retrieval-Augmented Generation）应用。

## 功能特点

- **自动同步**: 通过 GitHub Actions 每日自动拉取最新化学笔记
- **图片归档**: 将所有章节图片存储到 `images/` 目录，按章节分类
- **三级 Markdown 聚合**:
  - **Level 1**: 全局聚合为单个文件
  - **Level 2**: 按章节聚合（11 个文件）
  - **Level 3**: 文件级展开（平铺）

## 目录结构

```
Chemistry-Note-RAG/
├── images/                          # 图片资源
│   ├── 00 说明/
│   ├── 01 原子结构与元素周期律/
│   ├── ...
│   └── 10 化学反应与能量/
├── markdown/
│   ├── Anyayay_Chemistry_Note.md   # 完整汇总（Level 1备份）
│   ├── level1/
│   │   └── 000_all_chemistry.md    # 全局聚合
│   ├── level2/                    # 按章节聚合
│   │   ├── 00_说明.md
│   │   ├── 01_原子结构与元素周期律.md
│   │   └── ...
│   └── level3/                    # 文件级展开
│       ├── 00_说明_贡献者.md
│       ├── 01_原子结构与元素周期律_01_原子结构.md
│       └── ...
├── src/
│   └── chemistry_rag.py           # 核心处理脚本
├── .github/
│   └── workflows/
│       └── sync-chemistry-note.yml  # 自动同步工作流
└── pyproject.toml
```

## 章节结构

本项目包含以下 11 个章节：

| 编号 | 名称 | 文件数 | 图片数 |
|------|------|--------|--------|
| 00 | 说明 | 4 | 2 |
| 01 | 原子结构与元素周期律 | 8 | 19 |
| 02 | 微粒间作用力与物质性质 | 8 | 31 |
| 03 | 分子空间结构与配合物 | 4 | 22 |
| 04 | 有机化学基础 | 10 | 149 |
| 05 | 化学物质基本概念 | 8 | 0 |
| 06 | 元素及其化合物 | 11 | 24 |
| 07 | 化学实验 | 5 | 27 |
| 08 | 化学反应能量与速率 | 3 | 0 |
| 09 | 化学平衡 | 3 | 2 |
| 10 | 化学反应与能量 | 4 | 5 |

## 本地运行

### 环境要求

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) 包管理器

### 安装依赖

```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装 Python 3.12
uv python install 3.12
```

### 运行脚本

```bash
# 第一步：克隆 Chemistry-Note 仓库
git clone --depth 1 https://github.com/AnyayayPlus/Chemistry-Note.git Chemistry-Note

# 第二步：运行处理脚本
uv run src/chemistry_rag.py --source ./Chemistry-Note --output .

# 清理
rm -rf Chemistry-Note
```

## GitHub Actions 自动化

工作流设置如下：

- **定时触发**: 每天 UTC 02:00 (北京时间 10:00)
- **手动触发**: 通过 GitHub 界面的 "Run workflow" 按钮

### 触发条件

- 计划任务: `cron: '0 2 * * *'`
- 手动执行: `workflow_dispatch`

### 工作流步骤

1. 检出本仓库
2. 安装 uv 和 Python 3.14
3. 检出 Chemistry-Note 仓库
4. 运行 RAG 处理脚本
5. 检查并提交变更

## RAG 使用建议

### Level 1 - 全局聚合

适用场景: 需要完整上下文的大模型应用

```python
# 读取单个文件
with open('markdown/level1/000_all_chemistry.md', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Level 2 - 按章节聚合

适用场景: 针对特定章节的检索和问答

```python
import os

# 获取所有章节
chapters = [f for f in os.listdir('markdown/level2') if f.endswith('.md')]

# 按章节检索
for chapter in sorted(chapters):
    with open(f'markdown/level2/{chapter}', 'r', encoding='utf-8') as f:
        content = f.read()
        # 处理章节内容
```

### Level 3 - 文件级展开

适用场景: 精确到原始文件级别的检索

```python
import os

# 获取所有文件
files = os.listdir('markdown/level3')

# 按命名规则搜索
matching_files = [f for f in files if '化学实验' in f]
```

### 图片资源

```markdown
![图片说明](images/06 元素及其化合物/某图片.png)
```

## 贡献

本项目基于 [AnyayayPlus/Chemistry-Note](https://github.com/AnyayayPlus/Chemistry-Note) 构建，所有内容版权归原作者所有。

## 授权

### 代码

`src/`、`.github/workflows/`、`pyproject.toml` 等由本项目开发的代码采用 [MIT License](./LICENSE)。

### 内容

`markdown/`、`images/` 中的化学笔记内容来自 [AnyayayPlus/Chemistry-Note](https://github.com/AnyayayPlus/Chemistry-Note)，原始内容版权归原作者，本项目仅做格式转换和聚合处理，不改变其版权归属。

### 使用建议

- ✅ 个人学习、研究、RAG 应用
- ✅ 非商业性教育用途
- ❌ 商用出版、付费课程（请联系原项目获取授权）
