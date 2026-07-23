# Chemistry Note - Full Summary

---

# Chapter 00 说明

Source directory: `00 说明`

## Original file: Readme.md

---
description: "Anyayay's Chemistry Note 的使用说明，包括如何浏览、搜索、下载PDF，以及错误反馈方式。"
---

# Readme

![Anyayay's Chemistry Note](/images/Logo.png)

欢迎来到 Anyayay's Chemistry Note！

这是一个基于中国普通高中教科书的化学笔记项目，主要围绕 Bilibili Up主 [@一化儿](https://space.bilibili.com/1526560679/) 的视频展开的，也或许是你见过的 **免费的 最完整的 最真实的** 高中化学笔记，不仅仅是知识点的笔记，也有超多的实战解题技巧，以及我自己总结出来的经验，或一个盲猜技巧，或一个口诀。

## 如何使用？

左侧有目录（移动设备是顶上有一个 Menu 可以展开），可以打开对应章节来查看。

顶部有搜索栏，可以根据关键词来搜索内容，也内置了 AI 搜索功能，会基于本笔记内容来回答你的问题。

## 如何下载 PDF？

1. 顶部的菜单展开后的「下载」可以直接下载当前访问页的 PDF 文件。
2. 点此链接下载全部章节的 PDF 文件合集: [下载 PDF](https://umami.seeridia.top/q/e8e52FUHV)。

## 发现错误？

如果在使用中发现任何问题，欢迎通过 [错误反馈](./错误反馈.md) 来帮助我们改善。我们会在下面的 [反馈者名录](#反馈者名录) 中列出所有帮助反馈问题的朋友。

当然，如果你懒，你也可以直接在对应章节的评论区中直接留言。

如果你希望直接参与完善项目，可以查看 [贡献指南](./贡献指南.md)。

---

> [!NOTE]
> 下面是一个小小的 QQ 群，欢迎加入交流学习，不过目前还没啥人 QwQ
>
> 群号：[1074161116](https://qm.qq.com/q/CljGJy9p8Q)
>
> <img src="./images/qq-group.webp" style="width:200px;"/>

## 共建者名录

<script setup>
import { VPTeamMembers } from 'vitepress/theme'
import { CCAppreciators, CCAppreciatePayments, CCFeedbackers } from '/.vitepress/theme/components'

import appreciators from "/data/appreciators.json"
import members from '/data/members.json'
import feedbackers from '/data/feedbackers.json'

const appreciatorsList = appreciators.appreciators
const membersList = members.members

const appreciatePayments = [
  {
    type: 'WeChat',
    qrCodeSrc: '/images/wechat-pay.jpg',
    altText: 'WeChat Pay QR Code',
  },
  {
    type: 'Alipay',
    qrCodeSrc: '/images/alipay.jpg',
    altText: 'Alipay QR Code',
  },
]
</script>

如果有空？欢迎加入我们，一起完善这个项目！

<VPTeamMembers size="small" :members="membersList"/>

> [!NOTE]
> 当前该笔记项目正在寻找共建者！（有意者与我联系 seeridia@gmail.com ）

## 反馈者名录

感谢下面这些朋友对本项目中存在的问题进行反馈：

<CCFeedbackers :items="feedbackers.feedbackers" />

> 目前收录的反馈者名单较新（2026 年后），对于之前反馈过问题的朋友，如果没有出现在名单中，请及时与我联系，我会补充上去的！

## 参考资料

1.  Bilibili Up主 [@一化儿](https://space.bilibili.com/1526560679/)
2.  普通高中教科书 化学（人教版、鲁科版、苏教版、沪科技版）[_国家中小学智慧教育平台_](https://www.zxx.edu.cn/elecEdu)
3.  解题觉醒-化学 [天星教育](https://www.tesoon.com/)
4.  [璎晴宫·霁月台·芳兰亭](https://www.zhihu.com/column/c_1266657933414342656)
5.  [维基百科](https://zh.wikipedia.org/)
6.  [维基教科书 《高中化学》](https://zh.wikibooks.org/wiki/%E9%AB%98%E4%B8%AD%E5%8C%96%E5%AD%A6)

7.  高考必刷题 [_众望教育_](https://www.lxzwedu.com/)
8.  一本涂书
9.  教材划重点
10. [Khan Academy](https://zh.khanacademy.org/)

11. 邢其毅等.基础有机化学:第4版[M].北京:北京大学出版社,2016.

## 以及...

本项目从你所看到的这个在线网站到 PDF 文件，都是完全免费的，可以自由下载和使用的，全程没有任何广告和付费墙。

如果这份材料对你的帮助很大，可以考虑下赞赏吗？赞赏也将是支持网站和这份笔记的维护工作。

<CCAppreciatePayments :items="appreciatePayments" />

> [!NOTE]
> 如果您选择赞赏，希望能在备注中留下您的名字或昵称，也可以带上一句话，以便我们在项目的感谢名单中提及您！谢谢您的支持！😊
> 由于赞赏方式是人工统计的，如果您已经赞赏了，但没有出现在名单中，请及时与我联系（QQ: 1528926919），我会补充上去的！

感谢下面这些朋友对本项目的赞赏支持：

<CCAppreciators :items="appreciatorsList" />


---

## Original file: index.md

---
description: 本章提供站点使用说明、阅读建议与错误反馈入口，帮助你快速了解 Chemistry Note 的内容结构与参与方式。
---

# 00 说明

<CCChapterOverview />


---

## Original file: 向明天 · 2026 高考.md

---
title: 向明天
description: 写给 2026 年 6 月 9 日走进化学考场的同学们。
layout: page
outline: false
---

<script setup>
import CCTomorrowLetter from "../.vitepress/theme/components/specialPage/CCTomorrowLetter.vue";
</script>

<CCTomorrowLetter>

# 向明天 · 2026 高考

<p class="tomorrow-author">Seeridia</p>

刚刚结束了一天的实习工作，回到宿舍已经有点晚了。

每年这个时候，不管在哪，所有人都在讨论 “今天高考作文是什么”，“今年数学难不难？”。

去年的我也不例外，那时才大一，比更多人都激动，甚至第一时间去拿新鲜出炉的高考数学卷自己做做看，然后，笑着：

<p class="tomorrow-quote">“害，我都忘了“</p>

---

今年的我开始实习上班了，虽然还是个学生，但显然，工作的刺激和压力远比我最开始想象的要大，浑浑噩噩的度过每天——从工位到食堂，从食堂到床上。应付学校的作业和考试，完成实习公司的工作任务，偶尔还要参加各种各样的活动，自己每天都在忙碌中度过。

今年又到了这个时候，已不再对高考作文和数学卷感兴趣了，甚至有点厌倦了，只会看着抖音，笑着：

<p class="tomorrow-quote">“哈，今年又刷了几个 NPC 丢了准考证“</p>

---

宿舍里面的同学们都在讨论高考，这才想着噢，我还有化学笔记项目的孩子们呢，是不是该给他们说些啥？

知识点和考试技巧什么的？不行不行，好好笑，我自己都忘了，怎么能教他们呢？

所以也边犹豫边拖了好久，知道现在——明天就是化学考试了——才开始准备写些啥。

那便成了这篇碎碎念。

---

我高一、高二的时候化学非常差非常差，有多差呢？基本都是 30-40 分这样子，选化学纯粹是当时的物化绑定，实在没办法了。

这个笔记的诞生也就是这样的背景，想着自己一点点重投开始学化学，一点点认真的做笔记，一点点总结，边形成了你所看到的这个笔记——为了我自己而诞生的笔记

——陪伴我从 30 分到 90 分的笔记。

虽然最后的 90 分也不是很好，但至少是在当时 30 分的我看来，至少不觉得可惜了。

---

在毕业两年后，在 25 年的年底想着，或许可以把这个笔记分享出来，给正在学化学的孩子们一些帮助。

所以就有了这个网站。

从 2026 年 1 月 2 日开始，到现在，已经有 106,501 人次访问了这个网站，也帮助到了 30,168 位同学。

能帮助到这么多同学，我蛮开心的。

---

今天已经是 6 月 8 日了，明早就是化学考试了，或许明早大家在考试的时候我还在焦头烂额地和工作对线，无瑕祝福大家，那就将这些话放在今晚吧。

朋友，加油！我们明天见！

<p class="tomorrow-signature">写於 6 月 8 日傍晚</p>

</CCTomorrowLetter>


---

## Original file: 贡献指南.md

---
description: "Chemistry Note 项目贡献指南：如何反馈、提交内容修改、规范命名与提交前自检。"
---

# 贡献指南

感谢你愿意参与 **Chemistry Note** 的共建。

本章节主要讲的是如何参与贡献内容、提交修改、规范命名以及提交前的自检。参与的前置要求是需要有一个 GitHub 账号，并且熟悉基本的 Git 操作 和 Markdown 语法。

如果你是第一次参与开源项目，或者不太熟悉 Git 和 Markdown，那请不要花时间去学习这些工具的使用，他们会花费你大量的时间。如果你只是要反馈问题，参见 [反馈问题](./错误反馈.md) 部分。

## 项目结构

Chemistry Note 的项目示例如下：

```
├── docs
│   ├── 01 原子结构与元素性质
│   │   ├── 01 核外电子排布方式.md
│   │   ├── 02 构造原理、泡利原理、洪特规则
│   │   ├── 03 电子排布式与轨道表示式.md
│   │   └── 考点 元素周期律与元素推断.md
...
```

其中，我们的内容主要分为两类：

1. **章节内容**：以数字开头的 Markdown 文件，如 `03 电子排布式与轨道表示式.md`，这些文件包含了章节的主要内容。
2. **考点内容**：以 `考点` 开头的 Markdown 文件，如 `考点 元素周期律与元素推断.md`，这些文件包含了章节的考点等等。

请务必遵循上述的命名规范，以便我们能够更好地管理和维护项目内容。

## 文章结构

每篇文章的结构示例如下：

```
---
description: "介绍电子排布式、简化电子排布式和轨道表示式的概念、书写规则和意义，包括实例和价层电子轨道表示式表格。"
---
# 03 · 电子排布式与轨道表示式

正文...
```

其中，文章的开头需要包含一个 YAML Front Matter，用于描述文章的元信息，如 `description`。接下来是文章的标题，格式为 `# 数字 · 章节标题`，数字部分需要与文件名中的数字保持一致。

另外结构中也有要求如下：

1. 每篇文章有且仅有一个一级标题（`#`），且该标题必须以数字开头，后面跟着章节标题。
2. 每篇文章的标题深度不能超过三级标题（`###`），以保持内容的层次清晰。更多的结构请使用无序列表、有序列或者表格等方式来组织内容。

## 提交内容修改

如果你发现了文本中的错误，或者有更好的表达方式，欢迎提交修改建议。请按照以下步骤操作：

1. Fork 这个仓库到你的 GitHub 账号。
2. 在你的 Fork 中找到需要修改的文件，进行修改。
3. 提交修改，并创建一个 Pull Request，描述你修改的内容和原因。
4. 等待维护者的审核和合并。

对于 PR 的命名，请遵循以下规范：

- **文本修改**：`fix: 修正了某某错误` 或 `feat: 优化了某某表达`
- **新增内容**：`feat: 添加了某某内容`
- **其他修改**：`chore: 更新了某某内容`

## 自检

提交 PR 前，请先在本地运行格式化和构建检查：

```bash
bun install
bun run format
bun run format:check
bunx tsc --noEmit
bun run docs:build
```

其中，`bun run format` 会使用 oxfmt 统一格式化 Markdown、代码与配置文件；`bun run format:check` 会在 PR 中作为检查项运行。

我们部署了 CD 流程，在 PR 打开后会自动构建到预览环境，提交者可以在 PR 中查看预览链接，检查修改后的内容是否正确显示。

如下图所示，你可以点击 `Preview` 链接，进入预览环境查看修改后的效果

![&keep-color](images/preview.webp)

## 负责任地使用 LLM

请注意我们的首要贡献原则：**我们不接受 LLM 全篇生成的内容**，LLM 只能参与下面三个部分：

1. **内容的润色**：LLM 可以帮助我们优化文本的表达，使其更清晰、流畅，但不能生成新的内容。
2. **内容的校对**：LLM 可以帮助我们检查文本中的语法错误、拼写错误和逻辑不清的地方，但不能替代人工的校对
3. **OCR 转写**：LLM 可以帮助我们将图片中的文本转写成可编辑的文本，但需要人工进行校对和润色。

## Markdown 语法拓展

这边会介绍一些我们在项目中使用的 Markdown 语法拓展，以便你能够更好地编写内容。有一部分是 Vitepress 自带的，一部分是我们自定义的。

> 感谢 [Linho1219/LinhoNotes](https://github.com/Linho1219/LinhoNotes) 项目提供的 Markdown 语法拓展示例，我们在此基础上进行了一些修改。

### 公式

我们使用 mathjax 来渲染公式，支持行内公式和块级公式。行内公式使用 `$...$` 包裹，块级公式使用 `$$...$$` 包裹。

特别的，对于化学式的书写，我们使用 `$\ce{...}$` 来包裹化学式，这样可以更好地渲染化学式中的元素、离子、分子等。

```markdown
$$
\ce{2H2 + O2 -> 2H2O}
$$
```

$$
\ce{2H2 + O2 -> 2H2O}
$$

### Github 风格的警报

```markdown
> [!NOTE]
> 强调用户在快速浏览文档时也不应忽略的重要信息。

> [!TIP]
> 有助于用户更顺利达成目标的建议性信息。

> [!IMPORTANT]
> 对用户达成目标至关重要的信息。

> [!WARNING]
> 因为可能存在风险，所以需要用户立即关注的关键内容。

> [!CAUTION]
> 行为可能带来的负面影响。
```

> [!NOTE]
> 强调用户在快速浏览文档时也不应忽略的重要信息。

> [!TIP]
> 有助于用户更顺利达成目标的建议性信息。

> [!IMPORTANT]
> 对用户达成目标至关重要的信息。

> [!WARNING]
> 因为可能存在风险，所以需要用户立即关注的关键内容。

> [!CAUTION]
> 行为可能带来的负面影响。

### 徽章

可以使用全局组件 Badge 来创建徽章，支持不同的类型和颜色。

```markdown
### Title <Badge type="info" text="超纲内容" />

### Title <Badge type="tip" text="苏教版" />

### Title <Badge type="warning" text="整理中" />
```

### Title <Badge type="info" text="超纲内容" />

### Title <Badge type="tip" text="苏教版" />

### Title <Badge type="warning" text="整理中" />

### 图片反色

图片默认在深色模式下会进行反色处理，如果你不希望图片被反色，可以在图片标签中添加 `&keep-color` 参数。

```markdown
![&keep-color](images/example.webp)
```

更多 Markdown 语法拓展请参见 [Vitepress 官方文档](https://vitepress.dev/zh/guide/markdown)


---

## Original file: 错误反馈.md

# 错误反馈

笔记体量很大，且长期只有我个人维护，难免会有各种错误。如果你在使用过程中发现任何错误，欢迎通过点击下面的链接反馈给我：

[https://seeridia.feishu.cn/share/base/form/shrcnlJD1Np8oGgTOvkrp8hLOcf](https://seeridia.feishu.cn/share/base/form/shrcnlJD1Np8oGgTOvkrp8hLOcf)

当然，如果你懒，你也可以直接在对应章节的评论区中**直接留言**。

## 然后呢？

如果您的建议被采纳，我们会在后续的版本更新中进行改进，并在首页放上您填写的昵称以示感谢。

## 想要进一步成为共建者？

我们非常欢迎您成为 Chemistry Note 的共建者！

如果您有 Git 使用经验，可以通过 GitHub 提交代码，帮助我们完善笔记或添加新内容。


---



# Chapter 01 原子结构与元素性质

Source directory: `01 原子结构与元素性质`

## Original file: 01 核外电子排布方式.md

---
description: "介绍多电子原子核外电子的能层和能级划分，原子轨道的基本概念，以及电子排布的规则。"
---

# 01 · 核外电子排布方式

## 能层与能级

- **能层：** 多电子原子的核外电子的能量是不同的，离核近的电子能量较低，离核越远，电子的能量越高。可以将核外电子分成不同的能层，并用符号 $K、L、M、N、O、P、Q....$ 表示相应离核最近的第一能层，次之的第二能层，以此类推三、四、五、六、七能层。

  | 电子层序数( $n$ ) | $1$ | $2$               | $3$               | $4$               | $5$               | $6$               | $7$ |
  | ----------------- | --- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | --- |
  | **符号表示**      | $K$ | $L$               | $M$               | $N$               | $O$               | $P$               | $Q$ |
  | **能量大小**      | 小  | $\longrightarrow$ | $\longrightarrow$ | $\longrightarrow$ | $\longrightarrow$ | $\longrightarrow$ | 大  |
  | **距核远近**      | 近  | $\longrightarrow$ | $\longrightarrow$ | $\longrightarrow$ | $\longrightarrow$ | $\longrightarrow$ | 远  |

- 实验和量子力学研究表明，多电子原子中，同一能层的电子，能量可能不同，因此还能再将它们分成若干能级。在每一个能层中，能级符号的顺序是$ns、np、nd、nf...$（$n$ 表示能层）。
    <table>
        <tbody>
            <tr>
                <th rowspan="2"> 能层 </th>
                <td> n = 1 </td>
                <td colspan="2"> n = 2 </td>
                <td colspan="3"> n = 3 </td>
                <td colspan="4"> n = 4 </td>
            </tr>
            <tr>
                <td> K </td>
                <td colspan="2"> L </td>
                <td colspan="3"> M </td>
                <td colspan="4"> N </td>
            </tr>
            <tr>
                <th> 能级种类 </th>
                <td> s </td>
                <td> s </td>
                <td> p </td>
                <td> s </td>
                <td> p </td>
                <td> d </td>
                <td> s </td>
                <td> p </td>
                <td> d </td>
                <td> f </td>
            </tr>
            <tr>
                <th> 原子轨道 </th>
                <td> 1s </td>
                <td> 2s </td>
                <td> 2p </td>
                <td> 3s </td>
                <td> 3p </td>
                <td> 3d </td>
                <td> 4s </td>
                <td> 4p </td>
                <td> 4d </td>
                <td> 4f </td>
            </tr>
            <tr>
                <th> 原子轨道数 </th>
                <td> 1 </td>
                <td colspan="2"> 1+3 = 4 </td>
                <td colspan="3"> 1+3+5 = 9 </td>
                <td colspan="4"> 1+3+5+7 = 16 </td>
            </tr>
        </tbody>
    </table>

> 原子轨道数为 $n^2$
>
> 每一电子层所容纳的电子数最多为 $2n^2$ 个

## 电子云与原子轨道

### 概率密度

1913 年，**玻尔** 提出氢原子模型，电子在 **特定轨道** 上绕核运行。量子力学指出，一定空间运动状态的电子在核外空间各处都可能出现，但出现的 **概率** 不同，可用概率密度 $(\rho)$ 表示，即

$$
\rho＝\frac{P}{V}(P\ 表示电子在某处出现的概率,V\ 表示该处的体积)
$$

### 电子云

- 定义：处于一定空间 **运动状态** 的电子在原子核外空间的概率密度分布的形象化描述

- 含义：用单位体积内小黑点的疏密程度表示电子在原子核外出现概率大小，小黑点越 **密** ，表示概率密度越 **大**

> [×] $4s$ 电子能量较高，总是在比 $3s$ 电子离核更远的地方运动

### 原子轨道

量子力学把电子在原子核外的一个 空间运动状态 称为一个原子轨道

$$
形状
\begin{cases}
s\ 电子云：& 球形 & 只有一种空间伸展方向 \\
p\ 电子云：& 哑铃形 & 有\ 3\ 种空间伸展方向分别相对于\ x, y, z\ 轴对称 \\
\end{cases}
$$

> $空间运动状态种数=轨道数； 电子运动状态种数=电子数$
>
> $eg$：基态 $\ce{C}$ 原子核外共有 $4$ 种不同的空间运动状态，共有 $6$ 个运动状态不同的电子

### 原子轨道与能层序数的关系

1. 不同能层的同种能级的原子轨道形状 **相同**，只是半径 **不同**。能层序数 $n$ 越 **大**，原子轨道的半径越 **大**。

2. $s$ 能级只有 $1$ 个原子轨道。$p$ 能级有 $3$ 个原子轨道，它们互相垂直，分别以 $p_x、p_y、p_z$ 表示.

3. 原子轨道数与能层序数 $(n)$ 的关系：原子轨道数目 $= n^2$.

### 原子轨道能量高低

1. 相同能层上原子轨道能量的高低：$ns<np<nd<nf$；

2. 形状相同的原子轨道能量的高低：$1s<2s<3s<4s<\dots$；

3. 同一能层内形状相同而伸展方向不同的原子轨道的能量相等，如 $np_x,np_y,np_z$ 轨道的能量相等；


---

## Original file: 02 构造原理、泡利原理、洪特规则.md

---
description: "介绍原子轨道、构造原理的电子填充顺序、泡利不相容原理和洪特规则。"
---

# 02 · 构造原理、泡利原理、洪特规则

## 原子轨道

<br />
<img title="" src="./images/2.1.png" style="width:250px;" />

对每个 $n$ 值而言：

- 有 **$n$** 种能级；

- 有 $n^2$ 个原子轨道；

- 最多可容纳 $2n^2$ 个 $e^-$；

## 构造原理

**构造原理（aufbau principle）**：从氢开始，随核电荷数递增，新增电子填入能级的顺序称为构造原理。

<img title="" src="./images/2.2.png" style="width:200px" />

**顺序** ：$1s - 2s - 2p - 3s -  3p - 4s - 3d - 4p - 5s - 4d - 5p - 6s - \dots$

${\displaystyle E_{1l}<E_{2l}<E_{3l}<...<E_{nl}}$

${\displaystyle E_{ns}<E_{np}<E_{nd}<E_{nf}}$

${\displaystyle E_{ns}<E_{(n-2)f}<E_{(n-1)d}<E_{np}}$

我们把第三个不等式中涉及到的能级组成的集合称为能级组。

| 能级组序号         | 一   | 二        | 三        | 四             | 五             | 六                  | 七                  |
| ------------------ | ---- | --------- | --------- | -------------- | -------------- | ------------------- | ------------------- |
| **能级**           | $1s$ | $2s$ $2p$ | $3s$ $3p$ | $4s$ $3d$ $4p$ | $5s$ $4d$ $5p$ | $6s$ $4f$ $5d$ $6p$ | $7s$ $5f$ $6d$ $7p$ |
| **最大电子容纳量** | $2$  | $8$       | $8$       | $18$           | $18$           | $32$                | $32$                |

## 泡利不相容原理

**泡利原理**：在一个原子轨道里，最多只能容纳 **2** 个电子，它们的自旋 **相反**，常用上下箭头( $\uparrow$ 和 $\downarrow$ )表示自旋相反的 **电子**。

> $\ce{ _8O}$ 的轨道表示式如下：
>
> $$
> \ce{_8O}\quad \mathop{\boxed{\uparrow\downarrow}}\limits^{1s}\;
> \mathop{\boxed{\uparrow\downarrow}}\limits^{2s}\;
> \mathop{\boxed{\uparrow\downarrow}\;\boxed{\uparrow}\;\boxed{\uparrow}}\limits^{2p}
> $$
>
> - 简并轨道：**能量** 相同的原子轨道
> - 电子对：同一个原子轨道中，自旋方向 **相反** 的一对电子
> - 单电子：一个原子轨道中若只有一个电子，则该电子称为单电子
> - 自旋平行：**箭头同向** 的单电子称为自旋平行
> - 在氧原子中，有 **3** 对电子对，有 **2** 个单电子
> - 在氧原子中，有 **5** 种 _空间运动状态_（$1s,2s,2p_x,2p_y,2p_z$），有 **8** 种 _运动状态不同_ 的电子

## 洪特规则

1. 内容：基态原子中，填入 **简并轨道** 的电子总是先单独分占，且自旋平行

2. 特例：在简并轨道上的电子排布处于全充满、半充满和全空状态时，具有 **较低** 的能量和 **较大** 的稳定性

$$
相对稳定的状态   \begin{cases}
全充满& s^2, p^6, d^{10}, f^{14} \\
半充满& s^1, p^3, d^{5}, f^{7}\\
全空& s^0, p^0, d^{0}, f^{0} \\
\end{cases}
$$

> $\ce{\ _{24}Cr}$ 的电子排布式为 $[\ce{Ar}]3d^54s^1$，为半充满状态，易错写为 $[\ce{Ar}]3d^44s^2$。
>
> $\ce{\ _{29}Cu}$ 的电子排布式为 $[\ce{Ar}]3d^{10}4s^1$，为全充满状态，易错写为 $[\ce{Ar}]3d^94s^2$

> 1. 基态原子：处于 **最低能量** 状态的原子。
> 2. 激发态原子：基态原子 **吸收能量**，它的电子会跃迁到 **较高能级**，变成 **激发态原子**。

## 能量最低原理

1. 内容：在构建基态原子时，电子将尽可能地占据 **能量最低** 的原子轨道，使整个原子的能量最 **低**。

2. 因素：整个原子的能量由 **核电荷数** 、 **电子数** 和 **电子状态** 三个因素共同决定。

## 原子光谱

<img title="" src="./images/2.4.png" style="width:300px">

### 焰色反应

物理反应，进行焰色反应应使用 **铂丝**（镍丝、无锈铁丝）。把嵌在玻璃棒上的金属丝在 **稀盐酸** 里蘸洗后，放在酒精灯的火焰里灼烧，不同金属元素会使火焰变为各种颜色，这便是焰色反应。焰色反应的形成与原子光谱有关

详见 [06 元素及其化合物 - 01 钠及其化合物](../06%20元素及其化合物/01%20钠及其化合物.md)

### 光谱分析

在现代化学中，常利用原子光谱上的 **特征谱线** 来鉴定元素，称为光谱分析。


---

## Original file: 03 电子排布式与轨道表示式.md

---
description: "介绍电子排布式、简化电子排布式和轨道表示式的概念、书写规则和意义，包括实例和价层电子轨道表示式表格。"
---

# 03 · 电子排布式与轨道表示式

## 原子结构示意图、电子排布式、电子排布图

> 价层电子排布式书写规则是处于稳定状态的原子，核外电子将尽可能地按能量最低原理排布

| 核外电子排布的表示方法   | 意义                                        | 实例（以硫原子为例）                       |
| :----------------------- | :------------------------------------------ | :----------------------------------------- |
| 原子结构示意图           | 表示每个能层容纳的电子数                    | <img src="./images/3.30.png" height="50"/> |
| 电子排布式               | 表示每个能级容纳的电子数                    | $\ce{1s^2 2s^2 2p^6 3s^2 3p^4}$            |
| 简化的电子排布式         | 前一周期稀有气体元素符号 $+$ 剩余电子排布式 | $\ce{[Ne] 3s^2 3p^4}$                      |
| 电子排布图（轨道表示式） | 表示每个原子轨道容纳的电子数                | <img src="./images/3.31.png" height="50"/> |

## 孤电子对和价层电子对辨析

| 辨析对象   | 意义                                                           | 实例                                                                                                               |
| ---------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 孤电子对   | 在分子或原子团中，未参与成键的成对价电子                       | 如 $\ce{H2O}$ 中，中心 $\ce{O}$ 原子的6个价电子，2 个用于形成共价键，剩余的 4 个价电子即为水中氧原子的两个孤电子对 |
| 价层电子对 | 在分子或原子团中，中心原子的价层电子对 = σ 键电子对 + 孤电子对 | 如 $\ce{H2O}$ 中，中心 $\ce{O}$ 原子的价层电子对 = 2 个 σ 键电子对 + 2 个孤电子对 = 4                              |

## 部分元素电子排布式和价层电子轨道表示式

| 原子序数 | 元素名称 | 元素符号  | 电子（或简化电子）排布式        | 价层电子轨道表示式                                                                                                                                                                                                                                            |
| -------- | -------- | --------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | 氢       | $\ce{H}$  | $1s^1$                          | $\mathop{\boxed{\uparrow \enspace } }\limits^{1s}$                                                                                                                                                                                                            |
| 2        | 氦       | $\ce{He}$ | $1s^2$                          | $\mathop{\boxed{\uparrow \downarrow} }\limits^{1s}$                                                                                                                                                                                                           |
| 3        | 锂       | $\ce{Li}$ | $1s^2 2s^1$                     | $\mathop{\boxed{\uparrow \enspace } }\limits^{2s}$                                                                                                                                                                                                            |
| 4        | 铍       | $\ce{Be}$ | $1s^2 2s^2$                     | $\mathop{\boxed{\uparrow \downarrow } }\limits^{2s}$                                                                                                                                                                                                          |
| 5        | 硼       | $\ce{B}$  | $1s^2 2s^2 2p^1$                | $\mathop{\boxed{\uparrow \downarrow } }\limits^{2s} \mathop{\boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } } \boxed{\enspace^{\ ^{} }_{\ } } }\limits^{2p}$                                                                                         |
| 6        | 碳       | $\ce{C}$  | $1s^2 2s^2 2p^2$                | $\mathop{\boxed{\uparrow \downarrow } }\limits^{2s} \mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } } }\limits^{2p}$                                                                                              |
| 7        | 氮       | $\ce{N}$  | $1s^2 2s^2 2p^3$                | $\mathop{\boxed{\uparrow \downarrow } }\limits^{2s} \mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\uparrow \enspace } }\limits^{2p}$                                                                                                   |
| 10       | 氖       | $\ce{Ne}$ | $1s^2 2s^2 2p^6$                | $\mathop{\boxed{\uparrow \downarrow } }\limits^{2s} \mathop{\boxed{\uparrow \downarrow } \boxed{\uparrow \downarrow } \boxed{\uparrow \downarrow } }\limits^{2p}$                                                                                             |
| 11       | 钠       | $\ce{Na}$ | $1s^2 2s^2 2p^6 3s^1$           | $\mathop{\boxed{\uparrow \enspace } }\limits^{3s}$                                                                                                                                                                                                            |
| 12       | 镁       | $\ce{Mg}$ | $1s^2 2s^2 2p^6 3s^2$           | $\mathop{\boxed{\uparrow\downarrow}}\limits^{3s}$                                                                                                                                                                                                             |
| 13       | 铝       | $\ce{Al}$ | $1s^2 2s^2 2p^6 3s^2 3p^1$      | $\mathop{\boxed{\uparrow\downarrow}}\limits^{3s}\; \mathop{\boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } } \boxed{\enspace^{\ ^{} }_{\ } } }\limits^{3p}$                                                                                          |
| 14       | 硅       | $\ce{Si}$ | $1s^2 2s^2 2p^6 3s^2 3p^2$      | $\mathop{\boxed{\uparrow\downarrow}}\limits^{3s}\; \mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } } }\limits^{3p}$                                                                                               |
| 18       | 氩       | $\ce{Ar}$ | $1s^2 2s^2 2p^6 3s^2 3p^6$      | $\mathop{\boxed{\uparrow\downarrow}}\limits^{3s}\; \mathop{\boxed{\uparrow \downarrow } \boxed{\uparrow \downarrow } \boxed{\uparrow \downarrow } }\limits^{3p}$                                                                                              |
| 19       | 钾       | $\ce{K}$  | $1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$ | $\mathop{\boxed{\uparrow}}\limits^{4s}$                                                                                                                                                                                                                       |
| 20       | 钙       | $\ce{Ca}$ | $1s^2 2s^2 2p^6 3s^2 3p^6 4s^2$ | $\mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$                                                                                                                                                                                                             |
| 21       | 钪       | $\ce{Sc}$ | $[\ce{Ar}] 3d^1 4s^2$           | $\mathop{\boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } } \boxed{\enspace^{\ ^{} }_{\ } }\boxed{\enspace^{\ ^{} }_{\ } }\boxed{\enspace^{\ ^{} }_{\ } } }\limits^{3d} \mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$                              |
| 22       | 钛       | $\ce{Ti}$ | $[\ce{Ar}] 3d^2 4s^2$           | $\mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } }\boxed{\enspace^{\ ^{} }_{\ } }\boxed{\enspace^{\ ^{} }_{\ } } }\limits^{3d} \mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$                                   |
| 23       | 钒       | $\ce{V}$  | $[\ce{Ar}] 3d^3 4s^2$           | $\mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\uparrow \enspace }\boxed{\enspace^{\ ^{} }_{\ } }\boxed{\enspace^{\ ^{} }_{\ } } }\limits^{3d} \mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$                                        |
| 24 \*    | 铬       | $\ce{Cr}$ | $[\ce{Ar}] 3d^5 4s^1$           | $\mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\uparrow \enspace }\boxed{\uparrow \enspace}\boxed{\uparrow \enspace} }\limits^{3d}  \mathop{\boxed{\uparrow}}\limits^{4s}$                                                             |
| 25       | 锰       | $\ce{Mn}$ | $[\ce{Ar}] 3d^5 4s^2$           | $\mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\uparrow \enspace }\boxed{\uparrow \enspace}\boxed{\uparrow \enspace} }\limits^{3d} \mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$                                                    |
| 26       | 铁       | $\ce{Fe}$ | $[\ce{Ar}] 3d^6 4s^2$           | $\mathop{\boxed{\uparrow\downarrow \enspace } \boxed{\uparrow \enspace } \boxed{\uparrow \enspace }\boxed{\uparrow \enspace}\boxed{\uparrow \enspace} }\limits^{3d} \mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$                                          |
| 27       | 钴       | $\ce{Co}$ | $[\ce{Ar}] 3d^7 4s^2$           | $\mathop{\boxed{\uparrow\downarrow \enspace } \boxed{\uparrow\downarrow \enspace } \boxed{\uparrow \enspace }\boxed{\uparrow \enspace}\boxed{\uparrow \enspace} }\limits^{3d} \mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$                                |
| 29 \*    | 铜       | $\ce{Cu}$ | $[\ce{Ar}] 3d^{10} 4s^1$        | $\mathop{\boxed{\uparrow\downarrow \enspace } \boxed{\uparrow\downarrow \enspace } \boxed{\uparrow\downarrow \enspace }\boxed{\uparrow\downarrow \enspace}\boxed{\uparrow\downarrow \enspace} }\limits^{3d} \mathop{\boxed{\uparrow}}\limits^{4s}$            |
| 30       | 锌       | $\ce{Zn}$ | $[\ce{Ar}] 3d^{10} 4s^2$        | $\mathop{\boxed{\uparrow\downarrow \enspace } \boxed{\uparrow\downarrow \enspace } \boxed{\uparrow\downarrow \enspace }\boxed{\uparrow\downarrow \enspace}\boxed{\uparrow\downarrow \enspace} }\limits^{3d}  \mathop{\boxed{\uparrow\downarrow}}\limits^{4s}$ |
| 31       | 镓       | $\ce{Ga}$ | $[\ce{Ar}] 3d^{10} 4s^2 4p^1$   | $\mathop{\boxed{\uparrow\downarrow}}\limits^{4s}\; \mathop{\boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } } \boxed{\enspace^{\ ^{} }_{\ } } }\limits^{4p}$                                                                                          |
| 32       | 锗       | $\ce{Ge}$ | $[\ce{Ar}] 3d^{10} 4s^2 4p^2$   | $\mathop{\boxed{\uparrow\downarrow}}\limits^{4s}\; \mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\enspace^{\ ^{} }_{\ } } }\limits^{4p}$                                                                                               |
| 33       | 砷       | $\ce{As}$ | $[\ce{Ar}] 3d^{10} 4s^2 4p^3$   | $\mathop{\boxed{\uparrow\downarrow}}\limits^{4s}\; \mathop{\boxed{\uparrow \enspace } \boxed{\uparrow \enspace } \boxed{\uparrow \enspace } }\limits^{4p}$                                                                                                    |
| 36       | 氪       | $\ce{Kr}$ | $[\ce{Ar}] 3d^{10} 4s^2 4p^6$   | $\mathop{\boxed{\uparrow\downarrow}}\limits^{4s}\;  \mathop{\boxed{\uparrow \downarrow } \boxed{\uparrow \downarrow } \boxed{\uparrow \downarrow } }\limits^{4p}$                                                                                             |
| 37       | 铷       | $\ce{Rb}$ | $[\ce{Kr}] 5s^1$                | $\mathop{\boxed{\uparrow}}\limits^{5s}$                                                                                                                                                                                                                       |

> \*特殊情况：$\ce{Cr}:[\ce{Ar}]3d^54s^1$，$\ce{Cu}: [\ce{Ar}]3d^{10}4s^1$

## 过渡金属阳离子

过渡金属阳离子失去电子时**从最外层电子开始失去**：

- $\ce{Fe}: [\ce{Ar}] 3d^64s^2$

  $\ce{Fe}^{2+}:[\ce{Ar}]3d^6$

  $\ce{Fe}^{3+}:[\ce{Ar}]3d^5$

- $\ce{Cu}: [\ce{Ar}] 3d^{10}4s^1$

  $\ce{Cu}^{+}:[\ce{Ar}]3d^{10}$

  $\ce{Cu}^{2+}:[\ce{Ar}]3d^9$

- $\ce{Zn}: [\ce{Ar}] 3d^{10}4s^2$

  $\ce{Zn}^{2+}:[\ce{Ar}]3d^{10}$


---

## Original file: 04 原子结构 元素周期表.md

---
description: "介绍原子结构与元素周期表的划分，包括核外电子排布、价层电子排布、能级图和各周期的电子填充顺序。"
---

# 04 · 原子结构 元素周期表

<img src="./images/4.1.png"/>

###### 此元素周期表是人民教育出版社参照国际纯粹与应用化学联合会（IUPAC）推荐的元素周期表的新版制作的

> 类金属：$\ce{Te,Sb,B,Ge,As,Si}$
>
> 碱金属：$\ce{Li,Na,K,Rb,Cs,Fr}$
>
> 卤素：$\ce{F,Cl,Br,I,At,Ts}$

## 核外电子排布与周期的划分

> 化学家鲍林(L.Pauling)基于大量光谱实验数据及近似的理论计算，提出的多电子原子的原子轨道 **近似能级图**

<img src="./images/4.2.png"  data-align="inline" style="width:300px">

在这个图中，如果将 **能量相近的原子轨道归为一组**，所得到的能级组按照能量从低到高的顺序与元素周期表中的周期相对应。**不同能级组之间的能量差较大，同一能级组内能级之间的能量差较小**

进一步研究表明，**通常只有最外能级组的电子才有可能参与化学反应，最外能级组中那些有可能参与 化学反应的电子称为 价电子(valence electron)**

一般情况下，主族元素原子的价电子只包括最外层电子；过渡元素原子的价电子除最外层电子外，还包括次外层的部分电子，甚至倒数第三层的电子

## 价层电子排布与周期的划分

<img title="" src="./images/4.3.jpg"  data-align="inline">

- 第一周期：$1s^1\longrightarrow 1s^2$

- 第二周期：$2s^1\longrightarrow 2s^2\longrightarrow 2s^22p^1\longrightarrow \dots \longrightarrow 2s^22p^6$

- 第三周期：$3s^1\longrightarrow 3s^2\longrightarrow 3s^23p^1\longrightarrow...\longrightarrow 3s^23p^6$

- 第四周期：$4s^1 \longrightarrow 4s^2\longrightarrow 3d^14s^2\longrightarrow...\longrightarrow3d^{10}4s^2\longrightarrow4s^24p^1\longrightarrow...\longrightarrow4s^24p^6$

- 第五周期：$5s^1\longrightarrow 5s^2\longrightarrow 4d^15s^2\longrightarrow...\longrightarrow 4d^{10}5s^2\longrightarrow 5s^25p^1\longrightarrow...\longrightarrow 5s^25p^6$

- 第六周期：$\ce{La}$ 系 $6s\longrightarrow 4f\longrightarrow 5d\longrightarrow 6p$

- 第七周期：$\ce{Ac}$ 系 $7s\longrightarrow 5f\longrightarrow 6d\longrightarrow 7p$

除第一周期外，其余周期总是从 $ns$ 能级开始，以 $ns^2np^6$ 能级结束（稀有气体结构）；**一个能级组最多能容纳的电子数等于对应的周期包含的元素种数**

过渡元素优先填充内层的 $d$ 轨道，其余元素的价层电子无需写 $d$ 轨道

> 如：
>
> $\ce{_{33}As}$: 核外电子排布式：$[\ce{Ar}]3d^{10}4s^24p^3$
>
> $\ce{_{33}As}$: 价层电子排布式：$4s^24p^3$
>
> $\ce{_{54}Xe}$: 核外电子排布式：$[\ce{Kr}]4d^{10}5s^25p^6$
>
> $\ce{_{54}Xe}$: 价层电子排布式：$5s^25p^6$

价层电子排布式书写方式：（以 $\ce{Sb}为例$）

1. $\ce{Sb}$ 为第五周期 $\texttt{ⅤA}$ 族

2. $\texttt{ⅤA}$ 族：最外层有五个电子

3. 第五周期：第五能层

4. 所以电子排布式为 $5s^25p^3$

## 各族元素价层电子排布特点

- **主族**：$ns^1 \longrightarrow ns^2np^5$，且主族序数 $(n)$= 最外层电子数 = 价层电子数
- **0 族**：$\ce{He}$为$1s^2$，其他为 $ns^2np^6$（最外层 $8$ 电子）
- **过渡元素**（全部都是金属，最外层电子数不超 $2$ ）
  1. $ⅢB$ 族$\sim ⅤⅡB$ 族：
     $(n-1)d^{1-5}ns^{1-2}$
     族序数 = 价电子数
     $d$ 轨道未全满

     > 特殊：$\ce{Cr}:3d^54s^1$ $Cu:3d^{10}4s^1$
     >
     > 例外：$\ce{Pd}:4d^{10}$（ $d$ 轨道全满）以及 镧系、锕系

  2. $ⅤⅢ$ 族（8、9、10 列）：$(n-1)d+ns$ 能级的电子数之和

  3. $ⅠB、ⅡB$ 族：

     $(n-1)d^{10}ns^{1-2}$ [$(n-1)d$ 轨道为全充满状态]

  4. 镧系/锕系：$(n-2)f^{0-14}(n-1)d^{0-2}ns^2$

## 元素周期表的分区

按照核外电子排布，可把元素周期表划分成 5 个区：$s$ 区、$p$ 区、$d$ 区、$ds$ 区、$f$ 区

除 $ds$ 区外，**各区的名称来自按构造原理最后填入电子的能级符号**

<img title="元素周期表的分区" src="./images/4.4.png"  data-align="inline" style="width:500px">


---

## Original file: 05 电离能 电负性 元素周期律.md

---
description: "介绍元素的电离能概念、逐级电离能、意义和变化规律，包括同主族、同周期的变化趋势和特殊情况。"
---

# 05 · 电离能 电负性 元素周期律

## 元素的电离能

### 概念

1. **第一电离能**：**气态** 电中性 **基态原子** 失去一个电子转化为气态基态正离子所需要的最低能量叫做该元素的 第一电离能，用 $I_1$ 符号表示

   $$
   \ce{M}(g)-e^-\longrightarrow \ce{M}^+(g) \qquad I_1(第一电离能)
   $$

   > 「气态」、「电中性」、「基态」、「失去一个电子」等都是保证能量最低的条件

2. **逐级电离能**：气态基态 **一** 价正离子再 **失去** 一个最外层电子成为气态基态 **二** 价正离子所需的最小能量叫做第二电离能，第三电离能和第四、第五电离能依此类推。由于原子失去电子形成离子后，若再失去电子会更加 **困难**，**逐级电离能越来越大**

   > $\ce{M}(g)-e^-\longrightarrow{} \ce{M}^+ (g) \quad I_1$（第一电离能）
   >
   > $\ce{M}^+(g)-e^-\longrightarrow{} \ce{M}^{2+}(g) \quad I_2$（第二电离能）
   >
   > $\ce{M}^{2+}(g)-e^-\longrightarrow{} M^{3+}(g) \quad I_3$（第三电离能）
   >
   > $I_1<I_2<I_3< \dots$

### 意义

第一电离能可以衡量元素的气态原子失去一个电子的 **难易程度**

- 第一电离能数值越 **小**，原子越 **容易失去** 一个电子
- 第一电离能数值越 **大**，原子越 **难失去** 一个电子

### 变化规律

- **同主族** 的原子最外层电子数相同，**随着原子序数增大**，电子层数逐渐增多，原子半径逐渐增大，原子核对核外电子的有效吸引力作用逐渐减弱，**第一电离能逐渐减小**

- **同周期** 的主族元素具有相同的电子层数，**随着核电荷数增加**，原子半径逐渐减小，原子核对核外电子的有效吸引力作用逐渐增加，**第一电离能呈现增大趋势**。因此对同周期元素来说，**碱金属的第一电离能最小，稀有气体的第一电离能最大**

- 元素的第一电离能大小还与其原子的核外电子排布（特别是最外围电子排布）有关。通常情况下，当原子核外电子排布在能量相等的轨道上形成全空（ $p$、$d$、$f$ ）、半满( $p^3$、$d^5$、$f^7$ )和全满( $p^6$、$d^{10}$、$f^{14}$ )结构时，原子的能量较低，该元素具有较大的第一电离能。

- **前四周期内的同周期，由左至右，第一电离能逐渐增大，$Ⅱ A$、$Ⅲ A$互换，$Ⅴ A $、$Ⅵ A$互换**

- **第二周期元素第一电离能大小：**

  $$
  \ce{Li}<\ce{B}<\ce{Be}<\ce{C}<\ce{O}<\ce{N}<\ce{F}<\ce{Ne}
  $$

  > $\ce{B、Be}$ 位置互换：$\ce{Be}$ 为 $2s^2$ 全满稳定结构，失去一个电子需要破坏 $2S$ 全满稳定结构，所需的第一电离能比较大
  >
  > $\ce{O、N}$ 位置互换：$\ce{N}:2s^22p^3$，失去一个电子需要破坏 $2p$ 的半充满结构，所需的第一电离能比较大
  >
  > 另外注意：$\ce{C}<\ce{H}<\ce{O}$

- **第三周期元素第一电离能大小：**

  $$\ce{Na}<\ce{Al}<\ce{Mg}<\ce{Si}<\ce{S}<\ce{P}<\ce{Cl}<\ce{Ar}$$

  > $\ce{Al}、\ce{Mg}$ 位置互换：$\ce{Mg}$ 为 $3s^2$ 全满稳定结构，失去一个电子需要破坏 $3S$ 全满稳定结构，所需的第一电离能比较大
  >
  > $\ce{S}、\ce{P}$ 位置互换：$\ce{P}:3s^23p^3$，失去一个电子需要破坏 $3p$ 的半充满结构，所需的第一电离能比较大

        <img title="" src="./images/5.2.png"  data-align="inline" style="width:320px" />

> 下表的数据从上到下是钠、镁、铝逐级失去电子的电离能：
>
> | 电离能 | $\ce{Na}$ | $\ce{Mg}$ | $\ce{Al}$ |
> | :----: | :-------: | :-------: | :-------: |
> | $I_1$  |   $496$   |   $738$   |   $579$   |
> | $I_2$  |  $4562$   |  $1451$   |  $1817$   |
> | $I_3$  |  $6912$   |  $7733$   |  $2745$   |
> | $I_4$  |  $9543$   |  $10540$  |  $11545$  |
> | $I_5$  |  $13353$  |  $13630$  |  $14830$  |
>
> $\ce{Na}$ 的 $I_2$ 相比 $I_1$ 剧增：$\ce{Na}^+ : 1s^22s^22p^6$，此时是全满稳定结构，因此 $I_2$ 相比 $I_1$ 剧增
> $\ce{Mg}$ 的 $I_3$ 剧增、$\ce{Al}$ 的 $I_4$ 剧增 同理
> （可以通过判断电离能剧增地方，反向判断大致的元素）
>
> 1. 这些数据跟钠、镁、铝的化合价有什么关系？
>
>    > $\because \ce{Na}$：$I_2 \gg I_1$ $\therefore \ce{Na}$：$+1$
>    >
>    > $\because \ce{Mg}$：$I_3 \gg I_2$ $\therefore \ce{Mg}$：$+2$
>    >
>    > $\because \ce{Al}$：$I_4 \gg I_3$ $\therefore \ce{Al}$：$+3$
>
> 2. 比较钠、镁、铝的 $I_1$ 、 $I_2$ 、 $I_3$ 的大小：
>
>    > $I_1：$ 同周期，由左至右逐渐增大（$\ce{Na}$ 最小），但 $\ce{Mg}：3s^2$ 全满，$\therefore \ce{Mg}>\ce{Al}$
>    >
>    > $I_2：\ce{Na}>\ce{Al}>\ce{Mg}$ 因为 $\ce{Na}$ 已经失去电子到内层，电离能剧增，所以 $\ce{Na}$ 的 $I_2$ 最大
>    >
>    > $I_3：\ce{Mg}>\ce{Na}>\ce{Al}$ 因为 $\ce{Mg}$ 已经失去电子到内层，电离能剧增，所以 $\ce{Mg}$ 的 $I_3$ 最大
>
> **总结：**
> $I_1：\ce{Mg}>\ce{Al}>\ce{Na}$ （美女呐）
>
> $I_2：\ce{Na}>\ce{Al}>\ce{Mg}$ （哪里美）
>
> $I_3：\ce{Mg}>\ce{Na}>\ce{Al}$ （美那里）

> [ 2021 福建 ] $\ce{N、O、S}$ 的第一电离能（$I_1$）大小为 $I_1(\ce{N})>I_1(\ce{O})>I_1(\ce{S})$，原因是？
>
> > $\ce{N}$ 原子 $2p$ 轨道半充满，比相邻的 $\ce{O}$ 原子更稳定更难失电子
> >
> > $\ce{O、S}$ 同主族，（随着原子序数增大，电子层数逐渐增多），$\ce{S}$ 原子半径大于 $\ce{O}$ 原子半径，（原子核对核外电子的有效吸引力作用逐渐减弱），更易失电子
>
> **总结**：论证第一电离能变化规律，首先考虑半充满、全充满稳定结构失电子，其次考虑原子半径对核外电子的吸引力作用。

> **注意**：对于同一物质的不同电离能比较，不考虑半充满或全充满稳定结构，**电离能均逐级增大**
>
> 例如：$\ce{Mg}\space\frac {↑ ↓ }{3s}$ 与 $\ce{Mg}\space\frac {↑ }{3s}$ ，后者的电离能大于前者

## 元素的电负性

### 有关概念与意义

- **键合电子**：元素相互化合时，原子中用于形成 **化学键** 的电子称为 **键合电子**

- **电负性**：用来描述不同元素的原子对键合电子 **吸引力** 的大小。电负性越 **大** 的原子，对键合电子的吸引力越 **大**

- **电负性大小的标准**：以 $F$ 的电负性为 $4.0$ 和 $Li$ 的电负性为 $1.0$ 作为相对标准

### 递变规律

1. **同周期**，自左到右，元素的电负性逐渐 **增大** ，元素的非金属性逐渐 **增强** 、金属性逐渐 **减弱**

2. **同主族**，自上到下，元素的电负性逐渐 **减小** ，元素的金属性逐渐 **增强** 、非金属性逐渐 **减弱**

**电负性顺序（背诵）：$\ce{F(4.0)> O > N、Cl > Br > I、S、C > P、H > }$ 类金属 $\ce{(B、Si、Ge)>}$ 金属**

> 记忆方法：
>
> - 总体，越向右上角越大
> - $\ce{F}$ 最大，$\ce{O}$ 次之（死记）
> - 因此，$\ce{Cl}$ 与 $\ce{N}$ 相等（象棋中走「马」字）
> - 各自左移一格，$\ce{S}$ 与 $\ce{C}$ 相等（走「马」字）
> - 也是「马」字，所以，$\ce{S}$ 与 $\ce{I}$ 相等
> - $\ce{P}$ 和 $\ce{H}$ 电负性相等（ $pH$ ）
>
> <img title="" src="./images/5.5.svg" style="width:320px">

<img title="" src="./images/5.3.png"  style="width:320px">

### 应用

1. 判断元素的金属性和非金属性强弱
   1. **金属的电负性一般小于 $1.8$，非金属的电负性一般大于 $1.8$**，而位于非金属三角区边界的「类金属」（如锗、锑）的电负性则在 $1.8$ 左右，它们既有金属性，又有非金属性

   2. 金属元素的电负性 **越小** ，金属元素越活泼；非金属元素的电负性 **越大** ，非金属元素越活泼

2. 电负性可以判断化学键的类型

   $$
   两成键元素间电负性差值   \begin{cases}
   大于 1.7  &
            通常形成离子键 \\
          & 相应的化合物为离子化合物  \\
   小于 1.7 &
            通常形成共价键 \\
          & 相应的化合物为共价化合物
   \end{cases}
   $$

   > 如 $\ce{H}$ 的电负性为 $2.1$，$\ce{Cl}$ 的电负性为 $3.0$ ，$\ce{Cl}$ 的电负性与 $\ce{H}$ 的电负性之差为 $3.0-2.1=0.9<1.7$，故 $\ce{HCl}$ 为共价化合物；
   >
   > 如 $\ce{Al}$ 的电负性为 $1.5$ ，$\ce{Cl}$ 的电负性与 $\ce{Al}$ 的电负性之差为 $3.0-1.5＝1.5<1.7$，因此 $\ce{AlCl3}$ 为共价化合物；
   >
   > 同理，$\ce{BeCl2}$ 也是共价化合物
   >
   > 例外：$\ce{H}$ 的电负性为 $2.1$ ，$\ce{F}$ 的电负性为 $4.4$，虽然 $\ce{HF}$ 的电负性差值大于 $1.7$ ，但仍然形成共价键，是共价化合物

3. 电负性可以判断化合物中元素的化合价
   1. 电负性数值 **小** 的元素在化合物中吸引电子的能力 **弱** ，元素的化合价为 **正值**

   2. 电负性数值 **大** 的元素在化合物中吸引电子的能力 **强** ，元素的化合价为 **负值**

   > 已知：电负性 $\ce{Cl > H > Si}$
   >
   > 所以在 $\ce{SiHCl}$ 中，$\ce{Si:+4;H:-1;Cl:-1}$

4. 电负性可以比较极性的大小
   电负性相差越大，共价键的极性也就越大

## 对角线规则

「对角线」规则又称斜线关系，指元素周期表中某一元素及其化合物的性质与它左上方或右下方的另一元素及其化合物的性质相类似。在第 $2、3$ 周期中，**具有典型「对角线」规则的元素有三对：锂与镁，铍与铝，硼与硅**。有人从元素的电负性值相近解释「对角线」规则：锂 $1.0$、镁 $1.2$；铍 $1.5$、铝 $1.5$；硼 $2.0$、硅 $1.8$。

<img title="" src="./images/5.4.png"  data-align="inline" style="width: 150px">

> 1. 锂和镁的相似性：
>    1. 在氧气中燃烧生成氧化物，而其他碱金属则易生成过氧化物、超氧化物
>    2. 能直接与氮作用，生成氮化物 $\ce{Li3N}$ 、 $\ce{Mg3N2}$ ，而其他碱金属不与氮直接反应
>    3. 氟化物、碳酸盐、磷酸盐都难溶于水，而其他碱金属的相应盐易溶于水等
> 2. 铍和铝的相似性：
>    1. 单质在冷的浓硝酸中钝化
>    2. 氧化物、氢氧化物都有两性
>    3. 氯化物都是共价化合物，易汽化，能升华，能溶于有机溶剂等
> 3. 硼和硅的相似性：
>    1. 硼和硅的密度分别为 $2.35g \cdot cm^{-3}$ 和 $2.336g \cdot cm^{-3}$ , 两者相近
>    2. 硼和硅的简单气态氢化物都能直接被氧气氧化
>    3. 最高价氧化物的水化物都是弱酸等

## 原子半径

### 影响因素

原子半径的大小取决于两个相反的因素：**电子的能层数** 和 **核电荷数**

1. 电子的能层数：电子的能层越多，电子之间的 **排斥** 作用使原子半径 **增大**
2. 核电荷数：核电荷数越 **大** ，核对电子的吸引作用就越 **大** ，使原子半径 **减小**

### 递变规律

<img title="" src="./images/5.1.png"  data-align="inline" style="width:260px">

总结： 同周期由左至右，原子半径减小；同主族由上至下，原子半径增大

> 特别：$r(\ce{Li})>r(\ce{Al、Si、P、S、Cl})$

## 主族元素原子半径的递变规律

1.  **同周期**：从左至右，核电荷数越大，半径越小（口诀：序大径小）
    例：$r(\ce{Na})>r(\ce{Mg})>r(\ce{Al})>r(\ce{Si})>r(\ce{P})>r(\ce{S})>r(\ce{Cl})$  
    注：稀有气体原子不参与同周期原子半径的比较。

2.  **同主族**：从上到下，电子能层越多，半径越大（口诀：层多径大）
    例：$r(\ce{H})<r(\ce{Li})<r(\ce{Na})<r(\ce{K})<r(\ce{Rb})<r(\ce{Cs})$

## 主族元素离子半径的比较方法

1.  **电子层结构相同（或核外电子总数相同）的离子**：核电荷数越大，半径越小（口诀：序大径小）
    例：
    (1) 10 电子离子：$r(\ce{O^{2-}})>r(\ce{F^-})>r(\ce{Na^+})>r(\ce{Mg^{2+}})>r(\ce{Al^{3+}})$  
    (2) 18 电子离子：$r(\ce{S^{2-}})>r(\ce{Cl^-})>r(\ce{K^+})>r(\ce{Ca^{2+}})$

2.  **带相同电荷的离子**：能层数越多，半径越大
    例：
    (1) $r(\ce{Li^+})<r(\ce{Na^+})<r(\ce{K^+})<r(\ce{Rb^+})<r(\ce{Cs^+})$  
    (2) $r(\ce{F^-})<r(\ce{Cl^-})<r(\ce{Br^-})<r(\ce{I^-})$

3.  **核电荷数、能层数均不同的离子**：可选一种离子参照比较
    例：比较 $r(\ce{K^+})$ 与 $r(\ce{Mg^{2+}})$，可选 $r(\ce{Na^+})$ 为参照，$r(\ce{K^+})>r(\ce{Na^+})>r(\ce{Mg^{2+}})$

---

> [!Tip]
>
> 1. 比较粒子半径时，一定要先利用“层多径大”将粒子分类。在层数相同的基础上，再利用“序大径小”
> 2. 硅、碳等元素不能形成简单离子，所以第三周期半径最小的离子是 $\ce{Al^{3+}}$

> [!Tip]
> **解题技巧：粒子半径比较的一般思路**
>
> 1. 「一层」：先看能层数，能层数越 **多** ，一般微粒半径越 **大**
> 2. 「二核」：若能层数相同，则看核电荷数，核电荷数越 **大** ，微粒半径越 **小**
> 3. 「三电子」：若能层数、核电荷数均相同，则看核外电子数，电子数 **多** 的半径 **大**

本章串联：电离能反映原子**失电子能力**，电负性反映**得电子倾向**，两者结合揭示元素的**金属性与非金属性强弱**；原子半径与对角线规律则从结构角度解释这些性质的周期性变化。


---

## Original file: index.md

---
description: 本章系统梳理核外电子排布、构造原理、元素周期表与周期律、电离能和电负性等核心知识，适合原子结构与元素性质专题复习。
---

# 01 原子结构与元素性质

<CCChapterOverview />


---

## Original file: 考点 中心原子杂化轨道类型的判断方法.md

# 考点 · 中心原子杂化轨道类型判断方法总结

## 一、核心逻辑

杂化轨道类型由**中心原子价层电子对数**决定，价层电子对数 = σ键电子对数 + 孤电子对数，且满足：

- 价层电子对数 = 杂化轨道数
- 杂化类型与价层电子对数对应关系（高频核心）：
  | 价层电子对数 | 杂化类型 | 杂化轨道空间构型 | 典型示例 |
  |--------------|----------|------------------|----------|
  | 2 | sp | 直线形 | CO₂、BeCl₂ |
  | 3 | sp² | 平面三角形 | BF₃、SO₃ |
  | 4 | sp³ | 正四面体形 | CH₄、NH₃、H₂O |
  | 5 | sp³d | 三角双锥形 | PCl₅、I₃⁻ |
  | 6 | sp³d² | 正八面体形 | SF₆、[Fe(CN)₆]³⁻ |

## 二、具体判断方法（按题型分类，含实例）

### 方法1：ABₙ型分子/离子（直接计算法，高考高频）

#### 步骤1：计算价层电子对数

公式： 中心原子价层电子对数(杂化轨道数目) $=$
$$ n + \frac{1}{2}(\text{中心原子价电子数} - n \times \text{配位原子成键电子数} \pm \text{离子电荷数})$$

- 关键说明：
  - $n$：配位原子个数（双键/三键按1个配位原子计，只算σ键）
  - 中心原子价电子数：主族元素=最外层电子数（如C=4、N=5）；过渡元素=价电子数（$nd + (n+1)s$，如Fe=8、Cu=11）
  - 配位原子成键电子数：H/卤素=1，O/S=0（不提供电子），N=1
  - 离子电荷数：阳离子取“-”（如NH₄⁺取-1），阴离子取“+”（如SO₄²⁻取+2）

#### 步骤2：匹配杂化类型

#### 典型实例：

1. $SO₃$（AB₃型）  
   中心S价电子数=6，配位O成键电子数=2  
   价层电子对数 = $3 + \frac{6 - 3×2}{2} = 3$ → **sp²杂化**
2. $NH₄⁺$（AB₄型阳离子）  
   中心N价电子数=5，配位H成键电子数=1，电荷数=-1  
   价层电子对数 = $4 + \frac{5 - 4×1 - 1}{2} = 4$ → **sp³杂化**
3. $I₃⁻$（AB₂型阴离子）  
   中心I价电子数=7，配位I成键电子数=1，电荷数=+1  
   价层电子对数 = $2 + \frac{7 - 2×1 + 1}{2} = 5$ → **sp³d杂化**

### 方法2：非ABₙ型分子（结构式分析法）

#### 步骤1：提取σ键数和孤电子对数

- σ 键数：直接数中心原子与其他原子形成的 σ 键（单键=1，双键=1，三键=1）
- 孤电子对数：$\frac{1}{2}(\text{中心原子价电子数} - \text{成键电子数})$（成键电子数=σ键数×2，配位键按2电子计）

#### 步骤2：计算价层电子对数，匹配杂化类型

#### 典型实例：

1. 乙烯（$CH₂=CH₂$）  
   中心C原子：σ键数=3（2个C-H + 1个C-C），孤电子对数=0  
   价层电子对数=3+0=3 → **sp²杂化**
2. 乙二胺（$H₂N-CH₂-CH₂-NH₂$）  
   中心N原子：σ键数=3（2个N-H + 1个N-C），孤电子对数=1  
   价层电子对数=3+1=4 → **sp³杂化**
3. 苯（$C₆H₆$）  
   中心C原子：σ键数=3（2个C-C + 1个C-H），孤电子对数=0（1个电子参与大π键，不计入孤电子对）  
   价层电子对数=3+0=3 → **sp²杂化**

### 方法3：已知分子空间构型（反向推导法）

根据分子实际构型，略去孤电子对后推导杂化类型：
| 分子空间构型 | 杂化类型 | 关键说明 |
|--------------|----------|----------|
| 直线形 | sp | 无孤电子对（如CO₂）或含2对孤电子对（如I₃⁻） |
| 平面三角形 | sp² | 无孤电子对（如BF₃） |
| V形（角形） | sp²或sp³ | 含1对孤电子对（如SO₂，sp²）或2对孤电子对（如H₂O，sp³） |
| 三角锥形 | sp³ | 含1对孤电子对（如NH₃） |
| 正四面体形 | sp³ | 无孤电子对（如CH₄） |

### 方法4：等电子原理法（快速判断）

原子总数相同、价电子总数相同的分子/离子，中心原子杂化类型相同：

- 示例：CO₂与N₂O（均为sp杂化）；CH₄与NH₄⁺（均为sp³杂化）；SO₄²⁻与PO₄³⁻（均为sp³杂化）

### 方法5：特殊结构记忆法（避坑关键）

- 含碳碳双键、碳氧双键、苯环的分子：中心原子多为sp²杂化（如HCHO、C₂H₄）
- 含碳碳三键、直线形结构的分子：中心原子多为sp杂化（如C₂H₂、CS₂）
- 配位化合物：[Cu(NH₃)₄]²⁺（平面正方形，dsp²杂化）、[Zn(NH₃)₄]²⁺（正四面体，sp³杂化）

## 三、高考易错点提醒

1. 杂化轨道仅用于形成σ键和容纳孤电子对，π键由未杂化的p轨道形成（如乙烯中C原子sp²杂化后，剩余1个p轨道形成π键）；
2. 价层电子对数计算时，双键/三键只计1个σ键，不计π键电子对；
3. 离子型化合物必须考虑电荷数（如SO₃²⁻：价层电子对数 = $3 + \frac{6 - 3×2 + 2}{2} = 4$，sp³杂化）；
4. 过渡元素中心原子价电子数需包含nd电子（如Fe³⁺价电子数=5，[Fe(CN)₆]³⁺中Fe为d²sp³杂化）；
5. 注意“价层电子对构型”与“分子实际构型”的区别（如NH₃价层电子对构型为正四面体，实际构型为三角锥形）。


---

## Original file: 考点 元素周期律与元素推断.md

---
description: "介绍元素周期律与元素推断的考点，包括元素周期表结构、性质变化规律、氢化物稳定性、原子半径比较等。"
---

# 考点 · 元素周期律与元素推断

## 考点一 元素周期表结构与元素周期律

<img title="" src="./images/6.1.png"  style="width:480px">

- **随周期的↘，主族的↗而↗的性质**（从左下 **至右上**）：
  1. 非金属性

  2. 单质的氧化性（简单阴离子的还原性降低）

  3. 最高价氧化物对应的水化物的酸性（ $\ce{F}$ 无含氧酸）

  4. 简单气态氢化物稳定性（单质与 $\ce{H2}$ 反应难度减弱）

  5. 第一电离能（存在例外）

  6. 电负性

  7. 金属单质熔沸点

- **随周期的↗，主族的↘而↗的性质**（**从右上至左下**）：
  1. 金属性

  2. 单质的还原性（简单阳离子的氧化性降低）

  3. 最高价氧化物对应的水化物的碱性

  4. 与 $\ce{H2O}$、酸反应的剧烈程度

  5. 氢化物还原性（非金属性越强，单质的氧化性越强，离子或化合物的还原性越弱）

- **金属氢化物稳定性**:
  向左上方向增大（同周期左侧金属性强，但同主族向下时原子半径大，键长长，键能小，分子稳定性低，因此左上方稳定）
  > $\ce{NaH} > \ce{MgH_{2}} > \ce{AlH_{3}}$，$\ce{LiH} > \ce{NaH} > \ce{KH}$
- **非金属简单氢化物稳定性**: 向右上方向增大（右上方原子半径小，键长短，键能大，分子稳定性高）
  > $\ce{HF} > \ce{HCl} > \ce{HBr} > \ce{HI}$，$\ce{HF} >\ce{H_{2}O} > \ce{NH_{3}} > \ce{CH_{4}}$
- **氢化物的熔沸点**

  同为 **分子晶体** 的氢化物的熔沸点与 **氢键** 及 **范德华力** 有关，在有氢键的情况下，熔沸点较高，且数量越多，熔沸点越高；否则，相对分子质量越大，熔沸点越高

  对于 **离子晶体** 的氢化物的沸点则一定大于分子晶体

- **原子半径的比较方法**
  1. 同周期主族元素，从左到右，原子半径依次减小

  2. 同主族元素，从上到下，原子半径依次增大

- **离子半径的比较方法**
  1. 核外电子排布不同，电子层数多的半径大

  2. 核外电子排布相同，序大径小

## 考点二 元素推断

前提知识：短周期主族元素与其形成的共价键数目

|            共价键数目            |      元素       |                                                                                                                                           说明                                                                                                                                           |
| :------------------------------: | :-------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|            一个共价键            | $\ce{H、F、Cl}$ |                   $\ce{H}$ 最外层有 1 个电子，差 1 个电子满足稀有气体 $\ce{He}$ 的 2 电子稳定结构 <br>$\ce{F}$、$\ce{Cl}$ 最外层有 7 个电子，差 1 个电子满足 8 电子稳定结构 <br>$\ce{H}$、$\ce{F}$、$\ce{Cl}$ 都是差 1 电子满足稳定结构，所以在化合物中形成 1 个共价键                   |
|            二个共价键            |   $\ce{O、S}$   |                                                                                         $\ce{O}$、$\ce{S}$ 最外层有 6 个电子，都是差 2 个电子满足 8 电子稳定结构，所以在化合价中形成 2 个共价键                                                                                          |
|            三个共价键            | $\ce{B、N、P}$  |                                                               $\ce{B}$ 最外层有 3 个电子，可以形成 3 个共价键 <br>$\ce{N}$、$\ce{P}$ 最外层有 5 个电子，都是差 3 个电子满足 8 电子稳定结构，所以在化合物中形成 3 个共价键                                                                |
|            四个共价键            |  $\ce{C、Si}$   |                                                                                         $\ce{C}$、$\ce{Si}$ 最外层有 4 个电子，都是差 4 个电子满足 8 电子稳定结构，所以在化合物中形成 4 个共价键                                                                                         |
|  得一个电子后，再形成四个共价键  |  $\ce{B、Al}$   | $\ce{B}$、$\ce{Al}$ 最外层有 3 个电子，在复杂阴离子中，若多得 1 个电子，最外层有 4 个电子后，再差 4 个电子满足 8 电子稳定结构，所以在化合物中形成 4 个共价键 <br>在阴离子如 $\ce{[BH4]^-}$、$\ce{[AlH4]^-}$ 中，B 或 Al 通过接受一个电子形成类碳结构（$sp^3$ 杂化），从而形成 4 个共价键 |
| 失去一个电子后，再形成四个共价键 |   $\ce{N、P}$   |                                                                $\ce{N}$、$\ce{P}$ 最外层有 5 个电子，在复杂阳离子中，若失去一个电子，最外层有 4 个电子后，再差 4 个电子满足 8 电子稳定结构，所以在化合物中形成 4 个共价键                                                                |
|            五个共价键            |    $\ce{P}$     |                                               $\ce{P}$ 最外层有 5 个电子，可以直接形成 5 个共价键 <br/>但要注意的是 P 才能形成 5 个共价键，$\ce{N}$ 不能 <br/>第三周期及以后元素具有空的 $d$ 轨道，可扩充价层形成更多共价键（扩展八隅体）                                                |
|            六个共价键            |    $\ce{S}$     |                                            $\ce{S}$ 最外层有 6 个电子，可以直接形成 6 个共价键 <br/>但要注意的是 $\ce{S}$ 才能形成 6 个共价键，$\ce{O}$ 不能 <br/>第三周期及以后元素具有空的 $d$ 轨道，可扩充价层形成更多共价键（扩展八隅体）                                            |
|            七个共价键            |    $\ce{Cl}$    |                                           $\ce{Cl}$ 最外层有 7 个电子，可以直接形成 7 个共价键 <br/>但要注意的是 $\ce{Cl}$ 才能形成 7 个共价键，$\ce{F}$ 不能 <br/>第三周期及以后元素具有空的 $d$ 轨道，可扩充价层形成更多共价键（扩展八隅体）                                           |

**总结：**

1. 一般少几个电子满足 8 电子稳定结构（ $\ce{H}$ 是满足 2 电子稳定结构），就会形成几个共价键。

2. 不满足 8 电子稳定结构的情况：
   1. $\ce{B}$、$\ce{Al}$ 若只形成 3 个共价键（且无孤电子对），则不满足 8 电子稳定结构

   2. $\ce{P}$、$\ce{S}$、$\ce{Cl}$ 分别形成 $5$、$6$、$7$ 个共价键时，也不满足 $8$ 电子稳定结构

   3. 一些电子总数为奇数的分子，如 $\ce{NO2}$、$\ce{NO}$，不满足 $8$ 电子稳定结构

   4. 只要有 $\ce{H}$ 原子出现时，所有原子不可能都满足 $8$ 电子稳定结构

3. 一定要注意阴离子多出的电子落在哪种元素，阳离子少的电子从哪种元素扣，判定方式如下：
   1. 与正常的共价键数目不一样，例如 $\ce{O}$ 理应形成 $2$ 个共价键，若给定的结构式中 $\ce{O}$ 只形成 $1$ 个共价键，可知 $\ce{O}$ 多一个电子，最外层 $7$ 电子，所以只形成 $1$ 个共价键
   2. $\ce{X}$ 原子形成的共价键数目若有两种，得失电子算在 $\ce{X}$ 原子上

      > 如：<img inline src="./images/K-1.1.svg" />，$\ce{X}$ 既形成 $1$ 个共价键也形成 $2$ 个共价键，可知该 $-1$ 价阴离子多出的 $1$ 个电子算在 $\ce{X}$ 上，因此 $\ce{X}$ 最外层有 $6$ 个电子，若限定该离子的元素都是短周期元素，则 $\ce{W}$ 为 $\ce{S}$，$\ce{X}$ 为 $\ce{O}$

   3. 复杂离子中，若其他元素的多个原子形成的共价键数目都只有 $1$ 种，而 $\ce{X}$ 只有 $1$ 个原子，得失电子算在 $\ce{X}$ 原子上

      > 如：<img src="./images/K-1.2.svg"/>，由于所有 $\ce{Z}$ 形成的共价键数目都是 2 ，所有 $\ce{Y}$ 形成的共价键数目都是 4 ，而 $\ce{X}$ 只有 1 个原子，因此该阴离子多出的 1 个电子算在 $\ce{X}$ 上，可知 $\ce{X}$ 得 1 个电子后形成 4 个共价键，若限定该离子的元素都是短周期元素，则 $\ce{X}$ 可以是 $\ce{B}$ 或 $\ce{Al}$

**方法：**

1. **利用原子结构推断元素**
   1. 利用原子结构及元素在周期表中的位置推断

      $$
      原子^A_ZX \begin{cases}
      原子核\begin{cases}
      中子(决定核素的种类)N 个\\
      质子(决定元素的种类)Z 个\\
      \end{cases}\\
      原子核外电子 Z 个\\
      \end{cases}
      $$
      1. 电荷角度：核内质子数($Z$)= 核电荷数 = 核外电子数 = 原子序数

      2. 质量角度：质量数($A$)= 质子数($Z$)+中子数($N$)
      3. 原子电子层数 $=$ 周期序数

      4. 原子最外层电子数 $=$ 主族序数

   2. 根据元素主要化合价的关系推断
      1. 确定元素在周期表中的位置：最高化合价 $=$ 最外层电子数 $=$ 主族序数 ($\ce{O}$ 无最高正价、$\ce{F}$ 无正价)

      2. 如果已知非金属元素的最低化合价（或简单阴离子的符号），则常先求出最高化合价：最高化合价 $= 8- |\text{最低化合价}|$，再确定元素在周期表中的位置

      3. 若最高化合价与最低化合价之和 $= 8$，则该元素一定为主族非金属

   3. 根据原子半径的递变规律推断

      同周期主族元素中左边元素的原子半径一般比右边元素的大，同主族中下边元素的原子半径比上边元素的大

2. **利用元素周期表的片段推断元素**
   1. 元素周期表中第一周期只有 $\ce{H}$ 和 $\ce{He}$ 两种元素，如果推断时已知元素位于不同周期，可优先考虑或排除第一周期的 $\ce{H}$，简化推断思路

   2. 短周期中主族序数与周期序数相同的元素有 $\ce{H}、\ce{Be}、\ce{Al}$

3. **根据物质的转化关系推断元素**

   **常见元素提示词：**

   | 元素      | 核心提示                                                                                                              |
   | --------- | --------------------------------------------------------------------------------------------------------------------- |
   | $\ce{H}$  | 原子半径最小，同位素没有中子，密度最小的气体                                                                          |
   | $\ce{C}$  | 形成化合物最多的元素，单质有三种常见的同素异形体（金刚石、石墨、富勒烯），$\ce{^{14}C}$ 可用于测定年代                |
   | $\ce{N}$  | 空气中含量最多的气体（$78\%$），单质有惰性，化合时价态很多，化肥中的重要元素                                          |
   | $\ce{O}$  | 地壳中含量最多的元素，空气中含量第 $2$ 的气体（$21\%$），生物体中含量最多、与生命活动关系密切，有两种气态的同素异形体 |
   | $\ce{F}$  | 除 $\ce{H}$ 外原子半径最小，无正价，不存在含氧酸，氧化性最强的单质                                                    |
   | $\ce{Na}$ | 短周期主族元素中原子半径最大，焰色反应为黄色                                                                          |
   | $\ce{Mg}$ | 烟火、照明弹中的成分，植物叶绿素中的元素，铝热反应的引燃剂                                                            |
   | $\ce{Al}$ | 地壳中含量第三多的元素、含量最多的金属，两性的单质，常温下遇强酸会钝化                                                |
   | $\ce{Si}$ | 地壳中含量第二多的元素，半导体工业的支柱                                                                              |
   | $\ce{P}$  | 有两种常见的同素异形体（白磷、红磷），制造火药的原料（红磷）、化肥中的重要元素                                        |
   | $\ce{S}$  | 单质为淡黄色固体，能在火山口发现，制造黑火药的原料(一硫二硝三木炭)                                                    |
   | $\ce{Cl}$ | 单质为黄绿色气体，海水中含量最多的元素，氯碱工业的产物之一                                                            |
   | $\ce{K}$  | 焰色反应呈紫色（透过蓝色钴玻璃观察），化肥中的重要元素                                                                |
   | $\ce{Ca}$ | 人体内含量最多的矿质元素，骨骼和牙齿中的主要矿质元素                                                                  |
   | $\ce{Fe}$ | 地壳中含量第四的元素，用于制在常温下盛装浓硝酸、浓硫酸的容器，**其三价离子比二价离子更稳定**                          |
   | 地壳元素  | $\ce{O}、\ce{Si}、\ce{Al}、\ce{Fe}、\ce{Ca}$                                                                          |


---



# Chapter 02 微粒间作用力与物质性质

Source directory: `02 微粒间作用力与物质性质`

## Original file: 01 晶体与晶胞（基础知识）.md

---
description: "介绍物质的聚集状态、晶体与非晶体的区别、晶体的特点如自范性和各向异性，以及晶胞的基本概念。"
---

# 01 · 晶体与晶胞

## 物质的聚集状态

1. 20 世纪前，人们以为分子是所有化学物质能够保持其性质的最小粒子，物质固、液、气三态的相互转化只是分子间距离发生了变化

2. 20 世纪初，通过 X 射线衍射等实验手段，发现许多常见的晶体中并无分子，如氯化钠、石墨、二氧化硅、金刚石以及各种金属等

3. 气态和液态物质不一定都是由分子构成。如 **等离子体** 是由 **电子**、**阳离子** 和 **电中性粒子（分子或原子）** 组成的整体上呈电中性的气态物质；离子液体是熔点不高的仅由离子组成的液体物质

4. 其他物质聚集状态，如晶态、非晶态、塑晶态、液晶态等

**晶体**：内部微粒在三维空间里呈周期性有序排列而构成的具有规则几何外形的固体，分为离子晶体、分子晶体(共价晶体)、原子晶体、金属晶体

**非晶体**：内部微粒排列呈相对无序状态，不具有规则几何外形的固体

## 晶体的特点

1. 自范性：
   1. 定义：在 **适宜的条件** 下，晶体能够 **自发地呈现封闭的、规则的几何多面体外形**

   2. 形成条件：晶体生长的速率适当

      > 晶体呈自范性的条件之一是晶体生长的速率适当熔融态物质冷却凝固，有时得到晶体，但凝固速率过快，常常只得到看不到多面体外形的粉末或没有规则外形的块状物。水晶球是岩浆里熔融态的 $\ce{SiO_2}$ 侵入地壳内的空洞冷却形成的。剖开水晶球，它的外层是看不到晶体外形的玛瑙，内层才是呈现晶体外形的水晶。不同的是，玛瑙是熔融态 $\ce{SiO_2}$ 快速冷却形成的，而水晶则是熔融态 $\ce{SiO_2}$ ，缓慢冷却形成的

   3. 本质原因：**晶体的自范性是晶体中原子、分子和离子等微粒在三维空间里呈现周期性有序排列的宏观表现** 。相反， **非晶体** 中微粒的排列则相对无序，因而 **无自范性** 。例如，自然界中存在的各种石英晶体（晶体 $\ce{SiO_2}$ ）, 它们几乎都具有对称的六角形棱柱状的外形，而玻璃、玛瑙(非晶体 $\ce{SiO_2}$ )等就没有天然的、有规则的外形

2. 各向异性：

   晶体内部微粒的排列呈现周期性，而 **不同方向上的微粒排列情况是不同的**。因此，在晶体中，**不同的方向上具有不同的物理性质**，如导电性、导热性、硬度、解理性等

   > 例：石墨在与层平行的方向上的电导率数值约为在与层垂直的方向上的电导率数值的 1 万倍。云母晶体各个方向解理性不同，若沿两层平面的平行方向施加外力就容易剥离，若沿着垂直于平面的方向剥离就困难得多

   > 非晶体在各个方向上的物理性质都一致，显各向同性。例如，玻璃的折光率、热膨胀系数等，一般不随测定的方向而改变。

3. 晶体有固定的熔点。

4. 外形和内部质点排列的高度有序性。

5. 晶体颗粒在纳米尺度时，颗粒大小越小，熔点越低

## 晶体与非晶体的辨别

**区分晶体和非晶体最好的方法：X-射线衍射**

<img title="" src="./images/1.1.png" style="width:500px" />

## 获得晶体的途径

1. 熔融态物质凝固

2. 气态物质冷却不经液态直接凝固（凝华）

3. 溶质从溶液中析出

## 晶胞

1. 概念：描述晶体结构的基本单元

2. 晶胞与晶体的关系一般来说，晶胞都是 **平行六面体**，整块晶体可以看作是数量巨大的晶胞「无隙并置」而成
   - 「无隙」是指相邻晶胞之间无任何间隙

   - 「并置」是指所有晶胞都是 **平行排列** 的，**取向相同**

   - 所有晶胞的 **形状** 及其内部的原子 **种类**、**个数** 及几何排列是完全相同的

<img title="" src="./images/1.2.png" style="width:400px" />

## 晶胞中粒子数目的计算：均摊法

晶胞中粒子数目的计算：均摊法确定晶胞中粒子的个数

若晶胞中某个粒子为 $n$ 个晶胞所共用，则该粒子有 $\frac{1}{n}$ 属于这个晶胞。

长方体形（正方体形）晶胞中不同位置的粒子对晶胞的贡献


---

## Original file: 02 分子间作用力 分子晶体.md

---
description: "讲解分子间作用力的概念、范德华力和氢键的特点、影响因素，以及对物质熔点、沸点和溶解性的影响。"
---

# 02 · 分子间作用力 分子晶体

## 分子间作用力

1. 日常生活中，我们经常见到许多由分子聚集成的物质，它们常以液态或固态的形式存在，如汽油、水、冰、干冰等。降温加压时气体会液化降温时液体会凝固，这些事实表明分子之间存在着相互作用力

2. 将分子聚集起来的作用力叫分子间作用力
   1. 共价分子间都存在分子间作用力
   2. 分子间作用力本质上是一种 **静电作用**，比化学键弱得多
   3. **范德华力** 和 **氢键** 是两种最常见的分子间作用力

### 范德华力

1. 范德华力的特点
   1. 范德华力 **很弱**，比化学键的键能小 $1\sim2$ 数量级
   2. 范德华力一般 **没有方向性和饱和性**
   3. 范德华力主要影响物质的 **熔点、沸点、溶解度** 等物理性质

2. 影响因素：
   1. 组成和结构相似的分子，其范德华力一般 **随着相对分子质量的增大而增大**
   2. 相对分子质量相近时，分子的极性越大，范德华力一般也越大
   3. 对于相对分子质量相同、极性相似的分子，分子之间的接触面积越大，范德华力越大。如范德华力：正丁烷>异丁烷

      > |         分子         | $\ce{Ar}$ | $\ce{CO}$ | $\ce{HI}$ | $\ce{HBr}$ | $\ce{HCl}$ |
      > | :------------------: | :-------: | :-------: | :-------: | :--------: | :--------: |
      > |        分子量        |   $40$    |   $28$    |  $128.5$  |   $81.5$   |   $36.5$   |
      > | 范德华力（$KJ/mol$） |  $8.50$   |  $8.75$   |  $26.00$  |  $23.11$   |  $21.14$   |
      >
      > 1. 为什么范德华力：$\ce{HI>HBr>HCl>CO}$
      >
      >    > 答：相对分子质量越大，分子间作用力越大
      >
      > 2. 为什么范德华力：$\ce{CO>Ar}$
      >
      >    > 答：分子极性越大，范德华力越大

3. 对物质性质的影响因素
   1. 对物质熔、沸点的影响：由分子构成的物质中范德华力越大，物质的熔、沸点越高

   2. 对物质溶解性的影响：

      液体的互溶以及固态、气态的非电解质在液体里的溶解度都与范德华力有密切的关系。溶剂与溶质分子间作用力越大，溶质的溶解度越大。如 $273K、101kPa$ 时，氧气在水中的溶解量（$49cm^3 \cdot L^{-1}$）比氮气在水中的溶解量（$24cm^3 \cdot L^{-1}$）大，就是 $\ce{O_2}$ 与水分子之间的作用力比 $\ce{N_2}$ 与水分子之间的作用力大所导致的

      > 怎么解释卤素单质从 $\ce{F_2}\sim \ce{I_2}$ 的熔点与沸点越来越高
      >
      > > 答：组成和结构相似的分子，相对分子质量越大，范德华力越大，熔沸点越高
      >
      > 范德华力主要影响物质的物理性质，而化学键主要影响物质的化学性质

### 氢键

1. 概念：由已经与电负性很强的原子（如 $\ce{F、O、N}$）形成共价键的氢原子，与另一个分子中电负性很强的原子之间的作用力

2. 表示：通常用 $A-H\cdots B,A、B$ 为 $\ce{N、O、F}$ 等中的一种，「$-$」表示共价键，「$\cdots$」表示氢键

3. 特征：比化学键的键能小，但比范德华力强，**不属于化学键**

4. 存在：
   1. $\ce{H_2O、HF、NH_3}$、含氧酸、含氧酸的酸式盐、醇、羧酸、酚等

   2. 醛、酮等有机物，虽有 $\ce{H_2O}$ 存在，但与 $\ce{H}$ 原子直接连接的是电负性较小的 $\ce{C}$，故分子之间不能形成氢键

5. 氢键和范德华力共存：

   如 $\ce{H_2O、HF、NH_3}$ 的分子之间 **既存在范德华力**，**又存在氢键**。因此，把冰融化或把水汽化不仅要破坏范德华力，还必须提供额外的能量破坏分子间氢键，不能认为有氢键就不存在范德华力

#### 特点

1. **方向性**

   $X-H\cdots Y$ 三个原子一般在同一直线上，在这样的方向上成键两原子电子云之间的排斥力最小，形成的氢键最强，体系最稳定

   <img src="./images/2.6.png"  style="zoom: 25%;"/>

2. **饱和性**

   每一个 $X-H$ 只能与 $1$ 个 $Y$ 原子形成氢键，这是因为 $\ce{H}$ 原子半径很小，若再有一个原子 $Y$ 接近时，则 $Y$ 会受到 $X$ 原子电子云的排斥

   > <img src="./images/2.7.png"  style="zoom:25%;" />
   >
   > 平均 $1$ 分子 $H-F$，只有 $1$ 个氢键；平均 $1$ 分子 $\ce{NH_3}$，只有 $1$ 个氢键；平均 $1$ 分子 $\ce{H_2O}$，只有 $2$ 个氢键

#### 分子内氢键与分子间氢键

邻羟基苯甲醛能形成分子内氢键，而对羟基苯甲醛能形成分子间氢键。当对羟基苯甲醛熔融时，需要消耗较多的能量克服分子间氢键，所以对羟基苯甲醛的熔点高于邻羟基苯甲醛。邻羟基苯甲酸和对羟基苯甲酸也有类似的现象

<img src="./images/2.8.png"  style="zoom:33%;" />

> 总结：形成分子内氢键会降低物质熔点 （意味着分子间氢键数目减少，熔点降低）

#### 氢键对物质物理性质的作用

1. 含有分子间氢键的物质具有较高的熔点、沸点

   > <img src="./images/2.9.png"  style="zoom:28%;"/>
   >
   > $\ce{H_2O > H_2Te > H_2Se > H_2 S}$
   >
   > $\ce{HF > HI > HBr > HCl}$
   >
   > $\ce{NH_3 > SbH_3 > AsH_3 > PH_3}$
   >
   > $\ce{H_2O > HF > NH_3}$

2. 形成分子内氢键会降低物质熔点

3. 含有分子间氢键的液体一般黏度比较大

4. 分子间氢键的存在使溶质在水中的 **溶解度** 比较大

5. 含有分子内氢键的物质具有 **较低的熔、沸点**

6. 对物质密度的影响：氢键的存在会使某些物质的密度反常，如水的密度比冰的密度大

7. 对相对原子质量测定的影响：例如接近水的沸点的水蒸气的相对分子质量测定值比按化学式 $\ce{H_2O}$ 计算出来的相对分子质量大一些，原因是水分子因氢键而相互缔合

## 分子晶体的概念

1. 概念：只含 **分子** 的晶体，或者分子间以 **分子间作用力** 结合形成的晶体

2. 分子晶体中的粒子及粒子间的相互作用

   $$
   分子晶体 \begin{cases}
   构成微粒 & \longrightarrow  & 分子\\
   微粒间的作用力 & \longrightarrow  & 分子间作用力\\
   分子内各原子间 & \longrightarrow  & 共价键\\
   \end{cases}
   $$

3. 常见的典型分子晶体
   1. 所有 **非金属氢化物**：如 $\ce{H_2O}、\ce{H_2S}、\ce{NH_3}、\ce{CH_4}、\ce{HX}$ (卤化氢)等

   2. 部分 **非金属单质**：如 $X_2$ (卤素单质)、$\ce{O_2}、\ce{H_2}、\ce{S_8}、\ce{P_4}、\ce{C_{60}}$ 、稀有气体等

   3. 部分 **非金属氧化物**：如 $\ce{CO_2}、\ce{SO_2}、\ce{NO_2}、\ce{P_4O_6}、\ce{P_4O_{10} }$ 等

   4. 几乎所有的 **酸**：如 $\ce{H_2SO_4}、\ce{HNO_3}、\ce{H_3PO_4}、\ce{H_2SiO_3}$ 等

   5. 绝大多数 **有机物** ：如 苯、四氯化碳、乙醇、冰醋酸、蔗糖 等

4. 分子晶体的物理性质
   1. **分子晶体熔、沸点较低 ，硬度很小** （多数分子晶体在常温时为气态或液态）

      > 除 $\ce{Hg}$ 、离子液体 外，常温常压下呈气体或液体都是分子晶体

   2. 分子晶体不导电

   3. 分子晶体的溶解性一般符合「 **相似相溶** 」规律

      > $\ce{Br_2}$ 与 $\ce{CCl_4}$ 均为非极性分子，「相似相溶」，可相互溶解
      >
      > 而 $\ce{Br_2}$ 不易溶于 $\ce{H_2O}$ （极性分子）

|   堆积类型   |                  分子密堆积                  |                     分子非密堆积                     |
| :----------: | :------------------------------------------: | :--------------------------------------------------: |
| 微粒间作用力 |                 **范徳华力**                 |                  **范德华力和氢键**                  |
|   空间特点   |     通常每个分子周围有 $12$ 个紧邻的分子     | 每个分子周围紧邻的分子数小于 $12$ 个，空间利用率不高 |
|     举例     | $\ce{C_{60} }$、干冰、$\ce{I_2}$、$\ce{O_2}$ |              $\ce{HF}$、$\ce{NH_3}$、冰              |

## 常见分子晶体的结构分析

### 分子非密堆积：冰晶体

1. 条件：分子间的主要作用力是氢键

2. 结构：冰晶体中，水分子间主要通过 **氢键** 形成晶体。由于氢键具有一定的 **方向性**，一个水分子与周围四个水分子结合，这四个水分子也按照同样的规律再与其他的水分子结合。

   这样，**每个 $\ce{O}$ 原子周围都有四个 $\ce{H}$ 原子，其中两个 $\ce{H}$ 原子与 $\ce{O}$ 原子以共价键结合，另外两个 $\ce{H}$ 原子与 $\ce{O}$ 原子以氢键结合**，使水分子间构成 **四面体** 骨架结构。其结构可用下图表示

   <img title="" src="./images/2.2.png" style="width:250px" />

3. 性质：由于氢键具有方向性，冰晶体中水分子未采取密堆积方式，这种堆积方式使冰晶体中水分子的空间利用率不高，留有相当大的空隙。当冰刚刚融化成液态水时，水分子间的空隙 **减小** ，密度反而增大，超过 $4 \ce{°\!C}$ 时，分子间距离 **加大** ，密度逐渐减小

### 分子密堆积：干冰

1. 条件：分子间作用力只有范德华力，无分子间氢键

2. 结构：固态 $\ce{CO_2}$ 称为干冰，干冰也是分子晶体。 $CO_2$ 分子内存在 $C\xlongequal{} O$ 共价键，分子间存在 **范德华力** ， $CO_2$ 的晶胞呈面心立方体形，立方体的每个顶角有一个 $CO_2$ 分子，每个面上也有一个 $CO_2$ 分子。每个 $\ce{CO_2}$ 分子与 $12$ 个 $CO_2$ 分子等距离相邻(在三个互相垂直的平面上各 $4$ 个或互相平行的三层上，每层上各 $4$ 个)

<img title="" src="./images/2.3.png" style="width:350px" />

3. 性质：干冰的外观很像冰，硬度也跟冰相似，熔点却比冰低得多，在常压下极易升华，在工业上广泛用作制冷剂；由于干冰中的 $\ce{CO_2}$ 之间只存在 **范德华力** 不存在 **氢键** ，密度比 **冰** 的高。


---

## Original file: 03 共价键 共价晶体.md

---
description: "讲解共价键的概念、形成机制、类型包括σ键和π键的特点，以及极性共价键和配位共价键的区别。"
---

# 03 · 共价键 共价晶体

## 共价键

1. **概念**：原子间通 **过共用电子对** 所形成的相互作用，叫做 **共价键**

2. **成键粒子**：通常是 **电负性相同或差值小**（小于 $1.7$）的非金属原子或金属原子与非金属原子

3. **本质**：原子间通过 **原子轨道重叠**，高概率地出现在两个原子核之间的电子与两个原子核之间的电性作用

<img title="" src="./images/3.1.svg" width="180">

4. **共价键的形成**
   1. 当两个氢原子相互接近时，若两个氢原子核外电子的 **自旋方向相反**，它们接近到一定距离时，两个 $1s$ 轨道发生重叠，电子在两原子核间出现的机会较大。**随着核间距的减小，核间电子出现的机会增大，体系的能量逐渐下降，达到能量最低状态**。核间距进一步减小时，两原子间的斥力使体系的能量迅速上升这种排斥作用又将氢原子推回到平衡位置。氢分子的形成过程中能量（主要指势能）随核该间距的变化如图所示
   2. 若两个氢原子核外电子的自旋方向相同，当它们相互接近时，原子间总是排斥作用占主导地位。所以两个带有自旋方向相同的电子的氢原子不可能形成氢分子
      <img title="" src="./images/3.2.png" width="180">

### 共价键的类型

#### $\sigma$ 键（成键方式）

1. **形成**：由两个原子的 $s$ 轨道或 $p$ 轨道「**头碰头**」重叠形成
2. **类型**
   1. $s-s$ 型：（$H-H$ 的 $s-s$ $ σ $ 键的形成）
      <img title="" src="./images/3.3.png" width="250">
   2. $s-p$ 型：（$H-Cl$ 的 $s-p$ $ σ $ 键的形成）
      <img title="" src="./images/3.4.png" width="250">
   3. $p-p$ 型：（$Cl-Cl$ 的 $p-p$ $ σ $ 键的形成）
      <img title="" src="./images/3.5.png" width="250">
3. **特征**
   以形成化学键的两原子核的连线为轴做旋转操作，共价键电子云的图形不变，这种特征称为 **轴对称**；$\sigma$ 键的强度较大（稳定性较高）

#### $\pi$ 键（成键方式）

1. **形成**：由两个原子的 $p$ 轨道或轨道「**肩并肩**」重叠形成
2. $p-p$ $\pi$ 键：（$H-H$ 的 $s-s$ $ σ $ 键的形成）
   <img title="" src="./images/3.6.png" width="430">
3. **特征**
   $\pi$ 键的电子云具有 **镜面对称性** 即每个 $\pi$ 键的电子云由两块组成，分别位于由两原子核构成平面的两侧，如果以它们之间包含原子核的平面为镜面，它们互为镜像；**$\pi$ 键不能旋转，不如 $\sigma$ 键牢固，较易断裂** (所以优先形成 $\sigma$ 键)

> **以 $N_2$ 的共价键为例**
>
> 电子式：$N \equiv N$
> <img title="" src="./images/3.8.png" width="350">

#### 极性共价键与非极性共价键（电子偏向）

见 [3.3 分子的极性 手性分子](/03%20%E5%88%86%E5%AD%90%E7%A9%BA%E9%97%B4%E7%BB%93%E6%9E%84%E4%B8%8E%E7%89%A9%E8%B4%A8%E6%80%A7%E8%B4%A8/03%20%E5%88%86%E5%AD%90%E7%9A%84%E6%9E%81%E6%80%A7%20%E6%89%8B%E6%80%A7%E5%88%86%E5%AD%90.md)

#### 配位共价键与一般共价键（成键过程）

见 [3.4 配合物与超分子](/03%20%E5%88%86%E5%AD%90%E7%A9%BA%E9%97%B4%E7%BB%93%E6%9E%84%E4%B8%8E%E7%89%A9%E8%B4%A8%E6%80%A7%E8%B4%A8/04%20%E9%85%8D%E5%90%88%E7%89%A9%E4%B8%8E%E8%B6%85%E5%88%86%E5%AD%90.md)

### 成键规律判断

1. 共价单键是 $\sigma$ 键

2. 共价双键中一个是 $\sigma$ 键，另一个是 $\pi$ 键

3. 共价三键中一个是 $\sigma$ 键，另两个是 $\pi$ 键

>  <img title="" src="./images/3.7.svg" width="250">

> 注意：
>
> 1. 如给出有机物的结构式，有可能会省略 $\ce{H}$ 原子
> 2. 注意是否需要加上单位（ $\ce{N_A}$ ）

### 共价键的键参数

#### 键能

1. 共价键的强弱可用键能来衡量。**键能是指气态分子中 $1mol$ 化学键解离成气态原子所吸收的能量**。它通常是 $298.15K$、$100kPa$ 条件下的标准值，单位是 $kJ\cdot mol^{-1}$
2. 应用
   1. **判断共价键的稳定性**
      原子间形成共价键时，原子轨道重叠程度越大，释放能量越多，所形成的共价键键能越大，共价键越稳定
   2. **判断分子的稳定性**
      一般来说，结构相似的分子，共价键的键能越大，分子越稳定
      > 如分子的稳定性：$HF>HCl>HBr>HI$
   3. **利用键能计算反应热**
      $$△H=反应物总键能-生成物总键能$$

#### 键长

1.  **概念**
    构成化学键的两个原子的核间距，因此原子半径决定共价键的键长，原子半径越小，共价键的键长越短
2.  **应用**
    共价键的键长越短，**往往** 键能越大，表明共价键越稳定，反之亦然 > 键长：$C\equiv C<C=C<C-C$ > 键能：$C\equiv C>C=C>C-C$

        > 例外：（键氟三）
        > 键长：$F_2<Cl_2<Br_2<I_2$
        > 键能：$Cl_2>Br_2>F_2>I_2$

        > 注意：共价键的键能不一定能反映其熔沸点
        >
        > 例如：对 $\ce{Cl2、Br2}$ ，有 键能：$\ce{Cl-Cl>Br-Br}$，但不能就此认为 沸点 $\ce{Cl2、Br2}$ ，因为两者都是分子晶体

        > 特殊：键长（$C-C$）$C_6H_6 < C_2H_6$
        >

    > 共价半径、范德华半径：两核间距离的一半
    > <img title="" src="./images/3.10.png" width="150">

#### 键角

1. **概念**：在多原子分子中，两个相邻共价键之间的夹角
2. **应用**：在多原子分子中键角是一定的，这表明共价键具有方向性，因此键角影响着共价分子的空间结构
   <img title="" src="./images/3.9.png" width="420">
3. **知识点**：
   1. 杂化类型: $s p ^ { 1 }  → 1 8 0 ^ { \circ }  ， s p ^ { 2 }  → 1 2 0 ^ { \circ }  ， s p ^ { 3 } → 1 0 9 ^ { \circ } 2 8 ^ { \prime }$
   2. 中心原子存在孤电子对，对成键电子对有较大的排斥力，键角减小（半径相等时孤对电子分割更多圆周角）
      > 例: $C H _ { 4 } > N H _ { 3 } > H _ { 2 } O$
   3. （影响较小）双键对单键有较大的排斥力，单键键角减小（半径相等时双键分割更多圆周角）
      > 例: $C O C l _ { 2 }$ 中 $C$ 为中心原子，$\angle O - C - C l > \angle C l - C - C l$
   4. （影响较小）大体积的基团有较大的排斥力，单键键角减小（半径相等时大基团分割更多圆周角）
      > 例: $N H _ { 3 }  ， N H _ { 2 } O H  ， N H _ { 2 } \left( C H _ { 3 } \right)$ 中 $\angle H - N - H$ 递减
   5. 中心原子电负性增大，成键电子受到向中心更大的吸引力（半径减小），键角增大
      > 例: $N H _ { 3 } > P H _ { 3 }  ， H _ { 2 } O > H _ { 2 } S$
   6. 配原子电负性增大，成键电子受到向外侧更大的吸引力（半径增大），键角减小
      > 例: $N H _ { 3 } > N F _ { 3 }  ， H _ { 2 } O > O F _ { 2 }$

## 共价晶体

1. 概念：相邻原子间以 **共价键** 相结合形成共价键三维骨架结构的晶体。
2. 构成微粒：原子
3. 微粒间作用力：共价键
4. 典型的共价晶体
   1. 某些单质：如 **硼($B$)** 、 **硅($Si$)** 、**锗($Ge$)** 、 **金刚石** 等
   2. 某些非金属化合物：如 **碳化硅($SiC$)** 、**二氧化硅($SiO_2$)** 、**氮化硼($BN$)** 、**氮化硅($Si_3N_4$)** 等
   3. 极少数金属氧化物，如 **刚玉($α-Al_2O_3$)** 等
5. 物理性质 1. 共价晶体中，由于各原子均以强的共价键相结合，因此一般熔点 **很高** ，硬度 **很大** ，**难** 溶于常见溶剂，一般 **不导电** 2. 结构相似的共价晶体，原子半径越 **小** ，键长 **越短** ，键能越 **大** ，晶体的熔点越高 > > 熔点：$金刚石>金刚砂(SiC)>单晶硅$ > 键长：$C-C<Si-C<Si-Si$ > 键能：$C-C>Si-C>Si-Si$ >
   > 1. 共价晶体中不存在单个的分子
   > 2. 共价晶体汽化或熔化时破坏的作用力是共价键
   > 3. 共价晶体中只有其价键，但含有共价键的晶体不一定是共价晶体，如 $CO_2、H_2O$ 等分子晶体中也含有共价键

### 常见共价晶体的结构分析

#### 金刚石

1. 在金刚石晶体中每个碳原子周围紧邻的碳原子有 $4$ 个，每个碳原子都采取 $sp^3$ 杂化

2. 所有的 $C-C$ 键长相等，键角相等，键角为 $109^\circ28^\prime$

3. 晶体中每个 $C$ 参与了 $4$ 个 $C-C$ 键的形成，而在每个键中的贡献只有一半，故金刚石中 $ 1molC$ 原子含 $C-C$ 键数目为 $2N_A$

4. 整块金刚石晶体就是以共价键相连的三维骨架结构。其中最小的环是 **六元环**

5. 在金刚石晶胞中占有的碳原子数 $8$

6. 两个原子的最近距离：$\frac{\sqrt{3}}{4}\times晶胞参数$ （对角线的 $\frac{1}{4}$ ）

<img src="./images/2.4.png" style="zoom:45%;"/>

#### 二氧化硅

1. 杂化方式：$sp^3$ 杂化
2. 在 $SiO_2$ 晶体中，每个硅原子均与 $4$ 个氧原子结合；每个氧原子与 $2$ 个硅原子结合
3. 在 $SiO_2$ 晶体中硅原子与氧原子个数之比是 $1:2$
4. 在 $SiO_2$ 晶体中，每个硅原子形成 $4$ 个共价键；每个氧原子形成 $2$ 个共价键
5. 在 $SiO_2$ 晶体中，最小环为十二元环，有 $6$ 个硅原子和 $6$ 个氧原子
6. 硅原子个数与 $Si-O$ 共价键个数之是 $1:4$ ；氧原子个数与 $Si-O$ 共价键个数之比是 $1:2$
7. $SiO_2$ 晶体 中并不存在 $SiO_2$ 分子

<img title="" src="./images/2.5.png" width="180">

### 石墨晶体（混合型晶体）

1. **晶体类型**
   石墨晶体中既有共价键，又存在类似金属键的作用力，还有范德华力，属于 **混合型晶体**
2. **结构特点**
   1. 石墨晶体中，同层的碳原子采取 $sp^2$ 杂化形成共价键，每个碳原子通过共价键（$σ$ 键）与相邻的 $3$ 个碳原子相连，形成平面六元并环结构。层中 $C-C$ 键的键长( $142pm$ )、键角( $120°$ )相等。在同一平面的碳原子还各剩下一个 $p$ 轨道，它们相互平行且相互重叠，使 $p$ 轨道中的电子可在整个碳原子平面中运动
   2. 石墨晶体中，每个碳原子参与了 $3$ 个 $C-C$ 键的形成，每个 $C-C$ 键被 $2$ 个碳原子共用，因此每个碳原子成键数为 $1.5$；每个碳原子为 $3$ 个六元环共用，每个 $C-C$ 键被 $2$ 个六元环共用，每个六元环平均占有 $2$ 个碳原子、$3$ 个 $C-C$ 键
   3. 石墨晶体中层与层之间相隔距离较大( $335pm$ )，以范德华力相结合
      <img title="" src="./images/3.11.jpg" width="280">
3. 物理性质
   1. 石墨的熔点很高，比金刚石高，原因是石墨晶体中 $C-C$ 键的键长更短，键能更大
   2. 石墨质软，原因是石墨层与层间靠范德华力维系，可以发生层间的相对滑动
   3. 有良好的导电性，在同一层内，每个碳原子未参与杂化的 $p$ 轨道中的电子可以在整个碳原子平面中运动，形成大 $\pi$ 键。有类似金属晶体的导电性


---

## Original file: 04 金属键 金属晶体.md

---
description: "介绍金属键的概念和本质、电子气理论解释金属的延展性、导电性和导热性，以及金属晶体的熔沸点、硬度和常见堆积结构。"
---

# 04 · 金属键 金属晶体

## 金属键

1. **金属键的概念**
   除汞等少数金属外，大多数金属单质具有 **较高的熔点**，说明金属晶体中存在着 **强烈的相互作用**
   1. 金属键：金属阳离子与自由电子之间的强烈的相互作用
   2. 成键微粒： 金属阳离子和自由电子
   3. 存在：**金属单质** 或 **合金**
2. **金属键的本质**
   描述金属键本质的最简单理论是 「**电子气理论**」。该理论把金属键形象地描绘为金属原子脱落下来的价电子形成遍布整块晶体的「电子气」，被所有原子所共用，从而把所有的金属原子维系在一起，形成一种「巨分子」
3. **金属键的特征**
   金属键 **无方向性和饱和性**。金属晶体里的自由电子不专属于某几个特定的金属原子，而是几乎均匀地分布在整个晶体里，把所有金属原子维系在一起，所以金属键没有方向性和饱和性（共价键则有方向性和饱和性）
   <img title="" src="./images/4.1.png" height="90">

## 电子气理论解释金属的物理性质

1. **金属的延展性**
   弥漫在金属原子间的电子气可以起到类似轴承中滚珠之间润滑剂的作用。当金属晶体受到外力作用时，晶体中的各原子层就会发生相对滑动
   <img title="" src="./images/4.2.png" height="60">
2. **金属的导电性**
   在金属晶体中，存在许多自由电子，这些电子移动是没有方向的，但是 **在外加电场的作用下，自由电子就会发生定向移动，形成电流，使金属表现出导电性**
   当温度升高时，阳离子的振动加剧，对自由电子的定向移动产生了阻碍作用，故导电能力下降。金属导电的粒子是自由电子，而电解质溶液导电的粒子是自由移动的阴阳离子
   <img title="" src="./images/4.3.png" height="60">
3. **金属的导热性**
   自由电子在运动时与金属阳离子碰撞，引起两者能量的交换。当金属某部分受热时，那个区域里的自由电子能量增加，运动速度加快，通过碰撞，把能量传递给金属阳离子。自由电子与金属阳离子频繁碰撞，把能量从温度高的部分传递到温度低的部分，从而使整块金属达到相同的温度
4. 金属光泽：
   由于金属内部原子以最紧密堆积状态排列，且存在自由电子，所以当光线照射到金属表面时，**自由电子可以吸收所有频率的光并迅速释放**，使金属不透明且具有金属光泽。而金属在粉末状态时，晶格排列不规则，吸收可见光后反射不出去，所以金属粉末常呈暗灰色或黑色

## 金属晶体的熔沸点、硬度比较

1. 金属的熔沸点高低及硬度大小与金属键的强弱直接相关。金属键越强，金属的熔沸点越高，硬度一般也越大
2. **金属键的强弱主要取决于金属阳离子的半径和离子所带的电荷数**
3. 同周期金属单质，从左到右（如 $Na、Mg、AI$）熔、沸点逐渐升高同主族金属单质，从上到下（如碱金属）熔、沸点逐渐降低

   > $$
   > 熔点: Na < Mg < Al  \begin{cases}
   > 半径 & Na^+> Mg^{2+}> Al^{3+}\\
   > 电荷数 & Na^+< Mg^{2+}< Al^{3+}\\
   > \end{cases}
   > $$

4. 金属晶体熔点差别很大，如汞常温为液体，熔点很低 ( $-38.9\ce{°\!C}$ ) ，而铁等金属熔点很高( $1535\ce{°\!C}$ )，这是由于金属晶体紧密堆积方式、金属键强弱不同而造成的差别（碱金属的堆积方式类似，只考虑金属键强弱）
   > $碱金属熔点：Li>Na>K>Rb>Cs$ (常考)

## 常见金属结构

|                | 简单立方堆积                                            | 体心立方堆积                                                                        | 面心立方最密堆积                                                         | 六方最密堆积                                            |
| -------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | :------------------------------------------------------ |
| **原子位置**   | 顶角                                                    | 顶角、体心                                                                          | 顶角、面心                                                               |                                                         |
| **原子数**     | $8 \times \frac{1}{8}=1$                                | $8\times\frac{1}{8}+1=2$                                                            | $8\times\frac{1}{8}+6\times\frac{1}{2}=4$                                | $12\times\frac{1}{6}+2\times\frac{1}{2}+3=6$            |
| **配位数**     | $6$                                                     | $8$                                                                                 | $12$                                                                     | $12$                                                    |
| **空间利用率** | $\dfrac{\dfrac{4}{3}πr^3}{8r^3}\cdot100\%\approx52.4\%$ | $\dfrac{2\cdot \dfrac{4}{3}πr^3}{(\dfrac{4}{\sqrt{3}}r)^3}\cdot100\%\approx68.02\%$ | $\frac{4\cdot \dfrac{4}{3}πr^3}{16\sqrt{2}r^3}\cdot 100\%\approx74.05\%$ | $\frac{8\pi R^3}{24\sqrt2R^3}\times100\%\approx74.05\%$ |
| **代表金属**   | $Po$                                                    | $Na、K、Fe、Li、Ba$                                                                 | $Cu、Ag、Au、Al、Pd、Ca$                                                 | $Mg、Zn、Ti$                                            |

> 性质: 原子配位数越高，金属延展性、可塑性越好

> <img title="" src="./images/1.4.png" width="350">
>
> 钠晶胞（体心堆积）：钠原子：$8\times\frac{1}{8}+1=2$，配位数：$8$
>
> 铜晶胞（面心立方最密堆积）：铜原子：$8\times\frac{1}{8}+6\times\frac{1}{2}=4$，配位数：$12$

> <img title="" src="./images/1.6.png" width="100">
>
> 六方最密堆积：分子数：$12\times\frac{1}{6}+2\times\frac{1}{2}+3=6$ 配位数：$12$


---

## Original file: 05 离子键 离子晶体.md

---
description: "讲解离子键的概念和特点、晶格能的定义和影响因素，以及离子晶体的物理性质如熔沸点、硬度、导电性和溶解性。"
---

# 05 · 离子键 离子晶体

## 离子键

1. 概念：带相反电荷离子之间的相互作用称为离子键（ionic bond）。其成键粒子为阴阳离子，相互作用为 **静电作用**（引力和斥力），成键过程为：阴阳离子接近到某一定距离时， 吸引和排斥达到平衡
2. 离子键没有 **方向性** 和 **饱和性**，因此，以离子键结合的微粒倾向于形成紧密堆积，使每个离子周围尽可能多地排列带异性电荷的离子，从而达到稳定结构

### 晶格能

1. 概念：离子晶体中阴、阳离子间相互作用力的大小可用晶格能（lattice energy）来衡量。**晶格能**（符号为 $U$）是指拆开 $1 mol$ 离子晶体使之形成气态阴离子和气态阳离子时所吸收的能量。例如
   $$NaCl(s)\rightarrow Na^+(g)+Cl^-(g) \qquad U=786 kJ·mol^{-1}$$
2. **影响因素**：
   1. **离子的电荷数**：离子所带的电荷数越多，晶格能越大
   2. **离子半径**：离子半径越小，晶格能越大
3. 与离子晶体性质的关系
   **晶格能越大，形成的离子晶体更稳定，熔点更高，硬度更大**

## 离子晶体

1. 概念：由 **阳离子** 和 **阴离子** 相互作用而形成的晶体
2. 相互作用力：阴、阳离子间以离子键结合，离子晶体中还可能存在共价键、氢键等
3. 常见的离子晶体：强碱、活泼金属的氧化物和过氧化物、大部分的盐

> **离子晶体相关概念理解时的注意点**
>
> 1. 离子晶体中无分子。如 $NaCl$、$CsCl$ 只表示晶体中阴、阳离子的个数比，为化学式，不是分子式
> 2. 由金属元素和非金属元素形成的晶体不一定是离子晶体，如 $AlCl_3$，是分子晶体；全由非金属元素形成的晶体也可能是离子晶体，如 $NH_4Cl、NH_4NO_3$，等铵盐的晶体为离子晶体
> 3. 离子晶体中一定存在离子键，除离子键外可能有其他类型的化学键。如 $NaOH$ 晶体中除有钠离子与氢氧根离子间的离子键外，还有氢氧根离子内氢原子和氧原子间形成的极性共价键
> 4. 离子晶体中，每一个离子周围排列的带相反电荷的离子数目都是固定的，不是任意的
> 5. 对于超导材料，一般暗示为离子晶体

### 物理性质

1. **熔沸点**
   离子晶体具有 **较高的熔、沸点**，难挥发。离子晶体中，阴、阳离子间有强烈的相互作用（离子键），要克服离子间的相互作用力使物质熔化或沸腾，就需要较多的能量。因此，离子晶体具有熔、沸点较高和难挥发的性质 > > 注意：> 1. 离子晶体的熔、沸点和硬度与离子键的强弱有关，**离子键越强**，离子晶体的 **熔、沸点越高**，**硬度越大** > 2. 离子键的强弱与离子半径和离子所带电荷数有关，**离子半径越小**，离子所带的 **电荷数越多**，**离子键越强** >

1. **硬度**
   **离子晶体硬而脆**。离子晶体中，阴、阳离子间存在较强的离子键，使晶体表现出较大的硬度，当晶体受到冲击力作用时，部分离子键发生断裂，导致晶体破碎

1. **导电性**
   **离子晶体固态时不导电，熔融状态或溶于水后能导电**。离子晶体中离子键较强，离子不能自由移动，即晶体中无自由移动的离子，因此固态时不导电。当温度升高时，阴、阳离子获得足够能量，克服了离子间的相互作用，成为自由移动的离子，在外界电场作用下，离子定向移动而导电
   离子化合物溶于水时，阴、阳离子受到水分子作用变成了自由移动的离子（或水合离子），在外加电场作用下，阴、阳离子定向移动而导电

1. **溶解性**
   大多数离子晶体易溶于极性溶剂（如水），难溶于非极性溶剂（如汽油、煤油）。当把离子晶体放在水中时，极性水分子对离子晶体中的离子产生吸引作用，使晶体中的阴、阳离子克服了离子间的相互作用而发生电离，变成在水中自由移动的离子

## 常见离子晶体的结构

1. $NaCl$ 晶胞
   <img title="" src="./images/5.1.png" width="120">
   $NaCl$ 晶胞如图所示，每个 $Na^+$ 周围距离最近的 $Cl^-$ 有 $6$ 个，构成正八面体。每个 $Cl^-$ 周围距离最近的 $Na^+$ 有 $6$ 个，构成正八面体，由此可推知晶体的化学式为 $NaCl$
   1. 每个 $Na^+(Cl^-)$ 周围距离相等且最近的 $Na^+(Cl^-)$ 是 $12$ 个
   2. 每个晶胞中实际拥有的 $Na^+$ 数是 $4$ 个，$Cl^-$ 数是 $4$ 个
   3. 若晶胞参数为 $a$ $pm$，则氯化钠晶体的密度为 $\frac{234}{N_A\cdot a^3\times10^{-30}} g·cm^{-3}$
2. $CsCl$ 晶胞
   <img title="" src="./images/5.2.png" width="120">
   $CsCl$ 晶胞如图所示，每个 $Cs^+$ 周围距离最近的 $Cl^-$ 有 $8$ 个，每个 $Cl^-$ 周围距离最近的 $Cs^+$ 有 $8$ 个，它们均构成正六面体，由此可推知晶体的化学式为 $CsCl$
   1. 每个 $Cs^+(Cl^-)$ 周围距离最近的 $Cs^+(Cl^-)$ 有 $6$ 个，构成 正八面体
   2. 每个晶胞中实际拥有的 $Cs^+$ 有 $1$ 个，$Cl^-$ 有 $1$ 个
   3. 若晶胞参数为 $a$ $pm$，则氯化铯晶体的密度为 $\frac{168.5}{N_A\cdot a^3\times10^{-30}}g·cm^{-3}$
3. $CaF_2$ 晶胞
   <img title="" src="./images/1.5.png" width="120">
   1. $Ca^{2+}$ 的堆积方式为面心立方堆积，$F^-$ 所处位置为 $8$ 个小正方体的体心
   2. $Ca^{2+}$ 呈立方密堆积，阴离子 $F^-$ 填充在四面体空隙中，位于对角线的 $\frac{1}{4}$ 和 $\frac{3}{4}$ 处。$Ca^{2+}、F^-$ 离子的配位数分别为 $8$ 和 $4$
   3. 在一个晶胞中有 $4$ 个 $Ca^{2+}$、$8$ 个 $F^-$


---

## Original file: index.md

---
description: 本章聚焦分子间作用力、化学键与晶体结构，覆盖分子晶体、共价晶体、金属晶体和离子晶体的性质与常见考点。
---

# 02 微粒间作用力与物质性质

<CCChapterOverview />


---

## Original file: 考点 化学键与相互作用力.md

---
description: "总结化学键（共价键、离子键、金属键）和分子间作用力（范德华力、氢键）的性质、影响因素，以及化学键键角的比较方法。"
---

# 考点 · 化学键与相互作用力

## 考点一 化学键与相互作用力性质总结

|          | 总结                                                                                                                                                                                                                                       | 影响因素                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 共价键   | 原子之间共用电子形成的化学键，本质是高概率地出现在两个原子核之间的电子与两个原子核之间的电性作用；**具有方向性和饱和性**                                                                                                                   | $键能 \propto \frac { 1 } { 键长 } \propto \frac { 1 } { r }$ |
| 离子键   | 阴阳离子通过静电作用形成的化学键，本质是离子间引力与斥力平衡(实质是静电作用)；**无方向性和饱和性**，但成键数目受到空间体积的限制                                                                                                           | $键能 \propto\frac{Q}{r}$                                     |
| 金属键   | 自由电子与金属阳离子间的相互作用，本质类似于共价键，也是电性作用；**无方向性和饱和性**。金属键导致产生了金属光泽、导电性、导热性                                                                                                           | $键能 \propto\frac{Q}{r}$                                     |
| 范德华力 | 分子间普遍存在的一种短程相互作用力，是指也是电性作用，不属于化学键，属于分子间作用力；**无方向性和饱和性**。范德华力可提升物质熔沸点                                                                                                       | $作用力大小 \propto M$                                        |
| 氢键     | 一个裸露的 原子核与相邻原子产生静电相互作用和一定的轨道重叠作用，不属于化学键，属于分子间作用力；**有方向性和饱和性**。一般只有 $O、N、F$ 可以形成。分子间氢键可显著提升物质熔沸点，与水形成分子间氢键增大溶解度，形成分子内氢键降低溶解度 | $作用力大小 \propto 氢键原子电负性$                           |

## 考点二 化学键键角比较

依次从以下角度考虑

1. **杂化方式**

   $sp>sp^2>sp^3$

2. **孤电子对**

   孤电子对的斥力是大于成键电子的斥力

   > $\ce{H2O(两对孤电子)>NH3(一对孤电子)>CH4(没有孤电子)}$

3. **电负性**

   情况一：**中心原子**不同，电负性大的原子，吸引电子的能力越强，键角更**大**

   > 可以理解为，电负性大的原子将成键电子吸引，会把键角撑开，键角更大

   > 电负性：$\ce{N>P>As}\quad$ 键角：$\ce{NH3>PH3>AsH3}$

   情况二：**配位原子**不同，电负性大的原子，键角更**小**

   > 电负性：$\ce{F>Cl}\quad$ 键角：$\ce{NF3<NCl3}\quad$

4. **多重键**

   斥力：三键 $>$ 双键 $>$ 单键

   > 甲醛的 $\ce{∠ O-C-H}$ > $\ce{∠ H-C-H}$

   第二周期元素的氟化物的键角小于相应的氢化物，而其他周期元素则有相反的规律

   > 第二周期：$\ce{NF3<NH3\quad OF2<OH2}$
   >
   > 第三周期：$\ce{PF3>PH3\quad AsF3<AsH}$

5. **单电子与孤对电子对键角影响**

   单电子对成键电子对的排斥力**小于**孤电子对对成键电子对的斥力

   > 键角：$\ce{NO^+_2>NO2>NO^-_2 }\quad$
   > 理由：①$\ce{NO^+_2}\quad$为sp杂化，其余为sp^2杂化
   > ②单电子对成键电子对的排斥力**小于**孤电子对对成键电子对的斥力

6. **配体体积对键角影响**

   当配体基团体积较大时，基团电子云占据的空间也会相应**增大**，对相邻键有很强的**排斥**作用

   > ∠H-N-H键角比较：$\ce{NH3>NH2OH>NH2(CH3)}\quad$


---

## Original file: 考点 晶体结构与性质.md

---
description: "总结分子晶体、共价晶体、离子晶体和金属晶体的构成微粒、作用力、性质和判断方法，包括常见物质类别和例外情况。"
---

# 考点 · 晶体结构

## 考点一 晶体类型

|              | 分子晶体 $^1$                                                                                              | 共价晶体 $^2$                                                                                        | 离子晶体                               | 金属晶体             |
| ------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------- | -------------------- |
| 构成微粒     | 分子                                                                                                       | 原子                                                                                                 | 阴、阳离子                             | 金属阳离子和自由电子 |
| 微粒间作用力 | 分子间作用力                                                                                               | 共价键                                                                                               | 离子键（部分含共价键）                 | 金属键               |
| 典例         | 冰($H_2O$)、$P_4$、$I_2$、干冰($CO_2$)等                                                                   | 金刚石 $^3$、晶体硅、$SiO_2$、$SiC$ 等                                                               | $NaCl$、$NaOH$ 等                      | $Na、Mg、Al、Fe$ 等  |
| 硬度         | 较小                                                                                                       | 高硬度                                                                                               | 硬而脆                                 | 一般较高，部分较低   |
| 熔、沸点     | 低 $^4$                                                                                                    | 高                                                                                                   | 较高                                   | 一般较高，部分较低   |
| 溶解性       | 相似相溶                                                                                                   | 不溶于任何溶剂                                                                                       | 多数溶于水                             | 不溶于任何溶剂       |
| 导电性       | 固态不导电，部分溶于水能导电                                                                               | 多数不导电，部分为半导体                                                                             | 固态不导电，熔融态 $^5$ 或溶于水能导电 | 良好                 |
| 导热性       | 不良                                                                                                       | 不良（金刚石的导热性极好）                                                                           | 不良                                   | 良好                 |
| 常见物质类别 | ①所有非金属氢化物 <br>②部分非金属单质 <br/>③部分非金属氧化物 <br/>④几乎所有的酸 <br/>⑤绝大多数有机物的晶体 | ①某些单质（金刚石、硼、硅、灰锡等） <br/>②某些非金属化合物 ③极少数金属氧化物（刚玉$Al_2O_3$ ） <br/> | 离子化合物 $^6$                        | 金属单质及其合金     |

> $^1$ 分子晶体判断：1.溶、沸点低；2.有分子式；3.一般为非金属元素组成，但 $AlCl_3$ 是分子晶体，$NH_4Cl$ 等铵盐不是分子晶体。注意惰性气体分子均为单原子分子
>
> $^2$ 共价晶体：一般由非金属元素构成，但熔沸点高，硬度大，特别是第 $ⅥA$ 族 $C$、$Si$ 及其化合物，往往为共价晶体
>
> $^3$ 石墨不是共价晶体，是混合晶体
>
> $^4$ 分子晶体特征：熔沸点较低，常温下多为液态、气态（除去汞与离子液体外，常温下为液体、气体的晶体，均为分子晶体）
>
> $^5$ 熔融导电是离子晶体的特征
>
> $^6$ 离子化合物：大多由金属元素与非金属元素组成，除了少数特例如 $AlCl_3$ 以外，铵盐由非金属元素组成，但是是离子晶体

过渡晶体：介于典型四种晶体之间的晶体，如离子晶体与共价晶体之间的过渡晶体

混合型晶体：石墨晶体属于混合型晶体，碳原子呈 $sp^2$ 杂化，形成平面六元并环结构（类似共价晶体），层与层之间靠范德华力维持，易断裂（类似分子晶体）。从性质看，石墨有类似金属晶体的导电性，但只能沿着石墨平面的方向

## 考点二 晶体类型判断

1. **根据构成晶体的粒子和粒子间的作用力类别进行判断**
   1. 由阳离子和阴离子相互作用而形成的晶体属于离子晶体

   2. 分子间通过分子间作用力（包括氢键）相结合形成的晶体属于分子晶体

   3. 相邻原子间通过共价键结合形成的具有三维骨架结构的晶体属于共价晶体

   4. 金属阳离子和自由电子之间通过强烈的相互作用（金属键）形成的晶体属于金属晶体

2. **根据物质所属类别判断**
   1. 活泼金属氧化物($Na_2O$、$CaO$)、强碱和绝大多数盐类属于离子晶体（$AlCl_3$、$BeCl_2$ 例外，属于分子晶体）

   2. 所有非金属氢化物、部分非金属单质（除金刚石、石墨、晶体硅、硼外）、部分非金属氧化物(除 $\ce{SiO_2}$ 外)、几乎所有的酸和绝大多数有机物（除有机盐外）均属于分子晶体

   3. 金属单质（除汞、灰锡外）和合金属于金属晶体

   4. 金刚石、晶体硅、二氧化硅、碳化硅、硼等属于共价晶体

3. **根据各类晶体的特征性质判断**

   主要是根据物质的物理性质，如熔点、沸点、溶解性、导电性等进行判断
   1. **根据晶体的熔、沸点判断**：熔、沸点低的单质和化合物一般为分子晶体；熔、沸点较高的化合物一般为离子晶体；熔、沸点很高的晶体一般为共价晶体

   2. **依据导电性判断**：离子晶体处于固态时不导电，溶于水及处于熔融状态时能够导电；共价晶体不导电；分子晶体处于固态及熔融状态时均不导电，但部分分子晶体溶于水后能电离形成自由移动的离子，能够导电（如 $HCl、H_2SO_4$ 等），属于非电解质的分子晶体（如酒精、蔗糖等）的水溶液不导电；金属晶体是电的良导体

   3. **根据硬度和机械强度判断**：离子晶体硬度较大，难以压缩；共价晶体硬度大；金属晶体多数硬度较大，且具有金属光泽，有延展性；分子晶体的硬度小

## 考点三 有关晶胞结构的分析与计算

有关晶胞结构的分析与计算类题目的解题思路一般如下：

1. 截取一个晶胞或晶胞中的一部分（如 $NaCl$ 晶胞中的一个小立方体）

2. 用均摊法确定晶胞或截取的部分中所包含的原子或离子数目($N$)，进而可确定晶体的化学式

3. 计算晶胞中所包含的微粒或微粒组合（如 $CaF_2$）的物质的量：$n=\cfrac{N}{N_A}$

4. 计算晶胞的质量：$m=n\cdot M=\cfrac{N}{N_A}\cdot M$

5. 计算晶胞的体积：对于立方晶胞，若边长为 $a$ $cm$，则体积 $V_{晶胞} =a^3$ $cm^3$ [对于长方体，

6. 若底面边长分别为$a$ $cm$、$b$ $cm$，高为$c$ $cm$，则体积$V_{晶胞} = abc$ $cm^3$]

7. 计算晶体的密度：$p = \cfrac { m } { V_{晶胞} } = \cfrac { N \cdot M } { N _ { A } \cdot a ^ { 3 } } g \cdot cm^{-3}$ 式子中涉及 $5$ 个物理量，已知其中 $4$ 个物理量便可计算第 $5$ 个物理量

8. 根据晶胞中微粒空间位置关系、微粒半径以及晶胞胞参数，利用几何知识计算 $2$ 个粒子之间的距离

9. 根据晶胞中所含有的原子的体积和晶胞的体积晶胞中原子的空间利用率（一般用于金属晶体）原子的体积 $V_{原子}=N\times \frac{4}{3}\pi r^3$ （其中中 $N$ 为晶胞含有的原子数目，$r$ 为原子半径），则空间利用率 $=\cfrac{ V_{原子} }{ V_{晶胞} }\times100\%$

10. 原子分数坐标：可以根据题中建系方式，利用投影法、截距法或对称法判断目标原子的分数坐标，默认取该晶胞的边长为 $1$

11. 「正四面体」空隙：原子周围最近的 $4$ 个原子形成正四面体结构

    「正八面体」空隙：原子周围最近的 $6$ 个原子形成正八面体结构

    <img title="" src="./images/7.1.jfif" style="width:300px">

> $1cm=10mm\quad 1mm=10^3\mu m\quad 1\mu m=10^3nm \quad 1nm=10^3pm$
>
> $1cm=10mm=10^4\mu m=10^7nm=10^{10}pm$
>
> $1cm^3=10^{21}nm^3=10^{30}pm^3$

## 考点四 晶体熔、沸点的比较

### 根据 物质的聚集状态

常温常压下，固体的熔沸点高于液体，液体的熔沸点高于气体

### 根据 晶体类型

$$
\text{共价晶体 > 离子晶体 > 分子晶体}
$$

### 同种类型的晶体熔、沸点比较

1. **共价晶体**：比较共价键的强弱。一般来说，**原子半径越小**，形成的共价键，**键长越短**，**键能越大**，其晶体 **熔沸点越高**。

   > 如熔点：金刚石 $>$ 碳化硅 $>$ 晶体硅

2. **离子晶体**：比较晶格能的大小。阴、阳离子所带 **电荷数越多**（主要因素），**离子半径越小**（次要因素），其 **晶格能越大**，其离子晶体的 **熔沸点就越高**

   > 如熔点：$\ce{MgO>MgCl2>NaCl>CsCl}$
   >
   > - $\ce{MgO}$ 和 $\ce{CaO}$ 为 $+2$ 价阳离子与 $-2$ 价阴离子所形成的离子晶体； $\ce{NaCl}$ 和 $\ce{KI}$ 为 $+1$ 价阳离子与 $-1$ 价阴离子所形成的离子晶体，因此 $\ce{MgO}$ 和 $\ce{CaO}$ 熔点高于 $\ce{NaCl}$ 和 $\ce{KI}$
   > - 离子半径：$\ce{Mg^2+ < Ca^2+}$ ，因此 $\ce{Mg^2+}$ 与 $\ce{O^2-}$ 间的作用力大于 $\ce{Ca^2+}$ 与 $\ce{O^2-}$ 间的作用力，所以熔点 $\ce{MgO>CaO}$
   > - 离子半径：$\ce{Na+ < K+}$ 且 $\ce{Cl- < I-}$，因此 $\ce{Na+}$ 与 $\ce{Cl-}$ 间的作用力大于 $\ce{K+}$ 与 $\ce{I-}$ 间的作用力，所以熔点 $\ce{NaCl>KI}$

3. **金属晶体**：金属 **离子半径越小**，**离子电荷数越多**，其金属氧离子与自由电子间 **作用越强**，金属 **熔、沸点较高**

4. **分子晶体**：
   1. **（优先考虑）** 含有 **氢键** 的物质，**熔、沸点较高** ，且氢键越多，**熔、沸点较高**

   2. **（优先考虑）** **分子内形成氢键**，相对于分子间氢键，相应的分子间作用力会 **减小** ，该物质的熔、沸点比同系列物质的 **熔、沸点低**

   3. **组成和结构相似** 的物质：**相对分子质量越大**，**范德华力越大**，**熔、沸点越高**。如：$O_2>N_2，HI>HBr>HCl$

   4. **相对分子质量相等或相近**：**极性分子** 的 **范德华力大**，**熔、沸点高**。如：$CO>N_2，CH_3OH>CH_3CH_3$

   5. 在烷烃的同分异构体中，一般来说，**支链数越多**，熔、沸点越低。如沸点：正戊烷 $>$ 异戊烷 $>$ 新戊烷；芳香烃以及衍化物苯环上的同分异构体一般按照「邻位 $>$ 间位 $>$ 对位」的顺序


---



# Chapter 03 分子空间结构与物质性质

Source directory: `03 分子空间结构与物质性质`

## Original file: 01 价层电子对互斥模型.md

---
description: "介绍价层电子对互斥模型（VSEPR）的原理、价层电子对数的计算方法，以及如何预测分子的立体构型。"
---

# 01 · 价层电子对互斥模型

- 价层电子对互斥模型（**V**alence **S**hell **E**lectron **P**air **R**epulsion , **$\text{VSEPR}$** ）可以用来预测分子的立体模型

- 理论认为，分子的空间构型是中心原子周围的「价层电子对」相互排斥的结果。价层电子对是指分子中的中心原子与结合原子间的 **$\sigma$ 键电子对** 和 **中心原子上的孤电子对**，由于相互排斥作用，尽可能趋向彼此远离，**排斥力最小**

- 多重键只计其中的 $\sigma$ 键电子对，**不计 $\pi$ 键电子对**

## 判断分子中中心原子上的价层电子对数

### 情况一 题目给定分子式

$$
(中心原子)价层电子对数 = 孤电子对数+ \sigma 键个数(即成键电子对数)\\
孤电子对数 =\frac{1}{2}(a-xb)=\frac{1}{2}(中心原子的价电子数\pm离子电荷数-配原子为了稳定需要的电荷数\times配原子个数)
$$

> $a$ :中心原子的价电子数（阳离子要减去电荷数、阴离子要加上电荷数）；
>
> $x$ :配原子个数(与中心原子结合的原子数)；
>
> $b$(配原子为了稳定需要的电荷数) ：与中心原子结合的原子最多能接受的电子数之和
>
> 例如：氢为 $1$，其他原子为 “$8$ 减去该原子的价电子数”，如氧和氧族元素中的 $\ce{S、Se}$ 等均为 $2$，卤族元素均为 $1$；等等 ）

|   分子或离子    | 中心原子 |   $a$   | $x$ | $b$ |         孤电子对数          | 价层电子对数 |          说明           | $\text{VSEPR}$ 模型 |
| :-------------: | :------: | :-----: | :-: | :-: | :-------------------------: | ------------ | :---------------------: | :-----------------: |
|   $\ce{SO_2}$   | $\ce{S}$ |   $6$   | $2$ | $2$ | $\frac{1}{2}(6-2\times2)=1$ | $2+1=3$      | $2 \sigma + 1 孤电子对$ |     平面三角形      |
|   $\ce{NH+4}$   | $\ce{N}$ | $5-1=4$ | $4$ | $1$ | $\frac{1}{2}(4-4\times1)=0$ | $4+0=4$      | $4 \sigma + 0 孤电子对$ |     正四面体形      |
| $\ce{CO^{2-}3}$ | $\ce{C}$ | $4+2=6$ | $3$ | $0$ | $\frac{1}{2}(6-3\times2)=1$ | $3+0=3$      | $3 \sigma + 0 孤电子对$ |     平面三角形      |

> 注意：价层电子对数 $\neq \dfrac{\texttt{价电子数} }{2}$
>
> 价电子数：对于主族元素而言，最外层电子就是价电子；稀有气体没有价电子数。 对于副族元素而言，除了最外层电子外，次外层的 $d$ 电子也是价电子
>
> 价层电子对数： 成键电子对数 和 孤电子对数 的和

### 情况二 题目给定结构式

看最外层电子数可以形成几个共价键（包含 $\sigma$ 键和 $\pi$ 键），剩余的电子数/2，即为孤电子对数。如果是阳离子（或阴离子），则最外层电子数减去（或加上）其电荷的绝对值

> 1. [ 2020 全国卷 Ⅲ ] $\ce{B3H^{3-}6}$ 的结构为：
>
> <img src="./images/1.1.svg" style="height:100px;" align="center"/>
>
> $\ce{B}$ 原子最外层有 3 个电子，有 3 个电子形成共价键，无孤电子对，因此 $\ce{B}$ 原子的杂化轨道类型为：**$sp^2$**
>
> 2. <img src="./images/1.2.svg"/> 中的 $\ce{N}$ 最外层有 5 个电子，由 3 个电子形成共价键，因此，还剩下 2 个电子未形成共价键，因此， $\ce{N}$ 原子含一个孤电子对，杂化轨道类型为：**$sp^3$**

## $\text{VSEPR}$ 模型与分子空间结构

分子立体构型为实际构型，不包含孤电子对；$\text{VSEPR}$ 模型包含孤电子对

| 分子        | 价层电子对数 | $σ$ 键电子对数 | 孤电子对数 | $\text{VSEPR}$ 模型 | 分子立体构型 |
| ----------- | ------------ | -------------- | ---------- | ------------------- | ------------ |
| $\ce{CO_2}$ | $2$          | $2$            | $0$        | 直线形              | 直线形       |
| $\ce{BF_3}$ | $3$          | $3$            | $0$        | 平面三角形          | 平面三角形   |
| $\ce{SO_2}$ | $3$          | $2$            | $1$        | 平面三角形          | $V$ 形       |
| $\ce{CH_4}$ | $4$          | $4$            | $0$        | 正四面体形          | 正四面体形   |
| $\ce{NH_3}$ | $4$          | $3$            | $1$        | 四面体              | 三角锥       |
| $\ce{H_2O}$ | $4$          | $2$            | $2$        | 四面体              | $V$ 形       |

> 电子间排斥力大小：孤电子对 $-$ 孤电子对 $>$ 孤电子对 $-$ 成键电子对 $>$ 成键电子对 $-$ 成键电子对


---

## Original file: 02 杂化轨道理论.md

---
description: "讲解杂化轨道理论的概念和目的、sp3、sp2、sp杂化的特点，以及中心原子和孤电子对对杂化的影响。"
---

# 02 · 杂化理论体系

> 甲烷分子中， $C$ 的价电子是 $2s^2 2p^2$ , $C$ 原子的 $4$ 个价层原子轨道是 $3$ 个相互垂直的 $2p$ 和 $1$ 个球形的 $2s$ ; $H$ 的价电子是 $1s^1$
>
> 按照我们已经学过的价键理论，甲烷的 $4$ 个 $C-H$ 单键都应该是 $\sigma$ 键，然而，碳原子的 $4$ 个价层原子轨道是 $3$ 个相互垂直的 $2p$ 轨道和 $1$ 个球形的 $2s$ 轨道，用它们跟 $4$ 个氢原子的 $1s$ 原子轨道重叠，不可能得到正四面体构型的甲烷分子
>
> 为了解决这一矛盾，鲍林提出了杂化轨道理论

1. **杂化轨道**：在外界条件的影响下，原子内部能量相近的原子轨道重新组合为一组新的原子轨道，称为杂化轨道

2. **杂化目的**：原子轨道的电子云一头大一头小，成键时利用大的一头可以使电子云重叠程度更大，从而形成稳定的化学键。即杂化轨道增强的成键能力

3. **杂化轨道分类**：
   1. $sp^3$ 杂化：由 $1$ 个 $s$ 轨道和 $3$ 个 $p$ 轨道杂化而成，杂化轨道间夹角为 $109°28^′$，呈正四面体形

      $$
      \begin{aligned}
      {\displaystyle C^{*}\quad {\frac {↑ ↓ }{1s}}\;{\frac {↑ \,}{sp^{3}}}\;{\frac {↑ \,}{sp^{3}}}{\frac {↑ \,}{sp^{3}}}{\frac {↑ \,}{sp^{3}}}} \end{aligned}
      $$

      <img src="./images/2.3.jpg" width="300"/>

   2. $sp^2$ 杂化：由 $1$ 个 $s$ 轨道和 $2$ 个 $p$ 轨道杂化而成，杂化轨道间夹角为 $120°$，呈平面三角形

      $$
      \begin{aligned}
      {\displaystyle C^{*}\quad {\frac {↑ ↓ }{1s}}\;{\frac {↑ \,}{sp^{2}}}\;{\frac {↑ \,}{sp^{2}}}{\frac {↑ \,}{sp^{2}}}{\frac {↑ \,}   {2p}}} \end{aligned}
      $$

      <img src="./images/2.2.jpg" width="300"/>

   3. $sp$ 杂化：由 $1$ 个 $s$ 轨道和 $1$ 个 $p$ 轨道杂化而成，杂化轨道间夹角为 $180°$ ，呈直线形

      $$
      \begin{aligned}
      {\displaystyle C^{*}\quad {\frac {↑ ↓ }{1s}}\;{\frac {↑ \,}{sp}}\;{\frac {↑ \,}{sp}}{\frac {↑ \,}{p}}{\frac {↑ \,}{p}}} \end{aligned}
      $$

      <img src="./images/2.4.jpg" width="300"/>

## 中心原子对杂化的影响

当中心原子的杂化方式确定后，杂化轨道上的电子对就可以确定，从而分子的空间构型也就可以确定。但是，中心原子的孤电子对对杂化方式和分子构型也有影响。

孤电子对的排斥作用：孤电子对的排斥作用比成键电子对的排斥作用大，因此孤电子对的存在会使分子的空间构型发生改变

孤电子对的杂化：中心原子的孤电子对也可以参与杂化，从而影响分子的空间构型

<img src="./images/2.1.png" style="width:200px"/>

## 中心原子杂化类型和分子构型的相互判断

| 分子组成    | 中心原子的孤电子对 | 中心原子的杂化方式 | 分子空间构型 | 实例          |
| ----------- | ------------------ | ------------------ | ------------ | ------------- |
| $\ce{AB_2}$ | $0$                | $sp$               | 直线形       | $\ce{BeCl_2}$ |
| $\ce{AB_2}$ | $1$                | $sp^2$             | $V$ 形       | $\ce{SO_2}$   |
| $\ce{AB_2}$ | $2$                | $sp^3$             | $V$ 形       | $\ce{H_2O}$   |
| $\ce{AB_3}$ | $0$                | $sp^2$             | 平面三角形   | $\ce{BF_3}$   |
| $\ce{AB_3}$ | $1$                | $sp^3$             | 三角锥形     | $\ce{NH_3}$   |
| $\ce{AB_4}$ | $0$                | $sp^3$             | 四面体形     | $\ce{CH_4}$   |

## 大 $\pi$ 键

1. 定义

   在多原子分子或离子中如有 **相互平行的 $p$ 轨道**，它们连贯重叠在一起构成一个整体，$p$ 电子在多个原子间运动形成 $π$ 型化学键，这种不局限在两个原子之间的 $\pi$ 键称为 **离域 $π$ 键**，或共轭大 $π$ 键，简称**大 $π$ 键**

2. 条件

   **所有原子在同一平面**，中心原子采取 **$sp$ 杂化** 或 **$sp^2$ 杂化**

3. **表示方法：$\prod^{m}_{n}$**

   **其中，$n$ 指参与形成大 $\pi$ 键的原子数，$m$ 指参与形成大 $\pi$ 键的电子数**

### 判断大 $\pi$ 键

#### 常规判断方式

1. 观察给出的结构简式或画出结构简式

2. 判断各原子的杂化方式（一般为 $sp^2$ 杂化，有 $3$ 个杂化轨道）

3. 画出杂化轨道形成的 $\sigma$ 键，未形成 $\sigma$ 键的孤电子对用「<img src="./images/2.10.svg" height="25"/>」表示

4. 画出各原子剩余的价电子，它们存在于未杂化的 $p$ 轨道内，“肩并肩”重叠形成大 $\pi$ 键

> 吡啶 $\ce{C5H5N}$ 的结构分析:
>
> <img src="./images/2.11.svg" height="150"/>
>
> 1. $\ce{C}$ 原子和 $\ce{N}$ 原子均为 $sp^2$ 杂化，分子空间结构为平面形
> 2. 对 $\ce{N}$ 原子分析：
>    1. $\ce{N}$ 原子最外层有 $5$ 个价电子
>    2. $3$ 个杂化轨道中： $2$ 个用于形成 $\sigma$ 键， $1$ 个用于形成孤电子对
>    3. 还剩下 $1$ 个价电子放在未杂化的 $p$ 轨道内用以形成大 $\pi$ 键
> 3. 对 $\ce{C}$ 原子分析：
>    1. $\ce{C}$ 原子最外层有 $4$ 个价电子
>    2. $3$ 个杂化轨道中：全部 $3$ 个用于形成 $\sigma$ 键
>    3. 还剩下 $1$ 个价电子放在未杂化的 $p$ 轨道内用以形成大 $\pi$ 键
> 4. 总计以上在未杂化的 $p$ 轨道内的价电子一共 $6$ 个，参与原子 $6$ 个
> 5. 所以，大 $\pi$ 键类型为：$\prod^{6}_{6}$

> 咪唑 $\ce{C3H4N2}$ 的结构分析:
>
> <img src="./images/2.12.svg" height="150"/>
>
> 1. $\ce{C}$ 原子和 $\ce{N}$ 原子均为 $sp^2$ 杂化，分子空间结构为平面形
> 2. 对 $\ce{N^1}$ 原子分析：
>    1. $\ce{N}$ 原子最外层有 $5$ 个价电子
>    2. $3$ 个杂化轨道中： $3$ 个用于形成 $\sigma$ 键
>    3. 还剩下 $2$ 个价电子放在未杂化的 $p$ 轨道内用以形成大 $\pi$ 键
> 3. 对 $\ce{N^3}$ 原子分析：
>    1. $\ce{N}$ 原子最外层有 $5$ 个价电子
>    2. $3$ 个杂化轨道中： $2$ 个用于形成 $\sigma$ 键， $1$ 个用于形成孤电子对
>    3. 还剩下 $1$ 个价电子放在未杂化的 $p$ 轨道内用以形成大 $\pi$ 键
> 4. 对 $\ce{C}$ 原子分析：
>    1. $\ce{C}$ 原子最外层有 $4$ 个价电子
>    2. $3$ 个杂化轨道中：全部 $3$ 个用于形成 $\sigma$ 键
>    3. 还剩下 $1$ 个价电子放在未杂化的 $p$ 轨道内用以形成大 $\pi$ 键
> 5. 总计以上在未杂化的 $p$ 轨道内的价电子一共 $6$ 个，参与原子 $5$ 个
> 6. 所以，大 $\pi$ 键类型为：$\prod^{6}_{5}$

#### 规律判断

1. 对高中常见含有 大 $\pi$ 键 的分子或离子
   - 三原子分子：$\prod^{4}_{3}$
     $\ce{CO2、NO2、NO^-2、NO^+2、SO2、O3、N2O、N^-3、NCO^-、SCN^-、CS2}$

   - 四原子分子：$\prod^{6}_{4}$

     $\ce{SO^{2-}3、BF3、CO^{2-}3、BO^{3-}3、NO^{3-}3}$

   > 考试中可以直接使用三原子即为 $\prod^{4}_{3}$，四原子即为 $\prod^{6}_{4}$ ，仅有例外：$\ce{ClO2}\space\prod^{5}_{3}$

2. 能画出结构式的有机物

   数出 **不饱和键（双键和三键看成等价）、负电荷、孤对电子**

   要求：
   1. 每个原子只能数一次（一个原子不能数了两次负电荷或两对孤对电子）

   2. 每个原子只能数一种东西（每个原子数了不饱和键就不能数负电荷，数了负电荷就不能数孤对电子）

   3. 数一次记两个电子

   <img src="./images/3.1.png" style="zoom:33%;" />

## 等电子理论

1. **等电子体与等电子原理**

   原子总数相等且价电子总数相等的微粒互为等电子体，等电子体中心原子的杂化轨道类型相同，具有相同的空可结构和相同的化学键类型等结构特征，物理性质相近，但化学性质差别较大

2. **等电子体的确定方法**
   1. 同族元素互换法：即将既定粒子中的某元素换成它的同族元素
   2. 价电子迁移法：即将既定粒子中的某元素原子的价电子逐一转移给粒子中的另一种元素的原子，相应原子的质子数也随之减少或增加，变换为具有相应质子数的元素
   3. 电子电荷互换法：即将既定粒子中的某元素原子的价电子转化为粒子所带的电荷，相应原子的质子数也随之减少或增加。这种方法可实现分子与离子的互换

3. **常见等电子体**
   1. $5A-8e^{-}:\ce{CH_4}，\ce{NH^+_4}，\ce{SiH_4}，\ce{PH^+_4}，\ce{BH^-_4}$

   2. $2A-10e^{-}:\ce{N_2}，\ce{CO}，\ce{CN^-}，\ce{C^{2-}_2}$

   3. $3A-16e^{-}:\ce{CO_2}，\ce{CS_2}，\ce{BeCl_2}，\ce{N_2O}，\ce{SCN^-}，\ce{CNO^-}，\ce{N^-_3}$

   4. $3A-18e^{-}:\ce{SO_2}，\ce{O_3}，\ce{NO^-_2}$

   5. $4A-24e^{-}:\ce{NO^-_3}，\ce{CO^{2-}_3}，\ce{SO_3}，\ce{BF_3}，\ce{BO^-_3}$

   6. $4A-26e^{-}:\ce{SO^{3-}_3}，\ce{PO^{3-}_3}，\ce{ClO^-_3}$

   7. $5A-32e^{-}:\ce{CCl_4}，\ce{CBr_4}，\ce{SiCl_4}，\ce{SiF_4}，\ce{ClO^-_4}，\ce{SO^{2-}_4}，\ce{PO^{3-}_4}$

4. 等电子原理的应用
   1. 利用等电子原理可以判断一些陌生分子或离子的空间结构、成键情况，及其对应物质的某些性质，如 $\ce{CO_2}$ 与 $\ce{CS_2}$ 互为等电子体，二者同为直线形分子； $\ce{CO}$ 与 $\ce{N_2}$ 互为等电子体，二者分子结构中均存在共价三键等

   2. 利用等电子体可以制造新材料，如晶体硅、锗是良好的半导体材料，其等电子体 $AIP、GaAs$ 也是良好的半导体材料

## $spd$ 杂化 （拓展）

1. 简介

   有些元素原子在形成化合物时，除了 $ns、np$ 轨道发生杂化外，其同一能层能量相近的 $(n-1)d$ 轨道也参与杂化。常见的杂化方式有 $dsp^3、d^2sp^3、d^3sp^3$ 等，通常存在于过渡元素形成的化合物中

2. 判断方法

   先计算出中心原子的价层电子对数，若大于 $4$ ，一般有 $d$ 轨道参与杂化，并有相应的空间结构模型：

   | 价层电子对数     | $4$        | $5$        | $6$        | $7$        |
   | ---------------- | ---------- | ---------- | ---------- | ---------- |
   | **杂化类型**     | $dsp^2$    | $sp^3d$    | $sp^3d^2$  | $sp^3d^3$  |
   | **$VSEPR$ 模型** | 平面四边形 | 三角双锥形 | 正八面体形 | 五角双锥形 |

   > 不是所有的元素原子均能发生 $d$ 轨道参与的杂化，例如，由于第二周期元素原子的第二能层不存在 $d$ 轨道，$N$ 与 $Cl$ 只能通过 $sp^3$ 杂化形成 $NCl$ ；而 $P$ 与 $Cl$ 既可以通过 $sp^3$ 杂化形成 $ PCl_3$，也可以通过 $sp^3d$ 杂化形成 $PCl_5$


---

## Original file: 03 分子的极性 手性分子.md

---
description: "讲解共价键的极性和非极性、分子的极性判断方法，包括向量和和快速判断，以及手性分子的概念。"
---

# 03 · 分子的极性 手性分子

## 共价键的极性

1. 共价键有 **极性共价键** 和 **非极性共价键**

   **极性共价键**：由不同原子形成的共价键，电子对会发生偏移（向电负性大的一侧偏移）。极性键中的两个键合原子，一个呈正电性（$δ^+$），另一个呈负电性（$δ^-$）。在极性共价键中，成键原子吸引电子能力的差别越大，共用电子对偏移程度越大，共价键的极性越强

   **非极性共价键**：电子对不发生偏移的共价键

   > 因此，电负性差值越大，极性越大
   >
   > 特别：$\ce{O_3}$ 的 $\ce{O}$ 电负性不同，之间形成极性共价键；但由于其极性微弱，它在四氯化碳中的溶解度高于在水中的溶解度

2. 分子可分为 **极性分子** 和 **非极性分子**
   1. 极性分子的正电中心和负电中心不重合，使分子的某一个部分呈正电性（$δ^+$），另一部分呈负电性 ($δ^-$)

   2. 非极性分子的正电中心和负电中心重合

   <img src="./images/8.1.svg" width="100"/>

## 分子的极性的判断

判断分子的极性可依据分子中化学键的极性的 **向量和**

1. **只含非极性键** 的分子一定是非极性分子

   > 如：$H_2、Cl_2、Br_2$

2. 含极性键的分子有没有极性，必须依据分子中极性键的极性的 **向量和是否等于零** 而定。当分子中各个键的极性的向量和等于零时，是非极性分子，否则是极性分子

<img src="./images/8.2.png" width="470"/>

3. 也可以根据 **分子的正电中心和负电中心是否重合** 来判断它是否是极性分子

快速判断方法：

1. 化合价法：$AB_m$ 型分子中，**中心原子的化合价的绝对值** 等于 **该元素的价电子数** 时该分子为非极性分子，此时分子的空间结构对称；若中心原子的化合价的绝对值不等于其价电子数，则分子的空间结构不对称，其分子为极性分子，具体实例如下：

   | 分子                         | $BF_3$ | $CO_2$ | $PCl_5$ | $SO_3$ | $H_2O$ | $NH_3$ | $SO_2$ |
   | ---------------------------- | ------ | ------ | ------- | ------ | ------ | ------ | ------ |
   | **中心原子的化合价的绝对值** | $3$    | $4$    | $5$     | $6$    | $2$    | $3$    | $4$    |
   | **该元素的价电子数**         | $3$    | $4$    | $5$     | $6$    | $6$    | $5$    | $6$    |
   | **分子极性**                 | 非极性 | 非极性 | 非极性  | 非极性 | 极性   | 极性   | 极性   |

2. 根据分子所含键的类型及分子立体构型判断

   | 分子所含原子个数  | 键的极性 |         键角         |   立体构型   |  分子极性  |
   | :---------------- | :------: | :------------------: | :----------: | :--------: |
   | 单原子：$He、 Ne$ |   $-$    |         $-$          |     $-$      | 非极性分子 |
   | 双原子：$H_2$     | 非极性键 |         $-$          |    直线形    | 非极性分子 |
   | 双原子：$HCI$     |  极性键  |         $-$          |    直线形    |  极性分子  |
   | 三原子：$H_2O$    |  极性键  |    $104.5^\circ$     |    $V$ 形    |  极性分子  |
   | 三原子：$CO_2$    |  极性键  |     $180^\circ$      |    直线形    | 非极性分子 |
   | 四原子：$BF_3$    |  极性键  |     $120^\circ$      | 平面正三角形 | 非极性分子 |
   | 四原子：$NH_3$    |  极性键  |     $107^\circ$      |   三角锥形   |  极性分子  |
   | 五原子：$CH_4$    |  极性键  | $109^\circ28^\prime$ |  正四面体形  | 非极性分子 |
   | 五原子：$CH_3Cl$  |  极性键  |         $-$          |   四面体形   |  极性分子  |

   <img src="./images/8.3.png" width="500"/>

## 键的极性对化学性质的影响

键的极性对物质的化学性质有重要影响。例如，羧酸是一大类含羧基（$-COOH$）的有机酸，羧基可电离出 $H^+$ 而呈酸性

羧酸的酸性可用 $pK_a$ 的大小来衡量，$pK_a$ 越小，酸性越强。羧酸的酸性大小与其分子的组成和结构有关，如下表所示：

> 不同羧酸的 $pK_a$
>
> | 羧酸                        | $pK_a$ |
> | --------------------------- | ------ |
> | 丙酸($\ce{C_2H_5COOH}$)     | $4.88$ |
> | 乙酸($\ce{CH_3COOH}$)       | $4.76$ |
> | 甲酸($\ce{HCOOH}$)          | $3.75$ |
> | 氯乙酸($\ce{CH_2ClCOOH}$)   | $2.86$ |
> | 二氯乙酸($\ce{CHCl_2COOH}$) | $1.29$ |
> | 三氯乙酸($\ce{CCl_3COOH}$)  | $0.65$ |
> | 三氟乙酸($\ce{CF_3COOH}$)   | $0.23$ |
>
> 酸性至上而下由弱变强

三氟乙酸的酸性大于三氯乙酸酸性的原因：由于氟的电负性大于氯的电负性，$F-C$ 的极性大于 $Cl-C$ 的极性，使 $F_3C-$ 的极性大于 $Cl_3C-$ 的极性，导致三氟乙酸的羧基中的羟基的极性更大，更易电离出氢离子

三氯乙酸的酸性大于二氯乙酸酸性的原因：由于 $Cl_3C-$ 比 $Cl_2CH-$ 多一个氯原子，使 $Cl_3C-$ 的极性大于 $Cl_2CH-$ 的极性， 导致三氯乙酸的羧基中的羟基的极性更大，更易电离出氢离子

甲酸的酸性大于乙酸酸性的原因：烃基（$R—$）是推电子基团，烃基越长推电子效应越大，使羧基中的烃基的极性越小，羧酸的酸性越弱

## 「相似相溶」规则

非极性溶质一般能溶于非极性溶剂，极性溶质一般能溶于极性溶剂。如蔗糖、氨、水均是极性分子，$CCl_4$、萘和碘均是非极性分子，蔗糖和氨易溶于水，难溶于 $CCl_4$，而萘和碘易溶于 $CCl_4$，难溶于水

> 相似相融规则是一条经验规则，并不绝对，如 $H_2$ 既不溶于水，也难溶于苯

1. 内因
   1. 物质自身的结构，「相似相溶」还适用于分子结构的相似性。如低级醇（甲醇、乙醇等）可以与水以任意比互溶，而戊醇的烃基较大，其中的一个 $OH$ 与水分子的一个 $OH$ 的相似因素小得多，在水中的溶解度明显减小

   2. 如果溶质和溶剂之间形成氢键，则溶质在溶剂中的溶解度比较大。如果溶质分子不能与水分子形成氢键，则在水中的溶解度就比较小

   3. 化学反应—溶质与溶剂反应可增大溶解度。如 $SO_2$ 与 $H_2O$ 反应生成 $H_2SO_3$ 等。

2. 外因
   1. 温度：一般来说，温度升高，固体物质的溶解度增大，气体物质的溶解度减小

   2. 压强：压强越大，气体的溶解度越大

## 分子的手性

1. 手性异构体与手性分子

   具有完全相同的组成和原子排列的一对分子，如同左乎和右手一样互为镜像，在三维空间里不能叠合，互称手性异构体或对映异构体。有手性异构体的分子称为手性分子

2. 手性分子的判断

   在一个有机物分子中，如果有 1 个碳原子分别连有 $4$ 个不同的原子或基团，则该碳原子称为手性碳原子。名有手性碳原子的有机物分子即为手性分子。手性碳原子是产生手性的重要判断依据。

3. 手性分子的用途
   1. 构成生命体的有机分子绝大多数为手性分子。互为手性异构体的两个分子的性质不同

   2. 生成手性药物、手性催化剂（手性催化例只催化或主要催化一种手性分子的合成）


---

## Original file: 04 配合物与超分子.md

---
description: "讲解配位键的概念和形成条件、配合物的组成包括中心原子、配体和配位数，以及配合物对物质溶解性和颜色的影响，补充超分子相关知识。"
---

# 04 · 配合物与超分子

## 配位键

1. 概念：由一个原子单方面提供 **孤电子对** ，而另一个原子提供 **空轨道** 而形成的化学键，即「电子对给予 - 接受」键
2. 表示方法：配位键常用 $A-B$ 表示，其中 $A$ 是 **提供** 孤电子对的原子，叫给予体，$B$ 是接受孤电子对的原子，叫 **接受体**
   > 如：<img title="" src="./images/6.1.png" width="200">
   >
   > 1. 形成条件：形成配位键的一方（如 $A$）是能够提供 **孤电子对** 的原子，另一方（如 $B$）是具有能够接受孤电子对的空轨道的原子
   > 2. 孤电子对：分子或离子中，没有跟其他原子共用的电子对就是孤电子对
   >    含有孤电子对的微粒：分子如 $\ce{CO}$、$\ce{NH_3}$、$\ce{H_2O}$ 等，离子如 $\ce{Cl-}$、$\ce{CN-}$、$\ce{NO^{2-}}$ 等，如：
   >
   >  <img title="" src="./images/6.2.png" width="350">
   >
   > 3. 含有空轨道的微粒：过渡金属的原子或离子。一般来说，多数过渡金属的原子或离子形成配位键的数目基本上是固定的，如 $\ce{Ag+}$ 形成 $2$ 个配位键，$\ce{Cu^{2+}}$ 形成 $4$ 个配位键等

> 配位键与共价键的区别
>
> 1. 配位键是共价键的一种，只不过是一种特殊的共价键
> 2. 共价键一般是成键的双方都提供电子，配位键是一方提供孤电子对，一方提供空轨道

## 配合物

1. 概念：通常把金属离子或原子(称为 **中心离子** 或原子)与某些分子或离子(称为 **配体或配位体** )以 **配位键** 结合形成的化合物称为配位化合物，简称配合物。如 $\ce{[Cu(NH_3)_4]SO_4}$、$\ce{[Ag(NH_3)_2]OH}$ 等均为配合物

2. 组成：配合物 $\ce{[Cu(NH_3)_4]SO_4}$ 的组成如下图所示：

   <img title="" src="./images/6.3.png" width="350">
   1. **中心原子**：提供 **空轨道** 接受 孤电子对 的原子。中心原子一般都是带正电荷的阳离子(此时又叫 **中心离子** )，最常见的有过渡金属离子：$\ce{Fe^{3+}、Ag^+、Cu^{2+}、Zn^{2+}}$ 等
   2. **配体**：提供 **孤电子对** 的阴离子或分子，如 $\ce{Cl^-、NH_3、H_2O}$ 等。配体中直接同中心原子配位的原子叫做 **配位原子** 。配位原子必须是含有 **孤电子对** 的原子，

   > 如 $\ce{[Cu(NH_3)_4]^{2+}}$ 中的 $\ce{N}$ 原子是配位原子， $\ce{NH_3}$ 是配体3. **配位数**：直接与中心原子形成的 **配位键** 的数目。如 $\ce{[Fe(CN)_6]^-_4}$ 中 $\ce{Fe^{2+}}$ 的配位数为 $6$
   > 注意：配位数不一定等于中心原子与配位原子形成的配位键的键数或配位体的数目
   >
   > 1. 当中心原子与多基配体配合时，配位数不等于配位体的数目。如 $\ce{[Cu(en)_2]^{2+}}$ 中， $\ce{en}$ （乙二胺 $\ce{NH_2CH_2CH_2NH_2}$ 的简写）属于双基配体，每个分子有 $2$ 个 $\ce{N}$ 原子可以形成配位键，故 $\ce{Cu^{2+}}$ 的配位数为 $4$ 而不是 $2$
   >    <img title="" src="./images/6.4.png" width="70">
   > 2. 当中心离子原子同时以共价键与配位键结合时，配位数不等于配位键的键数。如 $\ce{[BF_4]^-、 [B(OH)_4]^-、[AlCl_4]^-、[Al(OH)_4]^-}$ 等配离子中，$\ce{B、Al}$ 原子均缺电子，它们形成的化学键，既有共价键，又有配位键，配位数与配位键的键数不相等，配位数均为 $4$
   >    <img title="" src="./images/6.5.png" width="170">
   > 3. 如 $\ce{Fe(CO)_5}$ 中 $\ce{C}$ 与 $\ce{O}$ 之间还可以生成一个配位键，所以 $\ce{Fe(CO)_5}$ 共有 $10$ 个配位键

3. **配合物的形成对性质的影响**
   1. **对溶解性的影响**
      一些难溶于水的金属氢氧化物、氯 化物、溴化物、碘化物、氰化物，可以溶解于氨水中，或依次溶解于含过量的 $\ce{OH^-、Cl^-、Br^-、I^-、CN^-}$ 的溶液中，形成可溶性的配合物
      > 如：$\ce{Cu(OH)_2 +4NH_3 = [Cu(NH_3)_4]+_2 +2OH^-}$
   2. **颜色的改变**
      当简单离子形成配离子时，其性质往往有很大差异。颜色发生变化就是一种常见的现象，根据颜色的变化就可以判断是否有配离子生成
      > 如：$\ce{Fe^{3+}}$ 与 $\ce{SCN^-}$ 形成硫氰化铁配离子，其溶液显 **红色**
   3. **稳定性增强**
      配合物具有一定的稳定性，若配位体给出电子的能力越强，配合物中的配位键越 **强** ，配合物越 **稳定** 。当作为中心离子的金属离子相同时，配合物的稳定性与配体的性质有关
      > 1. 电负性：$\ce{I<Cl}$，所以 $\ce{I^-}$ 更容易给出孤电子对 $e^-$ 与 $\ce{Hg^{2+}}$ 形成配位键，所以稳定性 ：$\ce{HgI^{2-}_4>HgCl^{2-}_4}$
      > 2. 已知 $\ce{NF_{3}}$ 与 $\ce{NH_{3}}$ 的空间构型相同，但 $\ce{NF_{3}}$ 不易与 $\ce{Cu^{2+}}$ 形成配离子，原因是 $\ce{NF_{3}}$ 的 $\ce{N}$ 原子偏正电性， $\ce{NH_{3}}$ 的 $\ce{N}$ 原子偏负电性，所以 $\ce{NH_{3}}$ 的 $\ce{N}$ 更容易与 $\ce{Cu^{2+}}$ 形成配位键
      > 3. $\ce{CN^-}$ 与 $\ce{CO}$ 均为配合物中常见的配体，提供孤电子对的通常是 $\ce{C}$ 原子而不是 $\ce{N}$ 原子，其原因是 $\ce{C}$ 电负性较小，更容易提供孤电子对，形成配位键
      > 4. 某一化合物形成了 $\ce{H_2O}$ 及 $\ce{NH_3}$ 与 $\ce{Cu^{2+}}$ 之间的配位键，加热时首先失去的组分是 $\ce{H_2O}$，因为 $\ce{N}$ 的电负性弱于 $\ce{O}$ ，$\ce{NH_3}$ 的配位能力强于 $\ce{H_2O}$ 的配位能力
4. 常见配合物的形状
   1. 正四面体：$\ce{[ZnCl_4]^{2-}\quad[Cd(CN)_4]^{2-}\quad[Zn(NH_3)_4]^{2+}}$
   2. 平面正方形：$\ce{[PtCl_4]^{2-}\quad[Ni(CN)_4]^{2-}\quad[Cu(NH_3)_4]^{2+}}$

   特殊配位离子： $\ce{\left[Ag\left(NH_{3}\right){2}\right]^{+} → sp^{1} ；[Zn(NH_3)_4]^{2+} → sp^{3} ；[Cu\left(NH\right)_{4}]^{2+} → dsp^{2}}$ (平面正方形)。只有 $ⅠB$ ，$ⅡB$ 族金属具有这种性质
   现象：在 $\ce{ZnSO_{4}}$ 溶液中加入过量氨水，先产生白色沉淀后溶解

## 超分子

1. 概念：由两种或两种以上的分子（**包括离子**）通过**分子间作用**形成的分子聚集体。

2. 特征
   i.**分子识别**
   （1）杯酚与$\ce{C_60}$通过尺寸匹配实现分子识别
   （2）**不同空腔尺寸**的冠醚与**不同的阳离子**匹配，靠**氧原子**吸引阳离子（可用作有机合成的催化剂，原理是将阳离子以及对应阴离子都带入有机溶剂中）(冠醚本身**不是超分子**，形成复合物后才算)
   （3）DNA中的碱基配对
   ii.**自组装**
   （1）**细胞和细胞器双分子膜**
   （2）DNA双螺旋结构的形成与稳定
   （3）三聚氰胺和三聚氰酸形成稳定的超分子晶体


---

## Original file: index.md

---
description: 本章围绕分子空间结构展开，包含价层电子对互斥模型、杂化轨道理论、分子极性与手性、配位键及配合物等重点内容。
---

# 03 分子空间结构与物质性质

<CCChapterOverview />


---



# Chapter 04 有机化学基础

Source directory: `04 有机化学基础`

## Original file: 01 研究有机化合物的一般方法.md

---
description: "介绍有机化合物的分离和提纯方法，包括蒸馏的原理、装置和注意事项，以及萃取的原理、萃取剂选择和操作步骤。"
---

# 01 · 研究有机化合物的一般方法

## 有机化合物的分离、提纯

### 蒸馏

1. **蒸馏原理**：利用有机物与杂质的沸点差异，将有机化合物以蒸汽的形式蒸出，然后冷凝得到产品
2. **适用对象**：互相溶解、沸点不同的液态有机混合物
3. **适用条件**：1. 用于分离互溶的液体混合物 2. 有机物的热稳定性较强 3. 有机物与杂质的沸点相差较大(一般大于 $30\ce{^\circ C}$ )

   > 无水乙醇的制取：
   > 会先加入 $\ce{CaO}$（吸水剂）$\ce{CaO}\stackrel{\ce{H2O}}{\longrightarrow}\ce{Ca(OH)2}(s)$，直接蒸馏出乙醇

4. **实验装置与注意事项**
   1. 蒸馏操作使用 **直形冷凝管**（不得使用球形冷凝管，其可能导致液体残留，影响蒸馏效果）
   2. 回流操作**回流直形、球形冷凝管**都可以，但多使用球形冷凝管（因为其冷却面积大，冷却效果好）
   3. 使用 **锥形瓶**（不用烧杯，烧杯口大，散热快，且不易密封，容易导致蒸汽逸出和冷凝液飞溅）
   4. 蒸馏烧瓶里盛液体的用量不超过 $\frac{2}{3}$，不少于 $\frac{1}{3}$
   5. 加入沸石或碎瓷片，**防止暴沸**，若忘记加沸石，应停止加热，待冷却之后再补加
   6. 温度计水银球应与蒸馏烧瓶的支管口齐平
   7. 冷凝水应 **下口进入**，**上口流出**，与蒸汽流向相反，以充分冷凝
   8. 蒸馏烧瓶需要垫石棉网加热（部分教材改为「陶土网」，请以实际教学为准）
   9. 实验开始时，**先通冷凝水，后加热**；实验结束时，**先停止加热，后停止通冷凝水**

   <img title="" src="./images/1.1.png" height="200">

### 萃取

1. **原理**：
   1. 液 $-$ 液萃取：利用待分离组分在两种不互溶的溶剂中的 **溶解性不同**，使待分离组分从 **溶解度较小** 的溶剂中转移到 **溶解度较大** 的溶剂中
   2. 固 $-$ 液萃取：用溶剂从固体物质中溶解出待分离组分

2. **萃取剂**：
   1. 选择原则：
      1. 与原溶剂 **互不相溶**
      2. 与溶质、原溶剂均不反应
      3. 溶质在萃取剂中的溶解度远大于原溶剂
   2. 常用萃取剂：乙醚( $C_2H_5OC_2H_5$ )、乙酸乙酯（ $CH_3COOCH_2CH_3$ ）、二氯甲烷( $CH_2Cl_2$ )、四氯化碳（ $CCl_4$ ）、苯（ $C_6H_6$ ）等

3. **检漏**：
   1. 关闭下方活塞，加入适量蒸馏水，静置，如没有水流下，说明活塞处不漏水
   2. 塞上上方玻璃塞，倒置，如没有水流出，将分液漏斗正立，把玻璃塞旋转 $180°$，再倒置，如仍没有水流出，说明玻璃塞处不漏水

4. **主要仪器**：**分液漏斗**

5. **实验装置与注意事项**
   操作步骤：检漏 $\longrightarrow$ 加试剂振荡 $\longrightarrow$ 静置分层 $\longrightarrow$ 分液
   1. 分液漏斗使用之前必须检漏

   2. 使用时需将漏斗上口的玻璃塞打开，或使玻璃塞上的凹槽对准分液漏斗上的小孔

   3. 漏斗下端管口紧靠烧怀内壁，分液时首先让**下层液体从下口流出**，**上层液体从上口倒出**

     <img align=left title="" src="./images/1.2.png" height="150" />

     <br/>

6. 举例：
   1. 用苯萃取溴水中的溴：溴水橙（红）色，苯无色，萃取后，苯密度小于水，溴的苯溶液处于上层橙（红）色，下层为水无色

   2. 用苯萃取碘水中的碘：碘水为棕黄色，萃取后，碘的苯溶液在上层紫红色，水在下层无色

   3. 用四氯化碳萃取溴水中的溴：萃取后，四氯化碳的密度大于水，溴的四氯化碳溶液处于下层橙（红）色，水在上层无色

   4. 用四氯化碳萃取碘水中的碘：萃取后，碘的四氯化碳溶液在下层紫红色，水在上层无色

### 重结晶

1. **原理**：利用被提纯物质与杂质在同一溶剂中的溶解度不同而将杂质除去

2. **适用对象**：固体有机化合物

3. **溶剂选择**：要求杂质在此溶剂中溶解度很小或溶解度很大，易于除去；**被提纯的有机化合物在此溶剂中的溶解度受温度的影响较大，能够进行冷却结晶**

4. **操作步骤**

   使用重结晶法分离固体化合物时，根据杂质的溶解度不同，应选择不同的操作步骤
   1. **杂质的溶解度很小**：加热溶解 $-$ 趁热过滤（滤去部分杂质，目标产物在溶液中）$-$ 冷却结晶
   2. **杂质的溶解度很大**：加热溶解 $-$ 蒸发浓缩 $-$ 冷却结晶（杂质在溶液中，目标产物结晶析出）

5. **注意**
   1. 如果重结晶所得的晶体纯度不能达到要求，可以再次进行重结晶以提高产物的纯度
   2. 若第一步「加热溶解」得到的是饱和溶液，过滤时会因溶液的温度降低而析出一部分溶质，造成损失，所以通常再加入少量蒸馏水，减少趁热过滤过程中的损失
   3. 若混有不溶性杂质，需充分溶解后过滤
   4. 样品制成粉末可增大样品与浸取液的接触面积，可提高浸取率

> 以重结晶法提纯苯甲酸为例
>
> 1. 实验目的：提纯含有少量氯化钠和泥沙杂质的苯甲酸
> 2. 资料：纯净的苯甲酸为无色结晶，其结构可表示为 <img title="" src="./images/1.3.png" style="height:25px">
>    熔点 $122\ce{^\circ C}$，沸点 $249\ce{^\circ C}$。苯甲酸 **微溶于水**，**易溶于乙醇等有机溶剂**。苯甲酸在水中的溶解度如下：
>
>    | 温度 $/\ce{^\circ C}$ | $25$       | $50$       | $75$      |
>    | --------------------- | ---------- | ---------- | --------- |
>    | **溶解度 $/g$**       | **$0.34$** | **$0.85$** | **$2.2$** |
>
> 3. 实验操作：
>    $$粗苯甲酸\ce{->[加热溶解]}溶液+泥沙\ce{->[趁热过滤]}溶液\ce{->[冷却结晶]}苯甲酸晶体$$
>    > 趁热过滤：避免苯甲酸因降温析出，影响产率

### 除杂实验

| 有机物（杂质）                 | 除杂方式                              |
| ------------------------------ | ------------------------------------- |
| $\ce{CH3COOC2H5}$(乙醇、乙酸） | 加入饱和碳酸氢钠溶液 $^1$             |
| 苯（苯酚）                     | 加入氢氧化钠溶液，分液 $^2$           |
| $\ce{C2H5OH}$（甲醇、水）      | 先加氧化钙（不必过滤），然后蒸馏 $^3$ |
| $\ce{CH4}$（$\ce{C2H4}$）      | 通入高锰酸钾溶液，然后通过碱石灰 $^4$ |
| 苯（$\ce{Br2}$)                | 先加氢氧化钠溶液，然后分液 $^5$       |
| 乙炔（硫化氢、磷化氢）         | 通过硫酸铜溶液 $^6$                   |
| 乙烯（二氧化硫）               | 通过碱石灰或加入氢氧化钠溶液 $^7$     |

> $^1:$ 乙醇溶于水；乙酸与碳酸氢钠反应，并降低乙酸乙酯的溶解度，分液后在上层
>
> $^2:\ce{C6H5-OH +NaOH = C6H5-ONa + H2O}$；苯酚钠不溶于苯
>
> $^3:\ce{CaO}$ 作吸水剂；蒸馏以除去甲醇
>
> $^4:$ 由于甲烷可溶于四氯化碳因此不能用溴的四氯化碳溶液来除去乙烯，但是可以使用溴水
>
> $^4:$ 乙烯被酸性高锰酸钾氧化后的产物是 $CO_2$:$\ce{5C2H4 + 12KMnO4 + 18H2SO4 = 10CO2 + 12MnSO4 + 6K2SO4 + 28H2O}$
>
> $^5:\ce{Br2 + 2NaOH = NaBr + NaBrO3 + H2O}$，$\ce{NaBr 、 NaBrO3}$ 可溶于水
>
> $^6:\ce{H2S + CuSO4 = CuS\downarrow + H2SO4}\quad\ce{PH3 + CuSO4= Cu3P\downarrow + H3PO4}$
>
> $^7:\ce{2NaOH + SO2 = Na2SO3 + H2O;CaO +SO2=CaSO3}$

> 气体杂质不得使用气体除杂

### 实验设计

| 实验目标                         | 实验设计                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 检测溴乙烷中的溴                 | 加入 $NaOH$ 溶液共热，**然后加入足量硝酸酸化(该句考察时常被删去)**<br>再加入 $\ce{AgNO3}$ 溶液，产生淡黄色沉淀<br>$\ce{C2H5Br + NaOH->[H2O][\Delta]C2H5OH + NaBr}$ |
| 粗苯甲酸的提纯                   | 重结晶（具体步骤：加热溶解，趁热过滤，冷却结晶）                                                                                                                   |
| 检验淀粉是否水解完全             | 加入碘液，观察颜色，溶液出现蓝色                                                                                                                                   |
| 检验溴乙烷发生消去反应生成的乙烯 | 先通过水除杂，然后通过酸性溶液 $\ce{KMnO4}$ ，紫色逐渐褪去 <br>（或通过 $\ce{Br2}$ 的 $\ce{CCl4}$ 溶液，橙色逐渐褪去）                                             |
| 鉴别甲烷、乙烯和乙炔             | 分别点燃，观察黑烟的浓度和火焰的亮度                                                                                                                               |
| 乙烯的实验室制取                 | 利用乙醇的消去反应<br>$\ce{CH3CH2OH  \xlongequal{浓硫酸，170℃}CH2=CH2 + H2O}$                                                                                      |
| 工业制备乙烯                     | 石油裂解                                                                                                                                                           |

## 有机化合物的组成、结构、反应的研究

### 核磁共振氢谱

1. **应用：测定有机化合物分子中有几种不同类型的氢原子及它们的相对数目**
2. **原理**：氢原子核具有磁性，如用电磁波照射含氢元素的化合物，其中的氢核会吸收特定频率电磁波的能量而产生核磁共振现象。用核磁共振仪可以记录到有关信号，处在不同化学环境中的氢原子因产生共振时吸收电磁波的频率不同，相应的信号在谱图中出现的位置也不同，具有不同的化学位移（用 $δ$ 表示），而且吸收峰的面积与氢原子数成正比
3. 关系：吸收峰数目 $=$ 氢原子种类数，吸收峰面积比 $=$ 不同种类的氢原子个数比
   > 乙醇和二甲醚的核磁共振氢谱
   > <img title="" src="./images/1.5.png" height="180">
   > $A:\ce{CH3CH2OH}$（乙醇）分子中有 $3$ 种处于不同化学环境的氢原子，对应的核磁共振氢谱图中只有 $3$ 个峰，强度比为 $3:1:2$
   > $B:\ce{CH3-O-CH3}$（二甲醚）分子中的 $6$ 个氢原子的化学环境相同，对应的核磁共振氢谱图中只有一个峰

### 红外光谱法

1. 作用：初步判断某有机物分子中所含有的 **化学键** 或 **官能团**
2. 原理：不同的化学键或官能团的吸收频率不同，在红外光谱图上将处于不同的位置
   > 例如：分子式为 C, H, O 的红外光谱上发现有 $O—H$、$C—H$ 和 $C-O$ 的吸收峰，可推知该分子的结构简式为 $\ce{C2H5OH}$
   > <img title="" src="./images/1.4.jpg" height="250">

### 质谱法

1. **原理**：用高能电子流等轰击样品，使有机分子失去电子，形成带正电荷的分子离子和碎片离子等，带正电荷的分子离子和碎片离子质量不同、电荷不同，因此它们在电场和磁场中的运动行为不同。它们在磁场的作用下到达检测器的时间不同，通过计算机分析得到质荷比，以质荷比为横坐标，以各类离子的相对丰度为纵坐标记录结果，得到质谱图
2. **质荷比**：质荷比是指分子离子或碎片离子的相对质量与其电荷数的比值。在有机化合物的质谱图中，**质荷比的最大值等于该有机化合物的相对分子质量**
3. **注意** 1. 质荷比的最大值对应的相对丰度不一定最大 2. 互为同分异构体的两种分子的质谱图中，虽然二者质荷比最大值相同但是质谱图并非完全相同
   > 如图所示为未知物 $A$ 的质谱图，质荷比最大值为 $46$，表示未知物 $A$ 的相对分子质量为 $46$
   > <img title="" src="./images/1.6.png" height="250">

### $X$ 射线衍射

1. 原理：$X$ 射线是一种波长很短（ 约 $10^{-10}m$ ）的电磁波，它和晶体中的原子相互作用可以产生衍射图。经过计算可以从中获得分子结构的有关数据，**包括键长、键角等分子结构信息**
2. 应用：将 $X$ 射线衍射技术用于有机化合物（特别是复杂的生物大分子）晶体结构的测定，可以获得更为直接而详尽的结构信息

### 总结

<img align=left title="" src="./images/1.7.png"  height="300"/>

**谱图法在确定有机物分子结构中的应用**：

1. **核磁共振氢谱图**：**各类氢原子个数之比**
2. **红外光谱图**：推知有机物分子中含有的 **化学键、官能团**
3. **质谱图**：质荷比的最大值等于该有机化合物的 **相对分子质量**
4. **$X$ 射线衍射技术**：用于有机化合物（特别是复杂的生物大分子）**晶体结构的测定**
5. **李比希元素分析法**：用于确定有机化合物中碳、氢含量，并可间接计算氧含量


---

## Original file: 02 有机化合物的结构.md

---
description: "讲解有机化合物中碳原子的成键特点、碳原子间的成键方式，以及有机化合物分子组成的各种表示方法如分子式、结构式、键线式等。"
---

# 02 · 有机化合物的结构

## 有机化合物中碳原子的成键特点

### 碳原子的成键特点

碳原子最外电子层有 $4$ 个电子，不易失去或获得电子而形成阳离子或阴离子，可以彼此间或与 $\ce{H、O、Cl、S、N}$ 等非金属元素原子形成共价键

### 碳原子间的成键方式

1. 碳原子间不仅可以形成碳碳单键（ $\ce{-C-C -}$ ）如乙烷( $\ce{CH3-CH3}$ )；还可以形成碳碳双键 <img title="" src="./images/2.1.png" style="height: 30px;"> 或碳碳三键( $\ce{-C#C-}$ )，如乙烯( $\ce{CH2=CH2}$ )、乙炔( $\ce{CH#CH}$ )
2. 多个碳原子之间可以结合形成碳链，碳链既可以是一条直链，也可以带有支链，如正丁烷( $\ce{CH3-CH2-CH2-CH3}$ )和异丁烷(<img title="" src="./images/2.2.svg" style="height: 75px;">)；碳原子间也可以结合成碳环，环上的碳原子还可以连接支链，如环丁烷(<img title="" src="./images/2.3.svg"  style="height: 75px;">)和甲基环丙烷(<img title="" src="/04 有机化学基础/images/2.4.jpg" style="height: 35px;">)

### 碳原子与其他原子间的成键方式

1. 碳原子与氢原子、卤素原子间只能形成单键
2. 碳原子与氧原子、硫原子间可以形成单键、双键
3. 碳原子与氮原子间可以形成单键、双键、三键

### 碳原子的成键方式与分子结构

$$
\begin{cases}
饱和碳原子 & 单键碳原子 \\
不饱和碳原子 &\begin{cases}
双键碳原子 \\
三键碳原子 \\
苯环碳原子 \\
\end{cases}\
\end{cases}
$$

含有不饱和键的有机化合物分子由于双键或三键中有部分键容易断裂，双键或三键两端的碳原子还可以结合其他原子或原子团，一般易于发生加成反应（苯环结构具有特殊性）

## 有机化合物分子组成或结构的表示方法

| 种类           | 表示方式                                                                                                                                                                                                     | 示例                                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| 分子式         | 用元素符号表示物质的分子组成                                                                                                                                                                                 | $\ce{CH4}$                                         |
| 最简式(实验式) | 用元素符号表示化合物中各元素原子个数的最简整数比                                                                                                                                                             | $\ce{CH2O}$ <br>（乙烯 $\ce{CH2}$）                |
| 电子式         | 在元素符号周围用「$·$」或「$×$」表示原子的最外层电子的成键情况                                                                                                                                               | <img title="" src="./images/2.7.png" width="100">  |
| 结构式         | 用短线「$\ce{-}$」来表示 1 个共价键，用「$\ce{-}$」（单键）「$\ce{=}$」（双键）或「$\ce{#}$」（三键）将所有原子连接起来                                                                                      | <img title="" src="./images/2.3.svg" width="100">  |
| 结构简式       | ①在结构式的基础上，表示单键的「$\ce{-}$」可以省略，将与碳原子相连的其他原子写在其旁边，在右下角注明其个数<br>②表示双键、三键的「$\ce{=}$」「$\ce{#}$」不能省略<br>③醛基、羧基可简化成 $\ce{-CHO、-COOH}$     | $\ce{CH3CH=CH2}$                                   |
| 键线式         | ①在结构简式的基础上，进一步省去碳原子及与碳原子直接相连的氢原子的元素符号，只要求表示出分子中键的连接情况和基团<br>②键线式中的每个拐点或端点均表示一个碳原子，每个碳原子都形成四个共价键，不足的用氢原子补足 | <img title="" src="./images/2.9.svg" width="100">  |
| 球棍模型       | 小球表示原子，短棍表示化学键                                                                                                                                                                                 | <img title="" src="./images/2.10.png" width="100"> |
| 空间填充模型   | 用不同体积的小球表示不同大小的原子                                                                                                                                                                           | <img title="" src="./images/2.11.svg" width="100"> |

> 注意：
>
> 1. 书写结构简式时，同一个碳原子上的相同原子或原子团可以合并，相邻且相同的原子团亦可以合并，如：$2,2$-二甲基戊烷可以写作 $\ce{(CH3)3C(CH2)2CH3}$
> 2. 结构简式不能表示有机化合物的真实空间结构。如从结构简式看，$\ce{CH3-CH2-CH2-CH3}$ 中的碳链是直线形的，而实际上是锯齿形的
> 3. 键线式中只可以省略与碳原子相连的氢原子，与其他原子相连的氢原子（如 $\ce{-OH}$ 中的氢原子）不可以省略
> 4. 用空间填充模型表示有机化合物结构时，代表不同原子的各小球的相对大小关系应与原子实际相对大小关系一致

## 有机化合物的同分异构现象

**同分异构现象**：分子内部原子的成键方式、连接顺序等差异产生分子式相同而结构不同的现象叫同分异构现象
**同分异构体**：分子式相同，结构不同，性质不同

### 同分异构现象的分类

$$
同分异构现象 \begin{cases}
构造异构 & \begin{cases}
碳链异构 \\
位置异构 \\
官能团异构 \\
\end{cases}\\
立体异构 & 顺反异构、对映异构等\\
\end{cases}
$$

- **碳链异构**
  碳链骨架不同

  > $\ce{CH3CH2CH2CH3}$ 和 $\ce{CH3CH(CH3)2}$

- **位置异构**
  官能团或取代基在碳骨架（碳链或碳环）上位置不同

  > $\ce{CH2=CHCH2CH3}$ 和 $\ce{CH3CH=CHCH3}$
  >
  > $\ce{CH3CH2CH2OH}$ 和 $\ce{CH3CH(OH)CH3}$
  >
  > $\ce{CH3OCH2CH2CH3}$ 和 $\ce{CH3CH2OCH2CH3}$
  >
  > $\ce{R1COOR2}$ 和 $\ce{R2COOR1}$ ($R1 \neq R2$，且均为烃基)

- **官能团异构**
  官能团不同

  > $\ce{CH3CH2OH}$ 和 $\ce{CH3OCH3}$
  >
  > $\ce{CH3CH2CHO}$ 和 $\ce{CH3COCH3}$
  >
  > $\ce{CH3COOH}$ 和 $\ce{HCOOCH3}$

- **顺反异构**
  原子或原子团在碳碳双键上的位置不同

  从复杂基团到简单的为正方向，当两侧均为同一方向，为顺，反之为反

  <img title="" src="./images/2.12.png" width="250">

  > 双键上的碳原子及与其直接相连的原子位于同一平面，碳碳双键中任意一个双键碳原子上连接 2 个相同的原子或原子团时，不存在顺反异构

- **对映异构**
  互为镜像且不能重叠的结构，即存在手性碳原子便存在对映异构

  手性碳原子：饱和碳的周围接了 4 个两两不同的原子或原子团

  <img title="" src="./images/2.13.svg" width="250">

### 同分异构体的书写与数目判断

#### 同分异构体的书写方法

高中阶段有关同分异构体的考查主要考虑构造异构（如需考虑立体异构，一般会给出说明），其中碳链异构是基础。书写同分异构体时要有一定的原则和顺序，做到不重复、不遗漏

1. **烷烃同分异构体的书写**
   由于烷烃只存在碳链异构，其书写一般采用「减碳法」。「减碳法」书写同分异构体的技巧如下：
   1. **三注意**：注意要选择最长的碳链作主链；注意要找出对称轴；注意要保证每次减掉碳原子后的碳链仍为主链
   2. **三原则**：对称性原则、有序性原则、互补性原则
   3. **四顺序**
      1） **主链由长到短**：选取最长的碳链为主链，再逐步减少主链的碳原子数，余下的碳原子作为取代基。
      2） 取代基由整到散余下的碳原子先作为一个取代基，再逐步拆散为多个小取代基。当有多个取代基存在时，应按连接在同一碳原子、相邻碳原子、相间碳原子…的顺序依次移动，避免漏项
      3） **位置由心到边不到端**：把取代基连在主链上，由主链的对称中心开始，逐步向一边移动，但注意不要移到端点
      4） **排列由对、邻到间**：两个取代基可以相对(连在同一个碳原子上)、相邻（分别连在相邻的两个碳原子上）和相间（分别连在不相邻的两个碳原子上）

   > 注意：利用减碳法书写同分异构体时应注意保证减掉碳原子后的碳链仍为主链，如甲基连在主链的端点碳原子上、乙基连在主链的二号碳原子上，均会改变主链，导致书写重复

2. **具有官能团的有机化合物同分异构体的书写**
   书写步骤为先确定可能含有的官能团类别，之后按照烷烃同分异构体的书写方法分别写出除官能团外的碳链异构，然后再移动官能团的位置，最后按照碳原子形成四个共价键的原则，把氢原子补齐

#### 同分异构体数目的判断方法

1. **等效氢法**
   等效氢法在判断有机化合物的一元取代物同分异构体的数目时尤其适用。有机化合物分子中有几种不同化学环境的氢原子，则其一元取代物就有几种同分异构体
   1. **同一碳原子上的氢原子是等效的**，如 $\ce{CH4}$ 分子中的 $4$ 个氢原子是等效的
   2. **同一碳原子所连的相同基团上的氢原子是等效的**，如新戊烷(<img  align=center title="" src="./images/2.14.png" height="75">)分子中的 $4$ 个甲基等效，各甲基上的氢原子完全等效，即新戊烷分子中的 $12$ 个氢原子是等效的
   3. **处于镜面对称位置上的氢原子是等效的**（相当于平面镜成像时，物与像的关系），如 $\ce{CH3CH2CH2CH3}$ 分子中有 $2$ 种等效氢原子

   > **以 含多个苯环的有机物 为例**
   >
   > 萘的一氯代物有 $2$ 种：<img src="./images/2.20.svg" style="zoom:30%;"/>
   >
   > 萘的二氯代物有 $10$ 种：<img src="./images/2.21.svg" style="zoom:30%;"/>
   >
   > > 「×」是由于在情况一中已经被考虑，之后不再考虑4. **苯环上处于中心对称的氢原子是等效的**

2. **定$-$移$-$法** 及其模板
   确定链状烷烃 **二元取代物** 的同分异构体数目时，可首先固定一个取代基，再按照顺序移动另一个取代基以确定同分异构体数目，下面以确定 $\ce{CH3CH2CH3}$ 的二氯代物的数目为例
   <img title="" src="./images/2.15.svg" width="250">
   1. 先固定 $1$ 个氯原子，有 $2$ 种
   2. 然后移动第 $2$ 个氯原子（a/b/c/d/e 表示第 $2$ 个氯原子的位置）：①结构中有 3 种，②结构中有 $2$ 种。其中① b 和② d 重复。故 $\ce{CH3CH2CH3}$ 的二氯代物有 $4$ 种
   3. 通过上述案例可以得到：
   - 形如 $\ce{C3X2}$ 的二元取代物有 $4$ 种
   - 形如 $\ce{C3XY}$ 的二元取代物有 $5$ 种
   - 形如 $\ce{C4X2}$ 的二元取代物有 $6$ 种
   - 形如 $\ce{C4XY}$ 的二元取代物有 $10$ 种
   4. 确定苯环上的二元、三元取代物的同分异构体数目时（不考虑基团异构），也可以采用类似定 $-$ 移 $-$ 法的方法，可以得到：
   - 苯环上二取代的同分异构体数目有 $3$ 种
   - 苯环上三取代($\ce{C6H3X3}$)的同分异构体数目有 $3$ 种
   - 苯环上三取代($\ce{C6H3X2Y}$)的同分异构体数目有 $6$ 种
   - 苯环上三取代($\ce{C6H3XYZ}$)的同分异构体数目有 $10$ 种

   > 如苯环上有多个相同的取代基，可将其视为 $\ce{H}$，移动其他物质计算同分异构体

3. **烷基取代法**
   该法主要适用于单一基团取代的同分异构体（可见下面案例），若题目限定了其他条件，则仍建议改用定 $-$ 移 $-$ 法防止数多
   1. 记住常见烷基的结构总数：甲基 $1$ 种，乙基 $1$ 种，丙基有 $2$ 种，丁基有 $4$ 种，戊基有 $8$ 种（ $1、1、2、4、8$ ）
   2. 将有机物分子拆分为烃基和官能团两部分，根据烃基异构体的数目，确定有机物分子的数目。如分子式为 $\ce{C4H10O}$ 属于醇的同分异构体，可改写成 $\ce{C4H9-OH}$ ，共有 $4$ 种结构；分子式为 $\ce{C5H10O}$ 属于醛的同分异构体，可改写成 $\ce{C4H9-CHO}$ ，共有 $4$ 种结构

> 注意：题目中如问 **给定结构** 的物质的同分异构体数目，**需要扣除该物质本身**

同分异构体计数口诀

定一移一不重复，镜面对称要剔除。丁基四种戊基八，苯环三同仅一种。

二氯丁烷有六种，混代异构数十种。烷基取代看尾巴，官能团异构先分类。

## 有机化合物的共线、共面判断

### 经典结构

| 代表物                              | 空间结构     | 碳原子杂化方式 | 结构特点                                                                           |
| ----------------------------------- | ------------ | -------------- | ---------------------------------------------------------------------------------- |
| $\ce{CH4}$                          | 正四面体     | $sp^3$         | 任意 3 原子共面                                                                    |
| $\ce{C2H4}$                         | 平面结构     | $sp^2$         | 6 点共面，$\ce{C=C}$ 不能旋转                                                      |
| $\ce{C2H2}$                         | 直线型       | $sp$           | 4 点共线(面)，$\ce{C#C}$ 不能旋转                                                  |
| $\ce{C6H6}$                         | 平面正六边形 | $sp^2$         | 12 点共面，4 点共线                                                                |
| $\ce{CH2O}$（甲醛）                 | 平面型       | $sp^2$         | 平面三角形结构，至少 4 原子共面                                                    |
| 萘、蒽                              | 平面型       | $sp^2$         | 所有原子一定共平面                                                                 |
| $\ce{C12H10}$（联苯）$\ce{⌬\!-\!⌬}$ | -            | -              | 至少 14 个原子共平面，最多 22 个原子共平面<br>至少 6 个原子共线，最多 6 个原子共线 |

> 有时有机化合物的结构简式、键线式会省略氢，此时氢原子应考虑

### 思路流程

1. 可能出现的题目要求

   「碳原子」、「所有原子」；「一定」、「可能」、「至少」、「最多」；「共线」、「共面」

2. 选定主体结构
   1. 凡出现碳碳双键结构形式的原子共面问题，以乙烯的结构为主体
   2. 凡出现碳碳三键结构形式的原子共线问题，以乙炔的结构为主体
   3. 凡出现苯环结构形式的原子共面问题，以苯的结构为主体

3. 画出有机化合物的结构式，观察原子的共线、共面情况。注意：单键可以旋转，双键、三键不可以旋转

4. 常见结构的重要结论
   1. 结构中出现饱和原子，则所有原子不可能共平面
   2. 结构中每出现一个碳碳双键，至少有 6 个原子共面
   3. 结构中每出现一个碳碳三键，至少有 4 个原子共线
   4. 结构中每出现一个苯环，至少有 12 个原子共面

5.共线共面判断口诀

双键平面三键线，苯环平面对位线。单键旋转是关键，饱和碳上四面散。

碳链骨架可扭动，三点必面记心间。若问原子是否共，双键苯环先定盘。

> 原子共面共线例题
>
> 1. $\ce{CH2=CH-C≡CH}$ 最多几个原子共平面？几个原子共线？
>
>    <img title="" src="./images/2.16.svg">
>
>    > 至少/最多 8 个原子共平面，4 个原子共线
>
> 2. 苯乙烯最多几个原子共平面？
>
>    <img title="" src="./images/2.17.svg" width="400">
>
>    > 共平面原子至少 12 个，最多 16 个
>
> 3. [福建化学 2021 · 2 · B,4 分] 豆甾醇是否含有平面环状结构？
>
>    <img title="" src="./images/2.18.svg">
>
>    > 其所含的环状结构中大多数为饱和碳原子，饱和碳原子为四面体构型，因此形成的环状结构不是平面结构
>
> 4. 最多几个碳原子共平面？
>
>    <img title="" src="./images/2.19.svg">
>
>    > 最多 11 个碳原子共平面


---

## Original file: 03 有机化合物的分类和命名.md

---
description: "介绍有机化合物的分类方法，包括官能团、同系物和各类化合物的通式，以及有机化合物的命名原则和规则。"
---

# 03 · 有机化合物的分类和命名

## 有机化合物的分类

1. **官能团**
   反映一类有机化合物其同特性的原子或原子团叫做官能团

2. **同系物**
   结构相似，分子组成相差一个或若干个 $\ce{CH2}$ 原子团的有机化合物互相称为同系物。同系物一般可用通式表示
   > | 类别         | 通式                                               |
   > | ------------ | -------------------------------------------------- |
   > | 链烷烃       | $\ce{C_{n}H_{2n+2} } \left( n \geqslant 1 \right)$ |
   > | 单烯烃       | $\ce{C_{n}H_{2n} } \left( n \geqslant 2 \right)$   |
   > | 环烷烃       | $\ce{C_{n}H_{2n} } \left( n \geqslant 3 \right)$   |
   > | 炔烃         | $\ce{C_{n}H_{2n-2} } \left( n \geqslant 2 \right)$ |
   > | 二烯烃       | $\ce{C_{n}H_{2n-2} } \left( n \geqslant 4 \right)$ |
   > | 苯及其同系物 | $\ce{C_{n}H_{2n-6} } \left( n \geqslant 6 \right)$ |
   >
   > 同系物因组成和结构相似，化学性质相似，而物理性质如熔沸点、密度，一般呈规律性变化
   >
   > 同系物定义中的「结构相似」是指碳链和成键方式相同、官能团相同、官能团数目相同、官能团与其他原子的连接
   > 方式相同等。如 $\ce{CH3CH2OH}$ 与 $\ce{HOCH2CH2OH}$ 不属于同系物

<table>
    <thead>
        <tr>
            <th> 类别 </th>
            <th> 官能团名称 </th>
            <th> 官能团结构 </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> 烯烃 </td>
            <td> 碳碳双键 </td>
            <td> <img src="./images/3.8.svg"height="50"> </td>
        </tr>
        <tr>
            <td> 炔烃 </td>
            <td> 碳碳三键 </td>
            <td> <img src="./images/3.9.svg"height="25"> </td>
        </tr>
        <tr>
            <td> 卤代烃 </td>
            <td> 碳卤键 </td>
            <td> <img src="./images/3.10.svg"height="50"> </td>
        </tr>
        <tr>
            <td> 醇 </td>
            <td> 醇羟基 </td>
            <td rowspan="2"> <img src="./images/3.11.svg"height="25"> </td>
        </tr>
        <tr>
            <td> 酚 </td>
            <td> 酚羟基 </td>
        </tr>
        <tr>
            <td> 醚 </td>
            <td> 醚键 </td>
            <td> <img src="./images/3.12.svg"height="50"> </td>
        </tr>
        <tr>
            <td> 醛 </td>
            <td> 醛基 </td>
            <td> <img src="./images/3.13.svg"height="50"> </td>
        </tr>
        <tr>
            <td> 酮 </td>
            <td> 酮羰基 </td>
            <td> <img src="./images/3.14.svg"height="50"> </td>
        </tr>
        <tr>
            <td> 羧酸 </td>
            <td> 羧基 </td>
            <td> <img src="./images/3.15.svg"height="50"> </td>
        </tr>
        <tr>
            <td> 酯 </td>
            <td> 酯基 </td>
            <td> <img src="./images/3.16.svg"height="50"> </td>
        </tr>
        <tr>
            <td> 胺 </td>
            <td> 氨基 </td>
            <td> <img src="./images/3.17.svg"height="25"> </td>
        </tr>
        <tr>
            <td> 酰胺 </td>
            <td> 酰胺基 </td>
            <td> <img src="./images/3.18.svg"height="50"> </td>
        </tr>
    </tbody>
</table>

> 1. 酚和醇的官能团均为羟基( $\ce{-OH}$ )，但酚中羟基直接与苯环相连，而醇中羟基直接连在饱和碳原子上；但最好应区分醇羟基与酚羟基
> 2. 酯基中与 $\ce{O}$ 成键的一定是 $\ce{C}$
> 3. <img src="./images/3.21.svg" style="zoom: 80%;"/> 含酯基、醛基，属于酯类
> 4. 醚键两端的 $\ce{C}$ 原子不一定要接三个单键

## 习惯命名法

$$
碳原子数 \begin{cases}
十以下 & 依次用 甲、乙、丙、丁、戊、己、庚、辛、壬、癸 表示\\
十以上 & 用 中文数字 表示\\
相同时 & 正、异、新\\
\end{cases}
$$

> 正：直链无支链的烷烃、异：带有一个支链的烷烃、新：带有两个支链的烷烃；正戊烷的主链是丁烷

## 系统命名法

### 烃基

_命名架构：位置编号-取代基-主碳链_

### 烷烃的系统命名步骤

1. 定主链要遵循 **「长」「多」** 原则
   以最长的连续碳链为主链，以此主链决定烷烃的基本名称
   当有几个相同长度的不同碳链时，选择 **含支链最多的一个作为主链**
2. 以阿拉伯数字（$1、2、3$）表示取代基或官能团的 **位置编号**
   以中文数字（$一、二、三$）表示 **取代基个数**
   阿拉伯数字与汉字间以短横线「$-$」分开，取代基则由 **碳数少的小取代基** 先写
   >  <img title="" src="./images/3.1.png" height="100">
3. 编号位要遵循 **「近」「简」「小」** 原则
   1. **首先考虑「近」**：以 **离支链较近** 的一端给主链碳原子编号
      <img title="" src="./images/3.2.jpg" height="100">
   2. **同「近」考虑「简」**：有两个不同的支链，且分别处于距主链两端同近的位置则从 **支链较简单的一端** 开始编号
      <img title="" src="./images/3.3.jpg" height="100">
   3. **同「近」同「简」考虑「小」**：若有两个相同的支链，且分别处于距主链两端同近的位置，而中间还有其他支链，从主链的两个方向编号，可得到两种不同的编号序列，两序列中各支链 **位次和最小者** 即为正确的编号
      <img title="" src="./images/3.4.jpg" height="100">

### 单烯烃和单炔烃的命名

1. **选主链**：将 **含有碳碳双键或碳碳三键** 的 **最长碳链** 作为主链，称为「某烯」或「某炔」
2. **编序号**：从距离碳碳双键或碳碳三键 **最近** 的一端对主链上的碳原子进行编号定位
3. **写名称**：将支链作为取代基，写在「某烯」或「某炔」的前面，并用阿拉伯数字标明碳碳双键或碳碳三键的位置，写出有机物的名称
   从前到后的顺序依次为 **简单取代基位置** $-$ **简单取代基数目** $-$ **简单取代基名称** $-$ **复杂取代基位置** $-$ **复杂取代基数目** $-$ **复杂取代基名称** $-$ **碳碳双键或三键位置** $-$ **主链名**
   <img title="" src="./images/3.5.jpg" height="100">

> 烯烃、炔烃的命名与烷烃的命名的不同点
>
> 1. 主链的选取：必须是含有碳碳双键或碳碳三键的最长碳链
> 2. 主链的编号：从距离碳碳双键或碳碳三键最近的一端开始编号
> 3. 名称的书写：先写取代基的位置和名称，再写碳碳双键或碳碳三键的位置

### 多烯烃和多炔烃的命名

与单烯烃或单炔烃的命名主要区分点在于主链的选择与不饱和键序号的确定。

1. **选主链**：将 **含有碳碳双键或碳碳三键** 的 **最多** 的 **最长碳链** 作为主链，称为「某几烯」或「某几炔」
2. **编序号**：从距离碳碳双键或碳碳三键 **最近** 的一端开始，双键或三键的位号由小到大排列。
3. **写名称**：将支链作为取代基，写在「某几烯」或「某几炔」的前面，并用阿拉伯数字标明碳碳双键或碳碳三键的位置，写出有机物的名称。

   若分子中同时含有碳碳双键与碳碳三键，可用某烯炔作结尾，并给予双键、三键尽可能低的位号，如果位号有选择时，使双键位号比三键小，书写时先烯后炔。

    <img title="" src="./images/3.19.svg"  height="150" width="250">

### 芳香烃的命名

1. **基本原则**：环状化合物的命名通常选择环作为母体，从环上连有最简单取代基的碳原子开始编号
2. **苯的同系物的命名**：

   将苯环上的 $6$ 个碳原子按最小位次和原则进行编号（从 $1-6$ ），命名时要指出取代基的位置和名称
   1. 以苯环作为命名的母体，苯环上的侧链烷基为取代基进行命名，如苯环上的一个氢原子被甲基取代称为甲苯，苯环上的一个氢原子被乙基取代称为乙苯。

   当苯环上有两个取代基时，根据取代基在苯环上的相对位置，可分别用「邻」「间」「对」来表示，如「对二甲苯」 「邻甲基苯酚」 等；当苯环上有三个 **相同** 取代基时，根据取代基在苯环上的相对位置，可分别用「连」「偏」「均」来表示。

     <img title="" src="./images/3.6.jpg" height="260">
   2. 采用习惯命名法命名，当苯环上有两个不同取代基时，以较大的取代基为母体来命名

   > 如图所示
   > <img title="" src="./images/3.7.jpg" height="100"> 3. 当苯环上连接不饱和基团或虽为饱和基团，但体积较大或结构比较复杂时，可将苯作为取代基

### 单官能团烃衍生物的系统命名

1. 将官能团作为取代基，仍以烷烃为母体，按烷烃的命名原则来命名

   采用这种方法的官能团有：卤素原子、硝基、（亚硝基）

2. 将含有官能团的最长主链作为母体化合物，其命名步骤如下：

   ① **选主链**：将 **含有母体官能团** 的 **最长碳链** 作为主链
   ② **编序号**：按 **最低系列原则**（即让官能团的位置号尽可能小）依次给主链碳原子编号。
   ③ **写名称**：将支链作为取代基，然后写全名。写全名时，根据主链的碳原子数称为某 A（A = 醇、醛、酮、酸、酰卤、酰胺、腈等）
   从前到后的顺序依次为 **简单取代基位置** $-$ **简单取代基数目** $-$ **简单取代基名称** $-$ **复杂取代基位置** $-$ **复杂取代基数目** $-$ **复杂取代基名称** $-$ **母体官能团位置** $-$ **母体名称**

3. 酯的命名

   酯是羧酸与醇脱水缩合形成的产物，此处以乙酸苯甲酯为例：
   ① 命名时先把羧酸名称放在前面，即「乙酸」；
   ② 将醇的名称放在后面，先删去「醇」字，而后加上「酯」字，即「乙酸苯甲酯」。

### 含有多个相同官能团的烃衍生物的系统命名

可参照 **单官能团烃衍生物的命名** 与 **烯烃和炔烃的命名** 进行

<!-- 如果需要保证完整度，可进一步补充 -->

### 含多种官能团的烃衍生物的系统命名

1. 当分子中含有多种官能团时，首先要确定一个主官能团，确定主官能团的顺序是查看下表所列顺序：
   <!-- 本表格尚不全 -->
   <table>
       <tbody>
       <tr>
           <th> 母体名称 </th>
           <th> 官能团名称 </th>
           <th> 官能团结构 </th>
       </tr>
       <tr>
           <td> 羧酸 </td>
           <td> 羧基 </td>
           <td> <img src="./images/3.15.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 酯 </td>
           <td> 酯基 </td>
           <td> <img src="./images/3.16.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 酰胺 </td>
           <td> 酰胺基 </td>
           <td> <img src="./images/3.18.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 醛 </td>
           <td> 醛基 </td>
           <td> <img src="./images/3.13.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 酮 </td>
           <td> 酮羰基 </td>
           <td> <img src="./images/3.14.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 醇 </td>
           <td rowspan="2"> 羟基 </td>
           <td rowspan="2"> <img src="./images/3.11.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 酚 </td>
       </tr>
       <tr>
           <td> 胺 </td>
           <td> 氨基 </td>
           <td> <img src="./images/3.17.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 醚 </td>
           <td> 醚键 </td>
           <td> <img src="./images/3.12.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 炔烃 </td>
           <td> 碳碳三键 </td>
           <td> <img src="./images/3.9.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 烯烃 </td>
           <td> 碳碳双键 </td>
           <td> <img src="./images/3.8.svg"height="50"> </td>
       </tr>
       <tr>
           <td> 烷烃 </td>
           <td> N/A </td>
           <td> N/A </td>
       </tr>
       <tr>
           <td>（一般不做母体）</td>
           <td> 碳卤键(卤素原子)</td>
           <td> <img src="./images/3.10.svg"height="50"> </td>
       </tr>
       <tr>
           <td>（一般不做母体）</td>
           <td> 硝基 </td>
           <td>（图片待补充）</td>
       </tr>
       </tbody>
   </table>

1. 然后，选择含有 **主官能团** 及尽可能含 **较多官能团** 的 **最长碳链** 为主链
1. 主链编号的原则是要让官能团的位号尽可能小。

下面来看一个简单的实例：

<img title="" src="./images/3.20.svg"  height="150" width="300">

> 先确定母体为羧酸，因此该物质以「某酸」结尾
> 选择含有 **主官能团** 及尽可能含 **较多官能团** 的 **最长碳链** 为主链，该化合物较为简单，直接选取整条碳链，因此该物质为「某戊酸」。
> 进行主链编号：羧基的位置被锁定在 1 号位，此时氯原子处于 3 号位，羟基处于 5 号位，因此该物质为 **5-羟基-3-氯戊酸**。

> 至于在编号已经完全正确时，「氯」和「羟基」在命名时究竟谁写在前面，也就是 3-氯-5-羟基戊酸 这个命名是否正确的问题，其实在高考中并无刻板要求.
> 只要官能团 **编号正确**，就能拿到相应分数（目前此类复杂化合物的命名在真题中出现率相对较低）

但是，若要刨根问底或追求精确，可以了解：

先写简单基团，与取代基相连的原子序数小的基团排在前面（常见原子为 $\ce{I > Br > Cl > S > O > N > C > H}$，如羟基中的氧与氯比较，氧序数较小，则氯排在前面）；而对于甲基、乙基、丙基等同为碳原子的基团，复杂度逐渐上升。该方法简便易用，且目前流传度尚广


---

## Original file: 04 烃.md

---
description: "介绍烃的分类，包括脂肪烃和芳香烃，重点讲解烷烃的结构、物理性质和化学性质如氧化、卤代和分解反应。"
---

# 04 · 烃

<img src="./images/4.0.svg" />

1. 按碳原子组成的 **分子骨架** 的不同，含苯环的烃称为 **芳香烃** ，不含苯环的烃称为 **脂肪烃**

2. 根据 **结构中是否含有不饱和键** ，可以将脂肪烃分为 **饱和烃** 和 **不饱和烃** ，烷烃为饱和烃，炔烃和烯烃为不饱和烃

## 脂肪烃

### 烷烃 $(\ce{C_{n}H_{2n+ 2} })$

1. **烷烃的存在形式**
   烷烃是一类最基础的有机化合物，广泛存在于自然界中。生活中的一些常见物质，如天然气、液化石油气、汽油、柴油、凡士林、石蜡等，主要成分都是烷烃
2. **烷烃的结构**
   烷烃分子中的碳原子都采取 $sp^3$ 杂化，形成四面体结构；碳原子以 $σ$ 键与其他碳原子或氢原子结合；每个碳原子形成 $4$ 个共价单键；除甲烷外，烷烃分子中既有极性键，又有非极性键
3. **烷烃的化学性质**
   烷烃的化学性质一般比较稳定，在通常状况下，烷烃不与强酸、强碱和强氧化剂（如溴水、$\ce{KMnO4}$ 溶液）反应，也难与其他物质化合，但在特定的条件下烷烃能发生下列反应
   1. **氧化反应**

      $$\ce{C_{n}H_{2n+2} +}\frac{3n +1}{2}\ce{O2->[点燃]nCO2 + }(n + 1)\ce{H2O}$$

   2. **卤代反应**

      在光照条件下，烷烃都能与纯的卤素单质发生取代反应

      $$
      \ce{CH4 + Cl2 ->[光] CH3Cl + HCl\quad CH3Cl + Cl2 ->[光] CH2Cl2 + HCl}
      $$

      $$
      \ce{CH2Cl2 + Cl2 ->[光] CHCl3 + HCl\quad CHCl3 + Cl2 ->[光] CCl4 + HCl}
      $$

      > $\ce{CH3Cl}$ 是气体（考察阿伏伽德罗常数时，注意仅 $\ce{CH3Cl}$ 在标况下是 $22.4\ce{L}$）；$\ce{CHCl3}$ 俗名氯仿
      >
      > 和卤素的反应中，一般不直接用 $\ce{F2}$ 和 $\ce{I2}$，因为 $\ce{F2}$ 反应剧烈，而 $\ce{I2}$ 不易反应

   3. **高温分解**

      烷烃在一定条件(加热、加压, 使用催化剂)下发生分解 反应, 可生成碳原子数较少的烷烃和烯烃, 高温下还可能生和氢气

      $\ce{C16H34 ->[加热、加压][催化剂] C8H18 + C8H16 (石油的裂化)}$

      $\ce{CH4 \xrightarrow{高温} C + 2H2}$

### 烯烃 $($ 单烯烃 $\ce{C_nH_{2n}})$

1.  **烯烃的结构**
    - 烯烃的官能团是 **碳碳双键**。分子中含有一个碳碳双键的烯烃称为单烯烃

    - 烯烃分子中的碳碳双键上的碳原子均采取 $sp^{2}$ 杂化，碳原子与氢原子间均形成 **单键**（$\sigma$ 键），碳原子与碳原子间以 **双键** 相连（$1$ 个 $\sigma$ 键，$1$ 个 $\pi$ 键），键角约为 $120 °$，分子中 **所有原子都处于同一平面内**

2.  **烯烃的化学性质**
    1.  **加成反应**：烯烃能与 $\ce{H2、X2}$(卤素单质)$、\ce{HX、H2O}$ 等发生加成反应
        1. 溴水

           $\ce{R-CH=CH2 +Br2 -> R-CHBr-CH2Br}$ _（工业上制备二氯代烃）_

           > $\ce{CH2=CH2 +Br2->CH2Br-CH2Br}$
           >
           > $\ce{CH2Br-CH2Br}$ 是无色液体，难溶于水，溶于四氯化碳。因此可使溴水或其四氯化碳溶液褪色，且不分层

        2. $\ce{H2}$

           $\ce{R-CH=CH2 +H2 ->[\Delta][催化剂] R-CH2-CH3}$

           > $\ce{CH3-CH=CH2 +H2 ->[\Delta][催化剂] CH3-CH2-CH3}$ _（丙烯转化成丙烷）_

        3. $\ce{H2O}$

           $\ce{R-CH=CH2 +H-OH ->[\Delta][催化剂]}$ <img src="./images/4.2.png" inline /> 或 $\ce{R-CH2-CH2OH}$ _（工业制备一元醇）_

           > $\ce{CH2=CH2 +H2O ->[\Delta][催化剂] CH3-CH2OH}$ _（乙烯制乙醇）_

        4. $\ce{HCl}$

           $\ce{R-CH=CH2 +HCl ->[一定条件] }$ <img inline src="./images/4.3.png"/> 或 $\ce{R-CH2-CH2Cl}$ _（工业制备单卤代烃）_

           > $\ce{CH2=CH2 +HCl ->[\Delta][催化剂] CH3-CH2-Cl}$ _（乙烯制氯乙烷）_

        5. 氰化物 $\ce{HCN}$

           $\ce{R-CH=CH2 +HCN ->[一定条件] }$ <img src="./images/4.4.png"/> 或 $\ce{R-CH2-CH2CN}$ _（实现碳链增长）_
        - 烯烃的不对称加成-马氏规则

                <img title="" src="./images/4.5.svg"  style="100px" />

          当不对称烯烃与含氢的化合物（ $\ce{HBr、H_{2} }$ 等）加成时，氢原子主要加到连有较多氢原子的碳原子上（马氏规则），在过氧化物存在的情况下, 氢原子主要加在连有较少氢原子的碳原子上（反马氏规则）

        - 实验室制备乙烯，即乙醇的消去反应

                <img src="./images/5.3.svg" style="zoom:25%;"/>

    2.  **加聚反应**

        在适宜的温度、压强和催化剂存在的条件下，乙烯分子中碳碳双键中的一个键可以断裂，分子间通过碳原子的相互结合形成很长的碳链

        生成聚乙烯：$\ce{nCH2=CH2->[一定条件]}\space[\!\!\!\ce{-CH2-CH2}$ $]\!\!\!-_n$ （聚乙烯，$n$ 为聚合度，$\ce{-CH_2-CH_2 -}$ 是链节）

        <img title="" src="./images/4.6.png" style="height:70px" />

        二烯烃加聚：$\ce{nCH2=CH-CH=CH_2 ->[一定条件]}\space[\!\!\!\ce{-CH2-CH=CH-CH2}$ $]\!\!\!-_n$

        烯烃共聚：$\ce{nCH2=CH2 +nCH2=CH-CH3->[一定条件]}\space[\!\!\!\ce{-CH2-CH2-CH(CH3)-CH2}$ $]\!\!\!-_n$

    3.  **氧化反应**
        1. 烯烃能使酸性高锰酸钾溶液 **褪色**：$\ce{CH2=CH2->[H+][KMnO4] CO2}$

           > 用于催熟果实、鉴别烷烃和烯烃；不能用于除去 $\ce{C2H6}$ 中的 $\ce{CH2=CH2}$ 会引入新的杂质 $\ce{CO2}$ ，可用溴水洗气
           >
           > 单烯烃被酸性高锰酸钾溶液氧化时，遵循以下原则：
           >
           > 1. 先将烯烃中的双键断开，烯烃会变成两部分
           > 2. 对于切割后的部分：
           >    > i. 对于 $\ce{=CH2}$，其最终产物会变为 $\ce{CO2}$
           >    > ii. 对于 $\ce{=CHR}$（$\ce{R}$ 为任意一个符合常理的基团），其对应的最终产物为 $\ce{R-COOH}$
           >    > iii. 对于 $\ce{=CR'R}$（$\ce{R,R'}$ 为任意一个符合常理的基团），其对应的最终产物为 <img inline src="./images/5.22.svg" style="zoom: 100%;">
           >
           > 例如，当归酸被酸性高锰酸钾溶液氧化成丙酮酸和乙酸的过程：
           >
           > <img title="" src="./images/4.27.png" style="zoom:130%" />

        2. 可燃性，燃烧通式为 $\ce{C_nH_{2n} + \frac{3n}{2}O_2 ->[点燃] nCO_2 + nH_2O}$（火焰明亮，出现黑烟）

3.  **共轭二烯烃**
    1. 定义：分子中含有 $2$ 个碳碳双键的烯烃称为二烯烃；分子中有 $2$ 个碳碳双键且两个双键只相隔一个单键的烯烃叫作共轭二烯烃，如 $1,3-$ 丁二烯 （ $\ce{C=C-C=C}$ ）

    2. $1,3-$ 丁二烯与溴单质发生加成反应时有两种情况：
       - $1,2-$加成（低温）

         $\ce{CH2=CH-CH=CH2 +Br2 ->}$ <img inline src="./images/4.7.svg"/>

       - $1,4-$加成（高温）

         $\ce{CH2=CH-CH=CH2 +Br2 ->}$ <img inline src="./images/4.8.svg"/>

       > 如果将低温转变为高温，$1,2-$ 加成的产物也会向 $1,4-$ 加成的方向转变

       > <img title="" src="./images/4.10.svg"  style="height:80px" />

### 炔烃 (单炔烃 $\ce{C_{n}H_{2n-2} }$)

1.  **炔烃的结构**
    - 分子中含有 **碳碳三键** （结构简式 <img inline src="./images/4.26.svg" style="width:100px"/>）的一类脂肪烃称为炔烃。分子中含有一个碳碳三键的炔烃称为单炔烃。

2.  **乙炔**
    - 分子中碳原子采取 $sp$ 杂化，碳原子和氢原子间均以 **单键**（$\sigma$ 键）相连接，碳原子和碳原子之间以 **三键**（$1$ 个 $\sigma$ 键和 $2$ 个 $π$ 键）相连接，相邻两个键之间的夹角为 $180 °$，分子为 **直线形** 结构

    - 乙炔（俗称电石气）是最简单的炔烃。乙炔是无色、无臭的气体，微溶于水，易溶于有机溶剂

    - 乙炔的实验室制法：

            <img title="" src="./images/4.11.png"  style="height:180px" />

      ① 发生装置：用 **饱和食盐水** 代替水的作用是减缓碳化钙 **$\ce{CaC2}$**（电石）与水反应的速率，实验原理为：$\ce{CaC2 + 2H2O -> C2H2↑ + Ca(OH)2}$。

      因反应剧烈且产生气泡，为防止产生的泡沫涌入导管，可以在装置①的导管口处塞入少量棉花（未画出）

      > 会产生 $\ce{H2S、PH3}$ 等还原性杂质气体

      > 制取乙炔 **不能使用启普发生器** 或具有启普发生器原理的装置，原因如下：
      >
      > - 碳化钙与水反应剧烈，不能随时停止；
      > - 反应过程中放出大量的热，易使得启普发生器炸裂；
      > - 生成的 $\ce{Ca(OH)2}$ 呈糊状，易堵塞球形漏斗。

      ② **硫酸铜溶液** 的作用是除去 $\ce{H2S}$ 等杂质气体，防止 $\ce{H2S}$ 等气体干扰乙炔性质的检验

      > 除去硫化氢： $\ce{H2S + CuSO4 = CuS v + H2SO4}$
      > 除去磷化氢： $\ce{12H2O + 11PH3 + 24CuSO4 \xlongequal{} 8Cu3P + 3H3PO4 + 24H2SO4}$

      ③ 乙炔能使酸性高锰酸钾溶液褪色

      ④ 乙炔能使溴的四氯化碳溶液褪色

      ⑤ 处对乙炔点燃，产生的现象为 **火焰明亮**，**伴有浓烈黑烟**（点燃前检验其纯度，防止爆炸）

    - **乙炔的化学性质**
      1. **加成反应**

         乙炔在一定条件下能与氢气、氯化氢和水等物质发生加成反应
         - $\ce{CH#CH + H2 \xrightarrow{\Delta}{催化剂} CH2 = CH2}\quad\ce{CH#CH + 2H2 ->[\Delta][催化剂] CH3CH3}$

         - $\ce{CH#CH + HCl ->[\Delta][催化剂] CH2 = CHCl}$

         - $\ce{CH#CH + H2O ->[\Delta][催化剂] CH3-CHO}$

         > 乙炔与水加成后的产物乙烯醇不稳定（ $\ce{CH2=CH-OH}$ ），很快转化为乙醛（互变异构）
         - $\ce{HC#CH->[HCN][催化剂] CH2 = CH-CN(丙烯腈)->[H2O、H+][\Delta] CH2 = CH-COOH}(丙烯酸)$

         > 用于增加碳链长度

      2. **加聚反应**

         乙炔可发生加聚反应，得到聚乙炔，聚乙炔可用于制备 **导电高分子材料**

         $\ce{nCH#CH->[一定条件]}\space[\!\!\!\ce{-CH=CH}$ $]\!\!\!-_n$

      3. **氧化反应**
         1. 燃烧：$2 \ce{C2H2 + 5 O2 ->[\text{点燃}] 4 CO2 + 2 H2O}$ 现象：火焰明显、冒出浓烈黑烟

         在氧气中燃烧时，氧炔焰的温度可达 $3000\ce{°\!C}$ 以上，因此常用它来焊接或切割金属

      4. 与强氧化剂反应：乙炔能被 $\ce{KMnO4}$ 氧化，使酸性 $\ce{KMnO4}$ 溶液褪色

         $\ce{2KMnO4 + C2H2 + 3H2SO4 -> K2SO4 + 2MnSO4 + 2CO2 + 4H2O}$

### 烷烃、烯烃、炔烃的结构和性质的比较

1. **物理性质**

   烷烃、烯烃、炔烃的物理性质类似，性质的变化规律也类似，都随分子中碳原子数的增加而呈周期性变化

   | 物理性质 |          相似性          |         递变性         |
   | :------- | :----------------------: | :--------------------: |
   | 熔沸点   |         一般较低         |        逐渐升高        |
   | 密度     |         均小于水         |        逐渐增大        |
   | 溶解性   | 难溶于水，易溶于有机溶剂 | 在水中的溶解度逐渐降低 |

   > **相对分子质量增大**，范德华力增大，沸点升高 一般情况下，同种烷烃的不同同分异构体中，**支链越多**，分子间作用力越小，沸点越低 状态：常温下由气态逐渐过渡到液态、固态，碳原子小于等于 4 的炔烃是气态烃
   >
   > 如沸点：正戊烷 > 异戊烷 > 新戊烷

2. **化学性质**

   | 名称     |                     烷烃                     |                        烯烃                        |                            炔烃                            |
   | :------- | :------------------------------------------: | :------------------------------------------------: | :--------------------------------------------------------: |
   | 取代反应 |                   光照卤代                   |                        $-$                         |                            $-$                             |
   | 加成反应 |                     $-$                      |       能与 $\ce{H2、X2、HX、H2O、HCN}$ 反应        |           能与 $\ce{H2、X2、HX、H2O、HCN}$ 反应            |
   | 氧化反应 | 燃烧，火焰较明亮；不与 $\ce{KMnO4(H+)}$ 反应 | 燃烧，火焰明亮伴有黑烟；能使 $\ce{KMnO4}$ 溶液褪色 | 燃烧，火焰很明亮伴有浓烈的黑烟；能使 $\ce{KMnO4}$ 溶液褪色 |
   | 加聚反应 |                     $-$                      |                       能发生                       |                           能发生                           |
   | 鉴别     |    不能使溴水和酸性 $\ce{KMnO4}$ 溶液褪色    |       均能使溴水和酸性 $\ce{KMnO4}$ 溶液褪色       |           均能使溴水和酸性 $\ce{KMnO4}$ 溶液褪色           |

### 脂肪烃与石油化工

| 石油炼制方法     | 目的                                   | 原理                                                                                           | 原料               |
| ---------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------ |
| 常压分馏（物理） | 获得以燃料油为常压主的不同石油分馏产品 | 用蒸发和冷凝的方法将原油分成不同沸点范围的馏分                                                 | 原油               |
| 减压分馏（物理） | 获得以润滑油为主的不同石油产品         | 通过减压降低重油的沸点，从重油中分离出不同沸点范围的馏分                                       | 重油               |
| 催化裂化（化学） | 提高汽油的产量和质量                   | 在加热、加压和催化剂存在的条件下，将相对分子质量大、沸点高的烃断裂成相对分子质量小、沸点低的烃 | 重油、凡士林、石蜡 |
| 裂解（化学）     | 获得有机化工原料                       | 又称深度裂化，在更高温度下，深度裂化，使长链烃断裂成相对分子质量小的气态烃或液态烃             | 煤油和柴油         |
| 催化重整（化学） | 获得芳香烃和提高汽油的质量             | 在催化剂作用下，把汽油中的直链烃转化为芳香烃和具有支链的异构烷烃                               | 汽油               |

- **催化裂化**

  $\ce{C16H34->[一定条件]C8H16 + C8H18}$

- **裂解**

  $\ce{C8H18->[催化剂][加热、加压]C4H10 + C4H8} \quad \ce{C4H10->[催化剂][加热、加压]C2H4 + C2H6}$

- **沸点顺序**

  $石油气<汽油<煤油<柴油<润滑油<重油$

> 煤的气化和液化都是化学变化

## 芳香烃

在烃类化合物中，有很多分子里含有一个或多个苯环，这样的化合物属于芳香烃，苯是最简单的芳香烃

<img title="" src="./images/4.1.png"  style="height:160px;width:auto" />

### 苯

1. **物理性质**

   苯是一种无色、有特殊气味的液体，有毒，不溶于水。苯易挥发。沸点为 $80.1\ce{°\!C}$，熔点 $5.5\ce{°\!C}$ ，常温下密度为 $0.88g/cm^3$ 。苯是一种重要的化工原料和有机溶剂，常用作萃取（用苯萃取碘水中的碘单质、萃取溴水中的溴单质）

2. **分子结构**

   **苯分子的碳碳键是一种介于碳碳单键和碳碳双键之间的特殊共价键**，**不存在碳碳双键**，也 **不具有碳碳单键和碳碳双键交替出现的结构**。故苯不能使溴的四氯化碳溶液褪色，也不能被酸性高锰酸钾溶液氧化。
   苯分子中 $6$ 个碳原子连接成平面正六边形，每个碳原子分别结合 $1$ 个氢原子，分子中 $6$ 个碳原子和 $6$ 个氢原子完全等价。人们称苯的这种特殊结构为苯环结构

   <img src="./images/4.12.png"  style="zoom:18%;"/>

3. **化学性质**
   1. **取代反应**
      1. 苯和溴在 $\ce{FeBr3}$ 催化下可以发生反应，生成溴苯

         <img src="./images/4.13.svg"  style="zoom:60%;"/>

         > 1. 苯与溴发生取代反应时，试剂选用纯净的液溴（不得使用溴水，使用溴水发生萃取，而非取代，未形成溴苯）。该反应中催化剂是 $\ce{FeBr3}$ ，实际操作中一般是加入铁粉与液溴，二者反应生成 $\ce{FeBr3}$
         > 2. 在催化剂作用下，苯也可以与其他纯净卤素单质发生取代反应，这类反应统称为卤代反应
         > 3. 纯净的溴苯是无色液体，不溶于水，密度比水大。溴苯常因溶有溴单质而显褐色
         > 4. 不能由于将产生的气体通入 $\ce{AgNO3}$ 溶液中产生淡黄色的沉淀（ $\ce{AgNO3}$ 与 $\ce{HBr}$ 生成 $\ce{AgBr}$ ）而判断反应的发生，因为产物含有杂质 $\ce{Br2}$ 蒸汽（可用 $\ce{CCl4}$ 洗气）

      2. 在浓硫酸作用下，苯在 $50-60\ce{°\!C}$ （水浴加热）与浓硝酸发生硝化反应，生成硝基苯

         <img src="./images/4.14.jpg"  style="zoom:50%;"/>

         > 纯净的硝基苯是无色、有苦杏仁味、密度比水大、不溶于水的油状液体，有毒，因溶有 $\ce{NO2}$ 而显黄色
         >
         > $\ce{H2SO4}$ 用作催化剂、吸水剂；水浴加热用于控制温度，受热均匀
         >
         > 注意：先加入浓硝酸，后加入浓硫酸（高中阶段浓硫酸均为后加入）

      3. 苯与浓硫酸在 $70-80\ce{°\!C}$ 可以发生磺化反应，生成苯磺酸

         <img src="./images/4.15.png"  style="zoom:30%;"/>

         > 苯磺酸易溶于水，是一种强酸，可以看作是硫酸分子里的一个羟基被苯环取代的产物

      4. **加成反应**

         在以 $\ce{Pt、Ni}$ 等为催化剂并加热、加压的条件下，苯能与氢气发生加成反应，生成环己烷

         <img src="./images/4.16.webp"  style="zoom:50%;"/>

         > 苯反应的特点：易取代，难加成（加成需要破坏苯的主体结构）
         >
         > 放出热量小于环己二烯，说明不存在三个双键

   2. **氧化反应**

      燃烧：苯具有可燃性，在空气里燃烧时火焰明亮，产生浓重的黑烟。

      $$\ce{2C6H6 + 15O2->[点燃] 12CO2 + 6H2O}$$

   3. **重要化学性质**
      1. 苯不能使酸性高锰酸钾溶液褪色

      2. 苯不能使溴的四氯化碳溶液褪色

      3. 苯使溴水褪色的原因是萃取而不是加成反应

      > 说明不存在三个双键

### 苯的同系物

苯环上的氢原子被烷基取代所得到的一系列产物称为苯的同系物，其通式为 **$\ce{C_nH_{2n-6}}\quad (n > 6)$**

1. **物理性质**

   苯的同系物一般是具有类似苯的气味的无色液体，不溶于水，易溶于有机溶剂，密度比水的小

   规律性：随着碳原子数的递增，苯的同系物的熔、沸点升高，密度增大，但都小于水的密度

2. **化学性质**

   苯的同系物与苯都含有苯环，在一定条件下发生 **溴代、硝化和催化加氢反应**。但由于苯环与烷基的相互作用，苯的同系物的化学性质与苯又有所不同。
   1. **氧化反应**
      1. 燃烧反应：$\ce{C_{ n }H_{ 2 n - 6 } + }\frac{ 3 n - 3 }{ 2 } \ce{O2 ->[点燃]nCO2 + }(n-3)\ce{H2O}$

      2. **与强氧化剂反应：苯的同系物大多数能被酸性 $\ce{KMnO4}$ 溶液氧化为 苯甲酸 而使其褪色**

      3. 烷基上 **与苯环直接相连的碳原子上必须有氢原子**，才能被酸性高锰酸钾氧化

      4. 无论侧链烃基有多少个 $\ce{C}$ 原子，烃基均被氧化为 $\ce{-COOH}$

         <img src="./images/4.17.png"  style="zoom: 20%;"/>

         <img src="./images/4.23.svg"  style="zoom:7%;"/>

         <img src="./images/4.24.svg"  style="zoom:70%;"/>

   2. **取代反应**
      1. **硝化反应**

         甲苯与浓硝酸和浓硫酸的混合物在加热条件下可以发生取代反应，生成一硝基取代物、二硝基取代物和三硝基取代物，硝基取代的位置均以甲基的邻、对位为主

         <img src="./images/4.18.svg"  style="zoom: 15%;"/>

         $2,4,6-$ 三硝基甲苯又叫梯恩梯(TNT)，是一种淡黄色晶体，不溶于水。它是一种烈性炸药，广泛用于国防、采矿、筑路、水利建设等

      2. **卤代反应**

         **在光照条件下**，甲苯与氯气发生取代反应时，氯原子取代甲基上的氢原子。反应后可能的有机产物是甲基上的氢原子分别被 $1$ 个、$2$ 个或 $3$ 个氯原子取代所生成的氯甲基苯

         **在 $\ce{FeBr3}$ 的催化下**，甲苯与氯发生取代反应生成的一氯代甲苯主要有两种：邻氯甲苯和对氯甲苯。**甲基的存在活化了苯环上处于甲基邻位和对位的氢原子**，使相应的 $\ce{C-H}$ 更容易断裂，发生取代反应。该反应对反应条件的要求更低

         <img src="./images/4.19.svg" style="zoom: 20%;"/>

   3. **加成反应**

      在 $\ce{Pt}$ 作催化剂和加热的条件下，甲苯可以与氢气发生加成反应

      <img src="./images/4.21.png"  style="zoom: 20%;"/>

### 稠环芳香烃

由两个或两个以上的苯环共用相邻的两个碳原子的芳香烃是稠环芳香烃

|     | 分子式        | 结构简式                                                   | 物理性质                                                   | 用途                                                                    |
| --- | ------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| 萘  | $\ce{C10H8}$  | <img inline src="./images/4.22.svg" style="zoom: 80%;" />  | 无色片状晶体，有特殊气味 <br/> 熔点 80 ℃，易升华，不溶于水 | ①曾用于杀菌、防蛀、驱虫 <br/> ②重要的化工原料，生产增塑剂、农药、染料等 |
| 蒽  | $\ce{C14H10}$ | <img inline  src="./images/4.25.svg" style="zoom: 80%;" /> | 无色晶体，易升华 <br/> 不溶于水，易溶于苯                  | 合成染料的重要原料                                                      |


---

## Original file: 05 烃的衍生物.md

---
description: "介绍烃的衍生物的分类，包括卤代烃、醇、酚等，重点讲解醇的分类、物理性质和化学性质。"
---

# 05 · 烃的衍生物

<img src="./images/5.0.svg"/>

根据官能团对有机化合物进行分类，是有机化学中常用的分类方法。用这种分类方法 可以将烃的衍生物分为 **卤代烃、醇、酚、醚、 醛、酮、羧酸、酯、胺、酰胺** 等

## 醇

### 醇的分类

1. 根据醇分子中所含羟基的数目：一元醇、二元醇、多元醇

2. 根据羟基所连烃基种类：

   $$
   \begin{cases}
   脂肪醇 \begin{cases}
   饱和醇(饱和一元醇\quad\!\!\ce{C_nH_{2n+1}OH}\quad n \ge 1) \\
   不饱和醇 \\
   \end{cases}\\
   脂环醇(环己醇\quad\!\!\ce{⌬\!-OH})\\
   芳香醇(苯甲醇\quad\!\!\ce{⌬\!-CH2OH})\\
   \end{cases}
   $$

### 生活中常见的醇

1. 甲醇( $\ce{CHOH}$ 木精)：无色、具有挥发性的液体易溶于水，沸点为 $65\ce{°\!C}$。甲醇有毒，误服会损伤视神经，甚至致人死亡。甲醇广泛应用于化工生产也可作为车用燃料

2. 乙二醇、丙三醇都是无色、粘稠、有甜味的液体，都易溶于水和乙醇，是重要的化工原料
   1. 乙二醇是汽车发动机防冻液的主要化学成分，也是合成涤纶等高分子化合物的主要原料

   2. 丙三醇具有很强的吸水能力，可用于制造日用化妆品

### 物理性质

1. 沸点
   1. **饱和一元醇** 的熔沸点随分子中 **碳原子数** 的递增而逐渐增大

   2. 相对分子质量相近的醇和烷烃相比，**醇的沸点远远高于烷烃的沸点**（**氢键的影响**）

   3. 碳原子数相同时，**羟基个数** 越多，醇的沸点越高；羟基的个数不限，但由于不稳定不存在一个 $\ce{C}$ 原子上连有 2 个羟基的醇

      > ①丙醇 ②丙二醇 ③丙烷 ④乙醇 ⑤丙三醇 等物质的沸点排列顺序：
      > $⑤>②>①>④>③$

2. 溶解性：

   醇在水中的溶解度一般随分子中 **碳原子数的增加而降低**。**羟基越多，溶解度越大**

   > 理解：烷基是憎水基，羟基是亲水基，接的烷基越多，使得羟基形成氢键导致溶解度增加的效果减弱，因此溶解性降低
   >
   > 甲醇、乙醇、丙醇、乙二醇、丙三醇等低级醇(碳数比较少的醇)可与水以任意比例混溶

3. 密度：醇的密度比水的密度小

### 化学性质

醇的化学性质主要由 **羟基** 官能团所决定。在醇分子中，由于氧原子吸引电子的能力比氢原子和碳原子的强(氧的电负性更大，吸引电子的能力更强)，使 $\ce{O-H}$ 和 $\ce{C-O}$ 的电子都向氧原子偏移。因此，醇在发生反应时， $\ce{O-H}$ 容易断裂，使羟基中的氢原子被取代，同样， $\ce{C-O}$ 也易断裂，使羟基被取代或脱去，从而发生取代反应或消去反应

#### 与活泼金属单质的置换反应

$\ce{2CH3CH2OH +2Na -> 2CH3CH2ONa + H2 ^}$

现象：钠沉于无水乙醇的底部（或因产生的氢气使得钠上下跳动），表面有气泡产生，慢慢消失；放出的气体可在空气中安静地燃烧，火焰呈淡蓝色（ $\ce{H2}$ ）；烧杯壁上有水珠生成；澄清石灰水未变浑浊（无 $\ce{CO2}$ ）

1. **乙醇羟基的 $\ce{H}$ 原子活泼性较水的 $\ce{H}$ 原子弱**（醇分子中的烷基具有 **推电子作用**）

   > 推电子作用：$\vec{\ce{CH3CH2}}\ce{-O-H}$
   >
   > 由于烷基具有推电子作用，使得 $\ce{O-H}$ 键极性变弱，因此反应不会很剧烈
   >
   > 「芙蓉犹想红，尘漫且不容」
   1. 其它活泼金属如钾、钙等也可与乙醇反应产生 $\ce{H2}$

   2. 产物乙醇钠在水中强烈水解：$\ce{CH3CH2ONa + H2O→CH3CH2OH + NaOH}$

> 与 $\ce{Na}$ 反应生成 $\ce{H2}$ 的官能团：$\ce{-COOH、-OH}$ (醇、酚)

#### 取代反应（以乙醇为例）

1. **醇与浓的氢卤酸**（ $\ce{HCl、HBr、HI}$ ）

   分子的碳氧键发生断裂，羟基被卤素原子取代，生成相应的卤代烃和水

   $\ce{CH3CH2-\!\!\!⁞\enspace OH + H-\!\!\!⁞\enspace Br -> CH3CH2\mathbf{Br} + H2O}$

   > 加热是为了蒸发为气体进入反应装置，加热并不是反应条件
   >
   > 实验室中会使用 $\ce{NaBr}$ 和浓硫酸代替浓氢溴酸

   > $\ce{C2H5Br + NaOH->[H2O][\Delta]C2H5OH + NaBr}$

2. **酯化反应**

   <img src="./images/5.1.svg" style="zoom:25%;"/>

   > **口诀：酸脱羟基醇脱氢**
   >
   > 对乙醇上的氧原子进行 $^{18}\ce{O}$ 进行追踪，发现出现在乙酸乙酯中，证明不是乙醇的碳氧键断裂（但一部分 $^{18}\ce{O}$ 还会留着乙醇中，因为是可逆反应）

   <img src="./images/5.39.png" style="zoom: 50%;"/>
   - 实验器材：铁架台 试管 导管 酒精灯
   - 试剂加入顺序：乙醇 3mL 乙酸 2mL 浓硫酸 2mL （可以集成「醇，硫，酸」）
   - 反应过程中右侧试管内液体上层有无色透明的油状液体产生，并且可以闻到香味
   - 饱和碳酸钠的作用：①吸收乙醇 ②中和乙酸 ③降低酯的溶解度
   - 浓硫酸的作用：①催化剂 ②吸收反应生成的水，使酯化反应平衡正向移动
   - 导管悬于液面上方：防止倒吸

3. **醇分子间脱水成醚**

   如果把乙醇与浓硫酸的混合物的温度控制在 **$140\ce{° C}$** 左右，每两个乙醇分子间会脱去一个水分子而生成乙醚

   <img src="./images/5.2.svg" style="zoom:25%;"/>

   乙醚是一种无色、易挥发的液体，有特殊气味，有麻醉作用，易溶于有机溶剂。像乙醚这样由 **两个烃基通过一个氧原子连接起来的化合物叫做醚**，**醚的结构可用 $\ce{R-O-R'}$ 来表示**， $\ce{R}$ 和 $\ce{R'}$ 都是烃基，可以相同，也可不同

   醚类物质在化工生产中被广泛用作溶剂，有的醚可被用作麻醉剂

#### 消去反应

- 将 **浓硫酸与乙醇按体积比 $3: 1$** 混合，即将 $15mL$ 浓硫酸緩缓加入到盛有 $5mL\enspace95\%$ 乙醇的烧杯中混合均匀（**浓硫酸加入乙醇中**），冷却后再倒入长颈圆底烧瓶中，并加入碎瓷片防止暴沸

- 加热混合溶液，**迅速升温到 $170\ce{° C}$**，将生成的气体 **先通入 $\ce{NaOH}$ 溶液除去杂质** 再分别通入 $\ce{KMnO4}$ 酸性溶液和溴的四氯化碳溶液中，观察现象

> 硫酸酒精 $3:1$：浓硫酸作催化剂与脱水剂
>
> 温度迅速 $170$ ：由于在 $140\ce{°C}$ 会发生脱水成醚，为避免产生杂质，应迅速升温
>
> $\ce{NaOH}$ 溶液除杂：通过导管的不仅有乙烯，还有挥发出来的乙醇，同时浓硫酸发生碳化，碳与浓硫酸再次反应，产生二氧化硫杂质，浓硫酸有强氧化性，生成 $\ce{CO2}$ 杂质。因此，不能将其不经除杂直接通入 $\ce{KMnO4}$ 或 溴水 中验证乙烯具有还原性，乙醇和 $\ce{SO2}$ 会使前者褪色， $\ce{SO2}$ 会使后者褪色

<img src="./images/5.4.png" style="zoom:33%;"/>

实验现象：产生了气体，该气体使酸性高锰酸钾溶液褪色，使溴的四氯化碳溶液褪色，烧瓶内有黑色固体生成

- 原理：

<img src="./images/5.3.svg" style="zoom:25%;"/>

- **反应条件：邻位 $\ce{C}$ 原子上有 $\ce{H}$**

  > 若邻位碳原子上有多种化学环境的氢原子，则有多种可能的消去方式

#### 氧化反应

1. **乙醇的燃烧**：火焰呈淡蓝色，放出大量的热

   $\ce{CH3CH2OH + 3O2->[点燃]2CO2 + 3H2O}$

2. **醇的催化氧化**

   <img src="./images/5.5.svg" style="zoom:25%;"/>

   <img src="./images/5.6.png" style="zoom:33%;"/>

   **条件：与$\ce{-OH}$相连的碳必须有 $\ce{H}$，才能发生催化氧化反应**

   **氧化反应**：有机物分子中失去氢原子或加入氧原子的反应（**去$\ce{H}$加$\ce{O}$**）

   **还原反应**：有机物分子中加入氢原子或失去氧原子的反应（**加$\ce{H}$去$\ce{O}$**）
   - **乙醇的催化氧化**

     $$
     {\mathop{\ce{CH3CH2OH}}\limits_{乙醇}\ce{->[氧化][2e-]} \mathop{\ce{CH3CHO}}\limits_{乙醛}\ce{->[氧化][2e-]}\mathop{\ce{CH3COOH}}\limits_{乙酸}}
     $$

     $\ce{2CH3CH2OH + O2 ->[Cu/Ag][△]2CH3CHO + 2H2O}$

     $\ce{铜丝->[\Delta]变黑->[插入乙醇溶液]变红,有刺激性气味产生}$

     分析：$\ce{2Cu + O2\xlongequal{\Delta}2CuO}$

     $\ce{2CuO + 2CH3CH2OH->[\Delta]2Cu + 2CH3CHO + 2H2O}$

     $\ce {2CH3CH2OH + O2 ->[Cu][△]2CH3CHO + 2H2O}$

     如果遇到强氧化剂（例如酸性高锰酸钾、酸性重铬酸钾溶液），直接氧化为乙酸

3. **醇与酸性重铬酸钾**

   $\ce{K2Cr2O7(橙红色) + C2H5OH + H2SO4->Cr2(SO4)3(绿色) + CH3COOH + K2SO4 + H2O}$

   > 交警利用乙醇能使橙色的酸性重铬酸钾变绿，检查司机是否酒后驾车

#### 乙醇的反应与断键位置总结

<table>
    <thead>
        <tr>
            <td colspan="2"> 反应类型 </td>
            <td> 反应物 </td>
            <td> 反应条件 </td>
            <td> 断键位置 </td>
            <td rowspan="8"> <img src="./images/5.7.png" style="zoom: 30%;"/> </td>
        </tr>
        <tr>
            <td colspan="2"> 置换反应 </td>
            <td> 乙醇、活泼金属 </td>
            <td>-</td>
            <td> ① </td>
        </tr>
        <tr>
            <td rowspan="3"> 取代反应 </td>
            <td> 卤代 </td>
            <td> 乙醇、浓 HX </td>
            <td>-</td>
            <td> ② </td>
        </tr>
        <tr>
            <td> 分子间脱水 </td>
            <td> 乙醇 </td>
            <td> 浓硫酸，140 ℃ </td>
            <td> ①/② </td>
        </tr>
        <tr>
            <td> 酯化 </td>
            <td> 乙醇、羧酸 </td>
            <td> 浓硫酸，△ </td>
            <td> ① </td>
        </tr>
        <tr>
            <td colspan="2"> 消去反应 </td>
            <td> 乙醇 </td>
            <td> 浓硫酸，170 ℃ </td>
            <td> ②⑤ </td>
        </tr>
        <tr>
            <td rowspan="2"> 氧化反应 </td>
            <td> 催化氧化 </td>
            <td> 乙醇、O <sub> 2 </sub> </td>
            <td> Cu 或 Ag, △ </td>
            <td> ①③ </td>
        </tr>
        <tr>
            <td> 燃烧 </td>
            <td> 乙醇、O <sub> 2 </sub> </td>
            <td> 点燃 </td>
            <td> 全部 </td>
        </tr>
    </thead>
</table>

### 醇的同分异构体

饱和一元醇的通式为 $\ce{C_nH_{2n+1}OH}$，分子式满足 $\ce{C_nH_{2n+2}O}$ 的有机物，可能是醇，也可能是醚，在醇醚里再分别考虑碳链异构、官能团位置异构。因此，$\ce{C3H8O}$、$\ce{C4H10O}$、$\ce{C5H12O}$ 不一定为同系物

## 酚

- 定义：(酚)羟基( $\ce{-OH}$ )与苯环直接相连的化合物称为酚

  > 与 $\ce{-OH}$ 相连的苯环可以是单环，也可以是稠环

- 苯酚结构

   <img src="./images/5.8.png"  style="zoom: 25%;"/>

  > 至少有 12 个原子共平面，最多有 13 个原子共平面

### 苯酚的物理性质

| 颜色 | 味道     | 状态 | 熔点        | 溶解度                     |
| ---- | -------- | ---- | ----------- | -------------------------- |
| 无色 | 特殊气味 | 晶体 | $43\ce{°C}$ | $9.2g$（可以与水形成氢键） |

- 溶解在水中出现白色浑浊。当温度高于$65\ce{° C}$时能与水混溶；苯酚易溶于酒精、苯等有机溶剂
- 苯酚有毒，也具有消毒作用，对皮肤有腐蚀性。如不慎沾到皮肤上，应立即用酒精冲洗，再用水冲洗（苯酚对酒精的溶解度比较大）
- 放置时间较长的苯酚往往是粉红色的，这是部分苯酚被空气中的氧气氧化所致（苯醌）。因此，苯酚应密封保存

### 苯酚的化学性质

#### 弱酸性

由于苯酚中的羟基和苯环直接相连，苯环与羟基之间的相互作用使酚羟基在性质上与醇羟基有显著差异。
酚羟基中的氢原子比醇羟基中的氢原子更活泼，**苯酚的羟基在水溶液中能够发生部分电离，显示弱酸性**，故苯酚俗称石炭酸

**苯酚水溶液不能使酸碱指示剂变色**

|     |                                     实验操作及现象                                      |                       方程式                        |
| :-: | :-------------------------------------------------------------------------------------: | :-------------------------------------------------: |
|  1  | 向盛有 $0.3$g 苯酚晶体的试管中加入 2 毫升蒸馏水 <br /> 振荡试管震荡后，液体呈乳白色沉淀 |  <img src="./images/5.9.svg" style="height:50px"/>  |
|  2  |                    滴加 5%氢氧化钠溶液并振荡试管<br>液体由浑浊变澄清                    | <img src="./images/5.10.svg" style="height:60px" /> |
|  3  |                   向试管中继续滴加稀盐酸后<br>溶液由澄清又重新变浑浊                    | <img src="./images/5.11.svg" style="height:60px"/>  |
|  4  |                               向苯酚钠溶液中通入二氧化碳                                | <img src="./images/5.12.svg" style="height:60px"/>  |
|  5  |                                 向苯酚溶液中通入碳酸钠                                  | <img src="./images/5.42.svg" style="height:60px"/>  |

> 结论与说明：
>
> 1. 常温下苯酚在水中的溶解度不大
> 2. 苯酚有酪酸性；苯酚钠易溶于水；苯酚可以与 $\ce{NaOH}$ 发生中和反应
> 3. 常温下苯酚在水中的溶解度不大，生成的苯酚不能完全溶于水
> 4. 酸性：碳酸 &gt; 苯酚 &gt; 碳酸根；反应产物与通入 $\ce{CO2}$ 的量无关

#### 取代反应

向盛有少量苯酚稀溶液的试管里逐滴加入过量饱和的溴水，边加边振荡

实验现象：立即产生 **白色沉淀**（该反应很灵敏，可用于苯酚的定性检验和定量测定）

<img src="./images/5.13.svg"  style="zoom: 60%;"/>

羟基对苯环的影响，**使苯环上羟基邻、对位氢原子更活泼，易被取代**

酚与浓溴水发生取代反应时，只取代羟基的邻，对位氢原子，间位氢原子不取代

> 由于相似相容原理（2，4，6-三溴苯酚溶于苯）该反应不能用于苯中苯酚的除杂

> 苯酚与苯取代反应的不同
>
> |                      |          苯酚           |             苯              |
> | :------------------: | :---------------------: | :-------------------------: |
> |        反应物        |      浓溴水与苯酚       |          液溴与苯           |
> |       反应条件       |       不用催化剂        |    $\ce{FeBr3}$ 作催化剂    |
> |       反应速率       |    反应灵敏，速率快     |        反应速率较慢         |
> | 取代苯环上的氢原子数 | 取代苯环上 $3$ 个氢原子 | 一次取代苯环上 $1$ 个氢原子 |
>
> 结论：苯酚与溴取代反应比苯容易
> 原因：酚羟基对苯环影响，使苯环上（邻、对位）氢原子变得活泼

#### 显色反应

实验：向盛有少量苯酚的稀溶液的试管中，滴入几滴 $\ce{FeCl3}$ 溶液，振荡，观察现象
现象：溶液显紫色（利用这一反应也可以检验苯酚的存在）

原理：

$$\ce{6C6H5OH + Fe^{3+} -> [Fe(C6H5O)6]^{3-} + 6H+}$$

酚类物质一般都可以与 $\ce{FeCl3}$ 作用显色，可用于检验其存在

#### 氧化反应

苯酚晶体在常温下易被空气中的氧气氧化生成粉红色物质
**苯酚可以被酸性高锰酸钾溶液等强氧化剂氧化，使高锰酸钾溶液褪色**（与醇羟基类似）

#### 加成反应

苯酚中含有苯环，可以与氢气发生加成：

<img src="./images/5.14.svg" style="zoom: 67%;"/>

## 醛

### 醛的定义

- **定义**：由烃基（或氢原子）与醛基相连而构成的化合物，简写为 $\ce{RCHO}$

- **官能团**：醛基，结构式为 <img src="./images/5.15.svg" style="zoom: 67%;"/>，可简写为 $\ce{-CHO}$

- **通式**：饱和一元醛的通式为 $\ce{C_nH_{2n}O}( n\geq1 )$ 或 $\ce{C_nH_{2n+1}CHO}( n\geq0 )$

  > 前者可能存在同分异构体，后者直接指向饱和一元醛

### 物理性质

1. **熔、沸点**：通常情况下，醛类除甲醛是气体外，其他醛都是无色液体或固体。醛类的熔、沸点随着分子内碳原子数的增加而呈增大趋势

2. 溶解性：醛类物质在水中的溶解度随分子内碳原子数的增加而呈减小趋势，这是由于属于极性基团的 $\ce{-CHO}$ 在分子中所占的比例减小

3. 乙醇的物理性质

   乙醛( $\ce{CH3CHO}$ )是无色、具有刺激性气味的液体，密度比水小，沸点为 $\ce{20.8°\!C}$，易挥发，易燃烧，能与水 $^1$、乙醇等互溶

   > $^1$ 本身不形成氢键，与水形成氢键

### 化学性质

#### 加成反应

1. **催化加氢**

   乙醛蒸气和氢气的混合气体通过热的镍催化剂，发生催化加氢反应，得到乙醇

   <img src="./images/5.16.svg" style="zoom: 25%;"/>

   > 1. 醛基催化加氢一定生成端醇
   > 2. 醛的催化加氢反应也是 **还原反应**

   > 乙醇氧化成乙醛：$\ce {2CH3CH2OH + O2 ->[Cu/Ag][△]2CH3CHO + 2H2O}$

2. **与 $\ce{HCN}$ 加成**

   > 在醛基的碳氧双键中，由于氧原子的电负性较大，碳氧双键中的电子偏向氧原子，**使氧原子带部分负电荷，碳原子带部分正电荷**，从而使醛基具有较强的极性 <img src="./images/5.17.svg" style="zoom:20%;"/>

   醛基与极性分子加成时，极性分子中带正电荷的原子或原子团连接在醛基的氧原子上，带负电荷的原子或原子团连接在碳原子（此类加成反应可用于增长碳链）

   <img src="./images/5.18.svg" style="zoom: 25%;"/>

3. **羟醛缩合反应**（常用的增长碳链的方法）

   醛分子中在醛基邻位碳原子上的氢原子 ( $α-\ce{H}$ ) 受羰基吸引电子作用的影响，具有一定的活泼性，分子内含有 $α-\ce{H}$ 的醛在一定条件下可以发生加成反应，生成 $\beta-$ 羟基醛，该产物易失水，得到 $\alpha,\beta-$ 不饱和醛

   <img src="./images/5.19.svg" style="zoom: 25%;"/>

#### 氧化反应

1.  **银镜反应**
    - 银氨溶液的配制：

      取 $1mL\space 2\%$ 的 $\ce{AgNO3}$ ，溶液于 **洁净** 试管中，然后边振荡试管边 **逐滴** 滴入 $2\%$ 的稀氨水，至产生的 **沉淀恰好完全溶解**，制得银氨溶液，化学反应方程式为：

      $\ce{AgNO3 + NH3*H2O=AgOH v + NH4NO3}$  
      $\ce{AgOH + 2NH3*H2O=[Ag(NH3)2]OH + 2H2O}$

    - 向银氨溶液中滴入 3 滴乙醛，振荡后将试管放在热水浴中温热。观察实验现象

         <img src="./images/5.20.png" style="zoom: 40%;"/>

      化学方程式：$\ce{CH3CHO + 2[Ag(NH3)2]OH ->[\Delta]H2O + 2Ag v + 3NH3 + CH3COONH4}$

      离子方程式：$\ce{CH3CHO + 2[Ag(NH3)2]+ + 2OH- ->[\Delta] H2O + 2Ag v + 3NH3 + CH3COO- + NH+4}$

      > 记忆：水银铵，$123$，再加一个羧酸铵

    - 该反应可以用来检验分子中是否存在醛基并可以确定醛基个数

    工业上可用银镜反应对玻璃涂银制镜和制保温瓶瓶胆

2.  **与新制 $\ce{Cu(OH)2}$ 反应**

    $\ce{2NaOH +CuSO4=Cu(OH)2 v +Na2SO4}$

    $\ce{CH3CHO + 2Cu(OH)2 + NaOH->[\Delta] CH3COONa + Cu_2O v +3H2O}$

    > $\ce{Cu(OH)2}$：蓝色 $\quad\ce{Cu2O}$：砖红色
    - 该反应需要加入过量的 $\ce{NaOH}$

    - 该反应可以用来检验分子中是否存在醛基并可以确定醛基个数

    斐林试剂检验葡萄糖（**检验葡萄糖的醛基**）

- **醛类的两个特征反应及 $\ce{-CHO}$ 的检验**

  | 特征反应 |                                                                         银镜反应                                                                         |                                                                                        与新制的 $\ce{Cu(OH)2}$ 反应                                                                                         |
  | :------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
  |   现象   |                                                                      产生光亮的银镜                                                                      |                                                                                               产生砖红色沉淀                                                                                                |
  | 注意事项 | 1. 试管内壁必须洁净<br>2. 银氨溶液现用现配<br>3. 水浴加热，不可用酒精灯直接加热<br>4. 醛用量不宜太多，如乙醛一般滴 3 滴<br>5. 银镜可用稀硝酸浸泡洗涤除去 | 1. 新制的 $\ce{Cu(OH)2}$ 要现用现配<br>2. 配制新制的 $\ce{Cu(OH)2}$ 时，所用 $\ce{NaOH}$ 溶液必须过量 <br/> 3. 该反应必须加热到沸腾，才有明显的红色沉淀产生，但不能太久，否则会有黑色的沉淀 $\ce{CuO}$ 生成 |

  > 可以检验含醛基的物质：醛类、甲酸、甲酸酯、葡萄糖等还原糖

1. **被强氧化剂氧化**
   - 酸性 $\ce{KMnO4}$ 溶液 $\ce{->[醛]}$ **紫红色** 变为 **无色**

   - 酸性 $\ce{K2Cr2O7}$ 溶液 $\ce{->[醛]}$**橙色** 变为 **绿色**

   - 可以使溴水褪色，但不能使溴的 $\ce{CCl4}$ 溶液褪色

     $\ce{Br2 +H2O<=>HBr +HBrO\quad CH3CHO + HBrO->CH3COOH +HBr}$

     $\ce{\Rightarrow CH3CHO +H2O->CH3COOH +2HBr}$

2. **燃烧**（具有可燃性）

   $\ce{2C2H4O + 5O2->[点燃] 4CO2 + 4H2O}$

#### 缩聚反应

**酚醛树脂的合成**

<img src="./images/5.36.svg" style="zoom: 75%;"/>

<img src="./images/5.37.svg" style="zoom: 25%;"/>

### 常见的醛类

#### 甲醛

俗名蚁醛，最简单的醛类物质，是一种无色、有强烈刺激性气味的 **气体**，易溶于水，质量分数为 $35\%\sim40\%$ 的水溶液叫做 **福尔马林**，具有防腐和杀菌能力，常作防腐杀菌剂（消毒、浸制标本）；制药（农药、消毒剂），香料，染料；制造酚醛树脂、脲醛树脂、维纶等

- 氧化

 <img src="./images/5.21.svg" style="zoom: 25%;">

- 银镜反应：$\ce{HCHO + 4 [Ag(NH3)2] OH ->[\Delta] 2H2O + 4Ag v + 6NH3 + (NH4)2CO3}$

- 与新制 $\ce{Cu(OH)2}$ 反应：$\ce{HCHO + 4Cu(OH)2 + 2NaOH->[\Delta] Na2CO3 + 2Cu2O v + 6H2O}$

  > $\ce{HCHO + 2[Ag(NH3)2]OH ->[\Delta]H2O + 2Ag v + 3NH3 + HCOONH4}$
  >
  > $\ce{HCOONH4 + 2[Ag(NH3)2]OH ->[\Delta]H2O + 2Ag v + 3NH3 + (NH4)2CO3}$

- 加成反应：$\ce{HCHO +H2->[催化剂][\Delta] CH3OH}$

#### 苯甲醛

- 物理性质：**苯甲醛是最简单的芳香醛**，俗称苦杏仁油，是一种有苦杏仁味的无色液体
- 用途：苯甲醛是制造染料、香料及药物的重要原料

## 酮

### 酮的定义

1. 概念：羰基与两个烃基相连的化合物
2. 官能团：酮羰基（羰基，<img src="./images/5.24.svg" style="zoom: 70%;">）
3. 酮结构可以表示为：<img src="./images/5.22.svg" style="zoom: 70%;">
4. 饱和一元酮的通式为：$\ce{C_nH_{2n}O}\quad (n>3)$
5. 分子中含相同碳原子数的 **饱和一元醛** 与 **饱和一元酮** 的分子式相同，结构不同，互为同分异构体

### 丙酮

1. 结构简式：$\ce{CH3COCH3}$

2. 丙酮的性质：无色透明的液体，沸点 $56.2\ce{°C}$，易挥发，能与水、乙醇等互溶

3. 丙酮 **不能** 被银氨溶液、新制的氢氧化铜等弱氧化剂氧化

   在催化剂存在的条件下，**丙酮可以发生催化加氢反应，也能与氰化氢加成**

   $\ce{CH3COCH3 +H2->[催化剂][\Delta]CH3CH(OH)CH3}$

4. 酮是重要的有机溶剂和化工原料。例如，丙酮可用作化学纤维、钢瓶储存乙炔等的溶剂，还用于生产有机玻璃、农药和涂料等

### 醛与酮的区别与联系

<table id="tg-5070X">
<tbody>
  <tr>
    <td colspan="2"> </td>
    <td> 醛 </td>
    <td> 酮 </td>
  </tr>
  <tr>
    <td colspan="2"> 官能团 </td>
    <td> 醛基 </td>
    <td> 酮羰基 </td>
  </tr>
  <tr>
    <td colspan="2"> 官能团位置 </td>
    <td> 碳链末端（最简单的醛是甲醛）</td>
    <td> 碳链中间（最简单的酮是丙酮）</td>
  </tr>
  <tr>
    <td rowspan="2"> 化学性质 </td>
    <td> 加成反应 </td>
      <td colspan="2"> 均可与 H <sub> 2 </sub>、HCN 加成 </td>
  </tr>
  <tr>
    <td> 氧化反应 </td>
    <td> 能被银氨溶液、新制氢氧化铜等弱氧化剂氧化 </td>
    <td> 不能被银氨溶液、新制氢氧化铜等弱氧化剂氧化 </td>
  </tr>
  <tr>
    <td colspan="2"> 联系 </td>
    <td colspan="2"> 碳原子数相同的饱和一元脂肪醛和饱和一元脂肪酮 互为同分异构体 </td>
  </tr>
</tbody>
</table>

## 羧酸

1. **定义**：由烃基（或氢原子）与羧基相连而构成的化合物

2. **官能团：$\ce{-COOH}$**

3. **饱和一元脂肪酸的通式**：**$\ce{C_{n}H_{2n}O2}\quad (n\geq1)\quad$** 或 **$\quad\ce{C_{n}H_{2n+1}COOH}\quad (n\geq0)$**

4. **分类**：
   $$
   羧酸\begin{cases}
   根据烃基\begin{cases}
   低级脂肪酸\quad\ce{CH3COOH}\\
   高级脂肪酸\begin{cases}
   硬脂酸&\ce{C17H35COOH}\\
   软脂酸&\ce{C15H31COOH}\\
   油酸&\ce{C17H33COOH}\\
   \end{cases}\\
   \end{cases}\\
   根据羟基数目\begin{cases}
   一元羧酸&\ce{CH3COOH}\\
   二元羧酸&\ce{HOOC-COOH}\\
   多元羧酸&柠檬酸\\
   \end{cases}\\
   根据羟基是否饱和\begin{cases}
   饱和羧酸&\ce{CH3COOH}\\
   不饱和羧酸&\ce{CH2 = COOH}\\
   \end{cases}\\
   \end{cases}
   $$

### 物理性质

1. **溶解性**：**分子中碳原子数在 4 以下的羧酸能与水氨溶**。随着分子中碳原子数的增加，一元羧酸在水中的溶解度迅速减小，甚至不溶于水（高级脂防酸是不溶于水的蜡状固体）
2. **沸点**：羧酸分子间可以形成 **氢键**，由于羧酸分子形成氢键的机会比相对分子质量相近的醇多，**羧酸的沸点比相应的醇的沸点高**，并且 **随着分子中碳原子数的增加，一元羧酸的沸点逐渐升高**

### 常见羧酸

- **甲酸**（最简单的羧酸）

  俗称蚁酸，是一种无色、有刺激性气味的液体，有腐蚀性，能与水、乙醇等互溶。甲酸在工业上可用作还原剂，在医疗上可用作消毒剂。甲酸中 **既有醛基**，**又有羧基**，所以甲酸既具有醛的性质（银镜反应、与氢氧化铜反应、与高锰酸钾反应），又具有羧酸的性质（酸的通性、酯化反应）

- **乙酸**

  是具有强烈刺激性气味的液体，纯净的乙酸又称为 **冰醋酸**

- **苯甲酸**

  俗称安息香酸，是一种无色晶体，易升华，微溶于水，易溶于乙醇。其钠盐是常用的 **食品防腐剂**

- **乙二酸**

  俗称 **草酸**，是无色透明晶体，通常含有结晶水，可溶于水和乙醇，以钠盐或钙盐形式广泛存在于植物中。草酸钙($\ce{CaC2O4}$)难溶于水，是人体肾结石和膀胱结石的主要成分。乙二酸是化学分析中常用的还原剂

### 化学性质

羧酸的化学性质主要取决于羧基官能团。由于受氧原子电负性较大等因素的影响，$\ce{O-H}$ 键、$\ce{C-O}$ 键容易断裂：
**当$\ce{O-H}$ 键断裂时**：会解离出 $\ce{H+}$，使羧酸表现出酸性
**当$\ce{C-O}$ 键断裂时**：$\ce{-OH}$ 可以被其他基团取代，生成酯、酰胺等羧酸衍生物

#### 弱酸性

1. 一元羧酸的电离方程式：$\ce{R-COOH<=>R-COO- +H+}$
2. 能使酸碱指示剂变色：使得紫红色石蕊试纸变红
3. 与活泼金属发生置换反应：$\ce{2CH3COOH + Mg=Mg(CH3COO)2 +H2 ^}$
4. 与碱性氧化物反应：$\ce{2CH3COOH + CuO=Cu(CH3COO)2 +H2O}$
5. 中和反应：$\ce{CH3COOH + NaOH=CH3COONa +H2O}$
6. 与某些盐反应：$\ce{2CH3COOH + CaCO3=Ca(CH3COO)2 +H2O + CO2 ^}$

**乙酸、碳酸 和 苯酚 的酸性比较**

<img src="./images/5.25.png"  style="zoom: 33%;"/>

1. A 装置：有无色气体产生，说明酸性：乙酸 $>$ 碳酸;
   方程式：$\ce{2CH3COOH +Na2CO3→2CH3COONa +CO2 ^ +H2O}$
2. C 装置：溶液变浑浊，说明酸性：碳酸 $>$ 苯酚
   方程式：$\ce{CO2 +H2O +C6H5ONa->C6H5OH +NaHCO3} $
3. B 装置：
   除去 $\ce{CO2}$ 中的乙酸蒸气，防止对碳酸酸性大于苯酚的检验产生干扰
4. 实验结论：酸性乙酸 $>$ 碳酸 $>$ 苯酚

> 常见物质的酸性强弱：乙二酸 $>$ 甲酸 $>$ 苯甲酸 $>$ 乙酸 $>$ 丙酸 $>$ 碳酸 $>$ 苯酚 $>$ $\ce{HCO^-_3}$

#### 取代反应

<img src="./images/5.1.svg" style="zoom:25%;"/>

<img src="./images/5.26.svg" style="zoom:25%;"/>

#### 还原反应

与醛、酮的联基相比，羧基中的羰基较难发生加成反应，只有在特定条件或催化剂作用下，反应才能进行。羧酸很难通过催化加氢的方法被还原，**用氢化铝锂能将羧酸还原为相应的醇**

$\ce{R-COOH->[LiAlH4]R-CH2OH}$

#### $\alpha-\ce{H}$ 被取代的反应

羧酸分子中的 $\alpha-\ce{H}$ 较活泼，易被取代。通过羧酸 $\alpha-\ce{H}$ 的取代反应，可以合成卤代酸，进而制得氨基酸、羟基酸等

$\ce{RCH2COOH +Cl2->[催化剂][\Delta] R-CHClCOOH +HCl}$

## 酯

1. **定义**：酯是羧酸分子羧基中的 $\ce{-OH}$ 被 $\ce{-OR'}$ 取代后的产物，结构简写为 $\ce{RCOOR'}$ 其中 $\ce{R}$ 和 $\ce{R'}$ 可以相同，也可以不同，但 $\ce{R'}$ 不能接氢
2. **官能团**：<img src="./images/5.38.svg" style="zoom:100%;"/> （酯基）
3. **通式**：饱和一元脂肪羧酸酯的分子通式为 $\ce{C_nH_{2n}O_2\quad(n\geq2)}$
4. **命名**：依据水解后生成的酸和醇的名称来命名：命名时，羧酸的名称写在前面，醇的名称写在后面，去掉「醇」换成「酯」，即命名为「**某酸某酯**」
5. **存在**：酯类广泛存在于自然界中，很多鲜花和水果的香味都来自酯。如苹果里含有戊酸戊酯，菠萝里含有丁酸乙酯，香蕉里含有乙酸异戊酯等
6. **用途**：低级酯是具有芳香气味的液体，可用做饮料、糖果和糕点等的香料

### 物理性质

1. 难溶于水，密度一般比水小
2. 易溶于苯、$\ce{CCl4}$、乙醇等有机溶剂中

### 化学性质

**水解反应（取代反应）**

在酸或碱催化的条件下，酯可以发生水解反应生成相应的酸和醇。酯的水解反应是酯化反应的逆反应。在碱性条件下，酯水解产生的羧酸可以与碱发生反应，使羧酸浓度减小，即减小了生成物的浓度，化学平衡正向移动，使酯的水解程度加大

酸性条件：$\ce{RCOOR' +H2O <=>[稀H2SO4][\Delta] RCOOH +R'OH}$

碱性条件：$\ce{RCOOR' +NaOH ->[\Delta] RCOONa +R'OH}$

> **$\ce{C_nH_{2n}O_2}$ 的同分异构体（羧酸、酯、羟基醛）**
>
> 例如：$\ce{C4H8O2}$（11 种）
>
> - 羧酸：$\ce{C3H7-COOH}$（丙基有 2 种不同结构）
> - 酯（4 种）
>
>   $\ce{H-COO-C3H7}$（2 种）、$\ce{CH3-COO-C2H5}$（1 种）、$\ce{CH3CH2-COO-CH3}$（1 种）
>
> - 羟基醛（5 种）
>
>   $\ce{C^1 - C^2 - C^3 - CHO}$（3 种）、$\ce{C^1 - C^2(C^1) - CHO}$（2 种）
>
> 例如：$\ce{C5H10O2}$（25 种）
>
> - 羧酸：$\ce{C4H9-COOH}$（丁基有 4 种不同结构）
> - 酯（9 种）
>
>   $\ce{H-COO-C4H9}$（4 种）、$\ce{CH3-COO-C3H7}$（2 种）、$\ce{C2H5-COO-C2H5}$（1 种）、$\ce{C3H7-COO-CH3}$（2 种）
>
> - 羟基醛（12 种）
>
>   $\ce{C^1 - C^2 - C^3 - C^4 - CHO}$（4 种）、$\ce{C^4 - C^3 - C^2(C^1) - CHO}$（4 种）、$\ce{C^1 - C^2(C^1) - C^3 - CHO}$（3 种）、$\ce{C^1(C^2)3 - CHO}$（1 种）
>
>   > - 能与 $\ce{NaOH(aq)}$ 反应：4（中和）+9（水解）= 13
>   > - 能发生银镜反应：12（醛基）+4（甲酸酯）= 16
>   > - 既能与 $\ce{NaOH(aq)}$ 反应，又能发生银镜反应：4 种（甲酸酯）

## 卤代烃

1. 烃分子中的 **氢原子** 被 **卤素原子** 取代后生成的化合物
2. 官能团：碳卤键（<img src="./images/5.32.svg" style="zoom: 70%;"/>）
3. 一元卤代烃可表示为：$\ce{R-X}$
4. 按卤素原子种类分：氟代烃、氯代烃、溴代烃、碘代烃
5. 根据烃基的不同分为 饱和卤代烃 、不饱和卤代烃 和 芳香卤代烃 等
6. 常见卤代烃
   1. $\ce{CHCl3}$：氯仿 过去曾经作麻醉剂，能够与空气中的氧气作用生成「光气」
   2. $\ce{CCl2F2}$：一种氟氯烃（氟利昂）造成臭氧层空洞
   3. $\ce{CCl4}$：一种常用的有机溶剂
   4. $\ce{CH3CH2Br}$：汽化时大量吸热，具有麻醉镇痛作用

### 物理性质

1. **状态**：常温下卤代烃除 $\ce{CH3Cl、CH3CH2Cl、CH2=CHCl}$ 等少数是气体外，大多数为液体或固体
2. **溶解度**：**卤代烃不溶于水**，可溶于有机溶剂。某些卤代烃本身是很好的有机溶剂
3. **密度**：高于同碳原子数的烃，**除脂肪烃的一氟代物和一氯代物密度比水小**，其余的密度都比水大。密度随着烃基中碳原子数目的增加而减小。卤代烃的密度随碳原子数目的增加而减小

4. **熔沸点**：

   熔沸点大于同碳个数的烃，随碳原子数增多，沸点依次升高（碳原子数相同时，支链越多沸点越低）

### 溴乙烷

1. 物理性质：
   溴乙烷是无色液体，沸点为 38.4 ℃，密度比水的大，难溶于水，可溶于多种有机溶剂
2. 溴乙烷的结构：
   分子式：$\ce{C2H5Br}$ 结构简式：$\ce{CH3CH2Br}$ 官能团：碳溴键
3. 在溴乙烷分子中，由于 **溴原子的电负性比碳原子的大**，使 $\ce{C-Br}$ 的电子向 $\ce{Br}$ 原子偏移，进而使碳原子带部分正电荷( **$\ce{\delta+}$** )， $\ce{Br}$ 原子带部分负电荷( **$\ce{\delta-}$** )，这样就形成一个极性较强的共价键： **$\ce{C^{\delta+}-Br^{\delta-}}$** ，其键长大而键能较小。因此在化学反应中， **$\ce{C-Br}$ 较易断裂**，使碳原子与带负电荷的基团结合， $\ce{Br}$ 原子被其他原子或原子团所取代，生成负离子离去

### 化学性质（以溴乙烷为例）

#### 水解反应（取代反应）

<img src="./images/5.33.png" style="zoom:33%;"/>

现象：①中溶液 **分层**；②中有机层厚度减小；④中有 **淡黄色沉淀** 生成

解释：溴乙烷与 $\ce{NaOH}$ 溶液共热产生了 $\ce{Br}$

条件： $\ce{NaOH}$ 水溶液、加热

原理：羟基取代溴原子

$\ce{C2H5-Br + H-OH->[\Delta]C2H5-OH + HBr}$

$\ce{NaOH + HBr=NaBr +H2O}$

**总反应：$\ce{C2H5Br + NaOH->[H2O][\Delta] C2H5OH + NaBr}$**

> **用实验的方法证明溴乙烷中含有溴元素**
>
> 取溴乙烷，先加氢氧化钠溶液，加热，冷却后，取上层清液体，**先加过量的稀硝酸酸化（中和溶液中的 $\ce{NaOH}$，$\ce{Ag+ +OH- = AgOH v -> Ag2O v}$）**，再加硝酸银溶液。结果产生浅黄色沉淀（$\ce{AgBr v}$），说明有溴原子
>
> $\ce{AgCl(白)->C2H5Cl\quad AgBr(浅黄)->C2H5Br\quad AgI(黄)->C2H5I}$

#### 消去反应（消除反应）

有机化合物在一定条件下，从一个分子中脱去一个或几个小分子(如 $\ce{H2O}$、$\ce{HX}$ 等)，而生成含不饱和键的化合物的反应

$\ce{CH3CH2Br +NaOH->[乙醇][\Delta]CH2=CH2 ^ +NaBr +H2O}$

1. **反应条件**：
   1. 至少有 **两个碳** 的卤代烃，否则不能发生消去反应

   2. $\beta$ 碳原子上必须有 $\ce{H}$ 原子存在，否则不能发生消去反应

   > 接卤素原子的为 $\alpha-\ce{C}$ 原子
   >
   > <img src="./images/5.35.svg" style="zoom:33%;"/>
   > 3. 直接连接在苯环上的卤原子不能消去

2. 当卤素原子所在碳原子有两个邻位碳原子，且邻位碳原子上均有氢原子时，发主消去反应可能生成不同的产物

   > 如：2-氯丁烷发生消去反应的产物为 1-丁烯和 2-丁烯
   >
   > $\ce{CH3-CH2Cl-CH2-CH3->CH2=CH-CH2-CH3 or CH3-CH=CH-CH3}$

3. 二元卤代烃发生消去反应后可以在有机物中引入碳碳三键或两个碳碳双键

   > $\ce{CH3-CH2-CCl2 + 2NaOH->[醇][\Delta]CH3-C\equiv CH + 2NaCl +2H2O}$

**如果将溴乙烷与强碱（如 $\ce{NaOH}$ 或 $\ce{KOH}$ ）的乙醇溶液共热，溴乙烷可以从分子中脱去 $\ce{HBr}$，生成乙烯**

$\ce{CH3-CH2Br + NaOH->[乙醇][\Delta]CH2=CH2 ^ +NaBr + H2O}$

<img src="./images/5.34.png" style="zoom:33%;"/>

现象：反应产生的气体经水洗后，**使酸性$\ce{KMnO4}$溶液褪色**
解释：生成的气体分子中含有 **碳碳不饱和键**

> 水洗气的目的：除去挥发出来的乙醇

#### 卤代烃的水解反应和消去反应对比

| 反应类型           | 水解（取代）反应                                             | 消去（消除）反应                                                        |
| ------------------ | ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| 反应条件           | $\ce{NaOH}$ 水溶液、加热                                     | $\ce{NaOH}$ 醇溶液、加热                                                |
| 有机反应物结构特点 | 含 $\ce{C-X}$ 键即可                                         | 与 $\ce{-X}$ 相连的 $\ce{C}$ 原子的邻位 $\ce{C}$ 原子上有 $\ce{H}$ 原子 |
| 产物特征           | 在碳原子上引入 $\ce{-OH}$ ，生成含 $\ce{-OH}$ 的有机物（醇） | 消去 $\ce{HX}$ ，引入碳碳双键或三键                                     |

## 酰胺

### 胺

1. **结构**：胺可以看作是氨（ $\ce{NH3}$ ）分子中的氢原子被烃基取代的衍生物。胺的分子结构与氨气相似，都是三角锥形

2. **分类**
   1. 根据氨分子中一个、两个或三个氢原子被烃基取代的情况，将胺分为伯胺（一级胺）、仲胺（二级胺）、叔胺（三级胺）
   2. 根据分子中氮原子所连烃基种类不同，胺可分为脂肪胺（ 如乙胺 $\ce{CH3CH2NH2}$ ）和芳香胺（ 如苯胺 $\ce{C6H5NH2}$ ）

3. **物理性质**
   1. 低级脂肪胺在常温下为气体，如甲胺、二甲胺、三甲胺、乙胺等，其他低级胺为液体。相对分子质量低的胺具有氨的气味，如三甲胺有鱼腥气味
   2. 胺可形成分子间氢键，故沸点比相对分子质量相近的烷烃高，比相应的醇和羧酸低。低级胺能与水形成氢键而易溶于水，随着相对分子质量的增加，溶解度降低
   3. 芳香胺是无色液体或固体，有特殊臭味，有毒，使用时应注意，避免芳香胺接触皮肤或吸入人体内而中毒

4. **化学性质**
   - 氨气是一种碱性气体，可以与酸反应生成盐。胺和氨气结构相似，胺分子中氮原子的未共用电子对，能接受 $\ce{H}$ ，与酸反应生成类似铵盐的物质，故显出碱性

   - 胺可以与大多数酸作用生成盐：$\ce{CH3CH2NH2 + HCl-> CH3CN2NH3Cl}$

   - 胺的碱性比较弱，它的盐与氢氧化钠或氢氧化钾溶液作用时可以得到有机胺：

   $\ce{CH3CH2NH3Cl +NaOH->CH3CH2NH2 +NaCl +H2O}$
   - 氨基在胺类药物的合成中，常利用上述反应将某些难溶于水、易被氧化的胺，转化为可溶于水的铵盐，增强药物的稳定性，便于保存和运输

### 酰胺

1. **结构**

   酰胺可看作是羧酸分子中羧基中的羟基被氨基或烃氨基（ $\ce{-NHR}$ 或 $\ce{-NR2}$ ）取代而成的化合物，也可看作是氨或胺分子中氨氮原子上的氢被酰基取代而成的化合物

   > 如：乙酰胺的结构 <img src="./images/5.40.svg" style="zoom:33%;"/>

2. **分类**

   根据氮原子上取代基的多少，酰胺可分为伯酰胺（$\ce{-CONH2}$）、仲酰胺（$\ce{-CONHR}$）、叔酰胺（$\ce{-CONR2}$）

3. **化学性质**
   - 酰胺在酸或碱存在并加热的条件下可以发生水解反应。在酸性条件下生成对应的羧酸和铵盐，在碱性条件下生成对应的羧酸盐并放出氨气

   $$
   \begin{aligned}
   &\ce{RCONH2 + H2O + HCl ->[\Delta] RCOOH + NH4Cl} \\
   \text{or} \quad &\ce{RCONH2 + H2O + H2SO4 ->[\Delta] RCOOH + (NH4)2SO4} \\
   &\ce{RCONH2 + NaOH ->[\Delta] RCOONa + NH3 ^}
   \end{aligned}
   $$
   - 酰胺可以通过氨气（或胺）与羧酸在加热条件下反应得到，或用羧酸的铵盐加热脱水 得到。例如乙酰胺可以通过以下反应合成
     $$
      \ce{CH3COOH + NH3->[\Delta] CH3CONH2 + H2O}
     $$
   - 胺可以转化成酰胺，酰胺又可以水解变成胺，常利用这种转化关系来保护氨基

   <img src="./images/5.41.svg" style="zoom:33%;"/>

4. **应用**

   酰胺常被用作溶剂和化工原料。如 $\ce{N,N -}$ 二甲基甲酰胺是生产多种化学纤维的良好溶剂，也用作合成农药、医药的原料等

## 油脂

1. **定义**：高级脂肪酸与甘油（丙三醇、<img src="./images/5.27.svg" style="zoom: 25%;"/>）形成的酯

2. **结构**：<img src="./images/5.28.svg" style="zoom:100%;"/>

   其中 $\ce{R、R'、R''}$ 可以表示 **饱和烃基** 或 **不饱和烃基**
   - 简单甘油酯： $\ce{R、R'、R''}$ 相同
   - 混合甘油酯： $\ce{R、R'、R''}$ 不同

   天然油脂大都为 **混甘油酯**，且动、植物体内的油脂大都为多种混甘油酯的 **混合物**，**无固定熔沸点**

   > 注意：油脂不是高分子化合物

3. **分类**：
   1. 油：常温下呈液态，含有较多不饱和脂肪酸成分（含有碳碳双键）的甘油酯，如花生油、芝麻油、大豆油
   2. 脂肪：常温下呈固态，含较多饱和脂肪酸成分的甘油酯，如牛油、羊油

4. **常见高级脂肪酸**：

   饱和脂肪酸：
   - 软脂酸：$\ce{C15H31COOH}$

   - 硬脂酸：$\ce{C17H35COOH}$

   不饱和脂肪酸
   - 油酸：$\ce{C17H33COOH}$

   - 亚油酸：$\ce{C17H31COOH}$

   > 口诀：软 15、硬 17、油酸不饱 17 烯；亚油酸再多一个烯；最后均含一羧基
   >
   > 植物油含有不饱和脂肪酸，动物油含有饱和脂肪酸

### 化学性质

油脂是高级脂肪酸的甘油酯，其化学性质与乙酸乙酯的相似，能够发生水解反应而高级脂肪酸中又有不饱和的，因此许多油脂又兼有烯烃的化学性质，可以发生加成反应

#### 水解反应

1. **酸性水解**：油脂在酸性条件下水解生成高级脂肪酸和甘油

<img src="./images/5.29.svg" />

2. **碱性水解**：油脂在碱性溶液(如 $\ce{KOH}$ 或 $\ce{NaOH}$ 溶液)中水解，生成甘油和高级脂肪酸盐。高级脂肪酸盐常用于生产肥皂，所以油脂在碱性溶液中水解反应又称 **皂化反应**

   <img src="./images/5.30.svg" />

   > 产物甘油与硬脂酸钠称为皂化液
   >
   > $\ce{皂化液->[饱和NaCl(aq)][盐析]析出C17H35COONa(s)->[过滤]...->肥皂}$

#### 油脂的氢化

不饱和程度较高、熔点较低的液态油，通过催化加氢可提高饱和程度，转化为半固态脂肪这个过程称为油脂的氢化，也称油脂的硬化。制得的油脂叫人造脂肪，通常又称为硬化油。硬化油不易被空气氧化变质，便于储存和运输，可以制造肥皂和人造奶油的原料

<img src="./images/5.31.png" style="zoom: 33%;"/>


---

## Original file: 06 生物大分子.md

---
description: "介绍生物大分子包括糖类、蛋白质和核酸，重点讲解糖类的分类、单糖的性质和多糖的结构与功能。"
---

# 06 · 生物大分子

**蛋白质**、**核酸**和**多糖**是3类主要的生物大分子

## 糖类

1. 定义：指多羟基醛或多羟基酮以及能水解生成它们的物质

2. 分类

   多糖 $\ce{->[水解]}$ 低聚糖 $\ce{->[水解]}$ 单糖
   1. 单糖：葡萄糖、果糖、核糖、脱氧核糖等
      1. 按照分子中所含碳原子数的多少，单糖可以分为丙糖、丁糖、戊糖（如核糖、脱氧核糖）和己糖（如葡萄 糖、半乳糖、果糖）等

      2. 按照所含官能团的不同，单糖又可以分为醛糖和酮糖

   2. 低聚糖（也称寡糖）：蔗糖、麦芽糖、乳糖等

   3. 多糖：淀粉、纤维素、甲壳质等

   > 低聚糖和多糖在一定条件下可以水解生成单糖；单糖一般就是多羟基醛或多羟基酮，不能再水解

### 单糖

**葡萄糖与果糖的比较**

|        | 分子式         | 结构简式                   | 官能团           | 类别     | 溶解性                           |
| ------ | -------------- | -------------------------- | ---------------- | -------- | -------------------------------- |
| 葡萄糖 | $\ce{C6H12O6}$ | $\ce{CH2OH(CHOH)4CHO}$     | $\ce{-OH、-CHO}$ | 多羟基醛 | 水中溶解，乙醇中稍溶，乙醚中不溶 |
| 果糖   | $\ce{C6H12O6}$ | $\ce{CH2OH(CHOH)3COCH2OH}$ | $\ce{-OH、-CO-}$ | 多羟基酮 | 在水、乙醇、乙醚中均易溶         |

**葡萄糖的化学性质**

1. 氧化反应

   $\ce{CH2OH(CHOH)4CHO +2[Ag(NH3)2]OH->[\Delta]CH2OH(CHOH)4COONH4 +2Ag v +3NH3 +2H2O}$

   $\ce{CH2OH(CHOH)4CHO +2Cu(OH)2 +NaOH->[\Delta]CH2OH(CHOH)4COONa +Cu2O v +3H2O}$

2. 加成反应

   $\ce{}$ $\ce{CH2OH(CHOH)4CHO +H2->[催化剂][\Delta]CH2OH(CHOH)4CH2OH}$

3. 发酵反应

   $\ce{C6H12O6->[酒化酶]2C2H5OH +2CO2 ^}$

4. 生理反应——人体主要供能反应

   $\ce{C6H12O6(s) +6O2(g)->6CO2(g) +6H2O(l)\qquad\Delta=-2804kJ\cdot mol^{-1}}$

### 二糖

1. 常见二糖
   1. 蔗糖：无色晶体，易溶于水，较难溶于乙醇，甜度仅次于果糖，是重要的甜味剂，非还原糖，无法与 $\ce{Cu(OH)2}$ 反应

   2. 麦芽糖：由两分子葡萄糖脱水形成，主要存在于发芽的谷粒和麦芽中。含有 $\ce{-CHO}$，属于还原糖

2. 水解反应

   $$
   \begin{matrix}
   \ce{&C12H22O11&+ \space H2O->[酶或酸]&C6H12O6& +&C6H12O6&} \\
   &葡萄糖 & &蔗糖 & & 果糖
   \end{matrix}
   $$

   $$
   \begin{matrix}
   \ce{&C12H22O11&+H2O->[酶或酸]&2C6H12O6}\\&麦芽糖&&葡萄糖
   \end{matrix}
   $$

### 多糖

1. 淀粉与纤维素的组成

   |                  | 淀粉                          | 纤维素                        |
   | ---------------- | ----------------------------- | ----------------------------- |
   | 分子式           | $\ce{(C6H10O5)_n}$            | $\ce{(C6H10O5)_n}$            |
   | $n$ 值大小       | 大                            | 更大                          |
   | 结构特点         | 无 $\ce{-CHO}$，有 $\ce{-OH}$ | 无 $\ce{-CHO}$，有 $\ce{-OH}$ |
   | 水解最终产物     | 葡萄糖                        | 葡萄糖                        |
   | 性质差别         | 遇碘变蓝，在人体内可水解      | 在人体内不能水解              |
   | 是否为纯净物     | 否                            | 否                            |
   | 是否为同分异构体 | 否                            | 否                            |

2. 化学性质
   1. 水解反应

      $$
      \begin{matrix}\ce{&(C6H10O5)_n&+nH2O->[酶或酸]&nC6H12O6}\\&淀粉、纤维素&&葡萄糖\end{matrix}
      $$

   2. 淀粉的特征反应：常温下，遇碘变蓝

   3. 两者均不发生银镜反应

3. 用途
   1. 淀粉：食物的重要组成成分，是主要供能物质；还可用于制备葡萄糖、酿醋、酿酒等

      纤维素：可用于纺织工业、造纸工业，制硝酸纤维、醋酸纤维等

> 实验：判断淀粉的水解程度
>
> 1. 实验原理：淀粉在酸作用下发生水解反应最终生成葡萄糖，反应物淀粉遇碘变蓝色，不能发生银镜反应；产物葡萄糖遇碘不变蓝，能发生银镜反应
> 2. 实验步骤：
>
> <img src="./images/6.1.svg" style="zoom:20%;"/>
>
> 3. 实验现象及相关结论
>
>    |     | 现象 A     | 现象 B       | 结论         |
>    | --- | ---------- | ------------ | ------------ |
>    | 1   | 未出现银镜 | 溶液变蓝色   | 淀粉尚未水解 |
>    | 2   | 出现银镜   | 溶液变蓝色   | 淀粉部分水解 |
>    | 3   | 出现银镜   | 溶液不变蓝色 | 淀粉完全水解 |
>
>    > 说明：
>    >
>    > 1. 验证水解产物时，首先要加入 $\ce{NaOH}$ 溶液中和后再进行实验
>    > 2. 要验证混合液中是否还有淀粉应直接取水解液加碘水，而不能在加入 $\ce{NaOH}$ 中和后再加碘水，因碘水与 $\ce{NaOH}$ 溶液反应

## 蛋白质

### 氨基酸

1. $\ce{\alpha}-$ 氨基酸
   1. 结构特点：羧基和氨基连在同一个碳原子上

   2. 物理性质：天然的氨基酸均为无色晶体，熔点较高，在 200~300 ℃ 熔化时分解。除少数外一般都能溶于水，而难溶于乙醇、乙醚等有机溶剂

2. 氨基酸的化学性质
   1. 氨基酸的两性：既能和强酸反应，又能和强碱反应

      $\ce{CH2(NH2)-COOH +NaOH->CH2(NH2)-COONa +H2O}$

      $\ce{CH2(NH2)-COOH +HCl->CH2(NH3Cl)-COOH}$

   2. 成肽反应

   <img src="./images/6.2.svg" style="zoom:40%;"/>

### 蛋白质

1. 蛋白质的组成与结构
   1. 元素：$\ce{C、H、O、N、(S、P)}$

   2. 高分子化合物：蛋白质是由氨基酸通过缩聚反应产生的，蛋白质属于高分子化合物

   3. 所含官能团：肽键（<img src="./images/6.3.svg"/> ），多肽链两端存在氨基和羧基

2. 双性：既能和强酸反应，又能和强碱反应

3. 水解：蛋白质 $\ce{->[酸、碱或酶]}$ 多肽类 $\ce{->[逐步水解]}$ 氨基酸

4. **盐析（物理变化）**
   1. 条件：加人浓的轻金属盐溶液，如 $\ce{(NH4)2SO4、Na2SO4}$ 等

   2. 结果：蛋白质的溶解度降低而从溶液中析出

   3. 特点：发生可逆的物理过程，加水稀释沉淀重新溶解，活性不变

   4. 应用：采用多次盐析和溶解，可以分离提纯蛋白质

5. **变性（化学变化）**
   1. 影响因素：
      1. 物理因素：加热、加压、搅拌、振荡、紫外线照射、超声波等

      2. 化学因素：强酸、强碱、重金属盐、某些有机物（甲醛、酒精、苯甲酸等）

   2. 结果：蛋白质的性质和生理功能发生改变而形成沉淀
   3. 特点：发生不可逆的化学过程

   4. 应用：
      1. 乙醇、碘酒杀菌消毒的原理是使细菌、病毒蛋白质变性死亡

      2. 食物加热烹调使蛋白质变性，利于酶发挥作用使其消化

6. 显色反应：浓硝酸与某些蛋白质发生显色（黄色）反应，可用于蛋白质的检验

7. 灼烧：产生烧焦羽毛的气味，可以用来鉴别蛋白质


---

## Original file: 07 化学品的合理使用.md

---
description: "讨论化学品的合理使用，包括化肥与农药、药物如阿司匹林和青蒿素，以及食品添加剂的种类和作用。"
---

# 07 · 化学品的合理使用(Shirley Amika)

本课针对新方案高考课本编写。

1. 化肥与农药

   有机氯、磷农药、氨基甲酸酯和拟除虫酯等有机合成农药：高效、低毒、低残留。

   <img src="./images/7.1.png"/>

   > 有机氯农药：DDT 转变为 DDE 后毒性降低昆虫表现出抗药性。

2. 药物

   阿司匹林（乙酰水杨酸）

   解热镇痛，以水杨酸为原料：

   <img src="./images/7.2.png"/>

   将阿司匹林和聚甲基丙烯酸（试着写出其结构简式？）连接，得到的缓释阿司匹林可作为抗血栓长效药。

   青蒿素：抗疟疾。对青蒿素进行修饰、改造后得到新药。

3. 食品添加剂（有二十多类功能）
   1. 着色剂、增味剂

      天然色素有：红曲红、β-胡萝卜素、姜黄、叶绿素铜钠盐、焦糖色

      合成色素有：苋菜红、柠檬黄、靛蓝

      味精（谷氨酸钠）是常用的增味剂，最早是从海带中发现并提取的，现在主要通过淀粉发酵生产。

      <img src="https://pic3.zhimg.com/80/v2-c029e03e626992e6aee03e9b2a6e8b2e_720w.webp" />

      > 谷氨酸钠（可以不画出立体结构）

   2. 凝固剂

      葡萄糖酸-内酯（现代制豆腐常用）

   3. 防腐剂、抗氧化剂
      - 苯甲酸及其钠盐、山梨酸及其钾盐是常用的防腐剂。

      - 抗坏血酸（即维生素C）可被氧化为脱氢抗坏血酸，是水果罐头、饮料中常用的抗氧化剂。

      - 叔丁基对苯二酚（TBHQ）是一种抗氧化剂，在市售食用油中普遍加入。

        由于不饱和脂肪酸甘油酯中含有碳碳双键，在空气中放置久了会被氧化，产生过氧化物和醛类等，变质的油脂有一种难闻的“哈喇”味，不能食用。

      - 丁基羟基茴香醚（BHA）在脂肪、乳化脂肪制品中使用。


---

## Original file: 08 合成高分子.md

---
description: "介绍合成高分子的方法，包括加聚反应和缩聚反应，举例说明聚乙烯、酚醛树脂等高分子的合成过程。"
---

# 08 · 合成高分子

## 加聚反应

1. 含义：具有不饱和键的有机化合物通过加聚反应得到高分子化合物的反应称为加聚反应

2. 特点：没有副产物生成

> <img title="" src="./images/4.6.png"  height="130">
>
> 例如：生成聚乙烯：$\ce{nCH2=CH2->[一定条件]}\space[\!\!\!\ce{-CH2-CH2}$ $]\!\!\!-_n$ （聚乙烯，$n$ 为聚合度，$\ce{-CH_2-CH_2 -}$ 是链节）

## 缩聚反应

1. 含义

   由有机化合物分子间脱去小分子获得高分子化合物的反应称为缩合聚合反应，简称缩聚反应

2. 缩聚反应的特点
   1. 缩聚反应生成聚合物的同时，还有小分子副产物（如 $\ce{H2O}$ 等）生成

   2. 缩聚反应的单体通常是具有两个或多个官能团（如 $\ce{-OH、-COOH、-NH2、-X}$ 等）的小分子

   3. 所得聚合物链节的化学组成与单体的化学组成不同

### 甲醛的缩聚反应

酚醛树脂的合成

<img src="./images/5.36.svg" style="zoom: 75%;"/>

<img src="./images/5.37.svg" style="zoom: 25%;"/>

### 羟基酸缩聚

<img src="./images/K-1.3.svg" style="zoom: 30%;"/>

### 醇酸缩聚

<img src="./images/K-1.4.svg" style="zoom: 30%;"/>

### 氨基酸缩聚

<img src="./images/K-1.5.svg" style="zoom: 30%;"/>

<img src="./images/K-1.6.svg" style="zoom: 30%;"/>

> 由 $\ce{n mol}$ 一种单体进行缩聚反应，生成小分子的物质的量应为 $\ce{n-1 mol}$ ；由物质的 $\ce{n mol}$ 的两种单体进行缩聚反小分子的物质的量应为 $\ce{2n-1 mol}$

## 高分子材料

### 塑料

例如：合成树脂，如聚乙烯、聚氯乙烯、酚醛树脂

1. “树脂”的含义是：未加工的处理物

2. **聚乙烯**制成的塑料是**热塑性塑料**，而**酚醛树脂**等只能一次成形，是**热固性塑料**。具有网状结构的高分子受热都不能软化或熔融，也不溶于任何溶剂

3. 不能用含增塑剂的聚氯乙烯薄膜等做食品包装材料

4. 超高相对分子质量（大于 100 万）的聚乙烯可用作防弹头盔和防弹衣的材料

根据制备工艺，可以将聚乙烯分为两种：
| 名称 | 工艺 | 特点 |
|------|------|----------|
| 高压法聚乙烯 | 150~300MPa，200℃左右，使用引发剂 | 碳链较短，分子量较小，密度较低，支链型结构 |
| 低压法聚乙烯| 0.1~2MPa，80℃左右，使用催化剂| 碳链较长，分子量较大，密度较高，线型结构 |

### 橡胶

1. 橡胶是一种具有高弹性的高分子材料。

2. 天然橡胶的成分主要是顺式聚异戊二烯，杜仲胶的成分是反式聚异戊二烯。

合成橡胶主要有：顺丁橡胶、丁苯橡胶、丁腈橡胶、乙丙橡胶、硅橡胶等

### 纤维

**天然纤维**：棉花、羊毛、蚕丝和麻等是大自然赋予人们的天然纤维

**化学纤维**

再生纤维：以木材、秸秆等农副产品为原料，经加工处理可以得到再生纤维

合成纤维：以石油、天然气、煤、农副产品为原料，将其转化为单体，再经过聚合反应得到的是合成纤维

①聚酯纤维：由苯二酸和乙二醇缩合而成，强度大，耐磨，易洗，快干，透气性、吸湿性较差

②聚酯胺纤维：耐磨性和强度较好。
$\ce{nH2N-(CH2)6-NH2 + nHOOC(CH2)4COONH <=>[催化剂,\Delta] HO[OC(CH2)4CONH(CH2)6NH]\_nH + (2n-1)H2O}\qquad $

> 另外注意，高分子化合物由于聚合度不同的高分子混合，是混合物


---

## Original file: 09 有机合成进阶.md

---
description: "讲解有机合成的进阶方法，包括碳骨架构建如加聚、缩聚、羟醛缩合，以及官能团转化和保护基的使用。"
---

# 09 · 有机合成进阶

<img src="./images/9.14.svg"/>

## 碳骨架构建

### 碳链增长

常见的有 **加聚反应、缩聚反应、醛或酮的羟醛缩合反应、炔/醛/酮与 $\ce{HCN}$ 的的加成反应、卤代烃与氰化钠的取代反应、题目所给信息反应** 等

#### 炔、酮、醛与 $\ce{HCN}$ 的加成反应

1. 炔烃与 $\ce{HCN}$ 的加成反应：生成含有氰基（$\ce{-CN}$）的物质，所得产物再经水解生成羧酸

   $$
   \begin{array}{c c c c c}
   \ce{HC#CH} & \ce{->[HCN][催化剂]} & \ce{CH2=CH-CN} & \ce{->[H2O,H+][\Delta]} & \ce{CH2=CHCOOH} \\
   \text{乙炔} & & \text{丙烯腈} & & \text{丙烯酸}
   \end{array}
   $$

   $$
   \ce{\quad\!\! CH3-CO-CH3->[HCN][催化剂](CH3)2C(OH)-CN->[H2O,H+][\Delta](CH3)2C(OH)-COOH}
   $$

2. 醛与 $\ce{HCN}$ 的加成反应：醛中的不饱和键与 $\ce{HCN}$ 发生加成反应生成含有氰基的物质，再经催化加氢还原成胺

   $$
   \ce{CH3CHO->[HCN][催化剂]CH3(OH)-CN ->[H2][催化剂] CH3(OH)-CH2NH2}
   $$

   <img title="" src="./images/9.2.svg"  height="100">

   > 此外，炔烃还可以和醛发生加成反应：$\ce{R-C#CH + R'CHO ->[一定条件] R-C#C-C(R')H-OH}$
   >
   > 如果是乙炔，那么两端都可以与醛基加成

#### 卤代烃与氰化钠的反应

如溴乙烷与氰化钠反应时，分子中的溴原子被氰基取代生成氰化物，该氰化物在酸性条件下水解，可以得到比溴乙烷分子多一个碳原子的丙酸分子

$\ce{CH3CH2Br +NaCN->CH3CH2CN +NaBr\quad CH3CH2CN->[H2O][H+]CH3CH2COOH	}$

#### 羟醛缩合反应 Aldol Condensation Reaction

醛分子中在醛基邻位碳原子上的氢原子 ( $α-\ce{H}$ ) 受羰基吸引电子作用的影响，具有一定的活泼性，分子内含有 $α-\ce{H}$ 的醛在一定条件下可以发生加成反应，生成 $\beta-$ 羟基醛，该产物易失水，得到 $\alpha,\beta-$ 不饱和醛

<img src="./images/5.19.svg" style="zoom: 20%;"/>

> 部分高考信息题会跳过 $\beta-$ 羟基醛 的步骤，直接得到不饱和醛
>
> 乙醛拥有三个 $α-\ce{H}$ ，因此可以发生三次羟醛缩合反应

#### 卤代烃与格氏试剂反应

卤代烃还可以与金属反应，形成金属有机化合物。其中最负盛名的是有机镁化合物，它是由法国化学家格利雅（V. Grignard）于 1901 年发现的

通过卤代烃与镁（用醚作溶剂）作用得到烃基卤化镁（ $\ce{RMgX}$ ，也称为格氏试剂），烃基卤化镁与其他物质（如卤代烃、醛、二氧化碳等）反应可以实现碳链增长，得到烃、醇、羧酸、酮等多种有机化合物

$$
\ce{CH3CH2MgBr} \begin{cases}
\ce{->[ROH 或 H2O] CH3CH3}\\
\ce{->[CH3Br] CH3CH2CH3}\\
\ce{->[① CO2 ② H2O/H+] CH3CH2COOH}\\
\ce{->[① HCHO, ② H2O/H+] CH3CH2CH2OH}\\
\end{cases}
$$

#### 卤代烃与醇钠反应实现不对称醚的合成

在课本中，我们学习了卤代烃与 $\ce{NaOH}$ 水溶液共热的反应，卤原子被羟基取代生成醇，称为卤代烃的 **水解**。而将卤代烃与 **醇钠** 的醇溶液共热，则卤素原子将被烷氧基取代生成醚，称为卤代烃的 **醇解**

$\ce{RONa + R'X ->[无水条件] ROR' + NaX}$

这是制备 **不对称醚** 的一种常用方法（当然也可以合成对称醚），被称为威廉森(Williamson)合成法

如果尝试使用课本内的方法合成不对称醚将会形成两种对称醚副产物。

反应示例：<img title="" src="./images/9.1.svg" width="450">

#### 傅列德尔-克拉夫茨反应 Friedel-Crafts Reaction（烷基化反应）

Friedel-Crafts Reaction 是在芳环上引入烷基和酰基的重要方法，在有机合成上有很大的实用价值

芳烃在无水 $\ce{AlCl3}$ 等 Lewis 酸 的催化下，苯环上的氢被烷基取代的反应：

<img src="./images/9.3.svg" style="zoom: 90%;"/>

$\ce{AlCl3}$ 是烷基化反应中活性最高的催化剂，此外， $\ce{FeCl3、 ZnCl2、 HF、H2SO4}$ 将均可作为催化剂
在烷基化反应中，进攻苯环的条电试剂为烷基碳正离子：

$$
\begin{align}
\ce{&R-Cl + AlCl3-> R+ +AlCl-} \tag1 \\
\ce{&PhH +R+-> H-Ph-R ->[-H+] PhR} \tag2
\end{align}
$$

在催化剂作用下产生碳正离子的化合物，如卤代烃、烯烃、环氧乙烷和醇均可作为烷基化试剂

$\ce{PhH +CH3CH=CH2->[AlCl3]Ph-CH(CH3)2}$

$\ce{PhH +CH3CH2OH->[AlCl3]Ph-CH2CH3}$

$\ce{PhH +}$ <img src="./images/9.4.svg"/> $\ce{->[(1)AlCl3][(2)H2O]}\ce{Ph-CH2CH2OH}$

> 由于烷基化反应中间体是碳正离子，所以如果卤代烃的碳原子数目大于等于 3，常会发生重排反应，生成不同烷基取代的芳香混合物
>
> $$
> \begin{array}{c c c c c}
> \ce{PhH + CH3CH2CH2Cl} & \ce{->[AlCl3]} & \ce{Ph-CH2CH2CH3} & + & \ce{Ph-CH(CH3)2} \\
> & & \text{正丙苯(30\%)} & & \text{异丙苯(70\%)}
> \end{array}
> $$
>
> 且由于生成的烷基苯比苯活泼，易发生多元取代生成二烷基苯和多烷基苯，因此，常加入过量芳烃及调节温度来控制产物
>
> 不过一般高考题里出现的反应物是本溴乙烷，不发生重排。高考中会给出相关信息

### 碳链缩短

烯烃、炔烃、芳香烃的氧化反应；羧酸或羧酸盐的脱羧反应；烷烃的裂化反应；题给信息反应等

#### 高锰酸钾氧化

1. 烯烃被酸性高锰酸钾溶液氧化：不同的结构可以得到不同的氧化产物

   $\ce{-CH2=->HO-CO-OH\quad RCH=->R-COOH\quad CR1R2=->CR1R2=O}$

   > 口诀：有氢成酸，无氢成酮，边碳成气
   >
   > $\ce{CH3-CH=CH2->HO-CO-OH->CO2 ^ +H2O}$

2. 炔烃被酸性高锰酸钾溶液氧化：对于炔烃，大多数情况下，都发生碳碳三键的断裂，生成 **两个羧酸**

   $$
   \ce{RC#CH->[KMnO4][H+] RCOOH +CO2}\\
   \ce{CH3CH2CH2C#CCH2CH3->[KMnO4][H+] CH3CH2CH2COOH +CH3CH2COOH}
   $$

3. 芳香烃的侧链被 $\ce{KMnO4、K2Cr2O7}$ 等强氧化剂氧化时，大多数情况是侧链被氧化成羧

   **注意：烷基上与苯环直接相连的碳原子上必须有氢原子，才能被酸性高锰酸钾氧化**

#### 酯的水解

酸性条件：$\ce{RCOOR' +H2O <=>[稀H2SO4][\Delta] RCOOH +R'OH}\qquad$

碱性条件：$\ce{RCOOR' +NaOH ->[\Delta] RCOONa +R'OH}$

### 成环反应

#### 狄尔斯-阿尔德反应 Diels-Alder Reaction

狄尔斯-阿尔德反应共轭二烯烃与含碳碳双键（或三键）的化合物在一定条件下反应，得到环加成产物，构建了环状碳骨架，该反应用于构建六元碳环骨架

如：<img title="" src="./images/9.5.svg" width="300">

> 理解：共轭二烯烃（如 1，3-丁二烯）的两根双键各自打开一半，与含亲双烯体（在这里是丙烯酸）的碳碳双键发生加成反应，两个“半截键”与原来的单键共同形成了新的双键，得到了环加成产物，构建了环状碳骨架

#### 酯化成环

如：二元酸与二元醇的酯化反应、羟基酸的酯化反应

#### 二元醇成环

如：$\ce{HOCH2CH2OH->[浓硫酸][\Delta]}$ <img src="./images/9.4.svg"/> $\ce{+H2O}$

#### 二元羧酸成环

如：$\ce{HOOCCH2CH2COOH->[浓硫酸][\Delta]}$ <img src="./images/9.6.svg"/> $\ce{+H2O}$

#### 氨基酸成环

如：$\ce{H2NCH2CH2COOH->[浓硫酸][\Delta]}$ <img src="./images/9.7.svg"/> $\ce{+H2O}$

## 聚合物的生成

### 烯烃共聚

$\ce{nCH2=CH2 +nCH2=CH-CH3->[一定条件]}\space[\!\!\!\ce{-CH2-CH2-CH(CH3)-CH2}$ $]\!\!\!-_n$

### 酚醛树脂

 <img src="./images/5.37.svg" style="zoom: 25%;"/>

## 官能团的转化

### 引入官能团

#### 引入碳碳双键

| 反应             | 示例                                                      |
| ---------------- | --------------------------------------------------------- |
| 卤代烃的消去反应 | $\ce{CH3CH2Br +NaOH->[乙醇][\Delta]CH2=CH2 ^ +NaBr +H2O}$ |
| 醇的消去反应     | $\ce{CH3CH2OH->[浓硫酸][170°C]CH2=CH2 ^ +H2O}$            |

#### 引入碳卤键

| 反应                            | 示例                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 烃、酚的取代                    | ①甲烷在光照条件下的氯代 <br/> $\ce{CH4 + Cl2 ->[光] CH3Cl + HCl}$<br>②苯与溴苯在 $\ce{Fe}$ 粉 或 $\ce{FeBr3}$ 催化下生成溴苯 <br/> <img src="./images/4.13.svg" style="zoom:80%;" > <br/> ③甲苯的卤代 <br/> <img src="./images/4.19.svg" style="zoom: 20%;" /> <br/> ④苯酚与溴水反应生成三溴苯酚 <br/> <img src="/04 有机化学基础/images/5.13.svg" style="zoom: 60%;"/> |
| 不饱和烃与 $\ce{HX、X2}$ 的加成 | $\ce{CH3CH=CH2 +HBr->CH3-CHBr-CH3}$（马氏规则）<br/> $\ce{CH3CH=CH2 +HBr->[过氧化物]CH3-CH2-CH2Br}$（反马氏规则）                                                                                                                                                                                                                                                       |
| 醇与氢卤酸（$\ce{HX}$）的取代   | $\ce{CH3CH2OH +HBr->[\Delta]CH3CH2Br +H2O}$                                                                                                                                                                                                                                                                                                                             |

#### 引入羟基

| 反应                       | 示例                                                                                                                                                                    |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 烯烃与水的加成             | $\ce{H2C=CH2 +H2O->[催化剂][加热、加压]CH3CH2OH}$                                                                                                                       |
| 醛、酮与氢气的加成         | $\ce{CH3-CHO +H2->[催化剂][\Delta]CH3CH2OH}(伯醇)$ <br/> $\ce{CH3-CO-CH3 +H2->[催化剂][\Delta](CH3)2-CH-OH}(仲醇)$                                                      |
| 卤代烃在碱性条件下水解     | $\ce{C2H5-Br +NaOH->[H2O][\Delta]C2H5-OH +NaBr}$                                                                                                                        |
| 酯的水解                   | $\ce{CH3COOC2H5 +H2O<=>[浓硫酸][\Delta]CH3COOH +C2H5OH}$                                                                                                                |
| 通过硼氢化钠引入羟基或醛基 | 硼氢化钠具有较强的还原选择性，它可以将羰基还原为羟基，将羧基还原为醛基，但是与碳碳双键、碳碳三键都不发生反应<br>例如：$\ce{CH2=CH-CH2-CHO->[NaBH_{4}]CH2=CH-CH2-CH2OH}$ |

#### 引入醛基或羰基（引入碳氧双键）

| 反应                     | 示例                                                          |
| ------------------------ | ------------------------------------------------------------- |
| 醇的催化氧化             | $\ce{2CH3CH2OH + O2 ->[Cu/Ag][△]2CH3CHO + 2H2O}$              |
| 含碳碳三键的物质与水加成 | $\ce{HC#CH +H2O->[催化剂][\Delta]H2C=CH-OH->[异构化]CH3-CHO}$ |
| 碳碳双键氧化             | <img src="/04 有机化学基础/images/9.8.svg">                   |

#### 引入羧基

| 反应                                                 | 示例                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 醇与强氧化剂反应                                     | $\ce{C2H5OH}$ 与与酸性 $\ce{KMnO4}$ 溶液或酸性 $\ce{K2Cr2O7}$ 溶液反应生成 $\ce{CH3COOH}$                                                                                                                                                                                                   |
| 醛的氧化                                             | $\ce{CH3-CHO +O2->[催化剂][\Delta]2CH3COOH}$<br>银镜反应：$\ce{CH3CHO + 2[Ag(NH3)2]OH ->[\Delta]H2O + 2Ag v + 3NH3 + CH3COONH4}$<br>与新制氢氧化铜反应：<br> $\ce{CH3CHO + 2Cu(OH)2 + NaOH->[\Delta] CH3COONa + Cu_2O v +3H2O}$<br>$\ce{CH3COONH4->[H+]CH3COOH\quad CH3COONa->[H+]CH3COOH}$ |
| 酯、酰胺键的水解                                     | <img src="/04 有机化学基础/images/9.9.svg">                                                                                                                                                                                                                                                 |
| 某些苯环侧链上的烷基与<br>酸性高锰酸钾溶液的氧化反应 | <img src="/04 有机化学基础/images/9.10.svg">                                                                                                                                                                                                                                                |
| 碳碳双键的氧化                                       | $\ce{R-CH=CH-R->[KMnO4(H+)]RCOOH}$                                                                                                                                                                                                                                                          |

#### 引入酯基

| 反应       | 示例                                                     |
| ---------- | -------------------------------------------------------- |
| 酯化反应   | $\ce{CH3COOH +C2H5OH<=>[浓硫酸][\Delta]CH3COOC2H5 +H2O}$ |
| 酰基化反应 | <img src="/04 有机化学基础/images/9.11.svg">             |

### 消除官能团

1. 通过加成反应消除不饱和键

2. 通过消去、氧化、酯化反应消除羟基
3. 通过加成、氧化反应消除醛基
4. 通过水解反应消去酯基、酰胺基、碳卤键

### 改变官能团

#### 改变官能团的种类

#### <img src="./images/9.12.png" style="zoom:50%;"/>

#### 改变官能团的数目

如：$\ce{CH3CH2OH->[消去][-H2O]CH2=CH2->[加成][+Cl2]Cl-CH2-CH2-Cl->[水解]HO-CH2-CH2-OH}$

#### 改变目标官能团的物质

通过不对称烯烃与卤化氢的加成改变官能团的位置（运用马氏规则）

如：$\ce{CH3CH2CH2Cl->[消去][-HCl]CH3CH=CH2->[加成][+HCl]CH3-CH(Cl)-CH3}$

## 官能团的保护与恢复

含有多个官能团的有机化合物在进行反应时，非目标官能团也可能受到影响，此时需要将受影响的官能团保护起来，先将其转化为不受该反应影响的其他官能团，反应后再将受影响的官能团复原。此类题目在命题时往往会给出已知信息

1. 羟基的保护

   $\ce{R-OH->[引入保护基]R-O-R'}\stackrel{合成反应}{\longrightarrow\cdots\longrightarrow}\ce{R''-O-R'->[脱除保护基]R''-OH}$

   > 合成反应会影响羟基，无法直接转化
   >
   > 如果体系受强碱影响，就用成醚反应保护，如果要受氧化，就要用酯化反应保护

2. 碳碳双键的保护

   碳碳双键易被氧化，在氧化其他基团前，可通过与卤素单质、卤化氢等加成的方法先将碳碳双键保护起来，待氧化其他基团后，再通过消去反应（$\ce{NaOH}$ 醇溶液，加热）重新转化为碳碳双键

3. 羧基

   羧基遇到高温容易脱羧，


---

## Original file: index.md

---
description: 本章覆盖有机化学基础知识与方法，包括有机物结构、分类命名、烃及其衍生物、生物大分子和有机推断等高频考点。
---

# 04 有机化学基础

<CCChapterOverview />


---

## Original file: 考点 有机反应类型梳理.md

---
description: "梳理有机化合物的反应类型，包括取代、加成、加聚、缩聚、水解等，列出各类化合物的常见反应。"
---

# 考点 · 有机反应类型梳理

|        | 取代 | 加成   | 加聚 | 缩聚 | 水解 | 消去 | 与活泼金属 | 酸性 | 硝化 | 磺化 | 银镜         | 强氧化       |
| ------ | ---- | ------ | ---- | ---- | ---- | ---- | ---------- | ---- | ---- | ---- | ------------ | ------------ |
| 烷     | $√$  |        |      |      |      |      |            |      |      |      |              |              |
| 稀、炔 | $√$  | $√$    | $√$  |      |      |      |            |      |      |      |              | $√$          |
| 苯     | $√$  | $√$    |      |      |      |      |            |      | $√$  | $√$  |              |              |
| 甲苯   | $√$  | $√$    |      |      |      |      |            |      | $√$  | $√$  |              | $√$          |
| 苯酚   | $√$  | $√$    |      |      |      |      | $√$        | 弱   | $√$  | $√$  |              | $√$          |
| 卤代烃 | $√$  |        |      |      | $√$  | $√$  |            |      |      |      |              |              |
| 醇     | $√$  |        |      | 二元 |      | $√$  | $√$        |      |      |      |              | $√$          |
| 羧酸   | $√$  |        |      | 二元 |      |      | $√$        | $√$  |      |      | $\ce{HCOOH}$ | $\ce{HCOOH}$ |
| 羟基酸 |      |        |      | $√$  |      | $√$  | $√$        | $√$  |      |      |              | $√$          |
| 醛     | $√$  | $√$    | $√$  |      |      |      |            |      |      |      | $√$          | $√$          |
| 酯     |      |        |      |      | $√$  |      |            |      |      |      | $\ce{HCOOR}$ | $\ce{HCOOR}$ |
| 油脂   |      | 植物油 |      |      | $√$  |      |            |      |      |      |              |              |
| 单糖   |      | $√$    |      | $√$  |      |      |            |      |      |      | $√$          | $√$          |
| 二糖   |      |        |      | $√$  | $√$  |      |            |      |      |      | 还原糖       | $√$          |
| 多糖   |      |        |      |      | $√$  |      |            |      |      |      | 还原糖       | $√$          |
| 蛋白质 |      |        |      |      | $√$  |      |            |      |      |      |              |              |

## 取代反应

有机物分子里的某些原子或原子团被其他原子或原子团所替代的反应

$\ce{A1-B1 +A2-B2->A1-B2 +A2-B1}$

### 卤代

1. 在光照条件下，烷烃都能与卤素单质发生取代反应

   $\ce{CH4 +Cl2->[光]CH3Cl + HCl}\qquad \ce{CH3Cl +Cl2->[光]CH2Cl2 + HCl}$

   $\ce{CH2Cl +Cl2->[光]CHCl3 + HCl}\qquad \ce{CHCl3 +Cl2->[光]CCl4 + HCl}$

   > 标况下，只有 $\ce{CH3Cl}$ 是气态，其余均为液态

2. 苯和溴在 $\ce{FeBr3}$ 催化下可以发生反应，生成溴苯

   <img src="./images/4.13.svg"  style="zoom:70%;"/>

   使用纯净的液溴，不得使用溴水（发生萃取，使溴水因萃取而褪色）

3. **在光照条件下**，甲苯与氯气发生取代反应时，氯原子取代甲基上的氢原子。反应后可能的有机产物是甲基上的氢原子分别被 $1$ 个、$2$ 个或 $3$ 个氯原子取代所生成的氯甲基苯

   **在 $\ce{FeBr3}$ 的催化下**，甲苯与氯发生取代反应生成的一氯代甲苯主要有两种：邻氯甲苯和对氯甲苯

   <img src="./images/4.19.svg" style="zoom: 20%;"/>

4. 苯酚稀溶液的试管里逐滴加入过量饱和的溴水，产生白色沉淀

<img src="./images/5.13.svg" alt="" style="zoom: 60%;"/>

5. 醇与浓的氢卤酸（$\ce{HCl、HBr、HI}$）

   $\ce{C2H5OH +HBr->[\Delta]C2H5Br + H2O}$

6. $\alpha-\ce{H}$ 被取代的反应

   与官能团直接相连接的碳被称为 $\alpha-\ce{C}$ ，其连接的氢离子易被取代。

   $\ce{CH3-CH=CH2 + Cl2->[\Delta]Cl-CH2-CH=CH2 +HCl}$

### 硝化

1. 在浓硫酸作用下，苯在 $50-60\ce{°\!C}$ （水浴加热）与硝酸发生硝化反应，生成硝基苯

<img src="./images/4.14.jpg" alt="img" style="zoom:50%;"/>

2. 甲苯与浓硝酸和浓硫酸的混合物在加热条件下可以发生取代反应，生成一硝基取代物、二硝基取代物和三硝基取代物，硝基取代的位置均以甲基的邻、对位为主

<img src="./images/4.18.svg" alt="image-20230429111425499" style="zoom: 18%;"/>

### 磺化

苯与浓硫酸在 $70-80\ce{°\!C}$ 可以发生磺化反应，生成苯磺酸苯与浓硫酸在 $70-80\ce{°\!C}$ 可以发生磺化反应，生成苯磺酸

<img src="./images/4.15.png" style="zoom:25%;"/>

### 醇分子间脱水成醚

如果把乙醇与浓硫酸的混合物的温度控制在 $140\ce{°C}$ 左右，每两个乙醇分子间会脱去一个水分子而生成乙醚

<img src="./images/5.2.svg" style="zoom:25%;"/>

### 酯化

<img src="./images/5.1.svg" style="zoom:25%;"/>

> 口诀：酸脱羟基醇脱氢

### 合成酰胺

<img src="./images/5.26.svg" style="zoom:25%;"/>

### 水解

1. 酯类

   在酸或碱催化的条件下，酯可以发生水解反应生成相应的酸和醇。酯的水解反应是酯化反应的逆反应。在碱性条件下，酯水解产生的羧酸可以与碱发生反应，使羧酸浓度减小，即减小了生成物的浓度，化学平衡正向移动，使酯的水解程度加大

   酸性条件：$\ce{RCOOR' +H2O <=>[稀H2SO4][\Delta] RCOOH +R'OH}\qquad$

   碱性条件：$\ce{RCOOR' +NaOH ->[\Delta] RCOONa +R'OH}$

2. 油脂
   1. **酸性水解**：油脂在酸性条件下水解生成高级脂肪酸和甘油

   <img src="./images/5.29.svg" />
   2. **碱性水解**：油脂在碱性溶液(如 $\ce{KOH}$ 或 $\ce{NaOH}$ 溶液)中水解，生成甘油和高级脂肪酸盐。高级脂肪酸盐常用于生产肥皂，所以油脂在碱性溶液中水解反应又称 **皂化反应**

   <img src="./images/5.30.svg" />

3. 卤代烃

   $\ce{C2H5-Br + H-OH->[\Delta]C2H5-OH + HBr}$

   $\ce{NaOH + HBr=NaBr +H2O}$

   总反应：$\ce{C2H5Br + NaOH->[H2O][\Delta]C2H5OH + NaBr}$

4. 酰胺

   酰胺在酸或碱存在并加热的条件下可以发生水解反应。如果水解时加入碱，生成的酸就会变成盐，同时有氨气逸出。

   酸性水解：$\ce{R-CONH2 +H-OH +HCl->[\Delta]R-COOH +NH4Cl}$

   碱性水解：$\ce{R-CONH2 +NaOH->[\Delta]R-COONa +NH3 ^}$

## 加成反应

有机物分子中的 **不饱和键** 两端的两个原子与其他原子或原子团直接结合，生成新的化合物的反应叫做加成反应

### 烯烃的加成

1. $\ce{CH3-CH=CH2 +H2 \xrightarrow[\Delta]{催化剂} CH3-CH2-CH3}$

2. $\ce{CH2=CH2 +HCl \xrightarrow[\Delta]{催化剂} CH3-CH2-Cl}$

3. $\ce{CH2=CH2 +H2O ->[\Delta][催化剂] CH3-CH2OH}$

4. $\ce{CH2=CH2 +Br2->CH2Br-CH2Br}$

   > 1,2-二溴乙烷是无色，且溶于四氯化碳，乙烯通到溴的四氯化碳，且溴的四氯化碳褪色且溶液不会分层，证明 1,2-二溴乙烷是无色且溶于四氯化碳的

5. $\ce{CH3-CH=CH2 +HCl->CH3-CHCl-CH3(主要) \& CH3CH2CH2Cl}$

   > 当不对称烯烃与含氢的化合物（ $\ce{HBr、H_{2}}$ 等）加成时，氢原子主要加到连有较多氢原子的碳原子上（马氏规则），在过氧化物存在的情况下, 氢原子主要加在连有较少氢原子的碳原子上（反马氏规则）

6. $1,2-$ 加成（低温）：$\ce{CH2=CH-CH=CH2 +Br2 ->}$ <img src="./images/4.7.svg"/>

   $1,4-$ 加成（高温）：$\ce{CH2=CH-CH=CH2 +Br2 ->}$ <img src="./images/4.8.svg"/>

### 炔烃的加成

1. $\ce{CH#CH + H2 ->[\Delta][催化剂] CH2=CH2}\quad\ce{CH#CH + 2H2 ->[\Delta][催化剂] CH3CH3}$

2. $\ce{CH#CH + HCl ->[\Delta][催化剂] CH2=CHCl}$

3. $\ce{CH#CH + H2O ->[\Delta][催化剂] CH3-CHO}$

   > 乙炔与水加成后的产物乙烯醇不稳定（ $CH_2=CH-OH$ ），很快转化为乙醛（醇的催化氧化）

4. $\ce{HC#CH->[HCN][催化剂]CH2=CH-CN(丙烯晴)->[H2O、H+][\Delta]CH2=CH-COOH}(丙烯酸)$

   > 用于增加碳链长度

### 苯的加成

<img src="./images/4.16.webp" alt="img" style="zoom:50%;"/>

<img src="./images/4.21.png"  style="zoom: 25%;"/>

### 醛与酮的加成

1. $\ce{CH3-CHO +H2->[催化剂][\Delta]CH3CH2OH}$

   > 乙醛与 $\ce{H2}$ 加成变成乙醇，既是加成，也是还原反应

2. <img src="./images/K-1.1.svg"  style="zoom: 35%;"/>
3. $\ce{CH3-CO-CH3 +H2->[催化剂][\Delta]CH3-CHOH-CH3}$

### 油脂的氢化或硬化

<img src="./images/5.31.png" style="zoom: 33%;"/>

## 缩聚反应

1. 含义
   由一种或多种有机化合物分子相互结合成高分子化合物，同时有小分子生成的反应称为缩合聚合反应，简称缩聚反应
2. 缩聚反应的特点
   1. 缩聚反应生成聚合物的同时，还有小分子副产物（如 $\ce{H2O}$ 等）生成
   2. 缩聚反应的单体通常是具有两个或多个官能团（如 $\ce{-OH、-COOH、-NH2、-X}$ 等）的小分子
   3. 所得聚合物链节的化学组成与单体的化学组成不同

### 甲醛的缩聚反应

酚醛树脂的合成

<img src="./images/5.36.svg" style="zoom: 75%;"/>

<img src="./images/5.37.svg" style="zoom: 25%;"/>

### 羟基酸缩聚

<img src="./images/K-1.3.svg" style="zoom: 30%;"/>

### 醇酸缩聚

<img src="./images/K-1.4.svg" style="zoom: 30%;"/>

### 氨基酸缩聚

<img src="./images/K-1.5.svg" style="zoom: 30%;"/>

<img src="./images/K-1.6.svg" style="zoom: 30%;"/>

> 由 $\ce{n mol}$ 一种单体进行缩聚反应，生成小分子的物质的量应为 $\ce{n-1 mol}$ ；由物质的 $\ce{n mol}$ 的两种单体进行缩聚反小分子的物质的量应为 $\ce{2n-1 mol}$


---

## Original file: 考点 有机推断.md

---
description: "讲解有机化合物的推断方法，根据反应条件、特征现象如褪色反应确定官能团和化合物类型。"
---

# 考点 · 有机推断

## 根据 反应条件 确定官能团

1. 「$\ce{NaOH}$ **水** 溶液、加热」为 $\ce{-X}$ 、酯基、酰胺基的水解反应
2. 「$\ce{NaOH}$ **醇** 溶液、加热」为 $\ce{-X}$ 的消去反应
3. 「浓 $\ce{HNO3}$、浓 $\ce{H2SO4}$、加热」为苯环上的硝化反应
4. 「浓 $\ce{H2SO4}$、加热」为 $\ce{R-OH}$ 的消去反应或酯化反应
5. 「稀 $\ce{H2SO4}$、加热」为酯（ $\ce{R-COO-R'}$ ）的水解反应
6. 「$\ce{Cl2/Fe}$ 或 $\ce{FeCl3、Br/Fe}$ 或 $\ce{FeBr3}$」 为苯环上的取代反应
7. 「$\ce{Cl2/}$ 光照」优先想到烷烃或烷基（如 $\ce{-CH3}$ ）的氯代、苯的同系物（如甲苯）侧链烷基上的氯代等
8. 「$\ce{O2/Cu、△}$」为醇羟基的催化氧化或醛基的催化氧化
9. 「$\ce{Ag(NH3)2OH/△}$」或「新制的 $\ce{Cu(OH)2/△}$」为醛基的氧化反应
10. 「$\ce{H2/Ni}$」：碳碳双键、碳碳三键、醛基、羰基、苯环与氢气的加成反应

## 根据 实际或特征现象 确定官能团

### 使 $\ce{KMnO4(H+)}$ 褪色的有机化合物

褪色原理一般为发生了氧化反应

1. 分子中含有 **碳碳双键**、**碳碳三键** 的不饱和有机化合物
2. 苯的同系物（**与苯环直接相连的碳上有氢原子**）
3. 与醛类等有 **醛基** 的有机物（如醛、甲酸、葡萄糖、麦芽糖等）发生氧化还原反应
4. 与 **羟基直接相连的碳原子上有氢原子** 的醇类物质，如甲醇、乙醇等
5. **酚类物质** （由于其氧化产物也可能有颜色，所以其褪色不一定明显）

> 与具有还原性的无机还原剂（如 $\ce{H2S、SO2、KI、FeSO4、HCl}$ 等）发生反应，使高锰酸钾溶液褪色

### 使溴水褪色的有机化合物

1. 分子中含有 **碳碳双键**、**碳碳三键** 的不饱和有机化合物
2. 含有 **醛基** 的物质，如醛类、糖类
3. **酚羟基所连碳原子的邻、对位上有氢原子** 的酚类物质
4. 萃取
   - 密度大于 1 的溶剂（水在上层）：四氯化碳、氯仿、溴苯、二硫化碳等
   - 密度小于 1 的溶剂（水在下层）：液态的饱和烃、直馏汽油、苯及其同系物、液态环烷烃、液态饱和酯

> 使 **溴水褪色等同于使溴的四氯化碳溶液褪色**，但 **醛基** 不能使溴的四氯化碳溶液褪色
>
> 因为 由 $\ce{CH3CHO +Br2 +H2O=CH3COOH +2HBr}$ ，醛基只有在水存在时，才得以被氧化成羧基

> - 与碱性溶液（如 $\ce{NaOH、Na2CO3}$ 溶液等）反应，使溴水褪色
> - 与较强的无机还原剂（如 $\ce{H2S、SO2、KI、FeSO4}$ 等）发生反应，使溴水褪色
> - 其它：石油产品（裂化气、裂解气、裂化石油等），天然橡胶等

### 其他

1. 与 $\ce{H2}$ 发生加成反应：碳碳双键、碳碳三键、醛基、酮羰基、苯
2. 遇 $\ce{FeCl3}$ 溶液发生显色反应，或加入饱和溴水出现白色沉淀：$\ce{-OH(酚)}$
3. 加入新制的 $\ce{Cu(OH)2}$ ，加热有砖红色沉淀生成或加入银氨溶液，加热有银镜生成：$\ce{-CHO、HCOO-}$（甲酸酯基）
4. 既能发生银镜反应，又能发生水解反应：<img src="./images/K-2.9.svg" style="zoom:15%;" />、<img src="./images/K-2.10.svg" style="zoom:15%;"/>
5. 加入 $\ce{NaOH}$ 溶液并加热放出 $\ce{NH3}$ ：<img src="./images/K-2.1.svg"/>
6. 遇 $\ce{I2}$ 变蓝：淀粉
7. 遇浓硝酸变黄：含有苯环结构的蛋白质
8. 加入茚三酮溶液并加热，溶液显紫蓝色：蛋白质、$α-$ 氨基酸

## 根据 有机反应中的定量关系 推断 官能团的数目

1. 烃和卤素单质的取代：取代 $\ce{1mol}$ 氢原子，消耗 $\ce{1mol}$ 卤素单质（ $\ce{X2}$ ）

2. 碳碳双键的加成：与 $\ce{H2、Br2、HCl、H2O}$ 等加成时按物质的量之比为 $1:1$ 反应

3. 含 $\ce{-OH(醇、酚)}$ 的有机物与 $\ce{Na}$ 反应时： $\ce{2mol}$ $\ce{-OH}$ 生成 $\ce{1mol}$ $\ce{H2}$

4. $\ce{1 mol-COOH、-OH(醇、酚)}$ 与 $\ce{Na2CO3}$ 溶液产生 $\ce{0.5mol H2}$

5. $\ce{1 mol-COOH、-OH(酚)}$ 与 $\ce{Na2CO3}$ 溶液产生 $\ce{0.5mol CO2}$

6. $\ce{1 mol-COOH、-OH(酚)}$ 与 $\ce{NaHCO3}$ 溶液产生 $\ce{1mol CO2}$

7. 醛基（ $\ce{-CHO}$ ）的定量关系
   1. $\ce{1mol}$ $\ce{-CHO}$ 与 $\ce{2mol}$ $\ce{[Ag(NH3)2]OH}$ 反应，生成 $\ce{2mol}$ $\ce{Ag}$
   2. $\ce{1mol}$ $\ce{-CHO}$ 与 $\ce{2mol}$ $\ce{Cu(OH)2}$ 反应，生成 $\ce{1mol}$ $\ce{Cu2O}$
   3. $\ce{1mol}$ 甲醛含 $\ce{2mol}$ $\ce{-CHO}$ ，其余定量关系和上述相同

8. 有机物与 $\ce{Cu(OH)2}$ 的定量关系
   - 水解：$\ce{1mol}$ $\ce{-CHO}$ $\ce{->}$ $\ce{2mol}$ $\ce{Cu(OH)2}$
   - 中和：$\ce{1mol}$ $\ce{-COOH}$ $\ce{->}$ $\ce{1mol}$ $\ce{Cu(OH)2}$

9. 有机物与 $\ce{NaOH}$ 的定量关系
   - 中和：
   1. $\ce{1mol}$ $\ce{-COOH->}$ $\ce{1mol}$ $\ce{NaOH}$

   2. $\ce{1mol}$ $\ce{-OH(酚)->}$ $\ce{1mol}$ $\ce{NaOH}$
   - 水解：
     1. $\ce{1mol}$ <img src="./images/5.38.svg" /> $\ce{→1mol}$ $\ce{NaOH}$（酯基水解）
     2. $\ce{1mol}$ <img src="./images/K-2.2.svg" /> $\ce{→1mol}$ $\ce{NaOH}$（酰胺基水解）
     3. $\ce{1mol}$ <img src="./images/5.32.svg" /> $\ce{→1mol}$ $\ce{NaOH}$（碳卤键水解）

   > **注意酚酯等有多个符合条件的物质，既有水解又有中和**，如：
   >
   > - $\ce{1mol}$ <img src="./images/K-2.3.svg" style="zoom:80%;"/> 最多与 $\ce{2mol}$ $\ce{NaOH}$ 反应
   >
   >   （ $\ce{1mol}$ 酯基水解用去 $\ce{1mol}$ $\ce{NaOH}$ ，水解后生成 $\ce{1mol}$ 的 $\ce{-OH(酚)}$ 被中和再消耗 $\ce{1mol}$ $\ce{NaOH}$）
   >
   > - 若卤素原子取代在苯环上，碳卤键水解后能还能进行酚的中和，消耗 $\ce{2mol}$ $\ce{NaOH}$ 反应
   >
   >   $\ce{Ph-Br +2NaOH->Ph-ONa +NaBr +H2O}$

10. 苯酚与浓溴水：$\ce{1mol}$ <img src="./images/K-2.4.svg" style="zoom:80%;"/> 反应，酚羟基的邻位与对位上的 $\ce{-H}$ 被 $\ce{-Br}$ 取代；若是含酚羟基的物质，其邻位或对位若被 $\ce{H}$ 以外的原子占据了，则无法发生取代

    > 如：$\ce{1mol}$ <img src="./images/K-2.5.svg" style="zoom:100%;"/> 最多可以和 $\ce{4mol}$ $\ce{Br2}$ 发生取代反应

11. 物质转化过程中相对分子质量的变化（ $M$ 代表第一种有机物的相对分子质量）
    1. $\begin{aligned}
        \ce{RCH2OH &-> RCHO &-> RCOOH} \\
        M &\rightarrow M-2 &\rightarrow M+14
        \end{aligned}$（醇、醛、酸的连续氧化）
    2. $\begin{aligned}
        \ce{RCH2OH &->[CH3COOH][浓 H2SO4,\Delta] CH3COOCH2R} \\
        M &\rightarrow M+42
        \end{aligned}$（乙酸的酯化反应）
    3. $\begin{aligned}
        \ce{RCHOOH &->[CH3CH2OH][浓 H2SO4,\Delta] RCOOCH2CH3} \\
        M &\rightarrow M+28
        \end{aligned}$（乙醇的酯化反应）

## 根据 特征产物 推断 碳骨架结构和官能团位置

1. 若醇能被氧化为醛或羧酸：含 $\ce{-CH2OH}$ 结构
2. 若醇能被氧化为酮：含 <img src="./images/K-2.6.svg"/> 结构
3. 若醇不能被催化氧化：含 <img src="./images/K-2.7.svg"/> 结构
4. 由消去反应的产物可确定 $\ce{-OH}$ 或 <img src="./images/5.32.svg"/> 的大致位置
5. 由取代产物的种类可确定碳骨架结构
6. 由加氢或加溴后的碳骨架结构可确定 <img src="./images/3.8.svg"/> 或 $\ce{-C#C-}$ 的位置
7. 由有机化合物发生酯化反应能生成环酯或高聚酯，可确定该有机化合物中含 $\ce{-OH}$ 和 $\ce{-COOH}$ ，并根据酯环的大小，确定 $\ce{-OH}$ 与 $\ce{-COOH}$ 的相对位置

## 根据 特殊的转化关系 推断 有机物类型

1. $\ce{醇->[氧化]醛->[氧化]羧酸}$
2. $\ce{酯->[无机酸或碱]B \& C}$
3. 有机三角 <img src="./images/K-2.8.svg" style="zoom:40%;"/> ，分别是醇、烯烃、卤代烃


---



# Chapter 05 化学物质基本概念

Source directory: `05 化学物质基本概念`

## Original file: 01 物质的组成和分类.md

---
description: "介绍物质的组成和分类，包括元素、单质、化合物、同素异形体和同位素的概念，以及物质的分类体系。"
---

# 01 · 物质的组成与分类

## 物质的组成

1. 任何物质都是由 **元素** 组成

2. 单质：只由 **一种元素** 组成的 **纯净物**

   化合物：由 **多种元素** 组成的 **纯净物**

3. 元素在物质中的存在形态：
   1. 游离态：元素以 单质 形式存在的状态
   2. 化合态：元素以 化合物 形式存在的状态

4. 同素异形体
   1. **同种元素** 形成不同 **单质** 称为 同素异形体

   2. 原子个数不同：如 $\ce{O2}$ 和 $\ce{O3}$
   3. 原子排列方式不同：如金刚石和石墨

   4. 同素异形体之间的性质差异主要体现在 **物理性质** 上，他们的化学性质相似

   同素异形体之间的转化属于化学变化

5. 同位素

   质子数相同中子数不同的同一元素的不同核素

   同位素之间化学性质相似

## 物质的分类

$$
物质\begin{cases}
纯净物
\begin{cases}
化合物\begin{cases}
有机化合物\\
无机化合物
\end{cases}\\
单质\begin{cases}
金属单质\\
非金属单质
\end{cases}\\
\end{cases}\\
混合物: 溶液、胶体、浊液\\
\end{cases}\\
$$

### 混合物

混合物是由两种或两种以上物质混合而成的物质

下面列举常见的混合物：

1. 分散系：溶液、胶体、浊液等

2. 高分子化合物：蛋白质、纤维素、淀粉、塑料等（聚合度不同的物质混合所以是混合物）

3. 其他物质：石油及其各种馏分、天然气、油脂、福尔马林、氨水、王水、碱石灰等

### 纯净物

#### 单质

单质是由同一种元素组成的纯净物

1. 金属单质：例如：$\ce{K、Ca、Na、Mg、Al}$ 等
2. 非金属单质：例如：$\ce{S、Cl2、He}$ 等
3. 稀有气体

> 1. 只含一种元素的物质不一定是纯净物。如氧气 $\ce{O2}$ 和臭氧 $\ce{O3}$ 混合得到的物质是混合物。
> 2. 同种元素的同位素单质混合得到的物质是纯净物。如氢的同位素氕氘氚组成的双原子分子 $\ce{H2、D2、T2}$ 混合在一起得到的是纯净物
> 3. 含水的物质不一定是混合物。如胆矾 $\ce{CuSO4 • 5H2O}$、绿矾 $\ce{FeSO4 • 7H2O}$、明矾 $\ce{KAl(SO4)2 • 12H2O}$ 都是纯净物

#### 化合物

化合物是由两种或两种以上的元素组成的纯净物

##### Ⅰ 氧化物

氧元素与另外一种化学元素组成的二元化合物叫做氧化物

$$
氧化物
  \begin{cases}
  不成盐氧化物:\ce{CO、NO}等\\
  成盐氧化物
    \begin{cases}
    碱性氧化物:\ce{Na2O、CaO}等\\
    酸性氧化物:\ce{CO2、P2O5、Mn2O7}等\\
    两性氧化物:\ce{Al2O3,ZnO,BeO}等\\
    \end{cases}\\
  过氧化物:\ce{Na2O2、H2O2}等\\
  \end{cases}\\
$$

**a. 酸性氧化物**

酸性氧化物指与水反应生成相应价态的酸，或与碱反应只生成一种相应价态的盐和水的氧化物。例如：$\ce{SO2}$、$\ce{SO3}$、$\ce{P2O5}$、$\ce{SiO2}$、$\ce{Mn2O7}$ 等

> 1. 酸性氧化物不一定是非金属氧化物。如高锰酸酐 $\ce{Mn2O7}$ 既是酸性氧化物，又是金属氧化物
> 2. 非金属氧化物不一定是酸性氧化物。如一氧化碳 $\ce{CO}$、一氧化氮 $\ce{NO}$、二氧化氮 $\ce{NO2}$ 都是不成盐氧化物
> 3. 酸性氧化物不一定能与水反应生成相应的酸。如二氧化硅 $\ce{SiO2}$ 不与水反应。能与碱反应生成盐和水的氧化物不一定是酸性氧化物。如二氧化氮 $\ce{NO2}$ 是不成盐氧化物，氧化铝 $\ce{Al2O3}$ 是两性氧化物
> 4. 酸性氧化物一定是酸酐，但酸酐不一定是酸性氧化物。如乙酸酐 $\ce{CH3COOOCCH3}$ 含有三种元素，不是氧化物，故不是酸性氧化物

**b. 碱性氧化物**

碱性氧化物指与水反应生成相应价态的碱，或与酸反应只生成一种相应价态的盐和水的氧化物。例如：$\ce{Na2O}$、$\ce{CaO}$、$\ce{MgO}$、$\ce{FeO}$、$\ce{Fe2O3}$ 等

> 1. 碱性氧化物一定是金属氧化物，但金属氧化物不一定是碱性氧化物。如高锰酸酐 $\ce{Mn2O7}$ 既是金属氧化物，又是酸性氧化物
> 2. 碱性氧化物不一定能与水反应生成相应的碱。如氧化铁 $\ce{Fe2O3}$ 不与水反应
> 3. 能与酸反应生成盐和水的氧化物不一定是碱性氧化物。如氧化铝 $\ce{Al2O3}$ 是两性氧化物

**c. 两性氧化物**

两性氧化物是指既可以与酸反应生成相应价态的盐和水，又可以与碱反应生成相应价态的盐和水的氧化物。例如：$\ce{Al2O3}$、$\ce{PbO}$、$\ce{ZnO}$ 等

> 双性物质：
>
> 单质：$\ce{Al、Zn、Be}$
>
> 氧化物：$\ce{Al2O3、ZnO、BeO}$
>
> 氢氧化物：$\ce{Al(OH)3、Zn(OH)2、Be(OH)2}$
>
> 盐：弱酸酸式盐
>
> 有机物：氨基酸、蛋白质

**d. 不成盐氧化物**

与两性氧化物完全相对地，不成盐氧化物是指既不可以与酸反应生成相应价态的盐和水，又不可以与碱反应生成相应价态的盐和水的氧化物。例如：$\ce{CO}$、$\ce{NO}$、$\ce{NO2}$ 等

##### Ⅱ 酸

酸是指在水溶液中电离时产生的阳离子都是是氢离子的化合物

$$
酸
  \begin{cases}
  按电离出的\ce{H+}数
    \begin{cases}
    一元酸:\ce{HCl、HNO3}等\\
    二元酸:\ce{H2SO4、H2S}等\\
    多元酸:\ce{H3PO4}等\\
    \end{cases}\\
  按酸根是否含氧
    \begin{cases}
    无氧酸:\ce{HCl、HF}等\\
    含氧酸:\ce{HClO4、H2SO4}等\\
    \end{cases}\\
  按酸性强弱
    \begin{cases}
    强酸:\ce{HCl、H2SO4、HNO3、HClO4、HBr、HI}\\
    弱酸:\ce{CH3COOH、HF}等\\
    \end{cases}\\
  按有无挥发性
    \begin{cases}
    挥发性酸:\ce{HCl、HNO3}等\\
    难挥发性酸:\ce{HClO4、H2PO4}等\\
    \end{cases}\\
  \end{cases}\\
$$

##### Ⅲ 碱

碱是指在水溶液中电离时产生的阴离子都是氢氧根离子的化合物

$$
碱
  \begin{cases}
  按水溶性
    \begin{cases}
    可溶性碱:\ce{NaOH、KOH、Ba(OH)2}等\\
    难溶性碱:\ce{Mg(OH)2、Cu(OH)2}等\\
    \end{cases}\\
  按碱性强弱
    \begin{cases}
    强碱:\ce{KOH、Ca(OH)2、Ba(OH)2、NaOH}\\
    弱碱:\ce{NH3 · H2O、Fe(OH)3}等\\
    \end{cases}\\
  \end{cases}\\
$$

##### Ⅳ 盐

盐是指金属离子或铵根离子（ $\ce{NH+4}$ ）与酸根离子或非金属离子结合的化合物

$$
盐
  \begin{cases}
  正盐:\ce{BaSO4、KNO3、NaCl}等\\
  酸式盐:\ce{NaHCO3、KHSO4}等\\
  碱式盐:\ce{Cu2(OH)2CO3,Mg(OH)Cl}等\\
  复盐:\ce{KAl(SO4)2 · 12H2O}等\\
  \end{cases}
$$

**a. 正盐**：在酸和碱完全中和生成的盐中，不含酸中的氢离子，也不含有碱中的氢氧根离子，这样的盐叫做正盐

**b. 酸式盐**：电离时生成的阳离子除金属离子（或 $\ce{NH+4}$ ）外还有氢离子，阴离子为酸根离子的盐叫做酸式盐

**c. 碱式盐**：电离时生成的阴离子除酸根离子外还有氢氧根离子

**d. 复盐：** 由两种金属离子（可含 $\ce{NH+4}$ ）和一种酸根离子构成的盐叫做复盐

### 材料分类

1. 金属材料：$\ce{Fe、Cu、Al}$、合金 等
2. 无机非金属材料
   1. 传统无机非金属材料：陶瓷、玻璃、水泥 等
   2. 新型无机非金属材料：高温结构陶瓷、光导纤维 等
3. 有机高分子材料
   1. 天然有机高分子材料：淀粉、纤维素、蛋白质、天然橡胶 等
   2. 合成有机高分子材料：塑料、合成纤维、合成橡胶 等

> 高温结构陶瓷作为新型无机非金属材料，那就不是像常规陶瓷那样主要成分是硅酸盐了

### 其他分类方式

电离程度

- 电解质

  在水溶液或熔融状态下能够导电的 **化合物**，如 $\ce{HCl、NaOH、NaCl}$ 等
  - 强电解质：强酸、强碱、盐（大部分）、活泼金属氧化物
  - 弱电解质：弱酸、弱碱、水、盐（$\ce{HgCl2、(CH3COO)2Pb}$）

- 非电解质

  在水溶液和熔融状态下都不能导电的 **化合物**，包含大多数有机化合物（酸类除外）、非金属氧化物（ $\ce{H2O}$ 除外），如酒精、葡萄糖、$\ce{CH4}$ 等

- 既不是电解质，也不是非电解质：单质和混合物

> - 电解质导电条件：水溶液或熔融状态。电解质不是任何状态下都能导电，如固态 $\ce{NaCl}$ 不导电，溶于水或熔融状态下才能导电
> - 电解质必须自身电离导电。如 $\ce{NH3、CO2、SO2}$ 等溶于水均能导电，但是溶于水后的产物导电，不是自身电离导电，所以均属于非电解质


---

## Original file: 02 物质的计量.md

---
description: "讲解物质的计量概念，包括物质的量、摩尔质量、气体摩尔体积和物质的量浓度的定义、单位和计算公式。"
---

# 02 · 物质的计量

## 物质的量 及其相关概念

### 物质的量 $n$

1. 概念：表示含有一定数目粒子的集合体，**是国际单位制中七个基本物理量之一（易混）**。
2. 符号：$n$
3. 单位：$\ce{mol}$（摩尔 简称“摩”）
4. 使用范围：适用于微观粒子或微观粒子的特定组合
5. 阿伏伽德罗常数：指一摩尔任何粒子的粒子数，符号为 $N_A$ ， $N_A\approx 6.02\times10^{23} \ce{mol^{-1}}$
6. 计量对象：微观粒子，包括分子、原子、离子、质子、中子、电子、原子团等
7. 公式：$n=\dfrac{N}{N_A}$

> $\ce{3mol\space CO2}$ 有 $9N_A$ 个原子

### 摩尔质量 $M$

1. 定义：单位物质的量的物质所具有的质量

2. 符号：$M$

3. 单位：$g/\ce{mol}\space(g\cdot\ce{mol^{-1}})$

4. 数值：摩尔质量以 $g/\ce{mol}$ 为单位时，在数值上等于该粒子的相对原子质量或相对分子质量

   > $\ce{H2O}$ 的相对分子质量为 $18$（单位为「1」），$\ce{H2O}$ 的摩尔质量为 $18\space g/\ce{mol}$

5. 物质的量、质量、摩尔质量的关系：$n=\dfrac{m}{M}$

### 气体摩尔体积 $V_m$

1. 定义：单位物质的量的气体所占的体积
2. 符号：$V_m$
3. 单位：$L/\ce{mol}\space(L\cdot\ce{mol^{-1}})$
4. 公式：$V_m=\dfrac{V}{n}$
5. 气体摩尔体积与气体所处的 **温度** 与 **压强** 有关
6. 在标准状况下（$0\ce{°C}、101\ce{kPa}$）气体的摩尔体积约为 $22.4L/\ce{mol}$
   1. 在标况下，$\ce{1mol}$ 任何气体的体积都为 $22.4L$
   2. 使用时，物质的聚集状态一定为 **气体**（可以是混合气），但条件必须为 **标准状况**

### 物质的量浓度 $c$

1. 定义：一定温度、压强下，单位溶液中所含溶质的量的多少
2. 符号：$c$
3. 单位：$\ce{mol}/L\space(\ce{mol}\cdot L^{-1})$
4. 公式：$c=\dfrac{n}{V}$

> 相互换算：
>
> $c=\cfrac{1000\rho w}{M}$
>
> $\rho:$ 密度 $w:$ 质量分数 $m:$ 溶质的摩尔质量

> 物质的量 及其相关概念 常见错误
>
> 1. [×] 摩尔是化学上常用的一个物理量：摩尔是单位
> 2. [×] $\ce{1mol}$ 水含有 $\ce{2mol}$ 氢 和 $\ce{1mol}$ 氧：没有明确粒子的种类
> 3. [×] $\ce{1mol}$ 任何物质都含有 $6.02\times10^{23}$ 个分子：物质不一定都由分子构成
> 4. [×] $\ce{2mol\space H2O}$ 是 $\ce{1mol\space H2O}$ 摩尔质量的 $2$ 倍：摩尔质量与物质的量无关


---

## Original file: 03 离子反应 离子方程式.md

---
description: "介绍离子方程式的概念、书写步骤和规律，以及离子反应的特点。"
---

# 03 · 离子方程式

## 离子方程式 及其相关概念

### 离子方程式

1. 概念：用<u>实际参加反应的离子符号</u>来表示反应的式子

2. 书写步骤：

   > 1.写：正确书写反应的化学方程式
   >
   > 2.拆：把易溶于水且易电离的物质（如强酸、强碱和大部分可溶性盐拆成离子的形式，单质、沉淀、气体、难电离的物质(如弱酸、弱碱、水）等仍用化学式表示
   >
   > 3.删：删去方程式两边不参加反应的离子，并将方程式化为最简
   >
   > 4.查：检查离子方程式两边各元素的<u>原子个数</u>和<u>电荷总数</u>是否相等

3. 拆写规律：能拆写成离子的物质必须同时具备**易溶**、**易电离**这两个条件，即易溶的强电解质写成离子形式，其他物质一律写化学式。
   1. 强酸、强碱、易溶盐写成**离子**形式。
   2. 单质、氧化物(如$CuO$)(水溶液不拆 熔融状态可拆)、气体、难溶物(如$CaCO3$)、弱电解质(弱酸、弱碱、水)一律写化学式。


---

## Original file: 04 离子共存 离子的检验和推断.md

---
description: "讲解离子共存的判断、常见阳离子和阴离子的检验方法，以及离子推断的技巧。"
---

# 04 · 离子检验

大题通用术语：取少量待测液于洁净试管中，滴加……，观察……

## 阳离子

- $\ce{Na+}$： 用 **铂丝** 蘸其溶液，用酒精灯火焰上灼烧，火焰呈 **黄色**

- $\ce{K+}$： 用 **铂丝** 蘸其溶液，用酒精灯火焰上灼烧，透过蓝色钴玻璃观察，火焰呈 **紫色**

  > 通过焰色反应检验离子
  >
  > - $\ce{Na+}$ 与 $\ce{K+}$ 在自然界中往往同时存在，火焰的紫色可能被黄色遮盖，因此判断 $\ce{K+}$ ，需透过蓝色钻玻璃观察
  > - 需使用铂丝或干净的铁丝，不得使用玻璃棒（$\ce{Na2SiO3}$）

---

- $\ce{Mg^{2+}->[少量 NaOH] 白色沉淀 Mg(OH)2  v ->[滴加 NaOH 至过量] 白色沉淀不溶解}$

- $\ce{Al^{3+}->[少量 NaOH] 白色沉淀 Al(OH)3  v ->[滴加 NaOH 至过量] 白色沉淀完全溶解 [Al(OH)4]^{-} }$

  > 如果白色沉淀部分溶解则说明均含有 $\ce{Mg^{2+}}$ 与 $\ce{Al^{3+}}$

---

- $\ce{Fe^{3+}}$
  1. 待测液 $\ce{->[KSCN 溶液]}$ 溶液变为血红色 $\ce{Fe(SCN)3}$
  2. 待测液 $\ce{->[NaOH 溶液]}$ 产生红褐色沉淀 $\ce{Fe(OH)3}$
  3. 待测液 $\ce{->[苯酚]}$ 溶液显紫色

- $\ce{Fe^{2+}}$
  1. 待测液 $\ce{->[\ce{K3[Fe(CN)6]}]}$ 产生蓝色沉淀
  2. 待测液 $\ce{->[NaOH 溶液]}$ 白色絮状沉淀 $\ce{->}$ 灰绿色沉淀 $\ce{->}$ 红褐色沉淀

- 有 $\ce{Fe^{2+}}$ 无 $\ce{Fe^{3+}}$

  待测液 $\ce{->[KSCN 溶液]}$ 溶液不变红（排除 $\ce{Fe^{3+}}$） $\ce{->[氯水 \text{or} H2O2][(无色氧化物)]}$ 溶液变红

---

- $\ce{NH+_4}$
  待测液 $\ce{->[足量 NaOH]->[加热]}$ 产生无色、具有刺激性气味 且 可使湿润的红色石蕊试纸变蓝的气体

  > $\ce{NH+_4}$ 与 $\ce{NaOH}$ 反应先生成一水合氨，只有一部分分解出氨气，且由于其氨气对水溶解性过大，会溶解在水中
  >
  > 加热用于促进一水合氨分解 且 降低氨气对水的溶解度

---

- $\ce{Cu^{2+}}$

  > 一般可通过溶液颜色直接判断是否含有 $\ce{Cu^{2+}}$，但如果溶液中含有多个有色离子则难以判断，需通过化学检验的方式判断

  待测液 $\ce{->[NaOH]}$ 蓝色沉淀 $\ce{Cu(OH)2}$

- $\ce{Ag+}$
  1. 待测液 $\ce{->[HNO3][酸化]}$ 无沉淀（排除 $\ce{SiO^{2-}_3}$ 干扰） $\ce{->[HCl]}$ 白色沉淀 $\ce{AgCl}$
  2. 待测液 $\ce{->[少量氨水]}$ $\ce{AgOH v}$（不稳定） $\ce{->}$ 棕褐色沉淀 $\ce{Ag2O}$ $\ce{->[氨水]}$ 沉淀溶解 $\ce{[Ag(NH3)2]OH}$

---

## 阴离子

- $\ce{Cl-}$
  待测液 $\ce{->[HNO3][酸化]}$ （排除 $\ce{CO^2-_3}$ 的干扰） $\ce{->[AgNO3]}$ 白色沉淀 $\ce{AgCl}$

  > 教材对比实验
  >
  > 在三支试管中分别加入 2~3mL 稀盐酸、$\ce{NaCl}$ 溶液、$\ce{Na2CO3}$ 溶液，然后各滴入几滴 $\ce{AgNO3}$ 溶液，观察现象。再分别加入少量稀硝酸，观察现象
  >
  > | 物质               | 加入 $\ce{AgNO3}$ 溶液后  | 加入稀硝酸后   | 解释或离子方程式                                                                             |
  > | :----------------- | :------------------------ | :------------- | :------------------------------------------------------------------------------------------- |
  > | 稀盐酸             | 白色沉淀（$\ce{AgCl}$）   | 不溶解         | $\ce{Ag+ +Cl- \xlongequal{}AgCl v}$                                                          |
  > | $\ce{NaCl}$ 溶液   | 白色沉淀（$\ce{AgCl}$）   | 不溶解         | $\ce{Ag+ +Cl- \xlongequal{}AgCl v}$                                                          |
  > | $\ce{Na2CO3}$ 溶液 | 白色沉淀（$\ce{Ag2CO3}$） | 溶解并产生气泡 | $\ce{2Ag+ +CO^2-_3\xlongequal{}Ag2CO3 v}$<br>$\ce{Ag2CO3 +2H+\xlongequal{}2Ag+ +H2O +CO2 ^}$ |

- $\ce{Br-}$
  待测液 $\ce{->[氯水]}$ 溶液变黄 $\ce{->[\ce{CCl4}]}$ 分层，且下层油状液体（有机层）呈橙色

- $\ce{I-}$
  1. 待测液 $\ce{->[氯水]}$ 溶液变黄 $\ce{->[苯]}$ 分层，且上层油状液体（有机层）呈紫色
  2. 待测液 $\ce{->[淀粉溶液][振荡]}$ 蓝色溶液

- $\ce{Br-} \space\And\space \ce{I-}$
  待测液 $\ce{->[AgNO3\ 溶液]}$ $\begin{cases}\text{淡黄色沉淀 } \ce{AgBr} \downarrow &\ce{Br-} \\ \text{黄色沉淀 } \ce{AgI} \downarrow &\ce{I-}\end{cases}$

---

- $\ce{SO^2-_4}$
  1. 原理：在溶液中，$\ce{SO^2-_4}$ 可与 $\ce{Ba^2+}$ 反应，生成 **不溶于稀盐酸** 的白色 $\ce{BaSO4}$ 沉淀

  > 强酸根形成的沉淀往往难溶于强酸，例如 $\ce{BaSO4}$ 、 $\ce{AgCl}$ 不溶于盐酸、硝酸 2. 操作方法
  1.  取少许待测液于洁净试管中，先加入足量稀盐酸酸化

      > $\ce{Ba^2+}$ 与 $\ce{SO^2-_4、CO^2-_3、SO^2-_3}$ 形成沉淀，$\ce{Ag+}$ 与 $\ce{Cl-}$ 形成沉淀；稀盐酸可排除 $\ce{CO^2-_3、SO^2-_3、Cl-}$ 的干扰

  2.  上一步后无明显现象（若有沉淀，则静置后取上层清液），滴加 $\ce{BaCl2}$ 溶液

  3.  若有白色沉淀产生，则说明待测液中含有 $\ce{SO^2-_4}$
      若无白色沉淀产生，则说明待测液中不含 $\ce{SO^2-_4}$

  4.  注意事项
      - 不能只加入 $\ce{BaCl2}$ ，且盐酸和 $\ce{BaCl2}$ 的顺序不可以颠倒

        > 例如：待测液先加入 $\ce{BaCl2}$ ，发现白色沉淀，再加入稀盐酸，观察到沉淀不消失，不可判断是 $\ce{SO^2-_4}$
        >
        > 因为虽然排除了 $\ce{BaCO3}$ 和 $\ce{BaSO3}$ 的干扰，但也有可能是 $\ce{AgCl}$ （$\ce{HCl}$ 不会使 $\ce{AgCl}$ 沉淀消失）

      - 不可以引入硝酸根，例如不可以加 $\ce{HNO3}$ 酸化或是加 $\ce{Ba(NO3)2}$

        > 会使得溶液中可能存在的 $\ce{SO^-3}$ 氧化为 $\ce{SO^2-_4}$

---

- $\ce{SO^{2-}_3} \space\And\space \ce{HSO^-_3}$

  $
  \left.\begin{array}{l}
  \begin{cases}
  \ce{SO^{2-}_3 &->[CaCl_2]&白色沉淀&->[足量 HCl] 白色沉淀完全溶解}\\
  \ce{HSO^-_3 &->[CaCl_2]&无沉淀&->[\qquad\qquad 足量 HCl\qquad\qquad]}
  \end{cases}\
  \end{array}\right\}
  \ce{->}$生成无色具有刺激性 且 可使品红溶液褪色的气体 $(\ce{SO2})$

- $\ce{CO^{2-}_3} \space\And\space \ce{HCO^-_3}$

  $
  \left.\begin{array}{l}
  \begin{cases}
  \ce{CO^{2-}_3 &->[CaCl_2]&白色沉淀&->[足量 HCl] 白色沉淀完全溶解}\\
  \ce{HCO^-_3 &->[CaCl_2]&无沉淀&->[\qquad\qquad 足量 HCl\qquad\qquad]}
  \end{cases}\
  \end{array}\right\}
  \ce{->}$生成无色无味 且 可使澄清石灰水变浑浊的气体 $(\ce{CO2})$

---

- $\ce{AlO^-_2} \space\And\space \ce{SiO^{2-}_3}$

  $
  \left\{
  \begin{array}{l}
  \ce{AlO^-_2 ->[少量 HCl]}\ \text{白色沉淀}\ \ce{->[过量 HCl]}\ \text{白色沉淀完全溶解} \\
  \ce{SiO^{2-}_3 ->[少量 HCl]}\ \text{白色沉淀}\ \ce{->[过量 HCl]}\ \text{白色沉淀不溶解}
  \end{array}
  \right.
  $

---

- $\ce{S2O^{2-}_3}$

  待测液 $\ce{->[HCl]}$ 黄色沉淀 且 生成具有刺激性气味的气体

  > $\ce{S2O^{2-}_3 + 2H+ \xlongequal{} S v + SO2 ^ + H2O}$

- $\ce{S^{2-}}$
  1. 待测液 $\ce{->[Cu^{2+}]}$ 黑色沉淀 $\ce{CuS}$
  2. 待测液 $\ce{->[氯水][(氧化剂)]}$ 黄色沉淀 $\ce{S}$

---

- $\ce{NO^-_3}$
  待测液 $\ce{->[浓缩]->[H2SO4、Cu]}$ 红棕色气体 $\ce{NO2}$（或 无色气体 $\ce{NO}$ 随后立即变为红棕色）

> 例题：
>
>     无色溶液的阴离子可能是 $\ce{Cl- 、Br- 、I- 、SO^2-_3 、SO^2-_4}$ 中的一种或几种，取少量该溶液与试管中，滴加少量氯水，溶液仍为无色，将试管中的溶液分成两份，分别加入 $\ce{AgNO3}$ 和 $\ce{BaCl2}$ 溶液，均有白色沉淀产生。则原溶液中一定存在的阴离子与可能存在的阴离子有哪些？
>
> 解答：
>
> 1. 由于溶液是无色的，因此滴加的少量氯水与还原性物质进行了反应，可被氧化的还原性物质有 $\ce{Br- 、I- 、SO^2-_3}$
> 2. 由于 $\ce{Br- 、I-}$ 被氧化后的溶液有颜色（$\ce{Br:}$ 橙黄；$\ce{I2:}$ 黄），而且 $\ce{\overset{+4}{S}}$ 的还原性较大，因此氯水使得 $\ce{SO^2-_3}$ 氧化为 $\ce{SO^2-_4}$ ，因此溶液中一定存在 $\ce{SO^2-_3}$
> 3. 但如果氯水较少，仅氧化 $\ce{SO^2-_3}$ ，而如果有 $\ce{Br- 、I-}$ ，则不会被氧化，因此溶液中可能存在 $\ce{Br- 、I-}$
> 4. 滴加少量氯水时为溶液引入 $\ce{Cl-}$ ，因此无法通过与 $\ce{AgNO3}$ 反应生成 $\ce{AgCl}$ 沉淀判断原溶液是否存在 $\ce{Cl-}$
> 5. 由于无论原溶液是否存在 $\ce{SO^2-_4}$ ， $\ce{SO^2-_3}$ 都会被氧化为 $\ce{SO^2-_4}$ ，因此无法通过与 $\ce{BaCl2}$ 反应生成 $\ce{BaSO4}$ 沉淀判断原溶液是否存在 $\ce{SO^2-_3}$


---

## Original file: 05 氧化还原反应及其配平.md

---
description: "介绍氧化还原反应的概念、氧化剂和还原剂的判断、化合价变化，以及氧化还原方程式的配平方法。"
---

# 05 · 氧化还原反应及其配平

## 氧化还原反应 及其相关概念

### 氧化还原反应

氧化还原的四组名词

氧化反应：失$e^{-}$，化合价↑

还原反应：得$e^{-}$，化合价↓

氧化剂：帮助别人氧化的物质，本身被还原.得$e^{-}$

还原剂：帮助别人还原的物质，本身被氧化.失$e^{-}$

抗氧化剂：帮助别人抵抗被氧化，容易被氧化→强还原剂

> 易错点：抗氧化剂是”还原剂”

氧化性：物质得电子的能力（氧化剂强弱）

还原性：物质失电子的能力（还原剂强弱）

氧化剂具有氧化性，还原剂具有还原性

​

氧化产物：被氧化所生成的产物 $\ce{还原剂->[失e^{-}]氧化产物}$

还原产物：被还原所生成的产物 $\ce{氧化剂->[得e^{-}]还原产物}$

口诀：升失氧化还原剂，具有还原性。

​ 降得还原氧化剂，具有氧化性。

> 解析：
>
> 升(升高化合价).失(失去$e^{-}$).氧化(被氧化).还原剂(是还原剂)，具有还原性。
>
> 降(降低化合价).得(得到$e^{-}$).还原(被还原).氧化剂(是氧化剂)，具有氧化性。

常见元素还原性顺序：

$$
\ce{S^{2-} }>\ce{SO}_{3}^{2-}> \ce{I-}> \ce{Fe^2+}> \ce{Br-}> \ce{Cl-}>\ce{F-}
$$

### 氧化还原反应配平（重要考点）

#### 歧化和归中反应

歧化反应：氧化剂和还原剂为同种物质，一种元素变价为多种价态，这样的氧化还原反应反应称为歧化反应

归中反应：同种元素由不同价态(高价态和低价态)转变为中间价态的氧化还原反应，称为归中反应

#### 氧化还原方程式的配平

1. 配平依据：电子得失相等，即化合价升降总数相等

2. 配平原则：

   ①质量（原子）守恒；

   ②得失电子守恒；

   ③离子方程式中电荷守恒

3. 配平步骤：

   ①标变价——表明变价元素前后化合价

   ②列得失——列出元素化合价变化值
   ③求总数——求出化合价升降的最小公倍数，使化合价升高和降低的数目相等
   ④配系数——配出氧化剂、还原剂、氧化产物、还原产物的系数，观察法配平其它物质的系数
   ③查守恒——查原子是否守恒、电荷是否守恒（通常通过检查氧元素的原子数），画上等号

   缺项配平：先配平含有变价元素的物质的化学计量数，然后由元素守恒确定未知物，再根据原子守恒和电荷守恒进行配平。其补项原则有

   | 条件           | 补项原则 |
   | -------------- | -------- |
   | 缺氢氧元素     | 补水     |
   | 缺酸根         | 补对应酸 |
   | 缺金属阳离子   | 补对应碱 |
   | 酸性条件缺电荷 | 补H+     |
   | 碱性条件缺电荷 | 补OH-    |


---

## Original file: 06 化学常识.md

---
description: "介绍化学物质的俗名和常见名称，以及特殊物质的用途和应用。"
---

# 06 · 化学常识

## 物质俗名

| 俗名                        | 物质                         | 俗名      | 物质                                         |
| --------------------------- | ---------------------------- | --------- | -------------------------------------------- |
| 生石灰                      | $\ce{CaO}$                   | 刚玉      | $\ce{Al2O3}$                                 |
| 石灰乳/石灰水/消石灰/熟石灰 | $\ce{Ca(OH)2}$               | 漂白粉    | $\ce{Ca(ClO)2(有效成分) +CaCl2}$             |
| 石灰石/大理石               | $\ce{CaCO3}$                 | 84 消毒液 | $\ce{NaClO +NaCl}$                           |
| 碱石灰                      | $\ce{CaO +NaOH +KOH}$        | 草木灰    | $\ce{K2CO3}$                                 |
| 苏打/纯碱                   | $\ce{Na2CO3}$                | 电石      | $\ce{CaC2}$                                  |
| 小苏打                      | $\ce{NaHCO3}$                | 冰晶石    | $\ce{Na3AlF6}$                               |
| 烧碱/火碱                   | $\ce{NaOH}$                  | 铁锈      | $\ce{Fe2O3 \cdot xH2O}$                      |
| 胆矾                        | $\ce{CuSO4 \cdot 5H2O}$      | 铜锈/铜绿 | $\ce{Cu2(OH)2CO3}$                           |
| 绿矾                        | $\ce{FeSO4 \cdot 7H2O}$      | 王水      | $\ce{HNO3 + 3HCl}$ (均为浓溶液；体积之比1:3) |
| 明矾                        | $\ce{KAl(SO4)2 \cdot 12H2O}$ | 可燃冰    | $\ce{CH4 . xH2O}$ 笼状结构                   |
| 石膏                        | $\ce{CaSO4 \cdot 2H2O}$      | 水煤气    | $\ce{H2 + CO}$                               |
| 热石膏                      | $\ce{2CaSO4 \cdot H2O}$      | 合成气    | $\ce{2H2 + CO}$                              |
| 重晶石                      | $\ce{BaSO4}$                 | 毒重石    | $\ce{BaCO3}$                                 |
| 芒硝/朴硝                   | $\ce{Na2SO4 \cdot 10H2O}$    | 倭铅      | $\ce{Pb3O4}$                                 |
| 石英/脉石                   | $\ce{SiO2}$                  | 朱砂      | $\ce{HgS}$                                   |
| 硅胶                        | $\ce{SiO2 \cdot xH2O}$       | 硝石      | $\ce{KNO3}$                                  |
| 黄铜矿                      | $\ce{CuFeS2}$                | 硇水      | $\ce{As2O3}$                                 |
| 水玻璃，泡花碱              | $\ce{Na2SiO3}$               | 黑火药    | $\ce{S +2KNO3 +3C}$                          |

## 特殊物质的用途

| 特殊物质                      | 用途                       |
| ----------------------------- | -------------------------- |
| 干冰、$\ce{AgI}$ 晶体         | 人工降雨剂                 |
| $\ce{AgBr}$                   | 感光剂                     |
| $\ce{K-Na}$ 合金              | 原子反应堆导热剂           |
| $\ce{NaHCO3}$、$\ce{Al(OH)3}$ | 治疗胃酸过多               |
| $\ce{NaHCO3}$                 | 作发酵粉 制药              |
| 明矾                          | 净水剂                     |
| $\ce{BaSO4}$                  | 钡餐                       |
| $\ce{SO2}$                    | 漂白剂、防腐剂             |
| $\ce{Ca(ClO)2}$               | 消毒、杀菌漂白             |
| $\ce{Na2O2}$                  | 供氧剂、漂白剂             |
| $\ce{H2O2}$                   | 氧化剂、漂白剂、消毒剂     |
| $\ce{O3}$                     | 漂白剂、杀菌剂、吸收紫外线 |
| 石膏                          | 水泥硬化调节剂             |
| 苯酚                          | 消毒剂                     |
| $\ce{Na2SiO3}$ 溶液           | 黏合剂、防火剂             |
| 乙烯                          | 催熟剂、有机合成基础材料   |
| 维生素 C                      | 抗氧化剂                   |
| $\ce{SiO2}$                   | 光导纤维                   |
| $\ce{Si}$                     | 半导体、太阳能电池         |
| $\ce{Na2FeO4}$                | 杀菌净水剂                 |
| 硅胶                          | 干燥剂                     |
| $\ce{Fe}$ 粉                  | 抗氧化剂                   |

## 物质颜色

### 焰色反应

$\ce{Li}$：紫红色

$\ce{Na}$：黄色

$\ce{K}$：紫色(透过蓝色钴玻璃)

$\ce{Cu}$：绿色

$\ce{Ba}$：（黄）绿色

### 实验现象

$\ce{H2}$ 与 $\ce{Cl2}$ 点燃：苍白色火焰

$\ce{Na}$ 与 $\ce{Cl2}$ 反应：黄色火焰/白烟

$\ce{Cu}$ 与 $\ce{Cl2}$ 反应：棕黄色烟

$\ce{Fe}$ 与 $\ce{Cl2}$ 反应：棕褐色烟

### 铁

$\ce{Fe}$ 粉：黑色

$\ce{FeO}$：黑色

$\ce{Fe2O3}$：红（棕）色

$\ce{Fe3O4}$：黑色

$\ce{Fe(OH)2}$：白色

$\ce{Fe(OH)3}$：红褐色

$\ce{Fe(OH)2}$，在空气中迅速被氧化：白色沉淀，迅速灰绿，最终红褐

$\ce{Fe^{3+}}$：（棕）黄色

$\ce{Fe^{2+}}$：浅绿色

检验 $\ce{Fe^{2+}}$：加入 $\ce{KFe(CN)6}$ →蓝色沉淀

检验 $\ce{Fe^{3+}}$：加入 $\ce{KSCN}$ →（血）红色溶液

### 卤素

$\ce{F2}$：淡黄绿色（气体）

$\ce{Cl2}$：黄绿色（气体）

$\ce{Br2}$：深红棕色（液体）

$\ce{I2}$：紫黑色（固体）

氯水：浅黄绿色

溴水：橙黄色

碘水：黄色

溴的四氯化碳（或苯）溶液：橙色

碘的四氯化碳（或苯）溶液：紫色

$\ce{AgCl}$：白色沉淀

$\ce{AgBr}$：淡黄色沉淀

$\ce{AgI}$：黄色沉淀

$\ce{AgF}$ 可溶 不为沉淀

### 红

紫红色：单质 $\ce{Cu}$

砖红色：$\ce{Cu2O}$、$\ce{Ag2CrO4}$

红棕色：气体 $\ce{NO2}$、液体 $\ce{Br2}$、固体 $\ce{Fe2O3}$

红褐色：$\ce{Fe(OH)3}$、$\ce{Fe(OH)3}$ 胶体

（血）红色溶液：$\ce{Fe^{3+}}$ 溶液中加入 $\ce{KSCN}$

粉红色：苯酚放置时间较长被氧化

### 橙

$\ce{Cr2O7^{2-}}$ 溶液：橙色

$\ce{Br2}$ 在水中显橙黄色，在 $\ce{CCl4}$（或苯）中显橙红色

### 黄

淡黄色固体：$\ce{S}$、$\ce{Na2O2}$、$\ce{AgBr}$

黄色固体（沉淀）：$\ce{AgI}$

$\ce{CrO4^2-}$ 溶液：黄色

$\ce{Na}$ 元素的焰色：黄色

黄蛋白实验：带有苯环的蛋白质与浓硝酸混合加热呈现黄色

### 绿

$\ce{Cu(OH)2}$：铜绿、铜锈

$\ce{CoSO4·7H2O}$：绿矾、青矾

$\ce{Cr^{2+}}$ 溶液：绿色

$\ce{FeSO4}$ 水溶液($\ce{Fe^{2+}}$ 溶液)：浅绿色溶液

$\ce{F2}$：浅黄绿色气体

$\ce{Cl2}$：黄绿色气体

### 蓝

淀粉+$\ce{I2}$：蓝色

$\ce{Cu(OH)2}$：蓝色固体（蓝色絮状沉淀）

$\ce{CuSO4·5H2O}$：蓝色晶体

$\ce{CuSO4}$ 水溶液：蓝色

$[\ce{Cu(NH3)4}]$ $\ce{SO4·5H2O}$：深蓝色晶体

### 紫

紫黑色固体：$\ce{I2}$、$\ce{KMnO4}$

$\ce{I2}$ 溶于 $\ce{CCl4}$（或是苯）：紫色

$\ce{KMnO4}$ 溶液：紫色溶液

$\ce{K}$ 元素的焰色：紫色（透过蓝色钴玻璃）

苯酚与 $\ce{FeCl3}$ 溶液反应：显紫色

### 黑

$\ce{MnO2}$、$\ce{Fe}$ 粉、$\ce{FeO}$、$\ce{Fe3O4}$、$\ce{CuO}$、$\ce{C}$

### 白

$\ce{BaSO4}$、$\ce{PbSO4}$、$\ce{CaSO4}$、$\ce{AgCl}$、$\ce{CaCO3}$、$\ce{BaCO3}$、$\ce{CaSO3}$、$\ce{BaSO3}$、$\ce{Na2CO3}$、$\ce{NaHCO3}$、$\ce{Mg(OH)2}$、$\ce{Al(OH)3}$、$\ce{Fe(OH)2}$、$\ce{H2SiO3}$、三溴苯酚

### 酸碱指示剂

酚酞：无色 $\ce{<-8.2-}$ 淡红 $\ce{ -10.0->}$ 红

石蕊：红色 $\ce{<-5-}$ 紫 $\ce{ -8->}$ 蓝

甲基橙：红色 $\ce{<-3.1-}$ 橙 $\ce{ -4.4->}$ 黄


---

## Original file: 07 化学与 STSE.md

---
description: "讨论化学与科学、技术、社会、环境的联系，包括金属和非金属化合物的性质与应用，以及环境污染问题。"
---

# 07 · 化学与 STSE

$\text{STSE = Science + Technology + Society + Environment}$

## 金属及其化合物

| 重要性质                                                                                                   | 应用                                                    |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| $\ce{Na2O2}$ 与 $\ce{H2O}$、 $\ce{CO2}$ 反应均生成 $\ce{O2}$                                               | 作供氧剂                                                |
| $\ce{Na2CO3}$ 水解使溶液显碱性，可促进油脂水解                                                             | 用热的纯碱溶液洗去油污                                  |
| $\ce{NaHCO3}$ 受热分解生成 $\ce{CO2}$，能与酸反应                                                          | 用作焙制糕点的膨松剂、胃酸中和剂                        |
| $\ce{Al}$ 具有良好的延展性和抗腐蚀性                                                                       | 常用铝箔包装物品                                        |
| 常温下，$\ce{Al}$、 $\ce{Fe}$ 遇浓硫酸或浓硝酸钝化                                                         | 盛装、运输浓硫酸或浓硝酸                                |
| $\ce{Al}$ 与 $\ce{Fe2O3}$ 反应放出大量的热                                                                 | 用于焊接钢轨                                            |
| $\ce{MgO}$、 $\ce{Al2O3}$ 熔点高                                                                           | 作耐高温材料                                            |
| $\ce{Al^{3+}}$ 水解生成的氢氧化铝胶体具有吸附性，$\ce{NaHCO3}$ 溶液和 $\ce{H2SO4}$ 溶液反应生成 $\ce{CO2}$ | 明矾作净水剂（混凝剂）                                  |
| 明矾溶液显酸性                                                                                             | 作泡沫灭火器，利用明矾溶液清除铜镜表面的铜锈            |
| $\ce{Al(OH)3}$ 有弱碱性                                                                                    | 中和胃酸，用作抗酸药                                    |
| $\ce{Fe}$ 具有还原性                                                                                       | 防止食品氧化变质                                        |
| $\ce{Fe2O3}$ 是红棕色粉末                                                                                  | 作红色颜料                                              |
| $\ce{Fe^{3+}}$ 水解生成的氢氧化铁胶体具有吸附性                                                            | 铁盐作净水剂（混凝剂）                                  |
| $\ce{K2FeO4}$ 是强氧化剂，还原产物 $\ce{Fe^{3+}}$ 水解生成氢氧化铁胶体                                     | 作新型消毒剂、净水剂                                    |
| $\ce{FeCl3}$ 溶液具有较强的氧化性                                                                          | 腐蚀铜刻制印刷电路板                                    |
| $\ce{CuSO4}$ 能使蛋白质变性                                                                                | 与石灰乳配制成波尔多液用于树木杀虫                      |
| $\ce{BaSO4}$ 不溶于水，不与胃酸反应，且有良好的吸收X射线的效果                                             | 在医疗上进行胃部造影前，$\ce{BaSO4}$ 作患者服用的“钡餐” |

## 非金属及其化合物

| 重要性质                                                                               | 应用                                                     |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 浓硫酸具有吸水性                                                                       | 作干燥剂（不能干燥 $\ce{NH3}$、 $\ce{H2S}$、 $\ce{HI}$） |
| 生石灰、无水氯化钙能与水反应                                                           | 作（食品）干燥剂                                         |
| $\ce{P2O5}$ 能与水反应                                                                 | 作干燥剂（不可干燥食品，可干燥HNO<sub>3</sub>）          |
| 硅具有半导体性能                                                                       | 制作芯片和太阳能电池                                     |
| $\ce{SiO2}$ 存在光的全反射                                                             | 制作光导纤维                                             |
| $4\ce{HF} + \ce{SiO2} \xlongequal{} 2\ce{H2O} + \ce{SiF4}$                             | 用氢氟酸刻蚀玻璃                                         |
| $\ce{ClO2}$ 具有较强的氧化性，且不会与水中微量有机物生成致癌性物质(优于Cl<sub>2</sub>) | 用于自来水的杀菌消毒                                     |
| 次氯酸盐具有强氧化性                                                                   | 作杀菌消毒剂、漂白剂                                     |
| 碘酸钾在常温下稳定                                                                     | 食盐中的加碘物质                                         |
| $\ce{NH4HCO3}$、 $\ce{NH4NO3}$ 是可溶的含氮化合物                                      | 用作氮肥                                                 |
| 浓氨水具有挥发性和还原性                                                               | 检验输送 $\ce{Cl2}$ 的管道是否漏气                       |
| $\ce{SO2}$ 具有漂白性                                                                  | 用于漂白纸浆、毛、丝等(可逆)                             |
| 硅酸钠的水溶液是一种无机黏合剂                                                         | 盛放碱性溶液的试剂瓶不能用玻璃塞                         |
| 干冰升华吸收大量的热                                                                   | 人工降雨                                                 |
| 液氨汽化吸收大量的热                                                                   | 做制冷剂                                                 |

## 环境污染

| 污染名称     | 主要污染物及形成原理                                                                                                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PM2.5        | 大气中直径小于或等于 2.5 微米的颗粒物，也称为可入肺颗粒物                                                                                                                                                        |
| 雾霾         | 混合了 $\ce{SO2}$、 $\ce{NO}$ 和可吸入颗粒物的雾气                                                                                                                                                               |
| 酸雨         | 主要形成原理（$\ce{CO2}$不是导致酸雨的气体）：<br> $\ce{SO2 + H2O \xlongequal{} H2SO3}$, $2\ce{H2SO3 + O2 \xlongequal{} 2H2SO4}$; $\ce{2NO + O2 \xlongequal{} 2NO2}$, $3\ce{NO2 + H2O \xlongequal{} 2HNO3 + NO}$ |
| 光化学烟雾   | 机动车尾气中的碳氢化合物和氮氧化物在光照条件下生成复杂的污染物                                                                                                                                                   |
| 臭氧空洞     | $\ce{NO2}$、氟氯代烷等与臭氧发生作用，导致了臭氧层的损耗                                                                                                                                                         |
| 水体污染     | 过度施用化肥和农药，工业“三废”和生活污水的随意排放，富营养化可引起“水华”或“赤潮”                                                                                                                                 |
| 温室效应气体 | 大量使用化石燃料导致大气中的 $\ce{CO2}$ 浓度增加，产生温室效应，导致地表温度上升                                                                                                                                 |


---

## Original file: index.md

---
description: 本章整理化学物质基本概念，涉及物质组成与分类、物质的量、离子反应、氧化还原反应、化学常识与 STSE 相关内容。
---

# 05 化学物质基本概念

<CCChapterOverview />


---

## Original file: 考点 离子方程式正误判断.md

---
description: "讲解离子方程式正误判断的要点，包括反应事实、守恒原则和符号使用。"
---

# 考点 · 离子方程式正误判断

## 一、注意是否符合反应事实

离子反应必须符合客观事实，而命题者往往设置不符合「反应原理」的陷阱

1. $\ce{Fe->[Cl_2、Br_2]Fe^{3+}}$ ；$\ce{Fe->[I_2、S、H_2(非氧化性酸)]Fe^{2+}}$ ；稀 $\ce{HNO3 +}\begin{cases}\ce{Fe(少量)->Fe^{3+}}\\u\ce{Fe(过量)->Fe^{2+}}\end{cases}\\$ ； $\ce{Fe(常温)}$ 与浓 $\ce{HNO3}$ 发生钝化

2. 金属和氧化性酸（如 $\ce{HNO3}$、浓 $\ce{H2SO4}$）反应不放 $\ce{H2}$

3. $\ce{Na}$ 不能置换出 $\ce{CuSO4}$ 溶液中的 $ \ce{Cu}$ （先与 $\ce{H2O}$ 反应生成 $\ce{NaOH}$ ）

4. 忽略氧化还原

   > 例如：$\ce{Na2\overset{-2}{S} +HNO3->H2S ^ +Na\overset{-2}{S}O3\qquad(×):\overset{-2}{S}}$ 有很强的还原性，遇到稀硝酸，一定会发生氧化还原反应

5. 忽略相互促进的水解反应（完全双水解）

   > 常见的双水解的离子：
   >
   > $\ce{Al^{3+}:HCO^-3、CO^{2-}3、HS- 、S^2- 、ClO- 、AlO^-2}$
   >
   > $\ce{Fe^{3+}:HCO^-3、CO^{2-}3 、ClO- 、AlO^-2}$
   >
   > $\ce{Fe^{2+}:AlO^-2、NH+4、SiO^{2-}3}$
   >
   > 例如：$\ce{Fe^{3+} +CO^{2-}3}$ 不会生成 $\ce{Fe2(CO3)3 v}$ ，因为会发生完全双水解，应生成 $\ce{Fe(OH)3 v +CO2 ^}$

6. 忽略络合反应

   > 三价铁离子和硫氰根离子反应：$\ce{Fe^{3+} +3SCN- -> Fe(SCN)3}$
   >
   > 铜离子遇到足量的浓氨水：$\ce{Cu^{2+} + NH3.H2O -> [Cu(NH3)4]^{2+}}$
   >
   > 银离子遇到足量的浓氨水：$\ce{Ag+ + NH3.H2O -> [Ag(NH3)2]+}$

## 二、注意是否满足 原子守恒、电荷守恒、电子得失守恒

检查配平、电子转移等是否正确

## 三、注意 $\xlongequal{}、\xrightleftharpoons{}、 \uparrow 、 \downarrow$ 是否使用恰当

1. 强电解质的电离（强酸、强碱、绝大多数盐）用「$\ce{=}$」；弱电解质的电离、盐类的水解用「$\ce{<=>}$」，盐类水解后的产物不写「$\downarrow$」或「$\uparrow$」；若两种离子相互促进水解，可以进行到底，则要写「$\xlongequal{}$」；可逆反应要用「$\xrightleftharpoons{}$」表示

   > $\ce{Mg^{2+} +2H2O<=>Mg(OH)2 v +2H+\qquad(×)}$
   >
   > $\ce{Mg^{2+}}$ 水解程度很弱，不足以形成沉淀，因此不标沉淀符号

2. 产物中形成胶体时应备注「（胶体）」，不可写「$\downarrow$」

   > $\ce{Fe^{3+} +3H2O\xlongequal{\Delta}Fe(OH)3(胶体) +3H+}$

3. $\ce{NH+4}$ 与 $\ce{OH-}$ 反应时，若条件为浓溶液或加热，生成 $\ce{NH3}$ 且要注明「$\uparrow$」；若为稀溶液，则生成 $\ce{NH3\cdot H2O}$

## 四、注意离子的拆分是否正确

1. 强酸（高中六大强酸：$\ce{HClO4、HI、HBr、HCl、HNO3、H2SO4}$）、可溶强碱（$\ce{NaOH、KOH、Ba(OH)2}$）、可溶性盐的化学式

   必须拆分，需要注意的是浓硝酸、浓盐酸的化学式可拆分，浓硫酸的化学式不拆分

2. 弱电解质（弱酸、弱碱、水等）、沉淀、气体、单质、弱酸的酸式酸根离子在离子方程式中都不能拆分成离子，氧化物在水溶液

   中不能拆分成 $\ce{O^{2-}}$ ；**且多元弱酸的多步电离只写第一步**

3. 对于微溶性的强电解质（如 $\ce{Ca(OH)2、CaSO4、MgCO3}$ 等），在反应物中是否拆分视情况而定

   > 澄清石灰水中 $\ce{Ca(OH)2}$ 以 $\ce{Ca^{2+}、OH-}$ 的形式存在，可拆成离子形式，但石灰乳为悬浊液，有大量未溶固体， $\ce{Ca(OH)2}$ 在离子方程式中不拆分。微溶物在生成物中一般不拆分，用化学式表示

4. 可溶性多元弱酸的酸式酸根离子（如 $\ce{HCO^-3、HSO^-3 、HS- 、HC2O^-4 、H2PO^-4、HPO^{2-}4}$ 等），一律保留酸式酸根离子的形式

   > 例如在水溶液中 $\ce{HSO^-3}$ 写成 $\ce{H+、SO^{2-}3}$ 是错误的。值得注意的是 $\ce{HSO^-4}$ 在水溶液中要拆分成 $\ce{H+、SO^{2-}4}$

## 五、注意是否漏写离子反应

判断离子方程式的书写正误时，要仔细审题，细心检查是否忽略了其他反应

> $\ce{CuSO4}$ 溶液和 $\ce{Ba(OH)2}$ 溶液反应：$\ce{Ba^{2+} +SO^{2-}4=BaSO4 v }\quad(×):$ 忽略了 $\ce{Cu^{2+} +2OH- =Cu(OH)2 v}$

## 六、注意是否符合反应的「量」

注意离子方程式是否符合题设条件的要求，如过量、少量、等物质的量、一定浓度和体积混合以及滴加顺序对反应产物的影响

### Ⅰ 与量有关的复分解反应

1. 向 $\ce{NH4Al(SO4)2}$ 溶液中滴 $\ce{Ba(OH)2}$ 溶液使 $\ce{SO^{2-}4}$ 恰好完全沉淀，离子方程式为：

   $\ce{NH+4 + Al^{3+} + 2SO^{2-}_{4 } + 2Ba^{ 2 + } + 4OH- = NH3\cdot H_{2}O + Al(OH)_{3} v + 2BaSO_{4} v }\quad (√)$

   > 1. 由 $\ce{SO^{2-}4 +Ba^{2+}=BaSO4 v}$ 进行配平得出由 $1$ 份 $\ce{NH4Al(SO4)2}$ 溶液 和 $2$ 份 $\ce{Ba(OH)2}$ 溶液
   > 2. 由 $\ce{Al^{3+} + 3OH- =Al(OH)3 v}$ 和 $\ce{NH^+4 +OH- =NH3\cdot H2O}$ 可知，优先反应 $\ce{Al^{3+}}$，生成 $1$ 份 $\ce{Al(OH)3}$
   > 3. 还剩余 $1$ 份 $\ce{OH-}$ ，与 $\ce{NH+4}$ 反应，生成 $1$ 份 $\ce{NH3\cdot H2O}$

2. 向 $\ce{NH4Al(SO4)2}$ 溶液滴入过量的 $\ce{NaOH}$ 溶液：$\ce{NH+4 +Al^3+ +5OH- =AlO^-2 +NH3\cdot H2O +2H2O}\quad (√)$

   > 1. 优先反应 $1$ 份 $\ce{Al^{3+} + 3OH- =Al(OH)3 v}$
   > 2. 其次反应 $1$ 份 $\ce{NH+4 +OH- =NH3\cdot H2O}$
   > 3. 最后反应 $1$ 份 $\ce{Al(OH)3 +OH- =AlO^-2 +2H2O}$

3. 向 $\ce{NH4Fe(SO4)2}$ 饱和溶液中滴加几滴（少量）$\ce{NaOH}$ 溶液：$\ce{Fe^3+ +3OH- =Fe(OH)3 v}\quad(√)$

   > 由 $\ce{NH+4 +OH- =NH3\cdot H2O}$ 和 $\ce{Fe^3+ +3OH- =Fe(OH)3 v}$ ，$\ce{Fe^3+}$ 优先反应

### Ⅱ $\ce{CO2}$ 少量与过量的比较

考虑反应物酸性与 $\ce{H2CO3、HCO^-3}$ 的酸性强弱比较

> 酸性大小：$\ce{H2CO3(CO2 +H2O)>HClO>Ph-OH>HCO^-3}$

1. 将少量的 $\ce{CO2}$ 通入 $\ce{NaClO}$ 溶液中：$\ce{2ClO- +CO2 +H2O =2HClO +CO^2-_3}\quad (×)$

   > 1. $\ce{H2CO3}$ 电离出的第一个 $\ce{H+}$ 用于制备 $\ce{HClO}$，$\ce{ClO- +CO2 +H2O =HClO +HCO^-3}$
   > 2. $\ce{HCO^-3}$ 电离出的 $\ce{H+}$ 无法制备次氯酸（ $\ce{ClO- +HCO^-3} \not=\ce{ HClO +CO^2-_3}$，弱酸不可制强酸）

2. 将少量的 $\ce{CO2}$ 通入苯酚钠溶液中：$\ce{2C6H5O- +CO2 +H2O =2C6H5OH +CO^2-_3}\quad (×)$

   > 1. $\ce{H2CO3}$ 电离出的第一个 $\ce{H+}$ 用于制备 $\ce{C6H5OH}$，$\ce{C6H5O- +CO2 +H2O =C6H5OH +HCO^-3}$
   > 2. $\ce{HCO^-3}$ 电离出的 $\ce{H+}$ 无法制备苯酚（ $\ce{C6H5O- +HCO^-3} \not=\ce{ C6H5OH +CO^2-_3}$，弱酸不可制强酸）

3. $\ce{Na2S}$ 溶液吸收少量 $\ce{CO2:S^2- +CO2 +H2O =CO^2-_3 +H2S ^}\quad(×)$

   [已知：$K_{a1}(\ce{H2CO3})> K_{a1}(\ce{H2S})> K_{a2}(\ce{H2CO3})$]

   > 1. 由 $K_{a1}(\ce{H2CO3})>K_{a1}(\ce{H2S})>K_{a2}(\ce{HS-})$ ，$\ce{H2CO3}$ 电离出的第一个 $\ce{H+}$ 可参与反应：
   >
   > $\ce{S^2- +CO2 +H2O =HS- +HCO^-3}$
   >
   > 2. 由 $K_{a1}(\ce{H2S})>K_{a2}(\ce{H2CO3})$ ，$\ce{HCO^-3}$ 电离出的 $\ce{H+}$ 不参与反应（$\ce{HS- +HCO^-3} \not=\ce{CO^2-_3 +H2S ^}$）

### Ⅲ $\ce{SO2}$ 的少量与过量

> $\ce{SO2}$ 的性质：
>
> 1. 酸性：$\ce{SO2 +H2O<=>H2SO3}$
> 2. 还原性：$\ce{\overset{+4}{S}O2->[氧化剂]\overset{+6}{S}O^2-_4}$
> 3. 氧化性：$\ce{\overset{+4}{S}O2 +H2\overset{-2}{S}->\overset{0}{S}}$

1. 用过量氨水吸收工业尾气中的 $\ce{SO2:2NH3\cdot H2O +SO2=2NH+4 +SO^2-_3 +H2O}\quad(√)$

   > 1. $\ce{SO2}$ 溶于水视为 $\ce{H2SO3}$
   > 2. 过量氨水中和 $\ce{H2SO3}$ 电离出的所有 $\ce{H+}$

2. 将过量的 $\ce{SO2}$ 通入次氯酸钠溶液中：$\ce{ClO- +SO2 +H2O=Cl- +SO^{2-}4 +2H+}\quad(√)$

   > 1. 少量的 $\ce{ClO-}$ 视为 $1$ 份，$\ce{SO2}$ 溶于水视为 $\ce{H2\overset{+4}{S}O3}$
   > 2. $\ce{ClO-}$ 为氧化剂，$\ce{H2SO3}$ 为还原剂

3. 将少量的 $\ce{SO2}$ 通入次氯酸钠溶液中：$\ce{ClO- +SO2 +H2O=Cl- +SO^{2-}4 +2H+}\quad(×)$

   > 1. $\ce{H+}$ 与 $\ce{ClO-}$ 不能共存，发生反应 $\ce{H+ +ClO- =HClO}$
   > 2. $\ce{SO2}$ 溶于水视为 $\ce{H2SO3}$
   >
   > 综上：$\ce{3ClO- +SO2 +H2O=Cl- +SO^{2-}4 +2HClO}$

4. 向 $\ce{Ba(ClO)2}$ 溶液中通入少量 $\ce{SO2:SO2 +Ba^2+ +2ClO- +H2O =BaSO3 v +2HClO}\quad(×)$

   > 1. $\ce{ClO^{-}}$ 将 $\ce{SO2}$ 氧化为 $\ce{SO4^{2-}}$：$\ce{SO2 + 3ClO^{-} + H2O \rightarrow SO4^{2-} + 3Cl^{-} + 2H^{+}}$
   > 2. $\ce{Ba^2+ +SO^{2-}4=BaSO4 v}$
   > 3. $\ce{H+ +ClO- =HClO}$
   >
   > 综上：$\ce{SO2 +3ClO- +Ba^2+ +H2O=BaSO4 v +Cl- +2HClO}$

5. 向过量 $\ce{SO2}$ 溶液通入 $\ce{K2S}$ 溶液：$\ce{2SO2 +2H2O +S^2- =2HSO^-3 +H2S}\quad(×)$

   > $\ce{\overset{+4}{S}O2 +H2\overset{-2}{S}->\overset{0}{S}}$


---



# Chapter 06 元素及其化合物

Source directory: `06 元素及其化合物`

## Original file: 01 钠及其化合物.md

---
description: "介绍钠单质的物理和化学性质、氧化钠和过氧化钠的性质、用途和反应。"
---

# 01 · 钠及其化合物

## 钠单质

### 化学性质

1. $\ce{Na}$ 与 氧气 反应：$\begin{cases}\ce{4Na +O2 \xlongequal{} 2Na2O\\2Na +O2 \xlongequal{点燃} Na2O2}\end{cases}\\$

2. $\ce{Na}$ 与 氯气 反应：$\ce{2Na +Cl2 \xlongequal{\Delta} 2NaCl}$

3. $\ce{Na}$ 与 硫 反应：$\ce{2Na + S \xlongequal{研磨或\Delta} Na2S}$ _爆炸性反应_

4. $\ce{Na}$ 与 水 反应：$\ce{2Na +2H2O = 2NaOH +H2 ^}$

   > 现象：「浮熔游响红」
   >
   > 钠的密度比水小，会 **浮** 在水面上；反应时，钠迅速 **熔** 化成小球（说明反应剧烈、大量放热、钠熔点偏低）；产生的氢气推动钠在水面上 **游** 动；发出 **响** 声；滴加酚酞后变 **红**

5. $\ce{Na}$ 与 $\ce{CuSO4}$ 水溶液 反应：$\begin{cases}\text{First}&\ce{2Na +2H2O \xlongequal{} 2NaOH +H2 ^}\\\text{Second}&\ce{2NaOH +CuSO4 \xlongequal{} Cu(OH)2 v + Na2SO4}\end{cases}\\$

6. $\ce{Na}$ 与 乙醇 反应：$\ce{2C2H5OH +2Na->2C2H5ONa +H2 ^}$

   > 现象：钠沉于无水乙醇的底部（或因产生的氢气使得钠上下跳动），表面有气泡产生，慢慢消失；放出的气体可在空气中安静地燃烧，火焰呈淡蓝色（$\ce{H2}$）；烧杯壁上有水珠生成；澄清石灰水未变浑浊（无 $\ce{CO2}$ ）
   >
   > 解释：由于烷基具有推电子作用（$\vec{\ce{CH3CH2}}\ce{-O-H}$），使得 $\ce{O-H}$ 键极性变弱，因此反应不会很剧烈

7. $\ce{Na}$ 与 盐酸 反应：$\ce{2Na + 2HCl = 2NaCl +H2 ^ \uparrow}$

   > 现象：反应比与水更剧烈，快速产生大量气泡，甚至发生轻微爆鸣
   >
   > 解释：钠具有强还原性，能与酸剧烈反应置换氢气

8. $\ce{Na}$ 与 $\ce{FeCl3}$ 水溶液 反应：$\ce{6Na + 6H2O + 2FeCl3 = 2Fe(OH)3\downarrow + 6NaCl + 3H2\uparrow}$

   > 现象：浮熔游响+生成红褐色沉淀
   >
   > 解释：钠具有强还原性，与盐溶液反应生成碱和氢气

### $\ce{Na}$ 与其他物质反应产物总结

1. 钠 + 水/酸/盐溶液 → 都生成 $\ce{H2}$
2. 钠 + 酸：直接置换生成 $\ce{H2}$，反应最剧烈
3. 钠 + 盐溶液：不生成金属，只生成碱沉淀和 $\ce{H2}$
4. 钠 + 熔融盐：置换金属
5. 钠 + 非金属：生成化合物，体现还原性

### 知识点

1. 制取：$\ce{2\ce{NaCl}(熔融) \xlongequal{电解} 2\ce{Na} + \ce{Cl2} ^}$

2. 用途：钠、钾合金（液态）可用于原子反应堆的导热剂；冶炼某些金属（如钛金属）；用作电光源，制作高压钠灯

3. 密度：$\rho(\ce{H}_{2}\ce{O})>\rho(\ce{Na})>\rho($ 煤油 $)$（密封保存，通常保存在石蜡油或煤油中）

4. 金属钠着火时用细沙覆盖灭火，不得使用水或二氧化碳灭火器

## 氧化钠与过氧化钠

|                    |                       氧化钠（$\ce{Na2O}$）                        |                            过氧化钠（ $\ce{Na2O2}$ ）                            |
| :----------------: | :----------------------------------------------------------------: | :------------------------------------------------------------------------------: |
|       电子式       | <img src="./images/1.1.png" style="zoom: 15%;" /> （仅含有离子键） |   <img src="./images/1.2.svg" style="zoom: 45%;"/>（含有离子键和非极性共价键）   |
|  离子个数比 $^4$   |                      $\ce{Na+:O^{2-} = 2:1}$                       |                             $\ce{Na+:O^{2-}2 = 2:1}$                             |
|  化合物类型 $^1$   |                      离子化合物（碱性氧化物）                      |                      离子化合物（非碱性氧化物，为过氧化物）                      |
|     颜色、状态     |                             白色、固体                             |                                   淡黄色、固体                                   |
|      主要性质      |                        具有碱性氧化物的通性                        |                                具有强氧化性 $^2$                                 |
|       稳定性       |                 不稳定，加热生成 $\ce{Na2O2}$ $^3$                 |                                      较稳定                                      |
|     与 水 反应     |                 $\ce{Na2O +H2O\xlongequal{}2NaOH}$                 |  $\ce{2Na2\overset{-1}{O}_2 +2H2O\xlongequal{2e^-}4NaOH +\overset{0}{O}_2 ^}^5$  |
| 与 $\ce{CO2}$ 反应 |                $\ce{Na2O +CO2\xlongequal{}Na2CO3}$                 | $\ce{2Na2\overset{-1}{O}_2 +2CO2\xlongequal{2e^-}2Na2CO3 +\overset{0}{O}_2 ^}^5$ |
|        用途        |                      制取烧碱（$\ce{NaOH}$）                       |                              漂白剂、消毒剂、供氧剂                              |

> 1. 碱性氧化物与酸反应生成盐和水：$\ce{Na2O +2HCl\xlongequal{}2NaCl +H2O}$
>    （$\ce{Na2O2}$ 不是碱性氧化物：$\ce{2Na2O2 +4HCl\xlongequal{}4NaCl +2H2O +O2 ^}$）
> 2. $\ce{Na2O2}$ 具有强氧化性
>    - $\ce{Na2O2}$ 加入品红溶液中，在水中生成 $\ce{H2O2}$ ，利用其氧化性，使得品红溶液褪色
>    - 如将其加入滴加酚酞的水中，溶液会先变红，后褪色
>    - 与 $\ce{SO2}$ 反应：$\ce{Na2O2 + SO2 → Na2SO4}$
>    - 投入 $\ce{FeCl2}$ 溶液中生成 $\ce{Fe(OH)3}$ 沉淀
>    - 投入氢硫酸，氧化硫化氢成硫单质，溶液浑浊
>    - 氧化 $\ce{SO^2–_3}$ 成 $\ce{SO^2–_4}$
> 3. $\ce{Na->[O2]Na2O->[{O}2 +\Delta]Na2O2->[H2O]NaOH}$
> 4. 考点：$1 mol\space\ce{Na2O +Na2O2}$ 混合物的离子数为 $3N_A$ (两者各自的离子数均为$3N_A/mol$，因此合并后无影响)
> 5. 考点：$\ce{Na2O_2 +H2O}(g)\ce{ +CO2}(g)$ 反应产生 $1 mol\space\ce{O2}$，即转移了 $2mol\space e^-$
> 6. $\ce{Na2O2}$ 与某水溶液反应与 $\ce{Na}$ 类似
>
>    例如：$\ce{NaHCO3}$ 与 $\ce{Na2O2}$ 反应 $\begin{cases}\text{First}&\ce{2Na2O2 +2H2O\xlongequal{}4NaOH +O2 ^}\\\text{Second}&\ce{NaOH +NaHCO3\xlongequal{}Na2CO3 +H2O}\end{cases}\\$
>
>    总方程式：$\ce{4NaHCO3 +2Na2O2\xlongequal{}4Na2CO3 +2H2O +O2↑}$

## 碳酸钠与碳酸氢钠

|                            | 碳酸钠（ $\ce{Na2CO3}$ ）                   | 碳酸氢钠（ $\ce{NaHCO3}$ ）                                                                                                                                        |
| -------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 俗名                       | 纯碱、苏打                                  | 小苏打 （大苏打为$\ce{Na2S2O3}$，硫代硫酸钠）                                                                                                                      |
| 溶解度                     | 易溶于水                                    | 在水中溶解度比 $\ce{Na2CO3}$ 小 $^1$                                                                                                                               |
| 热稳定性 $^2$              | 稳定，受热难分解                            | 受热易分解：$\ce{2NaHCO3\xlongequal{\Delta}Na2CO3 +CO2 ^ +H2O}$                                                                                                    |
| 与酸反应                   | $\ce{Na2CO3->[H+]NaHCO3->[H+]CO2 ^}^3$      | $\ce{NaHCO3->[H+]CO2 ^}$                                                                                                                                           |
| 与 $\ce{CO2}$ 反应         | $\ce{Na2CO3 +CO2 +H2O\xlongequal{}2NaHCO3}$ | 不反应 $^4$                                                                                                                                                        |
| 与 $\ce{Ca(OH)2}$ 反应     | $\ce{Ca^2+ +CO^2-_3 \xlongequal{} CaCO3 v}$ | $\ce{NaHCO3}$ 少量：$\ce{HCO^-3 +OH- +Ca^2+ \xlongequal{} CaCO3 v +H2O}$<br>$\ce{Ca(OH)2}$ 少量：$\ce{2HCO^-3 +2OH- +Ca^2+ \xlongequal{} CaCO3 v + CO^2-_3 +2H2O}$ |
| 与 $\ce{CaCl2/BaCl2}$ 反应 | $\ce{Ca^2+ +CO^2-_3 \xlongequal{} CaCO3 v}$ | 不沉淀 （探究题可能会考其与浓/饱和$\ce{CaCl2}$的反应）                                                                                                             |
| 用途                       | 纺织，制皂(与油脂的皂化反应)，造纸，制玻璃  | 制药，烘培糕点                                                                                                                                                     |

> 1. 碳酸钠的溶解度比碳酸氢钠更大
>
>    > 使得向饱和 $\ce{Na2CO3}$ 溶液中通入 $\ce{CO2}$ ，会析出白色晶体
>
>    > 侯氏制碱法中，向饱和 $\ce{NaCl(aq)}$ 中依次通入 $\ce{NH3}$ 和 $\ce{CO2}$，溶液中存在 $\ce{NH+4 、Na+ 、Cl- 、CO^{2-}3 、HCO^-_3}$ ，其中 $\ce{NaHCO3}$ 最先析出(其比$\ce{NH4HCO3}$溶解度还要小，故析出)，加热析出 $\ce{NaHCO3}$ ，得到 $\ce{Na2CO3}$
>    >
>    > $\ce{NH3}$ 和 $\ce{CO2}$ 的顺序不能调换，因为 $\ce{CO2}$ 在 $\ce{NaCl(aq)}$ 的溶解度较低，通入 $\ce{NH3}$ 会使食盐水呈碱性，从而可大量吸收 $\ce{CO2}$ ，产生 $\ce{HCO^-3}$
>
> 2. 碳酸钠是白色粉末，碳酸氢钠是细小的白色晶体。实验表明，向碳酸钠中加入少量水后，碳酸钠结块变成晶体(水合)，并伴随着**放热**现象。向碳酸氢钠中加入少量水后，碳酸氢钠能溶解，并伴随着**吸热**现象
> 3. 碳酸钠和碳酸氢钠的溶液均显碱性，可用作食用碱或工业用碱。
> 4. 实验：比较碳酸钠与碳酸氢钠的热稳定性
>
>    碳酸钠在外层，温度高，碳酸氢钠在内层，温度低，$Ⅱ$ 的澄清石灰水变浑浊，更能证明碳酸钠的热稳定性强
>
> 5. 实验：辨别 $\ce{HCl}$ 和 $\ce{Na2CO3}$
>
>    互滴。如 $\ce{HCl}$ 逐滴滴入 $\ce{Na2CO3}$ 溶液中，开始时没有气泡，后来有；如 $\ce{Na2CO3}$ 逐滴滴入 $\ce{HCl}$ 溶液中，一开始就有气泡
>
> 6. 考点：除去 $\ce{CO2}$ 中的 $\ce{HCl}$

相互转化：$\ce{Na2CO3 \xrightleftharpoons[加入适量\ce{NaOH(aq)/NaHCO3(s)}或\Delta]{适量\ce{H+}/通入\ce{CO2}} NaHCO3}$

除杂：

1. 固体 $\ce{Na2CO3(NaHCO3)}:$ 加热至恒重
2. 水溶液 $\ce{Na2CO3(NaHCO3)}:$ 加适量 $\ce{NaOH}$溶液
3. 水溶液 $\ce{NaHCO3(Na2CO3)}:$ 通入足量 $\ce{CO2}$

### 鉴别

$$
物质\begin{cases}
液体&
\begin{cases}
沉淀法：加入\ce{BaCl2}溶液或\ce{CaCl2}溶液产生沉淀的是\ce{Na2CO3}\\
气体法：滴入稀盐酸，立即产生气泡的是 \ce{NaHCO3}\\
测 pH 法：用 pH 试纸测其相同浓度的稀溶液，pH 大的是 \ce{Na2CO3} 溶液
\end{cases}\\
固体&加热法: 产生使澄清石灰水变浑浊的气体的是\ce{NaHCO3}固体\\
\end{cases}
$$

## 焰色反应

物理变化，进行焰色反应应使用 **铂丝**（镍丝、无锈铁丝，三者均无焰色因此可用于蘸取待测液）。把嵌在玻璃棒上的金属丝在 **稀盐酸**（金属氯化物沸点低，易挥发 **不可用稀硫酸**） 里蘸洗后，放在酒精灯的火焰里灼烧，不同金属元素会使火焰变为各种颜色，这便是焰色反应。焰色反应的形成与原子光谱有关

| 离子 | $\ce{Li+}$ | $\ce{Na+}$ | $\ce{K+}$ | $\ce{Rb+}$ | $\ce{Cs+}$ | $\ce{Ca^{2+} }$ | $\ce{Sr^{2+} }$ | $\ce{Ba^{2+} }$ | $\ce{Cu^{2+} }$ |
| :--: | :--------: | :--------: | :-------: | :--------: | :--------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 焰色 |     红     |     黄     |    紫     |    紫红    |    紫红    |      橙红       |      洋红       |      黄绿       |       绿        |

> 1. 灼烧白色粉末，火焰呈黄色，证明原粉末中有 $\ce{Na+}$ ，无 $\ce{K+}$ $\quad(×)$
>
>    解析：能证明有 $\ce{Na+}$ ，但无法确定是否有 $\ce{K+}$，因为 $\ce{Na+}$ 的黄光会遮盖 $\ce{K+}$ 的微弱紫光，因此必须透过蓝色钴玻璃过滤黄光，观察是否有紫光
>
> 2. 在火焰上灼烧搅拌过某无色溶液的玻璃棒，火焰出现黄色，说明溶液中含有 $\ce{Na+}$ $\quad(×)$
>
>    解析：不能用玻璃棒做焰色实验，因为玻璃棒中含有 $\ce{Na2SiO3}$ ，其焰色会干扰实验


---

## Original file: 02 铁及其化合物.md

---
description: "介绍铁单质的物理和化学性质、与氧、酸的反应，以及铁的化合物的性质和应用。"
---

# 02 · 铁 $(\ce{Fe})$ 及其化合物

## 铁单质

### 物理性质

- 银白色固体(铁粉为黑色)，有金属性光泽

- 容易被磁铁吸引

- 地壳中含量居第四位

### 化学性质

铁元素性质活泼，有较强的还原性，主要化合价为 $+2$ 价和 $+3$ 价

1.  - $\ce{3Fe + 2O2 \xlongequal{点燃} Fe3O4}$
    - $\ce{2Fe + 3Cl2 \xlongequal{△} 2FeCl3}$
    - $\ce{Fe + S \xlongequal{\Delta} FeS}$

2.  与水反应
    - 铁在高温下与水蒸气反应：$\ce{3Fe + 4H2O(g) \xlongequal{高温} Fe3O4 + 4H2}$

3.  与酸反应
    - 与非还原性酸：$\ce{Fe + 2H+ \xlongequal{} Fe^2+ + H2 ^}$
    - 与少量稀硝酸：$\ce{3Fe + 8H+ + 2NO^-_3 \xlongequal{} 3Fe^2+ + 2NO ^ + 4H2O}$
    - 与过量稀硝酸：$\ce{Fe + 4H+ + NO^-_3 \xlongequal{} Fe^3+ + NO ^ + 2H2O}$
    - 常温下，铁遇到冷的浓硫酸或浓硝酸会钝化

      > 常考：对于特定比例的 $\ce{Fe}$ 与 $\ce{HNO3}$ 进行反应的方程式
      >
      > 1. 当比例大于等于 $3:8$ ，此时铁过量，生成物全部都是亚铁
      >
      >    $\ce{3Fe(过量) +8HNO3(稀) \xlongequal{} 3Fe(NO3)2 + 2NO↑ + 4H2O}$
      >
      > 2. 比例介于 $3:8$ 和 $1:4$ 之间，则会有部分二价铁继续被硝酸氧化成三价铁
      >
      >    $\ce{3Fe(NO3)2 +4HNO3(稀) \xlongequal{} 3Fe(NO3)3 + NO↑ + 2H2O}$
      >
      > 3. 比例小于等于 $1:4$ ，此时稀硝酸足量，铁单质全都被氧化成三价铁
      >
      >    $\ce{Fe +4HNO3(稀) \xlongequal{} Fe(NO3)3 + NO↑ + 2H2O}$

4.  与盐溶液反应
    - 置换反应：$\ce{Fe + Cu^2+ \xlongequal{} Fe^2+ + Cu}$
    - 与氯化铁溶液：$\ce{Fe + 2Fe^3+ \xlongequal{} 3Fe^2+}$

## 铁的氧化物

### 物理性质

| 名称     | 氧化亚铁 $\ce{FeO}$ | 氧化铁 $\ce{Fe2O3}$              | 四氧化三铁 $\ce{Fe3O4}$ |
| -------- | ------------------- | -------------------------------- | ----------------------- |
| 俗称     | -                   | 铁红                             | 磁性氧化铁              |
| 化合价   | $+2$                | $+3$                             | 一个 $+2$、两个 $+3$    |
| 物理性质 | 黑色粉末            | 红褐色粉末                       | 黑色磁性晶体            |
| 用途     | 制青砖              | 制红砖、炼铁、铝热剂、油漆、涂料 | 炼铁、作纳米材料        |

### 化学性质

1. 与非氧化性酸（盐酸 $\ce{HCl}$ ）反应：
   - 氧化亚铁 $\ce{FeO}$：$\ce{FeO + 2H+} \xlongequal{} \ce{Fe^2+ + H2O}$
   - 氧化铁 $\ce{Fe2O3}$：$\ce{Fe2O3 + 6H+} \xlongequal{} \ce{2Fe^3+ + 3H2O}$
   - 四氧化三铁 $\ce{Fe3O4}$：$\ce{Fe3O4 + 8H+} \xlongequal{} \ce{Fe^2+ + 2Fe^3+ + 4H2O}$

2. 与氧化性酸（过量稀硝酸 $\ce{HNO3}$ ）反应：
   - 氧化亚铁 $\ce{FeO}$：$\ce{3FeO + 10H+ +NO^-_3} \xlongequal{} \ce{3Fe^3+ +NO ^ + 5H2O}$
   - 氧化铁 $\ce{Fe2O3}$：$\ce{Fe2O3 + 6H+} \xlongequal{} \ce{2Fe^3+ + 3H2O}$
   - 四氧化三铁 $\ce{Fe3O4}$：$\ce{3Fe3O4 + 28H^+ +NO^-_3} \xlongequal{} \ce{9Fe^3+ +NO ^ + 14H2O}$

3. 与氧化性酸（少量稀硝酸 $\ce{HNO3}$ ）反应：
   - 氧化亚铁 稀硝酸具有强氧化性，会将 $\ce{Fe^2+}$ 氧化为 $\ce{Fe^3+}$ ，因此不论稀硝酸的量为多少都生成铁离子
   - 氧化铁 $\ce{Fe2O3}$：$\ce{Fe2O3 + 6HNO3 \xlongequal{} 2Fe(NO3)3 + 3H2O}$
   - 四氧化三铁 $\ce{Fe3O4}$：$3Fe_3O_4 + 28HNO_3 = 9Fe(NO_3)_3 + NO\uparrow + 14H_2O$

4. 与还原性酸（ 氢碘酸 $\ce{HI}$ ） 反应：
   - 氧化亚铁 $\ce{FeO}$：$\ce{FeO + 2H+} \xlongequal{} \ce{Fe^2+ + H2O}$
   - 氧化铁 $\ce{Fe2O3}$：$\ce{Fe2O3 + 6H+ +2I-} \xlongequal{} \ce{2Fe^2+ +I2 + 3H2O}$
   - 四氧化三铁 $\ce{Fe3O4}$：$\ce{Fe3O4 + 8H+ +2I-} \xlongequal{} \ce{3Fe^2+ +I2 + 4H2O}$

5. 与还原性物质（ $\ce{CO}$ ）反应：
   - 氧化亚铁 $\ce{FeO}$：$\ce{FeO + CO} \xlongequal{高温} \ce{Fe + CO2}$
   - 氧化铁 $\ce{Fe2O3}$：$\ce{Fe2O3 + 3CO} \xlongequal{高温} \ce{2Fe + 3CO2}$
   - 四氧化三铁 $\ce{Fe3O4}$：$\ce{Fe3O4 + 4CO} \xlongequal{高温} \ce{3Fe + 4CO2}$

## 铁的氢氧化物

### 物理性质

| 名称     | 氢氧化亚铁 $\ce{Fe(OH)2}$ | 氢氧化铁 $\ce{Fe(OH)3}$ |
| -------- | ------------------------- | ----------------------- |
| 颜色状态 | 白色固体                  | 红褐色固体              |
| 水溶性   | 难溶                      | 难溶                    |

### 化学性质

1. 与非氧化性酸（盐酸 $\ce{HCl}$ ）反应：
   - 氢氧化亚铁 $\ce{Fe(OH)2}$ ：$\ce{Fe(OH)2 + 2HCl} \xlongequal{} \ce{FeCl2 + 2H2O}$
   - 氢氧化铁 $\ce{Fe(OH)3}$ ：$\ce{Fe(OH)3 + 3HCl} \xlongequal{} \ce{FeCl3 + 3H2O}$

2. 与氧化性酸（稀硝酸 $\ce{HNO3}$ ）反应：
   - 氢氧化亚铁 $\ce{Fe(OH)2}$ ：$\ce{Fe(OH)2 + 2HNO3(少量) \xlongequal{} Fe(NO3)2 + 2H2O}$

     $\ce{3Fe(OH)2 + 10HNO3(过量) \xlongequal{} 3Fe(NO3)3 + NO ↑+ 8H2O}$

   - 氢氧化铁 $\ce{Fe(OH)3}$ ：$\ce{Fe(OH)3 + 3HNO3} \xlongequal{} \ce{Fe(NO3)3 + 3H2O}$

3. 与还原性酸（ 氢碘酸 $\ce{HI}$） 反应：
   - 氢氧化亚铁 $\ce{Fe(OH)2}$ ：$\ce{Fe(OH)2 + 2HI} \xlongequal{} \ce{FeI2 + 2H2O}$
   - 氢氧化铁 $2\ce{Fe(OH)3 + 6HI \xlongequal{} 2FeI2 + I2 + 6H2O}$

4. 稳定性
   - $\ce{Fe(OH)2}$ 不稳定，在空气中易被氧化

     $\ce{4Fe(OH)2 +O2 +2H2O \xlongequal{} 4Fe(OH)3}$

   - $\ce{Fe(OH)3}$ 不稳定（但较 $\ce{Fe(OH)2}$ 稳定），受热脱去结晶水分解

     $\ce{2Fe(OH)3 \xlongequal{\Delta} Fe2O3 +3H2O}$

5. 制备
   - $\ce{Fe(OH)2}$ ：$\ce{Fe^2+ + 2OH- \xlongequal{} Fe(OH)2 v}$

     （将含有除去氧气的吸有 $\ce{NaOH}$ 溶液的滴管插入到含 $\ce{Fe^2+}$ 的溶液中，防止被空气中的 $\ce{O2}$ 氧化）

   - $\ce{Fe(OH)3}$ ：$\ce{Fe^3+ + 3OH- \xlongequal{} Fe(OH)3 v}$

6. 转化

   $\ce{4Fe(OH)2 + O2 + 2H2O \xlongequal{} 4Fe(OH)3}$

## 铁盐与亚铁盐

### $\ce{Fe^2+}$

含有 $\ce{Fe^2+}$ 的溶液呈浅绿色，既有氧化性又有还原性

1. 氧化性：$\ce{Zn + Fe^2+ \xlongequal{} Fe + Zn^2+}$

2. 还原性：$\ce{Cl2 + 2Fe^2+ \xlongequal{} 2Fe^3+ + 2Cl^-}$

3. 特性：含有 $\ce{Fe^2+}$ 的盐溶液遇铁氰化钾 $\ce{K3[Fe(CN)6]}$ 生成蓝色沉淀

### $\ce{Fe^3+}$

含有 $\ce{Fe^3+}$ 的溶液呈黄色，有较强的氧化性

1. 氧化性
   1. 铁离子与铜（$\ce{Cu}$）的反应：$2 \ce{Fe^3+ + Cu \xlongequal{} 2 Fe^2+ + Cu^2+}$
   2. 铁离子与碘离子（$\ce{I^-}$）的反应：$\ce{2Fe^3+ + 2I^- \xlongequal{} 2Fe^2+ + I2}$
   3. 铁离子与硫离子（$\ce{S^2-}$）的反应：$\ce{2Fe^3+ + 3S^2- \xlongequal{} 2FeS + S v}$ ($\ce{Fe2S3}$很不稳定，会分解成FeS与S)

2. 特性：含有 $\ce{Fe^3+}$ 的盐溶液遇 $\ce{KSCN}$ 溶液 变成红色

### 常见的铁盐与亚铁盐

1. 三氯化铁 $\ce{FeCl3}$：棕黄色固体，一种常见的氧化剂，能与多种还原剂发生氧化还原反应，能回收废铜，刻制印刷电路板时作腐蚀液，其反应的离子方程式为 $\ce{2Fe^3+ + Cu \xlongequal{} 2Fe^2+ + Cu^2+}$

   > - 制备无水 $\ce{FeCl3}$：在 $\ce{HCl}$ 气氛中加热蒸干 $\ce{FeCl3}$ 溶液，抑制 $\ce{FeCl3 +3H2O<=>Fe(OH)3 +3HCl}$ 正移
   > - 制备 $\ce{Fe(OH)3}$ 胶体：向沸蒸馏水中滴入饱和 $\ce{FeCl3}$ 溶液并煮沸至溶液呈红褐色为止

2. 绿矾 $\ce{FeSO4\cdot 7H2O}$：一种重要的还原剂，可用作补血剂及植物的补铁剂

3. 高铁酸钾 $\ce{K2FeO4}$ ：暗紫色晶体，具有强氧化性，极易溶于水呈浅紫红色溶液，与水反应生成的$\ce{Fe(OH)3}$胶体有吸附作用，可用作水处理剂 其也可作高能电池

4. 铁铵矾 $\ce{NH4Fe(SO4)2·12H2O}$ ：无色晶体，易溶于水，常用作化学分析试剂药物和织物媒染剂

5. 赤血盐（铁氰化钾，三价铁检验二价铁） $\ce{K3[Fe(CN)6]}$ ：红色晶体，易溶于水，常用于检验 $\ce{Fe^2+}$ ，生成蓝色沉淀（滕氏蓝）

6. 拓展：黄血盐（亚铁氰化钾，与上方相反） $\ce{K4[Fe(CN)6]}$ ：柠檬黄色晶体，易溶于水，常用于检验 $\ce{Fe^3+}$ ，生成蓝色沉淀（普鲁士蓝，实际上与滕氏蓝化学组成相同，晶型不同使得颜色略有差异）

### 盐溶液保存

- $\ce{Fe^2+}$ 的盐溶液：加入少量铁粉，防止 $\ce{Fe^2+}$ 被氧化；加入少量对应的酸，抑制 $\ce{Fe^2+}$ 水解

- $\ce{Fe^3+}$ 的盐溶液：加入少量对应的酸，抑制 $\ce{Fe^3+}$ 水解

## $\ce{Fe^2+}$ 与 $\ce{Fe^3+}$ 的检验

1. 直接观察颜色
   - 含有 $\ce{Fe^2+}$ 的溶液呈浅绿色
   - 含有 $\ce{Fe^3+}$ 的溶液呈黄色

2. 利用显色反应
   - $\ce{KSCN}$ 溶液
     - 溶液变红色：$\ce{Fe^3+}$
     - 溶液不变色，加入 $\ce{HCl}$ / 氯水，变红色：$\ce{Fe^2+}$

   - 苯酚
     - 溶液呈紫色：$\ce{Fe^3+}$

3. 利用 $\ce{Fe(OH)3}$ 沉淀的颜色
   - $\ce{NaOH}$ 溶液
     - 红褐色沉淀：$\ce{Fe^3+}$
     - 生成白色絮状沉淀，白色沉淀变为灰绿色，最后变为红褐色：$\ce{Fe^2+}$

4. 利用 $\ce{Fe^3+}$ 的氧化性
   - $\ce{Cu}$ 片
     - 铜被腐蚀，溶液变为蓝(若为盐酸盐，会稍显绿色)色：$\ce{Fe^3+}$

   - 淀粉$\ce{-KI}$ 试纸
     - 变蓝：$\ce{Fe^3+}$

   - $\ce{H2S}$ 水溶液
     - 产生淡黄色沉淀：$\ce{Fe^3+}$

5. 利用 $\ce{Fe^2+}$ 的还原性
   - 溴水
     - 溴水褪色： $\ce{Fe^2+}$

   - $\ce{KMnO4}$ 溶液
     - 紫色褪去：$\ce{Fe^2+}$

6. 利用 $\ce{Fe^2+}$ 的特殊反应
   - $\ce{K3[Fe(CN)6]}$
     - 蓝色沉淀 $\ce{KFe[Fe(CN)6]}$ : $\ce{Fe^2+}$

## 铁及其重要化合物的转化

<img src="/06 元素及其化合物/images/2.1.svg"/>


---

## Original file: 03 铜及其化合物.md

---
description: "介绍铜单质的物理和化学性质、与酸和盐的反应，以及铜的氧化物的性质和反应。"
---

# 03 · 铜 $(\ce{Cu})$ 及其化合物

## 铜单质

### 物理性质

- 紫红色金属，有良好的延展性、导电性和热导性(导电性仅次于 $\ce{Ag}$)

### 化学性质

铜元素在化学性质上相对稳定，主要化合价为 $+1$ 价和 $+2$ 价

<img src="./images/3.1.png" style="zoom:33%;"/>

1. 与潮湿空气反应：$\ce{2Cu + O2 + H2O + CO2\xlongequal{} Cu2(OH)2CO3}$
2. 与非金属单质反应
   - $\ce{2Cu + O2 \xlongequal{\Delta}2CuO }$
   * $\ce{4Cu + O2 \xlongequal{\Delta} 2Cu2O}$
   * $\ce{Cu + Cl2 \xlongequal{\Delta} CuCl2}$
   * $\ce{2Cu + S \xlongequal{\Delta} Cu2S}$
3. 与酸反应
   - 与非还原性酸（盐酸 $\ce{HCl}$ ）：不反应
   - 与浓硫酸反应：$\ce{Cu + 2H2SO4(浓) \xlongequal{\Delta} CuSO4 + SO2 ^ + 2H2O}$
   - 与稀硝酸：$\ce{3Cu + 8HNO3(稀) \xlongequal{} 3Cu(NO3)2 + 2NO ^ + 4H2O}$
   - 与浓硝酸：$\ce{Cu + 4HNO3(浓) \xlongequal{} Cu(NO3)2 + 2NO2 ^ + 2H2O}$
4. 与部分盐反应
   - $\ce{Cu +2Ag+ \xlongequal{} 2Ag +Cu^2+}$
   - $\ce{Cu +2Fe^3+ \xlongequal{} 2Fe^2+ +Cu^2+}$

## 铜的氧化物

### 物理性质

| 名称   | 亚氧化铜 $\ce{Cu2O}$ | 氧化铜 $\ce{CuO}$ |
| ------ | -------------------- | ----------------- |
| 颜色   | 砖红色               | 黑色              |
| 化合价 | $+1$                 | $+2$              |

### 化学性质

1. 氧化亚铜 $\ce{Cu2O}$ 的性质
   - 与酸反应歧化：$\ce{Cu2O + 2H+ \xlongequal{} Cu^2+ +Cu + H2O}$
   - 与 $\ce{H2}$ 反应：$\ce{Cu2O + H2 \xlongequal{\Delta} 2Cu +H2O}$

2. 氧化铜 $\ce{CuO}$ 的性质
   - 与酸反应：$\ce{CuO + 2H+ \xlongequal{} Cu^2+ + H2O}$
   - 与 $\ce{H2}$ 反应：$\ce{CuO + H2 \xlongequal{\Delta} Cu +H2O}$

3. 相互转化

   $\ce{4CuO\xlongequal{高温}2Cu2O +O2 ^}$

## 氢氧化铜

含有 $\ce{Cu^2+}$ 的溶液呈蓝绿色

1. 不稳定性

   $\ce{Cu(OH)2\xlongequal{\Delta}CuO +H2O}$

2. 弱氧化性

   检验醛基：$\ce{CH3CHO + 2Cu(OH)2 + NaOH->[\Delta] CH3COONa + Cu_2O v +3H2O}$

3. 弱碱性

   与氨水反应：$\ce{Cu(OH)2 + 4NH3 \xlongequal{} [Cu(NH3)4]^{2+} + 2OH^-}$

## 铜盐

1. 碱式碳酸铜 $\ce{Cu2(OH)2CO3}$，也写作$\ce{CuCO3·Cu(OH)2}$ ：铜绿、孔雀石的主要成分。

   受热分解（$\ce{Cu2(OH)2CO3\xlongequal{\Delta}2CuO +CO2 ^ +H2O}$）

   可溶于稀硫酸（$\ce{Cu2(OH)2CO3 +4H+\xlongequal{}Cu^2+ +CO2 ^ +3H2O}$）

2. 硫酸铜 $\ce{CuSO4·5H2O}$：俗称蓝矾、胆矾，蓝色晶体。

   受热分解（$\ce{CuSO4·5H2O \xlongequal{\Delta} CuSO4 + 5H2O}$），转换为白色粉末。

   无水硫酸铜遇水变蓝，可用作水的检测试剂。

   高温下会分解：$\ce{CuSO4 \xlongequal{高温} CuO + SO3 \uparrow}$古代用此反应制硫酸

   需注意的是，$\ce{FeSO4}$ 的分解不同于此：$\ce{2FeSO4 \xlongequal{680℃} Fe2O3 + SO2 \uparrow + SO3 \uparrow}$

3. 铜盐溶液有毒，主要是因为 $\ce{Cu^2+}$ 作为一种重金属离子能与蛋白质作用，使蛋白质空间结构发生改变从而变性，因此人们利用了它的这一性质用胆矾、生石灰、水配成了波尔多液，用来杀灭植物的病菌


---

## Original file: 04 镁及其化合物.md

---
description: "介绍镁单质的物理和化学性质、与各种物质的反应，以及氧化镁和氢氧化镁的性质和应用。"
---

# 04 · 镁 $(\ce{Mg})$ 及其化合物

## 镁的性质

1. 物理性质：具有银白色金属光泽的固体，密度、硬度均较小，熔点较低，有良好的导电、传热和延展性

2. 化学性质
   - 与非金属单质反应
     - 与 $\ce{N2}$ 反应：$\ce{N2 +3Mg \xlongequal{点燃}Mg3N2}$
     - 与 $\ce{Cl2}$ 反应：$\ce{Cl2 +Mg \xlongequal{点燃}MgCl2}$
     - 与 $\ce{S}$ 反应：$\ce{Mg + S \xlongequal{\Delta} MgS}$
     - 与 $\ce{O2}$ 反应：$\ce{O2 +2Mg \xlongequal{点燃}2MgO}$（产生强烈白光）

   - 与 $\ce{CO2}$ 反应：$\ce{2Mg + CO2 \xlongequal{点燃} 2MgO + C}$（耀眼白光，黑色固体生成）
   - 与 $\ce{H2O}$ 反应：$\ce{Mg + 2 H2O\xlongequal{\Delta} Mg(OH)2 + H2 ^}$
   - 与 $\ce{H+}$ 反应：$\ce{Mg + 2H+\xlongequal{} Mg^2+ + H2 ^}$
   - 特别要注意，很少有金属能与$\ce{NaHCO3}$溶液发生反应，而镁可以：$\ce{4Mg + 8NaHCO3 + 4H2O -> 3MgCO3 \cdot Mg(OH)2 \cdot 3H2O + 4Na2CO3 + 4H2 ^ + CO2 ^}$

     > 镁在空气中燃烧时会同时与 $\ce{CO2、N2、O2}$ 反应

3. 工业制备 $\left\{\begin{array}{lr}\ce{Mg^2+ + 2OH- \xlongequal{} Mg(OH)2 v}\\\ce{Mg(OH)2 + 2HCl \xlongequal{} MgCl2 + H2O}\\\ce{MgCl2(l) \xlongequal{电解} Mg + Cl2 ^}\\\end{array}\right.$

4. 用途：生产合金，冶金工业上用作还原剂和脱氧剂

## 镁的重要化合物

氧化镁 $\ce{MgO}$ ，重要氧化物：$\ce{MgO + 2 H+ \xlongequal{} Mg^2+ + H2O}$

氢氧化镁 $\ce{Mg(OH)2}$

1.  中强酸：$\ce{Mg(OH)2 +2H+\xlongequal{} Mg^2+ +2H2O}$
2.  难溶于水：$\ce{Mg^2+ +2OH- \xlongequal{}Mg(OH)2 v}$
3.  **溶解度小于碳酸镁**：$MgCO_3(s) + 2OH^- \rightarrow Mg(OH)_2(s) + CO_3^{2-}$

    例：向$\ce{Mg(HCO3)2}$溶液中加入$\ce{Ca(OH)2}$溶液：

    **加入少量**：$Mg^{2+} + 2HCO_3^- + Ca^{2+} + 2OH^- \rightarrow CaCO_3\downarrow + MgCO_3\downarrow + 2H_2O$

    **加入过量**：$Mg^{2+} + 2HCO_3^- + 2Ca^{2+} + 4OH^- \rightarrow Mg(OH)_2\downarrow + 2CaCO_3\downarrow + 2H_2O$

> 1. $\ce{MgO}$ 熔点很高，可作耐火材料
> 2. $\ce{Mg(OH)2}$ 为难溶于水的白色沉淀，常用 $\ce{NaOH}$ 溶液检验 $\ce{Mg^2+}$
> 3. 由于 $\ce{Mg(OH)2}$ 的溶解度比 $\ce{MgCO3}$ 的小，故水垢的主要成分是 $\ce{Mg(OH)2}$

## 海水中镁的提取

<img src="./images/4.1.png" style="zoom:33%;"/>

1. 制熟石灰：$\ce{CaCO3\xlongequal{高温}CaO +CO2 ^;CaO +H2O\xlongequal{}Ca(OH)2}$

2. 沉淀：$\ce{MgCl2 + Ca(OH)2\xlongequal{}Mg(OH)2 v + CaCl2}$ （有时候不写沉淀标也行… 具体看老师怎么说）

3. 酸化：$\ce{Mg(OH)2 + 2HCl=MgCl2 + 2H2O}$

4. 蒸发浓缩，冷却结晶：析出 $\ce{MgCl2·6H2O}$

5. 脱水：在 $\ce{HCl}$ 气流中使 $\ce{MgCl2·6H2O}$ 脱水制得无水氯化镁

   > $\ce{HCl}$ 气流用于抑制 $\ce{MgCl2}$ 的水解

6. 电解：电解熔融氯化镁制得镁：$\ce{MgCl2(熔融)\xlongequal{电解}Mg + Cl2 ^}$


---

## Original file: 05 铝及其化合物.md

---
description: "介绍铝单质的物理和化学性质、与酸碱的反应，以及氧化铝和氢氧化铝的性质和转化。"
---

# 05 · 铝 $(\ce{Al})$ 及其化合物

## 铝的性质

1. 物理性质：具有银白色金属光泽的固体，密度、硬度均较小，熔点较低，有良好的导电、导热性

2. 化学性质
   - 与非金属单质反应
     - 与 $\ce{O2}$ 反应：$\ce{4Al + 3O2 \xlongequal{点燃} 2Al2O3}$ 氧化铝熔点比铝高，因此在空气中加热铝至熔化可观察到铝被氧化铝薄膜“托着”而不滴落
     - 与 $\ce{Cl2}$ 反应：$\ce{2Al + 3Cl2 \xlongequal{\Delta} 2AlCl3}$
     - 与 $\ce{S}$ 反应：$\ce{2Al + 3S \xlongequal{\Delta} Al2S3}$
     - 与 $\ce{H2O}$ 反应：$\ce{2Al + 6H2O \xlongequal{} 2Al(OH)3 + 3H2 ^}$ 该反应可发生，但因铝表面致密的氧化层，反应开始很快后停止 而氢氧化钠可溶解 $\ce{Al(OH)3,Al2O3}$ ，因此可视为其促进反应右移（见下方方程式）

   - 铝在冷的浓硫酸或浓硝酸中钝化
   - 铝与强碱发生反应：$\ce{2Al + 2NaOH + 6H2O \rightarrow 2Na[Al(OH)4] + 3H2}$
   - 铝热反应：可以与 $\ce{FeO}、\ce{Fe2O3}、\ce{Fe3O4}、\ce{Cr2O3}、\ce{MnO2}、\ce{V2O5}$ 等氧化物反应。用于焊接金属、冶炼难溶金属$\left\{\begin{array}{lr}\ce{2Al + Fe2O3 ->[{高温}] Al2O3 + 2Fe}\\\ce{2Al + Cr2O3 ->[{高温}] Al2O3 + 2Cr}\\\end{array}\right.$

3. 制备：$\ce{2Al2O3(l) \xlongequal[冰晶石]{电解} 4Al + 3O2 ^}$

## 铝、氧化铝和氢氧化铝

$\ce{AlO^-2 <- [Al、Al2O3、Al(OH)3、Al^3+、AlO^-2]->Al^3+}$

### 与酸反应

- $\ce{2Al + 6H+ \xlongequal{} 2Al^{3+} + 3H2 ^}$（非氧化性酸）

- $\ce{Al2O3 + 6H+ \xlongequal{} 2Al^{3+} + 3H2O}$

- $\ce{Al(OH)3 + 3H+ \xlongequal{} Al^{3+} + 3H2O}$

### 与强碱反应

- $\ce{2Al + 2OH- + 2H2O \xlongequal{} 2AlO^-2 + 3H2 ^}$

- $\ce{Al2O3 + 2OH- \xlongequal{} 2AlO^-2 + H2O}$

- $\ce{Al(OH)3 + OH- \xlongequal{} AlO^-2 + 2H2O}$

### $\ce{Al(OH)3}$ 的电离

- $\ce{Al(OH)3 <=>[H2O] H+ + AlO^-2 + H2O}$

- $\ce{Al(OH)3 <=>[H2O] Al^{3+} + 3 OH-}$

### 铝离子

1. 与 $\ce{NaOH}$ 的相互滴加缓慢滴加并搅拌
   - 将$\ce{NaOH}$滴入$\ce{Al^{3+}}$溶液中
     1. 先出现白色沉淀：$\ce{Al^{3+} + 3OH- \xlongequal{} Al(OH)3 v}$
     2. 后沉淀消失：$\ce{Al(OH)3 + OH- \xlongequal{} AlO^-2 + 2H2O}$

   - 将$\ce{Al^{3+}}$滴入$\ce{NaOH}$溶液中
     1. 先无明显现象：$\ce{Al^{3+} + 4OH- \xlongequal{} AlO^-2 + H2O}$
     2. 后产生白色沉淀：$\ce{Al^{3+} + 3AlO^-2 + 6H2O \xlongequal{} 4Al(OH)3 v}$

2. 与氨水反应

   $\ce{Al^{3+} + 3 NH3*H2O \xlongequal{} Al(OH)3 v + 3NH4+}$

3. 双水解反应
   - $\ce{Al^{3+} + 3HCO^-3 \xlongequal{} Al(OH)3 v + 3CO2 ^}$
   - $\ce{Al^{3+} + 3CO^2-_3 + 3H2O \xlongequal{} Al(OH)3 v + 3HCO^-3}$
   - $\ce{Al^{3+} + 3AlO^-2 + 6H2O \xlongequal{} 4Al(OH)3 v}$
   - $\ce{2Al^{3+} + 3S^2- + 6H2O \xlongequal{} 2Al(OH)3 v + 3H2S ^}$
   - $\ce{AlO^-2 + NH4+ + H2O \xlongequal{} Al(OH)3 v + NH3 ^}$
   - $\ce{2Al^{3+} + 3SiO^2-_3 + 6H2O \xlongequal{} 2Al(OH)3 v + 3H2SiO3 v}$

### 偏铝酸根

1. 与强酸相互滴加，缓慢滴加并搅拌
   - 将$\ce{H2SO4}$滴入$\ce{AlO^-2}$溶液中
     1. 先出现白色沉淀：$\ce{AlO^-2 + H+ + H2O \xlongequal{} Al(OH)3 v}$
     2. 后沉淀消失：$\ce{Al(OH)3 + 3H+ \xlongequal{} Al^{3+} + 3H2O}$

   - 将$\ce{AlO^-2}$滴入$\ce{H2SO4}$溶液中
     1. 先无明显现象：$\ce{AlO^-2 + 4H+ \xlongequal{} Al^{3+} + 2H2O}$
     2. 后产生白色沉淀：$\ce{Al^{3+} + 3AlO^-2 + 6H2O \xlongequal{} 4Al(OH)3 v}$

2. 与碳酸反应

   立即生成 $\ce{Al(OH)3}$ 沉淀且不溶解。
   - $\ce{CO2}$过量：$\ce{AlO^-2 + 2H2O + CO2 \xlongequal{} Al(OH)3 v + HCO^-3}$
   - $\ce{CO2}$少量：$\ce{2AlO^-2 + 3H2O + CO2 \xlongequal{} 2Al(OH)3 v + CO^2-_3}$

3. 与铵盐溶液反应

   $\ce{NH4+ + AlO^-2 + H2O \xlongequal{} Al(OH)3 v + NH3 ^}$

### 氢氧化铝

#### 制备

- $\ce{Al^{3+} + 3 NH3*H2O \xlongequal{} Al(OH)3 v + 3NH4+}$

- $\ce{AlO^-2 + 2H2O + CO2 \xlongequal{} Al(OH)3 v + HCO^-3}$

- $\ce{Al^{3+} + 3AlO^-2 + 6H2O \xlongequal{} 4Al(OH)3 v}$

### 用途

1. $\ce{Al:}$ 铝合金，航空航天材料
2. $\ce{Al2O3:}$ 耐热材料；炼铝原料；刚玉（红宝石、蓝宝石）
3. $\ce{Al(OH)3:}$ 净水剂；制酸剂（治疗胃酸过多）；阻燃剂
4. 可溶性铝盐：净水剂（明矾：$\ce{KAl(SO4)2·12H2O}$）

## 铝及其重要化合物的转化

<img src="./images/4.3.svg" style="zoom: 25%;"/>

1. $\ce{2Al + 6H+ \xlongequal{} 2Al^3+ +3H2 ^}$

2. $\ce{2Al + 2OH- +2H2O \xlongequal{} 2AlO^-2 +3H2 ^}$ （记忆：4213，四个 2、一个 3）

3. $\ce{4Al + 3O2 \xlongequal{点燃} 2Al2O3}$

   $\ce{2Al + Fe2O3 \xlongequal{高温} Al2O3 + 2Fe}$

4. $\ce{2Al2O3(熔融) \xlongequal[冰晶石]{通电} 4Al + 3O2 ^}$

5. $\ce{2Al(OH)3 \xlongequal{\Delta} Al2O3 + 3H2O}$

6. $\ce{Al2O3 + 6H+ \xlongequal{} 2Al^3+ + 3H2O}$

7. $\ce{Al2O3 + 2OH- \xlongequal{} 2AlO^-2 + H2O}$

8. $\ce{Al(OH)3 + 3H+ \xlongequal{} Al^3+ + 3H2O}$

9. $\ce{Al^3+ + 3OH- \xlongequal{} Al(OH)3 v}$

10. $\ce{AlO^-2 + H+ +H2O \xlongequal{} Al(OH)3 v}$

11. $\ce{Al(OH)3 + OH- \xlongequal{} AlO^-2 + 2H2O}$

12. $\ce{AlO^-2 + 4H+ \xlongequal{} Al^3+ + 2H2O}$

13. $\ce{Al^3+ + 4OH- \xlongequal{} AlO^-2 + 2H2O}$

### 注：

> 氧化铝无法一步反应为氢氧化铝

> 由于教材版本差异，有 $\ce{AlO2}^{-}$ 和 $\ce{[Al(OH)4]^{-}}$ 两种写法，读者参阅时请注重自己手头的课本


---

## Original file: 06 氯与卤族元素.md

---
description: "介绍氯气的物理和化学性质、与氢气、金属、水的反应，以及卤族元素的通性。"
---

# 06 · 氯 $(\ce{Cl})$ 与卤族元素

## 氯 $\ce{Cl}$

### 氯气

#### 物理性质

**黄绿色** 气体，有刺激性气味，可溶于水(1体积的水溶解约2体积的氯气)，密度大于空气，沸点比气体高，易液化，有毒

闻氯气气味的方法：抽去盛氯气的集气瓶口处的毛玻璃片，用手掌在瓶口上方轻轻扇动，使(极)少量氯气飘进鼻孔

#### 化学性质

1. 氯气与氢气反应： $\ce{H2 + Cl2 \xlongequal{点燃} 2HCl}$

   > 实验操作：在空气中点燃氢气（点燃前要验纯），然后把导管伸入盛有氯气的集气瓶中。
   >
   > 实验现象：氢气在氯气中安静地燃烧，发出苍白色的火焰，瓶口出现白雾
   >
   > 工业制 $\ce{HCl}$ 时采用点燃法，工业浓 $\ce{HCl}$ 常显黄色，是因为含 $\ce{Fe^3+}$

2. 氯气与金属单质反应
   1. 与铁反应：$\ce{2Fe + 3Cl2 \xlongequal{\Delta} 2FeCl3}$

      > 反应现象：产生黄色火焰，棕褐色烟
      >
      > 与反应物的量无关（$\ce{Fe^3+->[Fe]Fe^2+}$ 只发生在氯化铁溶液中）
      >
      > 氧化性从高到低排列为：$\ce{Cl2}$ > $\ce{O2}$ > $\ce{S}$
      >
      > 1. $\ce{Cl2}$ 与 $\ce{Fe}$ 反应生成 $\ce{FeCl3}$
      > 2. $\ce{O2}$ 与 $\ce{Fe}$ 反应可以生成 $\ce{Fe3O4}$
      > 3. $\ce{S}$ 与 $\ce{Fe}$ 反应生成 $\ce{FeS}$

   2. 与铜反应：$\ce{Cu + Cl2 \xlongequal{\Delta} CuCl2}$

      > 反应现象：产生棕黄色烟

   3. 与钠反应：$\ce{2Na + Cl2 \xlongequal{\Delta} 2NaCl}$

      > 反应现象：产生大量白烟

3. 氯气与水反应：$\ce{Cl2 +H2O <=> HCl +HClO}$

   > 注意：该反应为可逆反应，且由于 $\ce{HClO}$ 为弱酸，**离子反应中不可拆**

4. 氯气与碱反应
   1. $\ce{Cl2}$ 与 $\ce{NaOH}$ 溶液

      $\ce{Cl2 + 2NaOH \xlongequal{} NaCl + NaClO + H2O}······①$

      > 应用：
      >
      > 1. 实验室吸收多余的 $\ce{Cl2}$
      > 2. 工业制漂白液、84 消毒液，有效成分为 $\ce{NaClO}$
      > 3. $\ce{NaClO}$的起效/失效方程式：$\ce{NaClO + H2O + CO2 \xlongequal{} NaHCO3 + HClO}$ 同时证明了次氯酸酸性比碳酸弱

      温度较高时会发生：

      $\ce{3Cl2 + 6NaOH \xlongequal{\Delta} 5NaCl + NaClO3 + 3H2O} ······②$

      上述①②方程式中$\ce{n(Na+)}$与$\ce{n(Cl^{-})}$之比均为$\ce{1:1}$，此结论可用于解Cl<sub>2</sub>与NaOH反应时各离子浓度/物质量的图像题

      同时，钾碱也能与氯气发生类似的反应，工业上利用$\ce{Cl2}$与浓$\ce{KOH}$的反应**②**制取较纯的$\ce{KClO3}$（欲实现KCl与KClO<sub>3</sub>的分离只需降温结晶）

   2. $\ce{Cl2}$ 与冷的石灰乳 $\ce{Ca(OH)2}$

      $\ce{2Ca(OH)2 + 2Cl2 \xlongequal{} CaCl2 + Ca(ClO)2 + 2H2O}$

      > 如果书写离子方程式，$\ce{Ca(OH)2}$ 不要拆开，其是以悬浊液存在的
      >
      > $\ce{Ca(ClO)2}$ 是漂白粉、漂白精的有效成分
      >
      > 起效/失效：$\ce{Ca(ClO)2 + CO2 +H2O \xlongequal{} CaCO3 + 2HClO}$ $\ce{2HClO\xlongequal{光照}2HCl +O2 ^}$

5. 氯气与还原性无机化合物反应
   1. $\ce{Cl2 + 2FeCl2 \xlongequal{} 2FeCl3}$（除去 $\ce{FeCl3}$ 中的 $\ce{FeCl2}$）
   2. $\ce{Cl2 + H2S \xlongequal{} 2HCl + S}$（氧化性：$\ce{Cl2}$ > $\ce{S}$）
   3. $\ce{Cl2 + 2NaBr \xlongequal{} 2NaCl + Br2}$（用于海水提取溴）
   4. $\ce{Cl2 + 2KI \xlongequal{} 2KCl + I2}$（用于用 $\ce{KI -}$ 淀粉试纸检验 $\ce{Cl2}$）
   5. $\ce{Cl2 + SO2 + 2H2O \xlongequal{} 2HCl + H2SO4}$（失去漂白作用）
   6. $\ce{3Cl2 + 8NH3 \xlongequal{} 6NH4Cl + N2 ^}$（用浓氨水检查氯气管道是否漏气）

#### 实验室制备

<img src="./images/6.1.png" style="zoom: 30%;"/>

1. 原理：$\ce{MnO2 +4HCl(浓)\xlongequal{\Delta}MnCl2 +Cl2 ^ +2H2O}$（**不浓不热不反应**）

2. 装置：
   1. 分液漏斗：固液加热生成气体所需，用于调节浓盐酸滴入速率
   2. 饱和食盐水：降低 $\ce{Cl2}$ 对水的溶解性，减少损耗（$\ce{Cl2 +H2O <=>H+ +Cl- +HClO}$，氯化钠促进平衡逆移）；用于除 $\ce{HCl}$ 气体（氯化氢极易溶于水）
   3. 浓硫酸：用于除 $\ce{H2O}$ 蒸气
   4. 向上排空气法：氯气密度比空气大（或排饱和食盐水法）
   5. $\ce{NaOH}$ 水溶液：$\ce{2NaOH + Cl2 \xlongequal{} NaCl + NaClO + H2O}$

3. 验满：将湿润的 $\ce{KI -}$ 淀粉试纸靠近瓶口，若试纸立即变蓝，则证明氯气已经收集满

> 其他制备方法：
>
> 1. 直接将高锰酸钾溶液加入**浓盐酸**中制备，无需加热
>    反应原理：$\ce{2KMnO4 +16HCl(浓) \xlongequal{} 2KCl +2MnCl2 +5Cl2 ^ +8H2O}$
> 2. $\ce{KClO3 +6HCl(浓) \xlongequal{} KCl +3Cl2 ^ +3H2O}$
> 3. 84 消毒液与洁厕灵混用易引发中毒：$\ce{ClO- +Cl- +2H^+ \xlongequal{} Cl2 ^ +H2O}$

### 氯水

#### 新制氯水

1. 新制氯水的成分——三分四离（由大到小）
   - 分子：$\ce{H2O、Cl2、HClO}$
   - 离子：$\ce{H+、Cl- 、ClO- 、OH-}$

2. 性质

   |    成分     | 表现性质                | 实例                                                                                                                                                                                                                                                                                                         |
   | :---------: | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | $\ce{Cl2}$  | 黄绿色 <br>强氧化性     | $\ce{(\overset{-2}{S})H2S、HS- 、S^2-->[Cl2]S v}$<br>$\ce{(\overset{+4}{S})SO2、H2SO3 、HSO^-_3 、SO^2-_3->[Cl2]SO^2-_4 v}$ <br/> $\ce{SO2 +Cl2 +2H2O\xlongequal{}H2SO4 +2HCl}$<br>$\ce{2I- +Cl2\xlongequal{}I2 +2Cl- \quad 2Br- +Cl2\xlongequal{}Br2 +2Cl-}$<br>$\ce{2Fe^2+ +Cl2\xlongequal{}2Fe^3+ +2Cl-}$ |
   |  $\ce{H+}$  | 弱酸性                  | 与镁反应放出 $\ce{H2}$<br>与 $\ce{CaCO3}$ 反应放出 $\ce{CO2}$                                                                                                                                                                                                                                                |
   | $\ce{HClO}$ | 弱酸性 <br>**强氧化性** | 1. 漂白、杀菌、消毒 <br/> 2. $\ce{Cl2}$ 使湿润的有色布条褪色，不能使干燥的有色布条褪色，说明 $\ce{Cl2}$ 没有漂白性，而是 $\ce{HClO}$ 起漂白作用<br>3. 使紫色石蕊试剂先变红（$\ce{H+}$ 酸性作用），后褪色（$\ce{HClO}$ 氧化性作用）                                                                           |
   | $\ce{Cl-}$  | 沉淀反应                | $\ce{Ag+ +Cl- \xlongequal{}AgCl v}$                                                                                                                                                                                                                                                                          |

#### 久置氯水

1. 反应方程式：$\ce{2HClO \xlongequal{光照}2HCl +O2 ^}$

2. 成分：$\ce{HCl}$ 水溶液

3. 性质：有酸性（比新制氯水强），无氧化性、无漂白性

4. 实验室中氯水需 **现用现配**，且避光、密封保存在 **棕色试剂瓶** 中

> 液氯、新制氯水、久置氯水的比较
>
> |          | 液氯       | 新制氯水                                    | 久置氯水                  |
> | -------- | ---------- | ------------------------------------------- | ------------------------- |
> | 分类     | 纯净物     | 混合物                                      | 混合物                    |
> | 颜色     | 黄色       | 浅黄绿色                                    | 无色                      |
> | 性质     | 氧化性     | 酸性、氧化性、漂白性                        | 酸性                      |
> | 粒子种类 | $\ce{Cl2}$ | $\ce{Cl2、HClO、H2O、H+、Cl- 、ClO- 、OH-}$ | $\ce{H2O、H+、Cl- 、OH-}$ |
> | 保存     | 钢瓶       | 棕色试剂瓶                                  |                           |

### 氯离子的检验

> 借助 $\ce{AgCl}$ 沉淀来检验氯离子的存在，但需要排除碳酸根离子的干扰

1. 实验过程：在三支试管中分别加入 2~3mL 稀盐酸、$\ce{NaCl}$ 溶液、$\ce{Na2CO3}$ 溶液，然后各滴入几滴 $\ce{AgNO3}$ 溶液，观察现象。再分别加入少量稀硝酸，观察现象

2. 实验现象：

   | 物质               | 加入 $\ce{AgNO3}$ 溶液后  | 加入稀硝酸后   | 解释或离子方程式                                                                             |
   | :----------------- | :------------------------ | :------------- | :------------------------------------------------------------------------------------------- |
   | 稀盐酸             | 白色沉淀（$\ce{AgCl}$）   | 不溶解         | $\ce{Ag+ +Cl- \xlongequal{}AgCl v}$                                                          |
   | $\ce{NaCl}$ 溶液   | 白色沉淀（$\ce{AgCl}$）   | 不溶解         | $\ce{Ag+ +Cl- \xlongequal{}AgCl v}$                                                          |
   | $\ce{Na2CO3}$ 溶液 | 白色沉淀（$\ce{Ag2CO3}$） | 溶解并产生气泡 | $\ce{2Ag+ +CO^2-_3\xlongequal{}Ag2CO3 v}$<br>$\ce{Ag2CO3 +2H+\xlongequal{}2Ag+ +H2O +CO2 ^}$ |

3. 结论：

   待测液 $\ce{->[HNO3][酸化]}$ （排除 $\ce{CO^2-_3}$ 的干扰） $\ce{->[AgNO3]}$ 白色沉淀 $\ce{AgCl}$

## 卤族元素

### 相似性

1. 都能与大多数金属反应：$\ce{Fe->[F2/Cl2/Br2]Fe^3+;Fe->[I2]Fe^2+}$

2. 都能与 $\ce{H2}$ 反应：$\ce{H2 +X2\xlongequal{}2HX}$

3. 都能与水反应：$\ce{H2O +Cl2/Br2/I2<=>HX +HXO;2H2O +2F2<=>4HF +O2}$

4. 都能与碱液反应：$\ce{2NaOH +Cl2/Br2/I2\xlongequal{}NaX +NaXO +H2O;2F2 +4NaOH\xlongequal{}4NaF +2H2O +O2}$

### 递变性

颜色：$\ce{F2(浅黄绿色)->Cl2(黄绿色)->Br2(深红棕色)->I2(紫黑色)}$ 颜色加深

熔沸点：$\ce{F2(气体)->Cl2(气体)->Br2(液体)->I2(固体)}$ 逐渐升高

密度：$\ce{F2->Cl2->Br2->I2}$ 逐渐升高

水溶性：$\ce{F2(反应)->Cl2(溶解-反应)->Br2(溶解-反应)->I2(微溶,1g/3L水)}$ 逐渐降低

氧化性：$\ce{->[F2、Cl2、Br2、I2][与氢化合由易到难]}$ 逐渐减小

还原性：$\ce{->[F- 、Cl- 、Br- 、I-]}$ 逐渐增强

> 比较氧化性的方法：
>
> 1. 与氢气化合难易程度；
> 2. 氢化物的稳定性；
> 3. 最高价氧化物对应水化物的酸性；
> 4. 置换反应

### 特殊性

1. 氟 $\ce{F2}$
   1. 氟没有正价，是非金属性最强的元素，$\ce{F-}$ 的还原性最弱
   2. $\ce{F2}$ 与 $\ce{H2O}$ 反应生成 $\ce{HF}$ 和 $\ce{O2}$，$\ce{F2}$ 与 $\ce{H2}$ 在暗处即可爆炸反应
   3. $\ce{HF}$ 是弱酸，能腐蚀玻璃，应保存在铅制器皿或塑料瓶中；有毒；在卤素氢化物中，$\ce{HF}$ 的沸点最高（分子间存在较强氢键）

2. 溴 $\ce{Br2}$
   1. $\ce{Br2}$ 是深红棕色液体，易挥发
   2. $\ce{Br2}$ 易溶于有机溶剂
   3. 盛放液态溴时，试剂瓶需加水封，保存时不能用橡胶塞封口

3. 碘 $\ce{I2}$
   1. $\ce{I2}$ 遇淀粉变蓝色
   2. $\ce{I2}$ 加热时易升华（用于分离提纯 $\ce{I2}$）
   3. $\ce{I2}$ 易溶于有机溶剂
   4. 食盐中添加 $\ce{KIO3}$ 可预防和治疗甲状腺肿大

### 卤素离子的检验

1. $\ce{AgNO3}$ 溶液——沉淀法（注意$\ce{AgF}$可溶，因此此法不能检验氟离子）

   未知液 $\ce{->[稀硝酸]->[\ce{AgNO3} 溶液]} \ce{\begin{cases}白色沉淀&Cl- \\淡黄色沉淀&Br- \\黄色沉淀&I- \end{cases}}$

2. 置换——萃取法

   未知液 $\ce{->[适量新制饱和氯水][振荡]->[\ce{CCl4} 或 汽油][振荡]} 有机层 \ce{\begin{cases}橙色或橙红色&Br- \\紫色、浅紫色或紫红色&I- \end{cases}}$

3. 氧化——淀粉法检验 $\ce{I-}$

   未知液（无色）$\ce{->[适量新制饱和氯水][振荡]->[淀粉溶液][振荡]}$ 蓝色溶液 $\ce{\quad I-}$

### 海水资源的开发和利用

1. 海水淡化：蒸馏法、电渗析法、离子交换法

2. 海水制盐：氯碱工业

   $\ce{2NaCl +2H2O\xlongequal{电解}2NaOH +H2↑+Cl2↑}$

   $\ce{海水→粗盐->[制取]饱和食盐水->[电解]\ce{\begin{cases}阴极产物&Cl2 \\阳极产物&H2、NaOH \end{cases}}}$

3. 海水提溴

<img src="./images/6.2.png" style="zoom:25%;"/>

4. 海水提碘

<img src="./images/6.3.png" style="zoom:25%;"/>

**注意事项：**
①双氧水（稀硫酸用于酸化）**不可用**氯气代替：氯气会进一步氧化$\ce{I_2}$为$\ce{IO^-_3}$等
②海带灰中**硫酸盐、碳酸盐**等杂质在**萃取分液**时实现与$\ce{I_2}$分离
③萃取时上层液应无色；若仍显浅黄色，则可能是**萃取不完全或$\ce{H2O2}$偏少（$\ce{I2}$转化成了$\ce{I^-_3}$)**


---

## Original file: 07 氮及其化合物.md

---
description: "介绍氮气的物理和化学性质、氮的固定过程，包括自然固氮和人工固氮，以及氮的化合物如氨、硝酸等。"
---

# 07 · 氮 $(\ce{N})$ 及其化合物

## 氮气

氮分子内两个氮原子间以 **共价三键**（$\ce{N\equiv N}$）结合，断开该化学键需要较多的能量，所以氮气的化学性质很稳定，通常情况下难以与其他物质发生化学反应，无法被大多数生物体直接吸收

但在高温、放电条件下，氮分子获得了足够的能量，使断裂，氮气能够与镁、氧气、氢气等物质发生化合反应

### 物理性质

1. 无色、无味气体
2. 密度与空气相近
3. 难溶于水
4. 在高压下可液化

### 化学性质

1. 与 $\ce{O2}$ 反应： $\ce{N2 + O2 \xlongequal{放电} 2NO}$

2. 与 $\ce{Mg}$ 反应：

   $$
   \ce{N2 + 3Mg \xlongequal{点燃,800℃} \underset{\text{黄绿色}}{Mg3N2}}
   $$

   以上得到的产物水解： $\ce{Mg3N2 + 6H2O = 3Mg(OH)2 + 2NH3 ^}$

   > 镁在空气中燃烧，同时还生成了氧化镁

### 氮的固定

氮的固定：将大气中 **游离态** 的氮转化为氮的 **化合物** 的过程，包括 **自然固氮** 和 **人工固氮**。

1. 自然固氮：
   - 高能固氮：大自然通过闪电释放的能量将空气中的氮气转化为含氮的化合物（雷雨发庄稼）
     - $\ce{N2 + O2 \xlongequal{放电} 2NO}$
     - $\ce{2NO + O2 \xlongequal{} 2NO2}$
     - $\ce{3NO2 + H2O \xlongequal{} 2HNO3 + NO}$

   - 生物固氮：豆科植物的根瘤菌将氮气转化成氨

2. 人工固氮：工业合成氨

   原理：$\ce{N2 + 3H2 \xrightleftharpoons[铁基催化剂]{高温、高压} 2NH3}$ （哈伯法）

   > 1. 合成氨工业化，对人类社会的影响极为深远。以合成氨为基础的化肥工业对粮食增产的贡献率占 $50\%$ 左右，使人类免受饥荒之苦
   > 2. **化学氮肥主要包括铵态氮肥（主要成分 $\ce{NH+4}$）、硝态氮肥（主要成分 $\ce{NO^-_3}$）和有机氮肥（尿素 $\ce{CO(NH2)2}$）**
   >
   >    工业上用氨气和二氧化碳在一定条件下合成尿素，肥效高、易保存、使用方便，是目前使用量很大的一种氨肥

## 一氧化氮 与 二氧化氮

| 物理性质 | 一氧化氮 $\ce{NO}$ | 二氧化氮 $\ce{NO2}$ |
| :------- | ------------------ | ------------------- |
| 状态     | 无色、无味         | 红棕色、刺激性气味  |
| 毒性     | 有毒               | 有毒                |
| 溶解性   | 不溶于水           | 溶于水并与水反应    |

转化：$\ce{NO \xrightleftharpoons[H2O]{O2}NO2}$

> 因此，除去一氧化氮中的二氧化氮只需通过水的洗气瓶即可

### 一氧化氮 $\ce{NO}$

1. 化学性质
   - $\ce{2NO + O2 \xlongequal{} 2NO2}$
   - $\ce{4NO + 2H2O + 3O2 \xlongequal{} 4HNO3}$

     > $\ce{NO}$ 既有氧化性又有还原性

   - 尾气处理：混合 $\ce{O2}$ 通入 $\ce{NaOH}$ 溶液（先化为二氧化氮再处理）

2. 制备
   - 实验室制备：$\ce{3Cu +8HNO3(稀) \xlongequal{} 3Cu(NO3)2 +4H2O +2NO ^}$
   - 工业制备：$\ce{4NH3 +5O2 \xlongequal [\Delta]{催化剂} 4NO +6H2O}$

     > $\ce{NO}$ 的密度与空气接近，且易与空气中的氧气反应，因此只能用排水法收集 $\ce{NO}$

3. 用途

   制硝酸、人造丝漂白剂，具有改善心脑血管的作用

### 二氧化氮 $\ce{NO2}$

1. 化学性质：
   - 与水反应生成硝酸

     $\ce{3NO2 + H2O \xlongequal{} 2HNO3 + NO}$

     > 与水反应生成硝酸的实验：
     >
     > - 实验步骤：将充满 $\ce{NO2}$ 的试管倒立于盛有水的水槽中。当液面在试管中不再上升时，通过导气管通入少量 $\ce{O2}$，并停一会儿，等待液面上升；当液面停止上升时，仍有气体剩余，可再通入少量 $\ce{O2}$，这样反复操作几次，直到液体充满整个试管
     > - 实验现象：
     >
     >   充满 $\ce{NO2}$ 的试管，倒立于盛有水的水槽中，液体进入试管中，并慢慢上升到试管高度的 $2/3$；试管内气体由红棕色慢慢变为无色，剩余气体的体积为原气体体积的 $1/3$
     >
     >   当通入 $\ce{O2}$ 时，气体迅速由无色变为红棕色
     >
     >   液面继续上升，气体又变为无色
     >
     >   这样反复几次，最终几乎没有气体剩余，液体充满整个试管
     >
     > - 解释及结论：
     >   $\ce{3NO2 + H2O \xlongequal{} 2HNO3 + NO}$
     >
     >   $\ce{2NO + O2 \xlongequal{} 2NO2}$
     >
     >   总反应：$\ce{4NO + 2H2O + 3O2 \xlongequal{} 4HNO3}$

   - 与碱反应

     $\ce{3NO2 + H2O \xlongequal{} 2HNO3 + NO}$

     $\ce{NaOH +HNO3 \xlongequal{} NaNO3 +H2O}$

     $\ce{NO + NO2 + 2NaOH \xlongequal{} 2NaNO2 + H2O}$

     总反应：$\ce{2NO2 + 2NaOH \xlongequal{} NaNO2 + NaNO3 + H2O}$

   - 氧化性

     $\ce{NO2 +SO2 +H2O \xlongequal{} H2SO4 +NO}$

   - $\ce{NO2}$ 与 $\ce{N2O4}$ 相互转化

     $\ce{2\underset{红棕色}{NO2} \xrightleftharpoons{} \underset{无色}{N2O4}}$

     > 阿伏伽德罗常数题型常考

   - 尾气处理：$\ce{2NO2 +2NaOH \xlongequal{} NaNO3 +NaNO2 +H2O}$

2. 用途

   $\ce{NO2}$ 在化学反应和火箭燃料中作氧化剂，在工业上可以用来制取硝酸

3. 制备

   常用 $\ce{NO}$ 氧化或用浓 $\ce{HNO3}$ 与 $\ce{Cu}$ 作用来制取 $\ce{NO2}$ ，使用向上排空气法收集，也可用加热分解重金属硝酸盐来制得

   $\ce{2Pb(NO3)2 \xlongequal{\Delta} 2PbO +4NO2 ^ +O2 ^}$

   工业：$\ce{N2->[H2]NH3->[O2]NO->[O2]NO2}$

### 酸雨

1. 正常雨水由于溶解了二氧化碳，其 $\text{pH}$ 约为 5.6，而酸雨的 $\text{pH}<5.6$

2. 成因：主要是大气中的 $\ce{SO2}$ 和 $\ce{NO_x}$ 以及它们在大气中发生反应后的生成物溶于水形成的

<img src="./images/7.1.png"/>

3. 危害
   1. 直接损伤农作物，破坏森林和草原，使土壤、湖泊酸化
   2. 加速建筑物、桥梁、工业设备、运输工具及电缆的腐蚀

4. 人类活动对氮循环和环境的影响
   - 以一氧化氮和二氧化氮为主的氮氧化物是形成光化学烟零、雾霾及酸雨的一个重要原因。汽车尾气中的氮氧化物与碳氢化合物经紫外线照射发生反应形成的有毒烟雾，成为光化学烟雾
   - 为了预防和控制氮氧化物的污染，具体措施为安装汽车尾气净化装置。净化装置含有钯等金属元素催化剂，尾气通过净化装置后，其中的有害气体 $\ce{NO、CO}$ 转化为无害气体 $\ce{N2}$ 与 $\ce{CO2}$

## 氨

### 物理性质

1. 氨是无色、有刺激性气味的气体，密度比空气小

2. 氨很容易液化，液化时放热。液氨汽化时要吸收大量的热，使周围温度急剧降低，可用作制冷剂

3. 氨极易溶于水，在常温常压下，1 体积水大约可溶解 700 体积氨

### 喷泉实验

在干燥的圆底烧瓶里充满 $\ce{NH3}$ 用带有玻璃管和胶头滴管（预先吸入水）的橡胶塞塞紧瓶口。倒置烧瓶，使玻璃管插入盛有水的烧杯中（预先在水里滴入少量酚酞溶液）。打开弹簧夹，挤压胶头滴管，使水进入烧瓶

<img src="./images/7.3.png" style="zoom:33%;"/>

> - 酚酞用于验证：①氨气极易溶于水；②氨气溶于水呈碱性
> - 其他喷泉实验：
>
> | 气体       | 液体                  |
> | ---------- | --------------------- |
> | $\ce{NH3}$ | 水或稀 $\ce{H2SO4}$   |
> | $\ce{HCl}$ | 水或 $\ce{NaOH}$ 溶液 |
> | $\ce{Cl2}$ | $\ce{NaOH}$ 溶液      |
> | $\ce{CO2}$ | $\ce{NaOH}$ 溶液      |
> | $\ce{SO2}$ | $\ce{NaOH}$ 溶液      |
> | $\ce{H2S}$ | $\ce{NaOH}$ 溶液      |

### 化学性质

1. 可燃性

   $\ce{4NH_3 + 3O_2 \xlongequal{\Delta{或点燃}} 2N_2 + 6H_2O}$

2. 碱性（唯一的碱性气体）
   - $\ce{NH_3(g) + HCl(g) \xlongequal{} \underset{\text{白烟}}{NH_4Cl}(s)}$
   - $\ce{NH_3 + HNO3 \xlongequal{} NH_4NO3}$

     > 元素推断：某元素的气态氢化物与最高价氧化物对应水化物化合生成盐

   - $\ce{NH_3 + H_2O \xrightleftharpoons{} NH_3*H_2O \xrightleftharpoons{} NH_4^+ + OH^-}$

     > <img src="./images/7.2.png"/>

3. 还原性
   - 催化氧化：$\ce{4NH_3 + 5O_2 \xlongequal [\Delta]{Pt} 4NO + 6H_2O}$
   - $\left\{\begin{array}{lr} \ce{2NH_3 + 3Cl_2 \xlongequal{} N_2 + 6HCl}\\ \ce{8NH_3 + 3Cl_2 \xlongequal{} N_2 + 6NH_4Cl}\\ \end{array}\right.$
   - $\ce{2NH_3 + CuO \xlongequal{\Delta} 3Cu + N_2 + 3H_2O}$

### 实验室制备

原理：$\ce{Ca(OH)2 +2NH4Cl \xlongequal{\Delta} CaCl2 +2NH3 ^ +2H2O}$ （固固加热型）

收集方法：向下排空气法（导管伸入，接近试管底部）

验满方法：将湿润的红色石蕊试纸放在管口（或 将沾有浓盐酸的玻璃棒靠近瓶口，有白烟生成）

棉花（用水或稀硫酸浸湿）的作用：防止 $\ce{NH3}$ 与空气对流，同时吸收多余的 $\ce{NH3}$ ，防止污染空气

试管口略向下倾斜，防止产生的水蒸气冷凝回流炸裂试管

<img src="./images/7.4.png" style="zoom: 33%;"/>

> - 不使用 $\ce{NaOH}$ 与 $\ce{NH4Cl}$ 共热来制备，因为 $\ce{NaOH}$ 碱性过强，在加热条件下易腐蚀玻璃（玻璃耐酸不耐碱）
> - 不得直接加热 $\ce{NH4Cl}$ 来制备氨气，因为生成的 $\ce{HCl}$ 和 $\ce{NH3}$ 在瓶口遇冷重新化合为 $\ce{NH4Cl}$
> - 使用碱石灰来干燥氨气，不能用浓硫酸、$\ce{P2O5}$、无水 $\ce{CaCl2}$ 作干燥剂（$\ce{NH3}$ 与 $\ce{CaCl2}$ 反应生成 $\ce{CaCl2・8NH3}$）
>
>       <img src="./images/7.6.png" style="zoom:50%;"/>
>
> - 要防止倒吸
>
>       <img src="./images/7.5.png" style="zoom: 50%;"/>

> 其他实验方式
>
> <img src="./images/7.7.png" style="zoom:33%;"/>
>
> | 反应物                  | 原理                                                                                                                               |
> | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
> | 浓氨水+固体 $\ce{NaOH}$ | $\ce{NaOH}$ 溶于水放热，促使氨水分解，且 $\ce{OH-}$ 浓度的增大有利于 $\ce{NH3}$ 的生成                                             |
> | 浓氨水+固体 $\ce{CaO}$  | $\ce{CaO}$ 与水反应，使溶剂（水）减少；反应放热，促使氨水分解。<br> 化学方程式为：$\ce{NH3·H2O +CaO \xlongequal{} NH3 ^ +Ca(OH)2}$ |

## 铵盐

1. 铵盐大多是无色晶体，绝大多数的铵盐都易溶于水，易于被农作物吸收，因此广泛用于化肥中。

2. 铵盐受热容易分解：$\ce{NH4Cl \xlongequal{\Delta} NH3 ^ +HCl ^}$ （冷却后重新化合为 $\ce{NH4Cl}$，可借此来提纯 $\ce{NH4Cl}$ ）
   $\ce{NH4HCO3 \xlongequal{\Delta} NH3 ^ +CO2 ^ +H2O}$

   > 一般铵盐受热分解为氨气，但存在例外 :
   >
   > $\text{NH}_4\text{NO}_3 \xrightarrow[169℃]{\Delta} \text{N}_2\text{O}\uparrow + 2\text{H}_2\text{O}$
   > $4\text{NH}_4\text{NO}_3 \xrightarrow[230℃]{\Delta} 2\text{N}_2\uparrow + 2\text{N}_2\text{O} + 8\text{H}_2\text{O} + \text{O}_2\uparrow$
   > $5\text{NH}_4\text{NO}_3 \xrightarrow[300℃]{\Delta} 4\text{N}_2\uparrow + 2\text{HNO}_3 + 9\text{H}_2\text{O}$ $2\text{NH}_4\text{NO}_3 \xrightarrow[400℃+]{\Delta} 4\text{H}_2\text{O} + 2\text{N}_2\uparrow + \text{O}_2\uparrow$

3. 与碱反应会放出氨：$\ce{Ca(OH)2 +2NH4Cl \xlongequal{\Delta} CaCl2 + 2NH3 ^ +2H2O}$

由于铵盐具有受热易分解的性质，在储铵态氮肥时，应密封包装并放在阴凉通风处；施肥时，应将其埋在土中以保持肥效。铵盐能与碱反应，因此铵态氮肥不能与碱性物质如草木灰（$\ce{K2CO3}$）等混合施用。

### 铵根离子的检验

取少量固体样品或溶液于试管中，再加入**浓**的 $\ce{NaOH}$ 溶液，**加热**，产生能使 **湿润** 的红色石蕊试纸变蓝的气体（或将蘸有浓盐酸的玻璃棒靠近管口，有白烟产生），证明固体样品或溶液中含有 $\ce{NH+4}$

原理：$\ce{NH+4 +OH- \xrightleftharpoons{} NH3·H2O->[\Delta]NH3}$

## 硝酸

### 物理性质

硝酸是无色、易挥发（在空气中形成白雾）、有刺激性气味的液体

### 化学性质

1. 不稳定性

   反应方程式：$\ce{4HNO3 \xlongequal[或光照]{\Delta} 4NO2 ^ +O2 ^ +2H2O}$

   浓硝酸一般呈黄色，是由于硝酸分解产生的 $\ce{NO2}$ 溶于硝酸

   硝酸浓度越大越易分解，因此，浓硝酸应放入棕色瓶（避光）在阴凉处保存（避免受热分解），用玻璃塞而不能用橡皮塞（硝酸腐蚀橡皮）

2. 硝酸与金属的反应

   $$
   \begin{cases}

       \ce{Cu + 4HNO3({浓}) \xrightarrow{} Cu(NO3)2 + 2NO2 ^ + 2H2O}\\
      \ce{3Cu + 8HNO3({稀}) \xrightarrow{} 3Cu(NO3)2 + 2NO ^ + 4H2O}\\

    \end{cases}
   $$

   > 常温下，**浓硝酸或浓硫酸使铁、铝钝化**（铁、铝表面被氧化生成一层致密的氧化物薄膜，这层薄膜阻止了酸与内层金属的进一步反应）。**故常温下，可以用铁或铝制容器来盛装浓硝酸或浓硫酸**
   >
   > 随反应的进行，浓硝酸变稀（阿伏伽德罗常数题常考）

3. 浓硝酸在加热条件下，还能与木炭等非金属单质发生氧化还原反应

   $\ce{C +4HNO(浓) \xlongequal{\Delta} CO2 ^ +4NO2 ^ +2H2O}$

4. 硝酸的酸性：

   硝酸是一元强酸，具有酸的通性，能与碱性氧化物、碱、盐等反应

### 工业制备

原理：$\ce{N2\xrightarrow[(1)]{\ce{H2} }NH3\xrightarrow[(2)]{\ce{O2} }NO->[O2][(3)]NO2->[H2O][(4)]HNO3}$

1. $\ce{N2 + 3H2 \xrightleftharpoons[高温、高压]{催化剂} 2NH3}$

2. $\ce{4NH_3 + 5O_2 \xlongequal[\Delta]{Pt} 4NO + 6H_2O}$

3. $\ce{2NO + O2 \xlongequal{} 2NO2}$

4. $\ce{3NO2 + H2O \xlongequal{} 2HNO3 + NO}$

   > $\ce{NO}$ 可循环使用


---

## Original file: 08 硫及其化合物.md

---
description: "介绍硫单质的物理和化学性质、与氢、氧、金属的反应，以及硫酸的性质和应用。"
---

# 08 · 硫 $(\ce{S})$ 及其化合物

1. 游离态：硫单质俗称硫黄，主要存在于火山口附近或地壳的岩层中

2. 化合态：主要以 硫化物 和 硫酸盐 的形式存在

   |   黄铁矿    |    黄铜矿     |         生石膏          |         熟石膏          |           芒硝            |
   | :---------: | :-----------: | :---------------------: | :---------------------: | :-----------------------: |
   | $\ce{FeS2}$ | $\ce{CuFeS2}$ | $\ce{CaSO4 \cdot 2H2O}$ | $\ce{2CaSO4 \cdot H2O}$ | $\ce{Na2SO4 \cdot 10H2O}$ |

   > $\ce{S}$ 的常见化合价：$-2,-1,0,+1,+2,+3,+4,+6,+7,+8$ （无 $+5$ 价）

## 硫单质

### 物理性质

1. 色态：黄色晶体，质脆，易研成粉末

2. 溶解性：**难溶于水，微溶于酒精、乙醚，易溶于二硫化碳 $\ce{CS2}$** ，易溶于热煤油（化工题常考）

   > 因此二硫化碳可用于洗涤内壁附着硫单质的试管

   > 浓氢氧化钠溶液可以与硫单质反应：$\ce{3S + 6NaOH ->[\Delta] 2Na2S + Na2SO3 + 3H2O}$，也可用于除去S

### 化学性质

硫单质既表现 **氧化性** ，又表现 **还原性**

1. 与 $\ce{H2}$ 反应：$\ce{H2 +S\xlongequal{\Delta}H2S}$

   > 硫化氢，$\ce{H2S}$，臭鸡蛋味，有剧毒

2. 与 $\ce{O2}$ 反应：$\ce{O2 +S\xlongequal{点燃}SO2}$

   > 无论氧气是否过量，产物均为二氧化硫（三氧化硫只在特殊的催化条件下生成）。发出明亮的蓝紫色火焰

3. 与金属反应

   $\ce{Fe +S\xlongequal{\Delta} \overset{+2}{Fe}S}\newline \ce{2Cu +S\xlongequal{\Delta} \overset{+1}{Cu2}S}\quad$

   > $\ce{S}$ 的氧化性比 $\ce{F、Cl}$ 弱，只能生成金属的低价态；

   $\ce{Hg +S\xlongequal{} HgS}$

   > 用于覆盖实验室撒落的汞以处理汞。

## 硫酸

### 物理性质

纯硫酸是无色、黏稠的油状液体，沸点高、**难挥发**。常用的浓硫酸的质量分数是 $98\%$（物质的量浓度为 $18.4 mol/L$），密度 $1.84g/cm^3$

### 化学性质

1.  **难挥发性**：用于制备挥发性酸（如 $\ce{HCl、HNO3}$ ）

    $\ce{NaCl +H2SO4(浓)\xlongequal{\Delta}NaHSO4 +HCl ^}$

    $\ce{NaNO3 + H2SO4 (浓)\xlongequal{\Delta}NaHSO4 + HNO3↑}$

2.  **强酸性**

    制磷酸：$\ce{Ca3(PO4)2 +3H2SO4(浓)\xlongequal{}3CaSO4 +2H3PO4}$

        > 一般使用 $70\%$ 的浓硫酸，因为 $98\%$ 的浓硫酸氢离子浓度过小

3.  **吸水性**

    浓硫酸具有 **强烈的吸水能力** ，能 **吸收空气中的水分** ，甚至能 **吸收结晶水合物的水** ，故浓硫酸常用作 **干燥剂** ，干燥一些 **不与浓硫酸反应的气体** 。

    > 用浓 $\ce{H2SO4}$ 可干燥 $\ce{O2、H2、N2、CO2、Cl2、HCl、CO2、CO、CH4}$ 等气体，但不能干燥 $\ce{NH3、H2S(酸碱反应)、HI、HBr(氧化还原)}$ 等气体
    >
    > 运用：在乙酸乙酯的制备实验中，用浓硫酸吸水，促进反应正向移动，提高乙酸乙酯的产率

4.  **脱水性**

    浓硫酸具有很强的腐蚀性，能按氢、氧原子 $2:1$ 的比例脱去纸、棉布、木条等有机物中的氢、氧元素；浓硫酸具有强腐蚀性与脱水性有很大关系，如浓硫酸会使蓝色石蕊试纸先变红，后变黑（碳化）

    > 1. 蔗糖的脱水实验：$\begin{cases}First.&\ce{C12H22O11->[浓H2SO4]12C +11H2O}\\Second.&\ce{C +H2SO4(浓)\xlongequal{\Delta}CO2 ^ +2SO2 ^ +2H2O}\end{cases}\\$
    >
    > 既体现浓硫酸的 **脱水性** 又体现 **强氧化性**
    >
    > 2. 醇的消去反应：$\ce{C2H5OH->[浓 H2SO4][170°C]CH2=CH2 ^ +H2O}$

5.  **强氧化性**

    硫酸中的硫元素处于最高价态。**浓硫酸** 能与许多物质发生氧化还原反应，是常见的氧化剂
    - 与铜反应：$\ce{Cu +2H2SO4(浓)\xlongequal{\Delta}CuSO4 +SO2 ^ +2H2O}$

      > 不浓不热不反应

    - 与木炭反应：$\ce{C +H2SO4(浓)\xlongequal{\Delta}CO2 ^ +2SO2 ^ +2H2O}$

6.  其他
    - 在常温下，浓 $\ce{H2SO4}$ 与 $\ce{Fe、Al}$ 反应，生成了致密的氧化膜阻止金属与浓 $\ce{H2SO4}$ 接触，从而保护了金属。因此常温下可用 $\ce{Fe、Al}$ 制容器盛放浓 $\ce{H2SO4}$ ；浓 $\ce{H2SO4}$ 与 $\ce{Fe、Al}$ 可以反应，**浓 $\ce{H2SO4}$ 与 $\ce{Cu}$ 常温下不反应**
    - 金属单质或低价金属的盐与浓 $\ce{H2SO4}$ 反应时，浓 $\ce{H2SO4}$ 既显氧化性又显酸性（与铜反应

## 二氧化硫

### 物理性质

无色、有刺激性气味的有毒气体，密度比空气大，易溶于水（1 体积的水能溶解约 40 体积的二氧化硫），可用于杀菌消毒和防氧化（向葡萄酒中加入适量二氧化硫）

### 化学性质

**Ⅰ $\ce{SO2}$ 是 **酸性氧化物**，具有酸性氧化物的通性**

1. 与水反应：$\ce{\overset{+4}{S}O2 +H2O <=> H2\overset{+4}{S}O3}$

   > $\ce{H2SO3}$ 为二元酸；$\ce{SO2\sim H2SO3\overset{完全}{\sim} 2OH-}$
   >
   > $\ce{H2SO3}$ 为中强酸，$\ce{HSO^-_3}$ 电离大于水解，因此 $\ce{NaHSO3}$ 显酸性（$\ce{H3PO4}$ 同理）

2. 与碱反应：
   1. 少量 $\ce{SO2}$ 通入 $\ce{NaOH}$ 溶液：$\ce{SO2 +2OH- \xlongequal{}SO^2-_3 +H2O}$
   2. 过量 $\ce{SO2}$ 通入 $\ce{NaOH}$ 溶液：$\ce{SO2 +OH- \xlongequal{} HSO^-_3 }$

3. 制备：$\ce{Na2SO3 +H2SO4(浓) \xlongequal{} Na2SO4 +SO2 ^ +H2O}$

**Ⅱ $\ce{SO2}$ 既有氧化性，又有还原性，以还原性为主**

1. 还原性
   1. 二氧化硫在适当的温度并有催化剂存在的条件下，可以被氧气氧化，生成三氧化硫

      $\ce{2SO2 +O2 <=>[V2O5][\Delta]2SO3}$

      > 三氧化硫也是一种酸性氧化物，溶于水时与水发生剧烈反应，生成硫酸
      >
      > $\ce{SO3 +H2O\xlongequal{}H2SO4}$
      >
      > 应用：工业制备硫酸（接触法制硫酸）
      >
      > <img src="./images/8.1.png" style="zoom:50%;"/>
      >
      > 工业上一般以硫磺（ $\ce{S}$ ）或其它含硫物（如黄铁矿 $\ce{FeS2}$ ）为原料来制备硫酸。金属冶炼时产生的含二氧化硫废气经回收后也可用于制备硫酸
      >
      > $\ce{4FeS2 +11O2\xlongequal{高温}2Fe2O3 +8SO2}$ 或 $\ce{S +O2\xlongequal{点燃}SO2}$
      >
      > $\ce{2SO2 +O2 <=>[V2O5][\Delta]2SO3}$
      >
      > $\ce{SO3 +H2O\xlongequal{}H2SO4}$
      >
      > （一般工业上不用水吸收三氧化硫，而是使用98%浓硫酸，因为三氧化硫溶于水大量放热，水沸腾形成酸雾，酸雾随着气流离开，减少对三氧化硫的吸收效果）

   2. 能被 $\ce{H2O2、Cl2、Br2、I2、Fe^3+、KMnO4、HNO3、ClO-}$ 等强氧化剂氧化生成 $\ce{SO^2-_4}$
      - $\ce{SO2 +H2O2\xlongequal{}H2SO4}$
      - $\ce{SO2 +Cl2(Br2/I2) +2H2O\xlongequal{}H2SO4 +2HCl(HBr/HI)}$
      - $\ce{SO2 +2Fe^3+ +2H2O\xlongequal{}SO^2-_4 +2Fe^2+ + 4H+}$
      - $\ce{5SO2 +2MnO^-_4 +2H2O \xlongequal{} 2Mn^2+ +5SO^2-_4 +4H+}$

        > 二氧化硫不与浓硫酸反应，因为两者如果反应，会归中反应至+5 价，而+5 价的硫化物不稳定
        >
        > 因此，二氧化硫可以用浓硫酸干燥

2. 氧化性

   $\ce{SO2}$ 与 $\ce{H2S}$ 反应： $\ce{SO2 +2H2S\xlongequal{}3S +2H2O}$

   > $\ce{H2S}$ 已是最低价态，只能表现还原性，二氧化硫表现氧化性

3. 漂白性
   - $\ce{SO2}$ 具有漂白作用，能使 **品红溶液** 等有色物质褪色
   - 漂白的原理是 **$\ce{SO2}$ 与有色物质结合生成了不稳定的无色物质**，与其氧化性无关。**加热后又显红色**，是由于不稳定的无色物质又分解为原来的物质
   - $\ce{SO2}$ 能漂白品红、鲜花等有机色素，**不能漂白酸碱指示剂，如酚酞、石蕊等**
   - 工业上常用 $\ce{SO2}$ 来漂白纸浆、毛、丝、草帽辫等，还用于消毒、杀菌等

     > - 将 $\ce{SO2}$ 通入含酚酞的 $\ce{NaOH}$ 溶液中，溶液褪色，与其漂白性无关， $\ce{SO2}$ 溶于水形成 $\ce{SO^-_3}$ ，与 $\ce{NaOH}$ 中和，使得溶液由碱性变酸性，因此酚酞变色
     > - $\ce{SO2}$ 使溴水、高锰酸钾褪色，与其漂白性无关，是由于其 **还原性**

     > - **氯水的漂白原理与 $\ce{SO2}$ 不同**，氯水的漂白原理是 $\ce{Cl2}$ 与 $\ce{H2O}$ 反应后生成了 $\ce{HClO}$ 具有 **强氧化性**，将有色的物质氧化为无色的物质，**褪色后不能恢复原来的颜色**
     > - 将氯水与 $\ce{SO2}$ 混合，会使得漂白性消失（ $\ce{SO2 +Cl2 +2H2O\xlongequal{}H2SO4 +2HCl}$ ）

#### $\ce{SO2}$ 的实验室制备

1. 不加热型制备

   反应原理：$\ce{Na2SO3 +H2SO4(浓) \xlongequal{} Na2SO4 +SO2 ^ +H2O}$

   离子方程式：$\ce{SO^{2-}_3 +2H+ \xlongequal{} SO2 ^ +H2O}$

   > 一般使用 $75\%$ 的浓硫酸，$98\%$ 的浓硫酸氢离子浓度过小；但也不能过小，因为会导致反应速率慢、$\ce{SO2}$ 过多溶解在水中

2. 加热型制备

   $\ce{Cu +2H2SO4(浓) \xlongequal{\Delta} CuSO4 +SO2 ^ +2H2O}$ （不浓不热不反应）

   > 常考有关阿伏伽德罗常数问题，无法根据 $\ce{Cu}$ 的量判断实际生成的 $\ce{SO2}$ ，**因为浓硫酸浓度随反应降低而停止反应**

3. 干燥：使用浓 $\ce{H2SO4}$ 干燥（两者不反应）

4. 收集：密度比空气大，向上排空气法

5. 尾气处理：$\ce{NaOH}$ 溶液

### $\ce{SO3}$

1. 物理性质：**标况下为无色固体，常温下为无色液体**，熔点为 $16.8°\ce{C}$， 易升华，极易溶于水并放出大量热

2. 化学性质：
   1. 与水反应：$\ce{SO3 +H2O=H2SO4}$
   2. 与碱性氧化物反应

      $\ce{CaO +SO3 = CaSO4}$

      $\ce{Na2O +SO3 = Na2SO4}$

   3. 与碱反应：$\ce{SO3 +2OH- = SO^2-_4 +H2O}$
   4. 与某些盐溶液反应：$\ce{SO3 +Ba^2+ +H2O = BaSO4 v +2H+}$

      > 用于鉴别 $\ce{SO2}$ 与 $\ce{SO3}$ ：$\ce{SO2}$ 加入 $\ce{BaCl2}$ 溶液中无沉淀（类比$\ce{CO2}$

## 硫酸根离子的检验

1. 原理：在溶液中，$\ce{SO^2-_4}$ 可与 $\ce{Ba^2+}$ 反应，生成 **不溶于稀盐酸** 的白色 $\ce{BaSO4}$ 沉淀

   > 强酸根形成的沉淀往往难溶于强酸，例如 $\ce{BaSO4}$ 、 $\ce{AgCl}$ 不溶于盐酸、硝酸
   >
   > 拓展：$\ce{BaSO4 + H2SO4(浓) \xlongequal{} Ba(HSO4)2}$ 从而溶解 探究题可能考到

2. 操作方法
   1. 取少许待测液于洁净试管中，先加入足量稀盐酸酸化

      > $\ce{Ba^2+}$ 与 $\ce{SO^2-_4、CO^2-_3、SO^2-_3}$ 形成沉淀，$\ce{Ag+}$ 与 $\ce{Cl-}$ 形成沉淀；稀盐酸可排除 $\ce{CO^2-_3、SO^2-_3、Cl-}$ 的干扰

   2. 上一步后无明显现象（若有沉淀，则静置后取上层清液），滴加 $\ce{BaCl2}$ 溶液
   3. 若有白色沉淀产生，则说明待测液中含有 $\ce{SO^2-_4}$

      若无白色沉淀产生，则说明待测液中不含 $\ce{SO^2-_4}$

3. 注意事项
   - 不能只加入 $\ce{BaCl2}$ ，且盐酸和 $\ce{BaCl2}$ 的顺序不可以颠倒

     > 例如：待测液先加入 $\ce{BaCl2}$ ，发现白色沉淀，再加入稀盐酸，观察到沉淀不消失，不可判断是 $\ce{SO^2-_4}$
     >
     > 因为虽然排除了 $\ce{BaCO3}$ 和 $\ce{BaSO3}$ 的干扰，但也有可能是 $\ce{AgCl}$ （$\ce{HCl}$ 不会使 $\ce{AgCl}$ 沉淀消失）

   - 不可以引入硝酸根，例如不可以加 $\ce{HNO3}$ 酸化或是加 $\ce{Ba(NO3)2}$ 这是因为酸性环境下的 $\ce{NO3^{-}}$具强氧化性，将溶液中可能存在的亚硫酸根离子氧化成硫酸根，因而干扰检验

## 硫及其化合物的转化

<img src="./images/8.2.svg"/>

## 其他含硫化合物

1、$\ce{Na2S2O3}$ 硫代硫酸钠：俗称海波，大苏打；易溶于水，水溶液呈碱性

- 制备：$\ce{Na2CO3(aq) + SO2(g) = Na2SO3(aq) + CO2(g)}$

  $\ce{Na2SO3(aq) + S(s) \xlongequal{\Delta} Na2S2O3(aq), 需长时间煮沸}$

- 性质：
  1. 酸性条件下歧化：$\ce{S2O3^{2-} + 2H+ = S v + SO2 ^ + H2O}$
  2. 还原性：可被碘氧化(碘量法的原理)：$\ce{2S2O3^{2-} + I2 = S4O6^{2-}(连四硫酸根) + 2I-}$
     若用$\ce{Cl2}$作氧化剂，则可将其氧化为$\ce{SO4^{2-}}$
  3. 与氧气反应：$\ce{2Na2S2O3 + O2 = 2Na2SO4 + 2S}$
  4. 无氧条件下分解：$\ce{4Na2S2O3 \xlongequal{\Delta} 3Na2SO4 + Na2S + 4S}$

2、$\ce{Na2S2O4}$ 连二亚硫酸钠：俗称保险粉，具有强还原性；极易溶于冷水，不溶于乙醇

- 制备：无氧条件下用锌粉还原亚硫酸氢钠：$\ce{2NaHSO3 + Zn = Na2S2O4 + Zn(OH)2}$

- 性质：其可看作是$\ce{NaHSO3}$的还原产物，还原性强于$\ce{NaHSO3}$

  被潮湿空气氧化：$\ce{Na2S2O4 + O2 + H2O = NaHSO3 + NaHSO4}$

3、$\ce{Na2S2O5}$ 焦亚硫酸钠

- 制备：由$\ce{NaHSO3}$过饱和溶液脱水而成：$\ce{2NaHSO3 = Na2S2O5 +H2O}$
- 性质：
  1. 与酸反应生成$\ce{SO2}$：$\ce{Na2S2O5 + 2H+ = 2Na+ +2SO2 + H2O}$
  2. 强还原性：$\ce{Na2S2O5 + 2I2 + 3H2O = 2NaHSO4 + 4HI}$

4、$\ce{H2S2O7, also H2SO4 \cdot SO3}$ 焦硫酸：三氧化硫溶于浓硫酸，冷却结晶得到的产物

- 性质：与水反应生成硫酸：$\ce{H2S2O7 + H2O = 2H2SO4}$

5、$\ce{Na2S2O7}$ 焦硫酸钠：由$\ce{NaHSO4}$加热制得

- 制备：$\ce{2NaHSO4 \xlongequal{\Delta} Na2S2O7 + H2O}$
- 分解：$\ce{Na2S2O7 \xlongequal{\Delta} Na2SO4 + SO3 ^}$
- 用途：用作熔矿剂

6、$\ce{Na2S2O8}$ 过二硫酸钠

- 性质：阴离子中含一个过氧键($\ce{-O-O -}$)，性质类似于$\ce{H2O2}$，具有强氧化性
  1. 氧化性：$\ce{S2O8^{2-} + 2I- \xlongequal{\ce{Cu^{2+}}} 2SO4^{2-} + I2}$

     $\ce{5S2O8^{2-} + 2Mn2+ + 8H2O \xlongequal{\ce{Ag+}} 10SO4^{2-} + 2MnO4- + 16H+}$

  2. 不稳定，遇热易分解：$\ce{2Na2S2O8 \xlongequal{\Delta} 2Na2SO4 + 2SO3 ^ + O2 ^}$


---

## Original file: 09 硅及其化合物.md

---
description: "介绍硅单质的结构和性质、与非金属的反应，以及二氧化硅的结构、物理性质和化学性质。"
---

# 09 · 硅 $(\ce{Si})$ 及其化合物

## 单晶硅 $\ce{Si}$

1. 单晶硅的结构与金刚石的相似，为正四面体的立体网状结构。晶体中每个 $\ce{Si}$ 原子与其他 ${4}$ 个 $\ce{Si}$ 原子相连接
2. 单晶硅是带有金属光泽的灰黑色固体，熔点高、硬度大、有脆性，在常温下化学性质不活泼
3. 单晶硅的导电性介于导体和绝缘体之间，是良好的半导体材料

### 化学性质

1. **与非金属单质反应**
   - $\ce{Si + 2F2 \xlongequal{} SiF4}$
   - $\ce{Si + 4HF \xlongequal{} SiF4 ^ +2H2 ^}$
   - $\ce{Si + 2NaOH +H2O \xlongequal{} Na2SiO3 + 2H2 ^}$

     > $\ce{Si}$ 与 $\ce{Al}$ 都可以和 $\ce{NaOH}$ 反应生成 $\ce{H2}$，而且前者是非金属，后者是金属。在元素推断题中常出现

   - $\ce{Si + 2Cl2 \xlongequal{\Delta} SiCl4}$
   - $\ce{Si + O2 \xlongequal{\Delta} SiO2}$
   - $\ce{Si + C \xlongequal{高温} \underset{\text{金刚砂}}{SiC}}$

2. **与水反应**
   - 野外制氢：$\ce{Si + H2O + 2NaOH \xlongequal{} Na2SiO3 + 2H2 ^}$

## 二氧化硅 $\ce{SiO2}$

1. **结构**
   1. 杂化方式：$sp^3$ 杂化
   2. 在 $SiO_2$ 晶体中，每个硅原子均与 $4$ 个氧原子结合；每个氧原子与 $2$ 个硅原子结合
   3. 在 $SiO_2$ 晶体中硅原子与氧原子个数之比是 $1:2$
   4. 在 $SiO_2$ 晶体中，每个硅原子形成 $4$ 个共价键；每个氧原子形成 $2$ 个共价键
   5. 在 $SiO_2$ 晶体中，最小环为十二元环，有 $6$ 个硅原子和 $6$ 个氧原子
   6. 硅原子个数与 $Si-O$ 共价键个数之比是 $1:4$ ；氧原子个数与 $Si-O$ 共价键个数之比是 $1:2$
   7. $SiO_2$ 晶体中并不存在 $SiO_2$ 分子

2. **物理性质**
   - 硬度大、熔沸点高、常温下为固体、难溶于水、不导电

3. **化学性质**

   **$SiO_2$ 是一种酸性氧化物**
   1. 与强碱反应：
      $\ce{SiO2 + 2NaOH \xlongequal{} Na2SiO3 + H2O}$（装 $\ce{NaOH}$ 溶液不用玻璃塞）
   2. 与唯一一种能与之反应的酸———氢氟酸 反应：
      $\ce{SiO2 + 4HF \xlongequal{} SiF4 ^ + 2 H2O}$（腐蚀玻璃、玻璃雕花）
   3. 与碱性氧化物反应：氧化硅与碱性氧化物反应，不与水反应（与水反应产物为硅酸，是沉淀，阻止反应进行）
   4. 与碱性盐反应
      - $\ce{SiO2 + Na2CO3 \xlongequal{高温} Na2SiO3 + CO2 ^}$（制作玻璃）
      - $\ce{SiO2 + CaCO3 \xlongequal{高温} CaSiO3 + CO2 ^}$（造渣反应，炼铁时加入CaCO<sub>3</sub>将原料中的SiO<sub>2</sub>转化为炉渣，提高炼铁效率）
      - $\ce{Na2SiO3 + CaCl2 \xlongequal{高温} CaSiO3 + 2NaCl}$ 水溶液中也可发生此反应

   5. 与碳反应
      - $\ce{SiO2 + 2C \xlongequal{高温} Si + 2CO ^}$
      - $\ce{SiO2 + 3C \xlongequal{高温} SiC + 2CO ^}$

   6. SiO<sub>2</sub>的精炼
      1. $\ce{SiO2 + 4Mg \xlongequal{高温} Mg2Si + 2MgO}$
      2. $\ce{Mg2Si + 4HCl \xlongequal{} 2MgCl2 + SiH4 ^}$
      3. $\ce{SiH4 + 2O2 \xlongequal{} SiO2 + 2H2O}$（空气中自燃）

   7. 高纯硅(9N+)的制备
      1. $\ce{SiO2 + 2C \xlongequal{1800-2000^\circ C} Si + 2CO \uparrow}$
      2. $\ce{Si + 3HCl \xlongequal{300^\circ C} SiHCl3 + H2}$
      3. $\ce{SiHCl3 + H2 \xlongequal{1100^\circ C} Si + 3HCl}$

<img title="" src="./images/9.1.png" width="180">

## 硅酸 $\ce{H2SiO3}$

- 白色胶状沉淀

- 弱酸性

  不使酸碱指示剂变色，酸性小于碳酸

- 不稳定性

  $\ce{H2SiO3 \xlongequal{\Delta} SiO2 + H2O}$

- 硅酸浓度大时在水中易聚合形成透明、胶冻状的硅酸凝胶，硅酸凝胶经干燥脱水后得到多孔的硅酸干凝胶，成为“硅胶”

  **硅胶是多孔状，吸附水分子能力强，常用作（食品级）干燥剂，或作催化剂的载体**

- 向硅酸盐溶液中加入盐酸或通入 $\ce{CO2}$，可制得硅酸胶体（凝胶）或沉淀
  - $\ce{Na2SiO3 +2HCl \xlongequal{} H2SiO3(胶体) +2NaCl}$
  - $\ce{Na2SiO3 + CO2 + H2O \xlongequal{} Na2CO3 + H2SiO3 v}$

    > 制备硅酸的原理是“强酸制弱酸”，这一原理可用来设计酸性强弱比较的实验，如：证明盐酸 > 碳酸 > 硅酸
    >
    > <img src="./images/9.2.png" style="zoom:25%;"/>
    >
    > - $\ce{CaCO3 + 2HCl \xlongequal{} CaCl2 + H2O + CO2 ^}$ 证明酸性：盐酸 > 碳酸
    > - $\ce{NaHCO3}$ 饱和溶液用于除去 $\ce{CO2}$ 中的 $\ce{HCl}$，防止其进入试管中也反应生成硅酸而干扰实验
    > - $\ce{Na2SiO3 + CO2 + H2O \xlongequal{} Na2CO3 + H2SiO3 v}$ 证明酸性：碳酸 > 硅酸
    > - 注意：该实验不能用于验证非金属性 $\ce{Cl>C>S}$ ，用于其要用最高价氧化物对应的水化物的酸性强弱来比较

## 硅酸钠 $\ce{Na2SiO3}$

最简单的硅酸盐

1. 白色、可溶于水的粉末状固体，其水溶液俗称水玻璃、**泡花碱**，是一种矿物胶，有很强的粘合性（所以装 $\ce{NaOH}$ 溶液不用玻璃塞）
2. 可以与酸（盐酸、碳酸等）反应，生成硅酸凝胶
3. 用途：制备硅胶，作木材、纺织品的防腐剂、防火剂

<img src="./images/9.3.png" style="zoom:50%;"/>


---

## Original file: 10 金属材料与金属矿物开发.md

---
description: "介绍金属的存在形式、冶炼的实质和方法，包括电解法、高温热还原法和铝热反应，以及金属材料的开发。"
---

# 10 · 金属材料与金属矿物开发

## 金属冶炼

1. **金属的存在形式**

   金、铂等化学性质不活泼的金属，在自然界以游离态存在；化学性质较活泼的金属在自然界中以化合态存在

   > 金属活动性越强，人类开发、利用该金属的时间就越晚

2. **金属冶炼的实质**

   金属冶炼的过程就是把金属从化合态还原为游离态的过程

3. **金属冶炼的方法**

   $$
   化合态\ce{->[\underbrace{K、Ca、Na、Mg、Al}_{电解法}、\underbrace{Zn、Fe、Sn、Pb、Cu}_{高温热还原法}、\underbrace{Hg、Ag}_{热分解法}][金属活动性逐渐减弱、金属阳离子得电子能力逐渐增强]}游离态
   $$
   1. **电解法**

   $\ce{Na:2NaCl(熔融)\xlongequal{电解}2Na +Cl2 ^}$

   $\ce{Mg:MgCl2(熔融)\xlongequal{电解}Mg +Cl2 ^}$

   $\ce{Al:2Al2O3(熔融)\xlongequal[冰晶石]{电解} 4Al +3O2 ^}$ 冰晶石可溶解氧化铝以降低其熔点，使铝的冶炼更加经济2. **高温热还原法**

   高温下利用碳、二氧化碳、氢气、铝等还原剂将金属元素从化合物中还原出来
   - 焦炭还原法：$\ce{C +2CuO\xlongequal{高温}2Cu +CO2 ^}$
   - $\ce{H2}$ 还原法：$\ce{3H2 +WO3\xlongequal{\Delta}W +3H2O}$
   - 活泼金属还原法：$\ce{2Al +Fe2O3\xlongequal{高温}2Fe +Al2O3}$

     > **铝热反应**
     >
     > 应用：
     >
     > 1. 冶炼难溶的金属（如钒、铬、锰，金属活动性在铝之后）
     >
     >    $\ce{2Al +Cr2O3\xlongequal{高温}2Cr +Al2O3}$
     >
     > 2. 焊接钢轨等大截面钢材部件
     > 3. 军事上用作铝热弹
     > 4. 传统的烟火剂
     >
     > 实验要点：
     >
     > 1. 镁条：作引燃剂，燃烧放出热能量，引发铝热反应
     > 2. 氯酸钾：作助燃剂，受热放出氧气，以保证镁条的持续燃烧
     > 3. 沙子：承接熔融的铁水，防止损坏实验台

   - $\ce{CO}$ 还原法：$\ce{3CO +Fe2O3\xlongequal{高温}2Fe +3CO2}$

     > 高炉炼铁
     >
     > 1. 产生还原剂：$\ce{C +O2\xlongequal{点燃}CO2}$ 、 $\ce{CO2 +C\xlongequal{高温}2CO}$
     > 1. 还原铁矿石：$\ce{3CO +Fe2O3\xlongequal{高温}2Fe +3CO2}$
     > 1. 造渣（除去 $\ce{SiO2}$ ）：$\ce{CaCO3 \xlongequal{高温} CO2 +CaO}$ 、 $\ce{CaO +SiO2 \xlongequal{高温} CaSiO3}$
   3. **热分解法**

   $\ce{Hg:2HgO\xlongequal{\Delta}2Hg +O2 ^}$

   $\ce{Ag:2Ag2O\xlongequal{\Delta}4Ag +O2 ^}$ 4. **其他冶金方法**
   1. 湿法冶金：利用溶液中发生的化学反应冶炼金属

      $\ce{CuSO4 +Fe \xlongequal{} Cu +FeSO4}$

   1. 富集法：利用物理方法筛选、淘洗，适用于 $\ce{Pt、Au}$

## 无机工业流程

<img src="./images/原料.svg"/>


---

## Original file: index.md

---
description: 本章汇总常见元素及其化合物性质，涵盖钠、铁、铜、铝、氯、氮、硫、硅等重点元素及综合应用题型。
---

# 06 元素及其化合物

<CCChapterOverview />


---



# Chapter 07 化学实验

Source directory: `07 化学实验`

## Original file: 01 实验仪器.md

---
description: "介绍化学实验中的加热仪器如酒精灯、石棉网，以及可加热仪器如试管、蒸发皿、坩埚的使用方法和注意事项。"
---

# 01 · 实验仪器

## 加热仪器

### 酒精灯（酒精喷灯）

1. 酒精灯的火焰分为外焰、内焰和焰心，应使用酒精的外焰进行加热
2. 添加酒精时，不超过酒精灯容积的 $\frac{2}{3}$，不少于 $\frac{1}{4}$。
3. 绝对禁止向燃着的酒精灯里添加酒精，以免失火
4. 绝对禁止用酒精灯引燃另一只酒精灯
5. 用完酒精灯，必须用灯帽盖灭，不可用嘴去吹
6. 不要碰倒酒精灯，万一洒出的酒精在桌上燃烧起来，应立即用湿布扑灭

### 石棉网——石棉网是石棉铁丝网的简称

石棉网用于给玻璃仪器加热，石棉的隔热作用，可使受热均匀，防止玻璃仪器因局部过热而炸裂（现多用陶瓷纤维网代替）

> 注：组装而成的加热装置，见模块化装置中的“反应装置”一节
> 部分教材改为「陶土网」，请以实际教学为准

## 可加热仪器

**A. 可直接加热的仪器：试管、蒸发皿、坩埚、燃烧匙、硬质玻璃管**

| 直接加热的仪器 | 试管                           | 蒸发皿                                   | 坩埚                                     |                                              燃烧匙、硬质玻璃管                                              |
| -------------- | ------------------------------ | ---------------------------------------- | ---------------------------------------- | :----------------------------------------------------------------------------------------------------------: |
| 图片           | <img src="./images/1.2.jpg" /> | <img src="./images/clip_image004.jpg" /> | <img src="./images/clip_image006.jpg" /> | <img src="./images/clip_image008.jpg" /> <img src="./images/image-20230906200028674-1694001632562-28.png" /> |

注意：可直接加热，但不能骤冷（防止冷热不均炸裂，通常放在石棉网上冷却）

### 试管

1. 加入液体：

   若要加热，液体体积不能超过试管容积 $\frac{1}{3}$ ;若不要加热，则不能超过 $\frac{2}{3}$

   试管夹：应夹在离试管口 $\frac{1}{3}$ 处（中上部）

2. 加热时：试管外壁应擦干，先均匀受热，再集中加热，不可骤冷骤热，管口不准对着人
   1. 给固体加热时，管口应略向下倾斜。若是粉末，试管口应加棉花。

   2. 给液体加热时，应用酒精灯的外焰（外焰燃烧充分，温度高），并使试管跟桌面成 $45\degree$

3. 振荡试管时，应用拇指、食指、中指握住离试管口的 $\frac{1}{3}$ 处，用腕力振荡试管底部

> <img src="./images/clip_image002-1694000728695-8.jpg" />
>
> <img src="./images/clip_image007.jpg" /> <img src="./images/clip_image009.jpg" />

### 坩埚

耐高温，主要用于固体物质的高温灼烧

1. 相关仪器：配套使用的仪器有：泥三角，三脚架，酒精灯； 取放坩埚时必须使用：坩埚钳；

2. 坩埚的种类：瓷坩埚（常用）、氧化铝坩埚、石英坩埚、铁坩埚

3. 坩埚的选择：原则是不与添加的反应物发生反应；

> <img src="./images/clip_image006.jpg" />

### 蒸发皿

液体物质的蒸发、浓缩、结晶（常为瓷质）

1. 液体不超过其容量的 $\frac{1}{3}$ ，边加热边搅拌（防止局部温度过高，造成液滴飞溅）

2. 若为蒸发结晶：一般当有大量晶体析出时停止加热，靠余热将剩余液体蒸干

3. 若为冷却结晶：一般是加热到表面有晶膜出现时，停止加热，降温结晶，获得晶体

> <img src="./images/clip_image006-1694001077244-22.jpg" />

### 燃烧匙

常用于块状或粉末状固体在气体中的燃烧实验（如硫、磷、钠等）

伸入集气瓶作燃烧实验时，应由瓶口慢慢下移，以使反应完全

高温时为防止燃烧匙与反应物反应，可铺一层细沙

**B. 可垫陶土（石棉）网加热的仪器：烧杯、 锥形瓶、 烧瓶（圆底烧瓶、蒸馏烧瓶 ,三颈烧瓶）**

| 相关仪器 |                   烧杯                   |               圆底、平底烧瓶               |                   蒸馏烧瓶                   |                    锥形瓶                     |                   三颈烧瓶                    |
| :------: | :--------------------------------------: | :----------------------------------------: | :------------------------------------------: | :-------------------------------------------: | :-------------------------------------------: |
|   图片   | <img alt="烧杯" src="./images/7.7.png"/> | <img alt="锥形瓶" src="./images/7.8.png"/> | <img alt="圆底烧瓶" src="./images/7.9.png"/> | <img alt="蒸馏烧瓶" src="./images/7.10.png"/> | <img alt="三颈烧瓶" src="./images/7.11.png"/> |
|   特点   |                   敞口                   |                  管口较小                  |                   有支管口                   |                   管口较小                    |                    “三颈”                     |

注意：加热时需要垫石棉/陶土网，液体体积范围为容积的 $[\frac{1}{3},\frac{2}{3}]$

## 干燥用仪器（附干燥剂）

**干燥的目的：制备纯净干燥产物；提供无水环境，避免反应物/生成物/催化剂反应（如水解），影响实验**
| 相关仪器 | 适用干燥剂|注意事项|
|-----|-----|-----|
| **球形干燥管**| 无水氯化钙（固体颗粒）、碱石灰（固体颗粒）、硅胶、$\ce{P₂O₅}$ | 干燥剂应为颗粒状，避免使用粉末 |
| **U 型干燥管**| 无水氯化钙、碱石灰等固体干燥剂 |
| **洗气瓶** | 浓硫酸| 气体“长管进、短管出”

| 干燥剂         | 适用气体（举例）                                                          | 不适用气体（举例）                                           | 备注                     |
| -------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------ |
| **浓硫酸**     | $\ce{H₂}$、$\ce{O₂}$、$\ce{CO₂}$、$\ce{Cl₂}$、$\ce{SO₂}$（酸性/中性气体） | $\ce{NH₃}$、$\ce{H₂S}$、$\ce{HI}$、$\ce{HBr}$（碱性/还原性） | 强氧化性、酸性           |
| **无水氯化钙** | 多数气体（ $\ce{H₂}$、$\ce{O₂}$、$\ce{CO₂}$、$\ce{Cl₂}$ 等）              | $\ce{NH₃}$（会形成配合物）                                   | 中性，价格便宜，常用     |
| **碱石灰**     | $\ce{NH₃}$、中性气体（如 $\ce{H₂}$、$\ce{O₂}$）                           | $\ce{CO₂}$、$\ce{SO₂}$、$\ce{Cl₂}$（酸性气体）               | 碱性，常用于干燥氨气     |
| **硅胶**       | 多数气体，常用于干燥器保存试剂                                            | 无特殊限制（物理吸附）                                       | 可变色指示，可再生       |
| **五氧化二磷** | 酸性、中性气体（干燥效率极高）                                            | 碱性气体                                                     | 易潮解，操作较麻烦       |
| **氧化钙**     | $\ce{NH₃}$、中性气体                                                      | 酸性气体                                                     | 碱性，常用于制取干燥氨气 |


---

## Original file: 02 实验过程.md

---
description: "介绍化学实验的基本过程、仪器选择和组装、仪器的检验方法，以及通入气体和试剂填装的注意事项。"
---

# 02 · 实验过程

> **实验基本过程**
>
> 实验前：①仪器选择与组装；②仪器的检验；③通入气体；④试剂的填装；⑤点火
>
> 实验后：①先移走液面内部导管（防止倒吸液体进入装置）； ②关闭热源，停止反应； ③再停止通气（最后停止通气的常考目的：防止产物与空气接触） ④仪器的洗涤
>
> **五个考察点**
>
> 1. 仪器选择与组装：①仪器规格选择、②仪器组装
> 2. 仪器的检验：①检验是否漏水、②气密性检验
> 3. 通入气体：①通气到何时停止、②通气的作用
> 4. 试剂的填装：①试剂的取用、②试剂的存放
> 5. 仪器的洗涤：①洗涤方法、②洗涤完成标志、③常见洗涤方法

## 仪器选择和组装

### 仪器规格的选择

1. 各类瓶瓶罐罐中液体体积范围：
   1. 仪器不需加热时：占容积的 $[\frac{1}{3}，\frac{2}{3}]$
   2. 仪器需要加热时：占容积的 $[\frac{1}{3}，\frac{1}{2}]$

2. 量筒量取一定量的液体：应选取略大于所需液体体积的量筒。

### 仪器的组装

仪器组装：方向为“先下后上，从左到右”

> 模块化装置的安装放在第三节

## 仪器的检验

1. 检验是否漏水（检漏）

   检漏方法：向分液漏斗中加入少量水，检查旋塞处是否漏水； 将漏斗倒转过来，检查玻璃塞是否漏水

   （补充：在玻璃旋塞两端涂一薄层凡士林，插入塞窝转动，使之均匀，以防漏水）

2. 气密性检验

   无论采用哪种装置制取气体．在成套装置组装完毕、装入反应物之前，必须检验装置的气密性，以确保实验的顺利进行。装置气密性的检验，其原理通常是设法造成装置的不同部位有压强差，并产生某种明显的现象。在叙述上要注意细节描述的严密性

   |                         步骤                         |                                                       具体方法                                                       |
   | :--------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |
   | Step1：形成密闭/封闭的体系<br>（活塞、弹簧夹、液封） |                        关闭：止水夹夹住导管/关闭活塞；液封：导管末端浸入水中，加水至浸没导管                         |
   |         Step2：①制造压强差；②描述产生的现象          | ①微热法：用手焐热/酒精灯微热现象：加热气泡冒出，停止后倒吸水柱<br>②注水法：向漏斗注水现象：形成液柱不动/液滴无法滴下 |
   |           Step3：一段时间后，现象保持不变            |                                                          ——                                                          |

## 通入气体

1. 通气到什么时候为止
   1. 水面下的导管，产生稳定气泡时；
   2. xx 装置中充满 xx 气体（描述气体颜色特点）

2. 通气的作用：本质是各种方式去“赶跑”装置内原有气体

   | 阶段   | 通气作用                                                                                                                                                                                          |
   | :----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | 实验前 | 排除装置中的空气，以免与空气中的 xx 发生反应（$\ce{H}_{2}\ce{O}/\ce{CO}_{2}/\ce{O}_{2}$）                                                                                                         |
   | 实验中 | ①减小气体浓度，防止出现倒吸现象（特别是极易溶于水的气体）<br>②将 xx 气体充分排净/将气体赶入 xx 装置<br/>③提供惰性气体环境，防止反应物与空气反应<br/>④减少定量实验误差<br/>⑤增大压强，加快反应速率 |
   | 实验后 | 将气体全部吹入 xx 中充分吸收<br/>①防止残留装置中造成污染<br/>②减小定量实验的误差                                                                                                                  |

## 填装物质

### 试剂取用

<table>
<thead>
  <tr>
    <th></th>
    <th colspan="3">固体药物</th>
    <th colspan="3">液体药物</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>药瓶取用</td>
    <td>粉末</td>
    <td>块状</td>
    <td>定量</td>
    <td>少量滴加</td>
    <td>定量</td>
    <td>大量倾倒</td>
  </tr>
  <tr>
    <td>使用仪器</td>
    <td>药匙</td>
    <td>镊子</td>
    <td>托盘天平</td>
    <td>胶头滴管</td>
    <td>量筒或滴定管</td>
    <td>直接倾倒</td>
  </tr>
  <tr>
    <td>注意事项</td>
    <td colspan="3">固体加入试管时：一横二放三慢竖</td>
    <td colspan="2">竖直悬滴</td>
    <td>倾倒口对口<br>标签对手心</td>
  </tr>
</tbody>
</table>

### 试剂存放

 <img src="./images/2.1.png" style="zoom: 25%;"/>

## 仪器洗涤

1. 基本方法：
   1. 注入少量水振荡倒掉，冲洗外壁
   2. 若仍有污迹，用洗涤液处理后刷洗（洗涤液）
   3. 最后用蒸馏水冲洗。（滴定管还要润洗）

2. 洗净的标准：内壁附着一层均匀的水膜，既不聚成水滴，也不成股流下

3. 常考污渍的洗涤方法

   | 附着杂质 | 油污 | 银镜 | 硫磺、碘、磷  | $\ce{CuO}$     | 乙酸乙酯                           |
   | :------: | :--- | :--- | :------------ | :------------- | :--------------------------------- |
   | 选择试剂 | 碱液 | 硝酸 | $\ce{CS}_{2}$ | $\ce{HNO}_{3}$ | $\ce{NaOH}$（水解）或 酒精（互溶） |


---

## Original file: 03 常见实验.md

---
description: "介绍常见化学实验如制备氯气、氨气、氯化铁的原理、装置、操作和注意事项。"
---

# 03 · 常见实验

> [!TIP]
> 部分实验在前文已经提及，此处不再赘述。

> **物质制备类** （气体、无机物、有机物）：掌握试剂选择、反应原理、装置搭建、除杂干燥<br>
> **分离提纯类**（过滤、蒸发、蒸馏、萃取、分液、洗涤、干燥）：掌握操作要点、仪器选择、适用范围<br>
> **定量测定类**（滴定、量气、称重）：掌握误差分析、计算方法、操作规范<br>
> **性质探究类**（氧化还原、速率、平衡）：掌握控制变量、现象分析、原理推导<br>
> **离子检验 & 物质推断**：掌握试剂选择、现象判断、排除干扰<br>

## 粗盐提纯

**实验**：溶解 → 过滤 → 蒸发 → 除杂（$\ce{Ca^{2+}}$、$\ce{Mg^{2+}}$、$\ce{SO4^{2-}}$）

**试剂及作用**：

- $\ce{BaCl2}$ 溶液：除去粗盐中的 $\ce{SO4^{2-}}$
- $\ce{Na2CO3}$ 溶液：除去 $\ce{Ca^{2+}}$ 和过量的 $\ce{Ba^{2+}}$
- $\ce{NaOH}$ 溶液：除去 $\ce{Mg^{2+}}$
- 稀$\ce{HCl}$：除去过量的$\ce{OH-}$和$\ce{CO3^{2-}}$

**反应方程式**：

- $\ce{BaCl2 + Na2SO4 = BaSO4 v + 2NaCl}$
- $\ce{Na2CO3 + CaCl2 = CaCO3 v + 2NaCl}$；$\ce{Na2CO3 + BaCl2 = BaCO3 v + 2NaCl}$
- $\ce{2NaOH + MgCl2 = Mg(OH)2 v + 2NaCl}$
- $\ce{HCl + NaOH = NaCl + H2O}$；$\ce{Na2CO3 + 2HCl = 2NaCl + H2O + CO2 ^}$

**知识点**：

- 过滤操作需遵循“一贴、二低、三靠”的原则
- 除杂顺序：$\ce{BaCl2}$ → $\ce{Na2CO3}$ → $\ce{NaOH}$ → $\ce{HCl}$
- 蒸发：当出现大量固体时停止加热，利用余热蒸干剩余液体

**注意事项**：除杂时 $\ce{Na2CO3}$ 需在 $\ce{BaCl2}$ 之后加入（除去过量 $\ce{Ba^{2+}}$）；$\ce{HCl}$ 最后加入（除去过量 $\ce{OH-}$、$\ce{CO3^{2-}}$）；蒸发时玻璃棒不停搅拌，避免局部过热导致液体飞溅。

## 蒸馏 & 萃取分液

### （1）蒸馏（物理变化）

**考点**：适用对象、装置、操作
**试剂及作用**：碎瓷片/沸石：防止液体暴沸
**知识点**：

- 蒸馏适用于沸点不同的物质分离
- 温度计水银球需放在支管口处
- 冷凝水需“下进上出”，加入碎瓷片可防止暴沸
  **题型**：装置图判断、选择、操作改错
  **注意事项**：蒸馏时温度计水银球不能插入液面下；冷凝水“下进上出”保证冷凝充分；蒸馏烧瓶需垫 石棉网（部分教材改为「陶土网」，请以实际教学为准） 加热

### （2）萃取分液（物理变化）

**考点**：适用对象、萃取剂选择、分液操作
**试剂及作用**：$\ce{CCl4}$（四氯化碳）：萃取溴水/碘水中的 $\ce{Br2}$/$\ce{I2}$（萃取剂，与水不互溶、不反应，对 $\ce{Br2}$/$\ce{I2}$ 溶解度远大于水）
**知识点**：

- 可用 $\ce{CCl4}$ 萃取溴水或碘水中的 $\ce{Br2}$、$\ce{I2}$
- 分液操作时需先放出下层液体，再倒出上层液体
  **题型**：装置图判断、选择、操作改错
  **注意事项**：萃取剂不能与原溶剂互溶（如不能用酒精萃取碘水）；分液时下层液体从下口放出，上层液体从上口倒出，避免交叉污染；振荡分液漏斗后需放气。

## 一定物质的量浓度溶液配制

**知识点**：

- 配制步骤：计算 → 称量 → 溶解 → 冷却 → 转移 → 洗涤 → 定容 → 摇匀
- 所需仪器：容量瓶、烧杯、玻璃棒、胶头滴管、托盘天平/量筒
- 误差判断：俯视读数偏小，仰视读数偏大
  **注意事项**：溶解后的溶液需冷却至室温再转移至容量瓶（防温度过高影响容量瓶精度）；洗涤烧杯和玻璃棒 $2~3$ 次，洗涤液全部转移至容量瓶；定容时胶头滴管垂直悬空，不接触容量瓶内壁。

## 制备 $\ce{FeCl3}$

![image-20230924143606556](images/image-20230924143606556.png)

- A：$\ce{MnO2 + 4HCl(浓) \xlongequal{\Delta} MnCl2 + Cl2 ^ + 2H2O}$
- B（饱和食盐水）：吸收氯化氢气体
- C（浓硫酸）：除去氯气中的水分
- E： $\ce{FeCl3}$ 易升华，使用冷水使其变为固体，方便收集
- F（碱石灰）：Ⅰ尾气吸收；Ⅱ防止外界水蒸气进入

> $\ce{FeCl3}$ 水解程度较大（$\ce{FeCl3 + 3H2O <=> Fe(OH)3 + 3HCl}$），因此要注意不能使外界水蒸气进入，同时如果要制备 $\ce{FeCl3}$ 溶液时，应先将 $\ce{FeCl3}$ 固体溶于少量盐酸（使反应逆向移动），再加水稀释。

## 化学平衡移动（以 $\ce{FeCl3 + KSCN}$、$\ce{NO2}$ 二聚为例）

**试剂及作用**：

- $\ce{FeCl3}$ 溶液、$\ce{KSCN}$ 溶液：建立 $\ce{Fe^{3+} + 3SCN- <=> Fe(SCN)3}$ 平衡
- 浓 $\ce{HCl}$/$\ce{NaOH}$ 溶液：改变离子浓度
- $\ce{NO2}$ 球：建立 $\ce{2NO2 <=> N2O4}$ 平衡，热水/冷水改变温度

**反应方程式**：

- $\ce{Fe^{3+} + 3SCN- <=> Fe(SCN)3}$（血红色）
- $\ce{2NO2(g)}$（红棕色） $\ce{<=>}$ $\ce{N2O4(g)}$（无色） $\Delta H < 0$

**注意事项**：

- 探究单一变量时，需保证其他条件相同（如探究温度影响时，浓度、催化剂用量一致）
- 催化剂只改变反应速率，不影响平衡移动
- 观察现象时需及时记录，避免因反应放热/吸热导致温度变化干扰实验

## 弱电解质电离 & 盐类水解

### （1）弱电解质的电离（盐酸/醋酸对比）

**实验**：同浓度盐酸/醋酸 pH、导电性
**反应方程式**：

- $\ce{HCl = H+ + Cl-}$
- $\ce{CH3COOH <=> H+ + CH3COO-}$

### （2）盐类的水解

**试剂及作用**：

- $\ce{NaCl}$、$\ce{CH3COONa}$、$\ce{NH4Cl}$ 溶液：不同类型盐，测酸碱性
- pH 试纸：判断溶液酸碱性
- 酚酞/石蕊：显色剂

**反应方程式**：

- $\ce{CH3COO- + H2O <=> CH3COOH + OH-}$
- $\ce{NH4+ + H2O <=> NH3.H2O + H+}$（或写作 $\ce{NH3\cdot H2O}$）

**知识点**：

- 弱电解质电离不完全，强电解质电离完全
- 盐类水解规律：越弱越水解，谁强显谁性

**注意事项**：

- 测 pH 时，pH 试纸需干燥，不能湿润（避免稀释溶液影响结果）
- 导电性实验需在相同温度下进行（温度影响离子迁移速率）
- 盐类水解吸热，加热可促进水解，需控制实验温度一致

## 沉淀溶解平衡

**实验**：沉淀转化（$\ce{AgCl}$ → $\ce{AgI}$ → $\ce{Ag2S}$）
**考点**：溶度积、沉淀先后、转化方向
**试剂及作用**：

- $\ce{AgNO3}$溶液：提供 $\ce{Ag+}$，生成 $\ce{AgCl}$ 沉淀
- $\ce{NaCl}$溶液：提供 $\ce{Cl-}$
- $\ce{KI}$溶液：提供 $\ce{I-}$，实现 $\ce{AgCl}$ → $\ce{AgI}$ 转化
- $\ce{Na2S}$溶液：提供 $\ce{S^{2-}}$，实现 $\ce{AgI}$ → $\ce{Ag2S}$ 转化

**反应方程式**：

- $\ce{AgNO3 + NaCl = AgCl v（白色） + NaNO3}$
- $\ce{AgCl + KI = AgI v（黄色） + KCl}$
- $\ce{2AgI + Na2S = Ag2S v（黑色） + 2KI}$

**注意事项**：

- 沉淀转化实验需控制离子浓度一致，确保实验现象由 $K_{sp}$ 大小决定
- $\ce{AgNO3}$溶液需少量滴加，避免过量导致现象干扰
- 实验后废液需处理（含重金属离子），不能直接排放

## 电化学（原电池 & 电解池）

### （1）原电池（以铜锌原电池为例）

**试剂及作用**：

- $\ce{Zn}$ 片、$\ce{Cu}$ 片：电极（$\ce{Zn}$ 为负极，$\ce{Cu}$ 为正极）
- 稀 $\ce{H2SO4}$/$\ce{ZnSO4}$/$\ce{CuSO4}$ 溶液：电解质溶液，提供离子，形成闭合回路

**反应方程式**：

- 负极（$\ce{Zn}$）：$\ce{Zn - 2e- = Zn^{2+}}$（氧化反应）
- 正极（$\ce{Cu}$）：
  - 酸性电解质：$\ce{2H+ + 2e- = H2 ^}$
  - 硫酸铜电解质：$\ce{Cu^{2+} + 2e- = Cu}$
- 总反应：
  - $\ce{Zn + H2SO4 = ZnSO4 + H2 ^}$
  - $\ce{Zn + CuSO4 = ZnSO4 + Cu}$

### （2）电解池（以电解饱和食盐水、电解 $\ce{CuCl2}$ 溶液为例）

**试剂及作用**：

- 石墨电极/$\ce{Cu}$ 电极：阳极/阴极
- 饱和 $\ce{NaCl}$ 溶液/$\ce{CuCl2}$ 溶液：电解质溶液
- 淀粉-$\ce{KI}$ 试纸：检验电解食盐水生成的 $\ce{Cl2}$

**反应方程式**：

- 电解 $\ce{CuCl2}$（石墨电极）：
  - 阳极：$\ce{2Cl- - 2e- = Cl2 ^}$
  - 阴极：$\ce{Cu^{2+} + 2e- = Cu}$
  - 总反应：$\ce{CuCl2 \xlongequal{电解} Cu + Cl2 ^}$
- 电解饱和食盐水（石墨电极）：
  - 阳极：$\ce{2Cl- - 2e- = Cl2 ^}$
  - 阴极：$\ce{2H2O + 2e- = H2 ^ + 2OH-}$
  - 总反应：$\ce{2NaCl + 2H2O \xlongequal{电解} 2NaOH + H2 ^ + Cl2 ^}$

**知识点**：

- 原电池：负极发生氧化反应，正极发生还原反应（负氧正还）
- 电解池：阳极发生氧化反应，阴极发生还原反应（阳氧阴还）

**注意事项**：

- 原电池两极需为不同活泼性金属（或一极为非金属导体），电解质溶液需能与负极反应
- 电解池阳极若为活性电极，电极本身参与反应


---

## Original file: 04 文字描述题模板.md

---
description: "提供化学实验文字描述题的模板，包括装置、试剂和操作的常见解释和理由。"
---

# 04 · 文字描述题模板

## 装置

1. 反应容器中和大气相通的玻璃
   - 指示容器内压强大小，避免容器内压强过大；平衡气压
2. 恒压分液漏斗上的支管或分液漏斗相连的橡皮管
   - 平衡气压，使恒压滴液漏斗或分液漏斗内的气体顺利滴下
   - （定量测量生成气体体积）抵消加入液体所带来的体积误差
3. 装置末端的干燥管
   - 防止空气中的水蒸气干扰实验
4. 不用酒精（明火）加热
   - （开放容器中）某物质沸点低、易挥发、易燃，明火加热存在安全隐患
   - （用水浴加热）物质沸点低，水浴加热有利于反应平衡进行
5. 毛细管
   - （减压蒸馏中毛细管通外界）可以调节蒸馏体系的真空度；通入的气体在加热过程中起到搅拌作用，使体系受热均匀，防止爆沸
   - （毛细管用于通入液体）液滴不易飞溅，不易形成酸雾

## 试剂

1. 某试剂过量
   - 增大另一物质的转化率
   - （特定）使 $\ce{Fe^3+}$ 完全转为 $\ce{Fe^2+}$ 等
2. 通入与体系内物质不作用的气体（如 $\ce{N2}$ ）
   - （反应前通入）排出装置内的空气，避免对反应造成干扰或发生副反应
   - （反应后通入）将产生的气体全部排出，被后续装置完全吸收

## 操作

1. 忘记加入沸石
   - 停止加热，待反应物冷却至室温后补强
2. 水浴加热（小于100℃）
   - 使反应受热均匀，方便控制反应温度
3. 冷水浴（冷却）
   - 防止某物质分解或挥发，冷凝收集产物等
   - （过度冷却会导致液体凝固后堵塞导管）
4. 控制温度在一定范围内
   - 若温度过低，反应速率（或溶解速率）较慢；若温度过高，某物质会分解或挥发；防止副反应发生
5. 趁热过滤
   - 保持过滤温度，防止温度降低后，某物质析出（溶解度随温度升高而增大）或便于某物质析出（溶解度随温度升高而减小）
6. 减压蒸发
   - 降低蒸发温度，防止某物质分解
7. 有机溶剂洗
   - （题干中提示物质难溶于有机物）减少在洗涤过程中的溶解损失
   - 有机溶剂易挥发，能快速带走固体表面的水分，使产品易于干燥
8. 碱煮水洗（将 $\ce{Na2CO3}$ 溶液加入盛有一定量废铁屑的烧杯中）
   - 去除表面的油污
   - （该过程中加热的目的）促进 $\ce{CO^2-_3}$ 的水解，使溶液碱性增强，油脂水解更彻底
9. 在某气体氛围中蒸发、反应
   - 抑制某离子的水解，防止某离子被氧化
10. 离子检验
    - 取少量待测液于洁净试管中，滴加……，观察……
11. 判断沉淀是否洗涤干净
    - 取最后一次洗涤液滴加……，若（不）出现……，证明沉淀已经洗涤完全
12. 判断沉淀是否完全
    - 静置，取适量上层清液于另一洁净试管中，向其中加入少量……（沉淀剂），若无沉淀发生，证明已经沉淀完成


---

## Original file: index.md

---
description: 本章聚焦高中化学实验，包含实验仪器、实验流程、常见实验现象与文字描述题模板，帮助提升实验题解题能力。
---

# 07 化学实验

<CCChapterOverview />


---

## Original file: 考点 滴定实验.md

---
description: "讲解滴定管的使用、化学滴定实验及误差分析"
---

# 考点 · 滴定实验

## 滴定管

### 类型

酸式滴定管，碱式滴定管，通用滴定管（聚四氟乙烯滴定管，酸碱皆可）

<img src="../07 化学实验/images/5.0.png" style="zoom: 55%;"/>

### 构造

- 标有使用温度：$20℃$
- 容积：$25$ $mL$、$50$ $mL$
- 刻度：$0$ 刻度线在上方，越往下读数越大，只标在中间一段
- 读数：小数点后两位

## 滴定实验

### 仪器

- 酸/碱式滴定管、锥形瓶、铁架台、滴定管夹、烧杯、（移液管可用）

### 步骤

- 检查装置是否漏水
- 洗涤（清水）、润洗（标准液）
- 注液、赶气泡、调液面、移液
- 滴定
- 记录
- 重复 $2\sim3$ 次
- 整理数据、计算

**检漏**

- 酸式：关闭活塞，装水至 $0$ 刻度线以上，直立约 $2$ $min$，仔细观察有无水渗出。将活塞转 $180°$，再直立 $2$ $min$，观察有无水渗出。（漏水：先用滤纸擦干活塞及活塞窝，用手指沾上少量凡士林，在活塞粗端和活塞细端或活塞内两端涂上一薄层，）
- 碱式：装水后直立 $2$ $min$。（漏水：换橡胶管和玻璃球）

**润洗**：从滴定管上口加入 $3\sim5$ $mL$所要盛装的酸或碱，倾斜慢慢转动滴定管，使液体润湿全部滴定管（锥形瓶不可润洗）。（移液管先用蒸馏水洗，再润洗）

**注液**：先把活塞完全关好，左手三指握住滴定管上部无刻度处，滴定管可以稍微倾斜些以接受溶液。右手拿住试剂瓶往滴定管中倒溶液，直到溶液充满0刻度线以上为止（不能借助其他仪器，用试剂瓶直接装入）。

**排气泡**

- 酸式：将酸式滴定管倾斜约 $30°$，迅速打开活塞，气泡随溶液排出。
- 碱式：将橡胶管倾斜 $30°$，弯折橡胶管，转动玻璃球，并使液面位于0刻度。

<img src="../07 化学实验/images/5.1.png" style="zoom: 55%;"/>

**调液**：调节液面至 $0$ 刻度线或以下（约 $2\sim3$ $cm$），并记下读数。

**读数**：装满溶液或放出溶液后，必须等 $1~\sim2$ $min$，使附着在内壁上的溶液流下再读数；读数时，将滴定管从滴定管架上取下，左手捏住上部无液处，保持滴定管垂直。读数读到小数点后第二位。

**移液**：用滴定管或移液管量取一定体积的标准液或待测液于锥形瓶中，加 $2\sim3$ 滴指示剂（锥形瓶中下滴的液，便于观察）。

**滴定**

- 在锥形瓶下垫一张白纸，左手控制滴定管，右手摇动锥形瓶，眼睛注视锥形瓶溶液颜色变化。摇动时右手握住锥形瓶颈，使溶液单方向不断旋转（左旋、右旋均可），不可前后振动。
- 滴定速度：开始可稍快，不超过每分钟 $10mL$（$3\sim4$ 滴/s），此滴液成串但不成线为度；接近终点时改为一滴滴加入，即加一滴摇几下再加再摇，最后改为半滴。

<img src="../07 化学实验/images/5.2.png" style="zoom: 55%;"/>

- 半滴操作：旋塞稍稍转动（轻轻挤压玻璃球），使半滴溶液悬于管口，瓶内壁将半滴溶液沾落，再用洗瓶以少量蒸馏水吹洗锥形瓶，继续摇动锥形瓶，观察颜色变化。

**记录**

- 滴定终点判断：当滴入最后半滴XX溶液后，溶液由XX色变成XX色且半分钟内不变色，说明达到滴定终点。
- 若滴定中不慎过量，可用反滴法。

**重复试验**（最好每次实验时滴定管内起始液面差不多）

**数据计算**（误差较大应舍去）

### 指示剂的选择

| 指示剂   | 酸色 (pH)         | 过渡色 (pH)           | 碱色 (pH)         | 备注                 |
| :------- | :---------------- | :-------------------- | :---------------- | :------------------- |
| 甲基橙   | 红（$< 3.1$）     | 橙（$3.1 - 4.4$）     | 黄（$> 4.4$）     | 强酸滴定常用         |
| 酚酞     | 无色（$< 8.2$）   | 浅红（$8.2 - 10.0$）  | 红（$> 10.0$）    | 强碱滴定常用         |
| 甲基红   | 红（$< 4.4$）     | 橙（$4.4 - 6.2$）     | 黄（$> 6.2$）     |                      |
| ~~石蕊~~ | ~~红（$< 5.0$）~~ | ~~紫（$5.0 - 8.0$）~~ | ~~蓝（$> 8.0$）~~ | 不使用（变色不敏锐） |

- 强酸滴定强碱（或强碱滴定强酸）时，甲基橙和酚酞均可做指示剂。
- 盐酸滴定 $\ce{Na2CO3}$、$\ce{NaNO3}$ 混合液：采用双指示剂法。

### 氧化还原滴定

- $\ce{KMnO4}$ 滴定 $\ce{Fe^2+}$ 或 $\ce{H2C2O4}$：
  - 终点标志：当滴入最后半滴时，溶液变为紫红色，且半分钟不褪色。
- $\ce{H2C2O4}$ 或 $\ce{Fe^2+}$ 滴定 $\ce{KMnO4}$：
  - 终点标志：当滴入最后半滴时，滴液紫红色褪去，且半分钟不恢复。
- 相关仪器：酸式滴定管、碱式滴定管。
- 碘量法 $\ce{I2 + 2Na2S2O3 \xlongequal{} 2NaI + Na2S4O6}$
  - 指示剂：淀粉溶液（$\ce{I2}$ 会与淀粉形成包合物，消耗 $\ce{I2}$，因此在滴定 $\ce{I2}$ 的实验中淀粉应在反应将结束时添加）
  - 碘水滴定 $\ce{Na2S2O3}$：滴至最后半滴时，溶液变蓝色，且半分钟不变。
  - $\ce{Na2S2O3}$ 滴定碘水：滴至最后半滴时，溶液由蓝色变为无色，且半分钟不恢复。

### 误差分析

1. 分析原理：
   $C_{标} \cdot V_{标} = C_{待} \cdot V_{待}$

2. 解题要领：
   因 $C_{标}$ 与 $V_{待}$ 已确定，因此只要分析出不正确操作引起 $V_{标}$ 的变化，即分析出结果。

以标准酸溶液滴定未知浓度的碱（酚酞作指示剂）为例

洗涤过程

| 操作                       | $V_{标}$ 变化 | 对结果的影响 |
| :------------------------- | :------------ | :----------- |
| 酸式滴定管未用标准溶液润洗 | ↑↑            | ↑↑           |
| 碱式滴定管未用待测溶液润洗 | ↓↓            | ↓↓           |
| 锥形瓶用待测液润洗         | ↑↑            | ↑↑           |
| 锥形瓶残留蒸馏水           | 无影响        | 无影响       |

取液过程

| 操作                                           | $V_{标}$ |
| :--------------------------------------------- | :------- |
| 放出碱液的滴定管开始有气泡，放出液体后气泡消失 | ↓↓       |

滴定过程

| 操作                                                                  | $V_{标}$ |
| :-------------------------------------------------------------------- | :------- |
| 酸式滴定管滴定前有气泡，滴定终点时气泡消失                            | ↑↑       |
| 振荡锥形瓶时部分液体溅出                                              | ↓↓       |
| 部分酸液滴出锥形瓶外                                                  | ↑↑       |
| 溶液颜色较浅时滴入酸液过快，停止滴定后反加半滴 $\ce{NaOH}$ 溶液无变化 | ↑↑       |

读数过程

| 操作                                                   | $V_{标}$ |
| :----------------------------------------------------- | :------- |
| 酸式滴定管滴定前读数正确，滴定后俯视读数（或前仰后俯） | ↓↓       |
| 酸式滴定管滴定前读数正确，滴定后仰视读数（或前俯后仰） | ↑↑       |


---



# Chapter 08 化学反应能量与速率

Source directory: `08 化学反应能量与速率`

## Original file: 01 化学反应速率与限度.md

---
description: "介绍化学反应速率的定义、表示方法和单位，以及影响反应速率的因素如温度、浓度等。"
---

# 01 · 化学反应速率与限度 <Badge type="warning" text="整理中" />

### 对应高中课本必修部分

## 化学反应速率

### 含义与表示方法

1. 定义：化学反应速率是用来衡量化学反应进行快慢程度的物理量。

2. 表示方法：通常用单位时间内反应物浓度的减少量或生成物浓度的增加量（均取正值）来表示。

3. 计算公式与单位：$v=\dfrac{\Delta c}{\Delta t}$

   > $v$：$mol/(L · min)$ 或 $mol/(L · s)$

4. 固体、纯液体的浓度视为定值（在一定温度下），不因其质量或物质的量的增减而变化，**所以不能用固体和纯液体的浓度变化来表示反应速率。**

### 化学反应速率的换算与比较

1. 对于同一个反应来说，用不同的物质来表示该反应的速率时，其数值可能不同，但表达的意义是相同的。因此，表示化学反应的速率时必须指名是用反应体系中的哪种物质作标准。

2. 在同一反应中用不同的物质来表示反应速率时，其数值之比等于各物质的化学计量数之比。

   > 如化学反应$mA_(g_)+nB_(g) \rightleftharpoons pC_(g)+qD_(g)$的速率关系为：
   >
   > $v_A:v_B:v_C:v_D=m:n:p:q$或$\dfrac{V_A}{m}:\dfrac{V_B}{n}:\dfrac{V_C}{p}:\dfrac{V_D}{q}$。

### 实验：探究温度对反应速率的影响

| 实验操作 | 试管中均有 2 mL 5%的 $H_2 O_2$ 溶液,并滴有 2 滴 $ 1 mol·L^-1 FeCl_3 $ 溶液 |
| -------- | -------------------------------------------------------------------------- |
| 实验现象 | 两支试管中均有气泡产生,但产生气泡的快慢:热水>冷水                          |
| 实验结论 | 其他条件相同时,升高温度,反应速率增大;降低温度,反应速率减小                 |

### 实验：探究反应物浓度对反应速率的影响

| 实验现象 | 两支试管中均有气泡产生，但产生气泡的快慢：甲>乙        |
| -------- | ------------------------------------------------------ |
| 实验结论 | 其他条件相同时,增大(降低)反应物浓度,反应速率增大(减小) |


---

## Original file: 02 化学反应速率进阶.md

---
description: "介绍化学反应速率选择性必修补充的相关内容。"
---

# 02 · 化学反应速率 <Badge type="warning" text="整理中" />

### （对应高中课本选择性必修额外部分，基本概念请参见前一课）

## 活化能与有效碰撞

### 1.基本概念

#### 活化能

- **定义**：**活化分子的平均能量与反应物分子的平均能量之差**
- **通俗理解**：反应物分子要发生反应，**必须“跨越”的能量“门槛”**——只有能量达到或超过该门槛的分子（即活化分子），才能发生有效碰撞并转化为生成物。
- **本质**：活化能是反应物分子断键、重组为生成物分子过程中，克服分子间作用力、化学键断裂所需的最低能量。

#### 有效碰撞

- **定义**：能发生化学反应的分子碰撞
- **发生有效碰撞的两个必备条件**：碰撞的分子必须是**活化分子**；碰撞时，**空间取向必须合理**

### 2. 与催化剂的关联（重点）

- 催化剂的作用原理：**降低反应的活化能（不改变反应物、生成物的总能量，也不改变反应热）；**
- 具体影响：活化能降低后，更多普通分子转化为活化分子，**活化分子百分数显著增大，有效碰撞频率大幅提高，反应速率加快**
- **注意：**
  ①催化剂只能降低 “正、逆反应的活化能”，且降低幅度相同，**不改变正、逆反应速率的比值，也不影响平衡移动。**

### 3. 与温度的关联

- 具体影响：分子能量升高后，更多普通分子因达到能量门槛转化为活化分子，**活化分子百分数显著增大**，分子碰撞频率同时提高，有效碰撞频率大幅提高，反应速率**加快**

### 4. 与压强的关联

- （充入反应气体）体积缩小导致浓度增大后，单位体积内的分子总数增加，**单位体积内的活化分子数目相应增多，有效碰撞频率提高，反应速率加快**
- 如果是恒容条件下充入惰性气体（如氦气、氖气）：虽然总压强增大了，但**反应体系的体积没变，反应物浓度没变，单位体积内的活化分子数也没变，所以反应速率不变**

## 反应速率常数与阿伦尼乌斯公式

- 反应速率常数（通常用 $k$ 表示）是化学反应动力学中的一个核心参数。它定量描述了在给定温度下，反应物转化为产物的固有快慢程度，$k$ 值越大，反应速率越快。
- 可以通过**阿伦尼乌斯方程**描述，其中 $E_a$ 是活化能，$A$ 是指前因子（常数），$R$ 是气体常数，$T$ 是热力学温度：

$$ k = A e^{-\frac{E_a}{RT}} $$

- 用于实验图象的另一写法：
  $$ \ln k = \ln A - \frac{E_a}{RT} $$
- 可见，$\ln k$ ∝ ${\frac{1}{T}}$ ，图线斜率越大，活化能越大


---

## Original file: index.md

---
description: 本章讲解化学反应速率与反应限度等核心概念，梳理影响因素、典型图像与常见解题方法。
---

# 08 化学反应能量与速率

<CCChapterOverview />


---



# Chapter 09 化学平衡

Source directory: `09 化学平衡`

## Original file: 01 化学平衡状态.md

---
description: "介绍可逆反应和化学平衡状态的概念、特征、建立过程，以及平衡状态的判断方法。"
---

# 01 · 化学平衡状态 <Badge type="warning" text="整理中" />

## 可逆反应

### 概念

在相同条件下，既能向正反应方向进行，同时又能向逆反应方向进行的化学反应。

在化学方程式中用 $\xrightleftharpoons{}$ 表示。

### 特征

1. 双向性：可逆反应包含方向相反的正反应和逆反应。
2. 双同性：在同一条件下，正、逆反应同时进行。
3. 共存性：反应物转化率小于 $100\%$，反应物与生成物共存。

## 化学平衡状态

### 概念

在一定条件下，可逆反应体系中，当正、逆反应速率相等，且反应物和生成物浓度保持不变时，体系组成不再随时间改变，此时称为化学平衡状态。

<img alt="化学平衡-1.1" src="/09 化学平衡/images/1.1.svg"/>

### 平衡建立过程

1. 反应开始时：反应物浓度最大，$v(\text{正})$ 最大；生成物浓度为 $0$，$v(\text{逆})=0$。
2. 反应进行时：反应物浓度降低，$v(\text{正})$ 减小；生成物浓度增大，$v(\text{逆})$ 增大。
3. 达到平衡时：$v(\text{正})=v(\text{逆})\neq0$，各组分浓度保持不变。

### 特征

1. 研究对象：可逆反应。
2. 动态平衡：$v(\text{正})=v(\text{逆})\neq0$。
3. 浓度不变：各组分浓度、百分含量保持不变。
4. 条件依存：外界条件变化后会建立新平衡。

## 化学平衡状态判断

以 $m\ce{A}_{(g)}+n\ce{B}_{(g)} \xrightleftharpoons{} p\ce{C}_{(g)}+q\ce{D}_{(g)}$ 为例：

### 判断核心

1. 正、逆反应速率之比等于化学计量数之比，且必须体现“一正一逆”。
2. 随反应进行而变化的变量不再变化。

### 具体判断依据

| 类型                              | 判断依据                                                                               | 是否为平衡状态 |
| --------------------------------- | -------------------------------------------------------------------------------------- | -------------- |
| 混合体系中各成分含量              | 各物质的物质的量或物质的量分数一定                                                     | 是             |
|                                   | 各物质的质量或质量分数一定                                                             | 是             |
|                                   | 各气体的体积或体积分数一定                                                             | 是             |
| 正逆反应速率关系                  | 单位时间内消耗 $m\ \text{mol}\ \ce{A}$，同时生成 $m\ \text{mol}\ \ce{A}$               | 是             |
|                                   | 单位时间内消耗 $n\ \text{mol}\ \ce{B}$，同时生成 $p\ \text{mol}\ \ce{C}$               | 否             |
|                                   | $v(\ce{A}):v(\ce{B}):v(\ce{C}):v(\ce{D})=m:n:p:q$                                      | 否             |
|                                   | 单位时间内生成 $n\ \text{mol}\ \ce{B}$，同时消耗 $q\ \text{mol}\ \ce{D}$（同为逆反应） | 否             |
| 压强                              | $m+n\ne p+q$ 时，总压强一定（其他条件不变）                                            | 是             |
|                                   | $m+n=p+q$ 时，总压强一定（其他条件不变）                                               | 否             |
| 平均相对分子质量 $\overline{M_r}$ | $m+n\ne p+q$ 时，$\overline{M_r}$ 一定                                                 | 是             |
|                                   | $m+n=p+q$ 时，$\overline{M_r}$ 一定                                                    | 否             |
| 气体密度                          | $m+n\ne p+q$，恒温恒压时，密度不变                                                     | 是             |
|                                   | $m+n=p+q$，恒温恒压时，密度不变                                                        | 否             |
| 颜色                              | 有色物质颜色一定                                                                       | 是             |
| 绝热条件温度                      | 体系温度不变                                                                           | 是             |
| 绝热条件压强                      | $m+n=p+q$ 时，压强不变                                                                 | 是             |

## 化学平衡常数

### 浓度商 $Q$

1. 定义：任意时刻，生成物浓度幂之积与反应物浓度幂之积的比值。
2. 对于
   $m\ce{A}_{(g)}+n\ce{B}_{(g)} \xrightleftharpoons{} p\ce{C}_{(g)}+q\ce{D}_{(g)}$：

$$
Q=\frac{c^p(\ce{C})\cdot c^q(\ce{D})}{c^m(\ce{A})\cdot c^n(\ce{B})}
$$

### 化学平衡常数 $K$

1. 定义：温度一定时，反应达到平衡状态后，生成物浓度幂之积与反应物浓度幂之积的比值。
2. 表达式：

$$
K=\frac{c^p(\ce{C})\cdot c^q(\ce{D})}{c^m(\ce{A})\cdot c^n(\ce{B})}
$$

固体和纯液体不写入表达式。

3. 意义：$K$ 越大，反应进行越完全，反应物转化率越高。通常 $K>10^5$ 可视为基本完全，$K<10^{-5}$ 反应较难进行。
4. 与方程式关系：
   - 正逆反应的平衡常数互为倒数：$K_{\text{正}}=\frac{1}{K_{\text{逆}}}$。
   - 方程式各系数同乘 $x$，则新平衡常数为原来的 $x$ 次方。
   - 两反应方程式相加，总反应平衡常数等于各自平衡常数乘积：$K_{\text{总}}=K_1\cdot K_2$。
5. 影响因素：只受温度影响，与浓度、压强、催化剂无关。

### 用 $Q$ 与 $K$ 判断反应方向

1. $Q<K$：反应正向进行，$v(\text{正})>v(\text{逆})$。
2. $Q=K$：反应达到平衡，$v(\text{正})=v(\text{逆})$。
3. $Q>K$：反应逆向进行，$v(\text{正})<v(\text{逆})$。

## 化学平衡移动

### 概念与实质

1. 概念：平衡后改变条件，原平衡被破坏，经过一段时间建立新平衡。
2. 实质：条件变化导致 $v(\text{正})\ne v(\text{逆})$，各组分百分含量随之变化。

### 勒夏特列原理

改变影响平衡的条件之一（浓度、压强、温度），平衡将向减弱该改变的方向移动。

### 外界条件对平衡的影响

| 改变条件（其他不变） | 平衡移动方向                   | 说明                                                      |
| -------------------- | ------------------------------ | --------------------------------------------------------- |
| 浓度                 | 增大反应物浓度或减小生成物浓度 | 正向移动                                                  |
|                      | 减小反应物浓度或增大生成物浓度 | 逆向移动                                                  |
| 压强（有气体参与）   | $m+n\ne p+q$，增大压强         | 向气体分子数减小方向移动                                  |
|                      | $m+n\ne p+q$，减小压强         | 向气体分子数增大方向移动                                  |
|                      | $m+n=p+q$，改变压强            | 平衡不移动                                                |
| 温度                 | 升高温度                       | 向吸热反应方向移动                                        |
|                      | 降低温度                       | 向放热反应方向移动                                        |
| 催化剂               | 加入催化剂                     | 平衡不移动（同等程度改变 $v(\text{正})$、$v(\text{逆})$） |

### 惰性气体影响

1. 恒温恒容：充入惰性气体后总压强增大，但各组分浓度不变，平衡不移动。
2. 恒温恒压：充入惰性气体后容器体积增大，各组分浓度同倍数减小，等效于减压，平衡按减压规律移动。

## 等效平衡

### 定义

同一可逆反应在一定条件（恒温恒容或恒温恒压）下，采用不同投料方式达到平衡时，若相同组分的百分含量（体积分数、物质的量分数、质量分数）相等，则称为等效平衡。

### 判断方法

极值转换法（“一边倒”）：将反应物或生成物按计量数完全转化到另一侧，再比较投料关系。

### 分类与结论

1. 恒温恒容：
   - 一边倒后投料量完全相等：平衡时各物质浓度、百分含量均相等。
   - 一边倒后投料量成比例且气体分子数不等：等效于加压或减压，平衡移动，百分含量不同。
   - 一边倒后投料量成比例且气体分子数相等：平衡不移动，百分含量相等。
2. 恒温恒压：
   - 一边倒后投料量完全相等或成比例：都可形成等效平衡，百分含量相等。

### 转化率与热量关系

1. 若两过程为等效平衡且反应方向相反，则转化率之和为 1：$\alpha_1+\alpha_2=1$。
2. 热量关系：$|Q_1|+|Q_2|=|\Delta H|$（$Q$ 为过程放热或吸热，$\Delta H$ 为反应焓变）。


---

## Original file: 02 化学平衡常数.md

# 化学平衡常数知识点 <Badge type="warning" text="整理中" />

## 一、浓度商（$Q$）

1. **定义**：在可逆反应的任意时刻（非平衡状态），生成物浓度幂之积与反应物浓度幂之积的比值，称为浓度商。

2. **表达式**：对于可逆反应 $m\mathrm{A}(g) + n\mathrm{B}(g) \rightleftharpoons p\mathrm{C}(g) + q\mathrm{D}(g)$，浓度商表达式为：

   $$
   Q = \frac{c^p(\mathrm{C}) \cdot c^q(\mathrm{D})}{c^m(\mathrm{A}) \cdot c^n(\mathrm{B})}
   $$

3. **注意事项**：
   - 表达式中浓度为任意时刻的瞬时浓度，非平衡浓度。
   - 固体、纯液体的浓度视为常数，不列入浓度商表达式。

## 二、化学平衡常数（$K$）

### （一）定义

温度一定时，可逆反应达到化学平衡状态时，生成物浓度幂之积与反应物浓度幂之积的比值为定值，该定值即为化学平衡常数（简称平衡常数）。

### （二）表达式

1. **通用表达式**：对于可逆反应 $m\mathrm{A}(g) + n\mathrm{B}(g) \rightleftharpoons p\mathrm{C}(g) + q\mathrm{D}(g)$，平衡常数表达式为：

   $$
   K = \frac{c^p(\mathrm{C}) \cdot c^q(\mathrm{D})}{c^m(\mathrm{A}) \cdot c^n(\mathrm{B})}
   $$

2. **特殊情况**：
   - 反应中有固体/纯液体参与时，其浓度视为常数，不列入表达式（如 $\mathrm{CaCO}_3(s) \rightleftharpoons \mathrm{CaO}(s) + \mathrm{CO}_2(g)$，$K = c(\mathrm{CO}_2)$）。
   - 表达式中浓度为平衡时的浓度，单位需与化学计量数匹配。

### （三）单位

平衡常数的单位由反应方程式中各物质的化学计量数决定，无固定值：

- 如 $\mathrm{H}_2(g) + \mathrm{I}_2(g) \rightleftharpoons 2\mathrm{HI}(g)$ 的 $K$ 无单位；
- 如 $\mathrm{N}_2(g) + 3\mathrm{H}_2(g) \rightleftharpoons 2\mathrm{NH}_3(g)$ 的 $K$ 单位为 $(\mathrm{mol \cdot L}^{-1})^{-2}$。

### （四）意义

平衡常数值的大小反映化学反应的进行程度（反应限度）：

- $K > 10^5$：反应基本完全，反应物平衡转化率极高；
- $10^{-5} < K < 10^5$：反应为可逆反应，反应物有一定转化率；
- $K < 10^{-5}$：反应难以发生，反应物转化率极低；
- **注意**：$K$ 仅反映反应限度，与反应速率无关（$K$ 大不代表反应速率快）。

### （五）与化学方程式书写形式的关系

平衡常数与化学方程式的书写形式一一对应，规律如下：

1. **正逆反应**：正反应平衡常数 $K_{\text{正}}$ 与逆反应平衡常数 $K_{\text{逆}}$ 互为倒数，即 $K_{\text{正}} = \dfrac{1}{K_{\text{逆}}}$；
2. **系数缩放**：化学方程式乘以系数 $x$，平衡常数变为原常数的 $x$ 次方，即 $K' = K^x$；
3. **反应叠加**：两个方程式相加得到总方程式，总反应平衡常数等于两分反应平衡常数的乘积，即 $K_{\text{总}} = K_1 \cdot K_2$。

### （六）影响因素

1. **核心影响因素：温度**（平衡常数是温度的函数）：
   - **放热反应**（$\Delta H < 0$）：升温，$K$ 减小；降温，$K$ 增大；
   - **吸热反应**（$\Delta H > 0$）：升温，$K$ 增大；降温，$K$ 减小。

2. **无关因素**：反应物/生成物的浓度（或分压）、压强、催化剂等，只要温度不变，$K$ 始终不变。

### （七）核心应用

1. **判断反应进行方向**：通过比较 $Q$ 与 $K$ 的大小判断：
   - $Q < K$：反应正向进行（$v_{\text{正}} > v_{\text{逆}}$）；
   - $Q = K$：反应达到平衡状态（$v_{\text{正}} = v_{\text{逆}}$）；
   - $Q > K$：反应逆向进行（$v_{\text{正}} < v_{\text{逆}}$）。

2. **计算平衡相关量**：已知 $K$ 和初始浓度，可通过"三段式"计算平衡浓度、反应物转化率等；

3. **比较反应限度**：同一温度下，相同类型的可逆反应，$K$ 越大，反应进行得越完全。

### （八）补充说明

1. **分压平衡常数（$K_p$）**：若反应体系为气体，可采用分压代替浓度计算平衡常数（$K_p$），其数值与 $K$ 不同，但意义一致，且仅受温度影响；

2. **多步反应**：总反应的平衡常数等于各步反应平衡常数的乘积，可通过该规律计算难直接测定的反应的 $K$；

3. **表达式书写**：需明确物质聚集状态，仅气体、溶液中的溶质列入，固体、纯液体除外。


---

## Original file: 03 水溶液中的离子反应.md

---
description: "水溶液中的离子反应"
---

# 03 · 水溶液中的离子反应<Badge type="warning" text="整理中" />

## 电离与水解

### 电离平衡

1. 定义：弱电解质电离与结合的的速率相同，各粒子浓度不变；

2. **注意**：
   1. 电离过程吸热；

   2. 平衡时，转化率极小；

3. **影响因素**：自身性质；温度（$T$ 增大，平衡右移）、浓度（**越稀越电离，但是离子浓度降低**）

4. **比较依据**：$K_a$、$K_b$ 越大，越易电离，越显酸性、碱性。

### 盐类水解

1. **注意**：
   1. 水解吸热；

   2. 水解一般极微弱；

2. **影响因素**：自身因素、**体系温度 $T$**、**溶液浓度 $c$**；

3. **应用**：
   1. 加热 $\ce{Na_2CO_3(aq)}$更容易去污；

   2. 储存、配置易水解的盐加酸；

   3. 可溶性铝/铁盐净水；

   4. 制取 $\ce{TiO_2}$、$\ce{SnO}$、$\ce{SnO_2}$ 等过渡金属氧化物；

   5. 判断溶液酸碱性；

   6. 制备固盐、胶体；

   7. 判断离子是否共存。

## 盐类的酸碱性

1. 强酸强碱盐不水解，呈中性；

2. 弱酸根离子水解产生 $\ce{OH^-}$，弱碱阳离子水解产生 $\ce{H^+}$，因此强酸弱碱盐呈酸性，弱酸强碱盐呈碱性；

3. 弱酸弱碱盐应当看两种离子水解的 $K$，$K_{ha}$ 大呈碱性，$K_{hb}$ 大呈酸性，相近则中性；

4. 弱酸酸式盐的酸碱性应当比较 $K_a$ 和 $K_h$，$K_h$ 大于 $K_a$，溶液呈碱性，反之呈酸性。

### 强弱酸的判断

1. $0.1$ $mol/L$ 的溶液中，$pH=1$ 的为强酸，$pH>1$ 的为弱酸；

2. 同 $t$ 同 $c$ 的两种酸与金属反映的速率或导电能力；

3. 钠盐的 $pH$。

### 水溶液中的三大守恒

1. 电荷守恒：溶液中所有阳离子所带的正电荷总浓度等于所有阴离子所带的负电荷总浓度；

2. 物料守恒：不同形式的相同元素之和之比是化学式之比；

3. 质子守恒：水电离出的以不同形式存在的 $\ce{H+}$ 和 $\ce{OH-}$ 的量相等。

## pH

$pH=-lg c(\ce{H^+})$；

意义：

1. 常温下，$pH=7$ 为中性，$pH<7$ 为酸性，$pH>7$ 为碱性；

2. $pH$ 越小则越酸，越大则越碱。

### pH试纸

1. 操作：取一小块pH试纸于干燥洁净的玻璃片或表面皿上，用**干燥清洁的玻璃棒蘸取待测液于pH试纸上**，与标准比色卡对准读数；

2. 种类：
   1. 广泛 $pH$ 试纸：测定范围为 $(1,14)$ 或 $(1,10)$，可识别的差距为 $1$；

   2. 精密 $pH$ 试纸：测定范围较窄，差距为 $0.2$ 或 $0.3$；

   3. 专用 $pH$ 试纸：只适用于酸性/碱性/中性溶液；

   **其它检测$pH$的工具**：$pH$ 计/酸度计：精密测量 $pH$，量程 $0-14$.

3. 注意：
   1. $pH$ 试纸本身为黄色，酸红碱蓝；

   2. $pH$ 试纸不能润湿，否则会导致酸性溶液结果偏大，碱性溶液结果偏小；

   3. $pH$ 试纸不能测量有漂白性、脱水性的物质，如**氯气、次氯酸**（但是二氧化硫溶液可以用 $pH$ 试纸测）。

### 酸碱指示剂

<img src="./images/4.1.png" />

## 沉淀溶解平衡

1. 定义：沉淀（生成）的速率与溶解的速率相等；

2. 移动：一般升温会使平衡正移，但也有例外，例如 $\ce{Ca(OH)_2}$。

**溶解度（$s$）**

1. 定义：一定温度（压强）下，某一物质在 $100$ $g$ 溶液里的质量（体积）；

2. **影响因素**：
   1. 溶质本身与溶剂、溶液的因素；

   2. 一般温度增大，固体的溶解度增加，气体减少；

   3. 一般压强增大，气体的溶解度增大。

### 溶解度大小的比较

1.  阴阳离子之比相同的物质，$K_{sp}$ 越大，溶解度越大；

2.  其他物质应当计算平衡时的浓度；

3.  复分解反应中，溶解性大的生成溶解性小的。

### 沉淀生成

1. 方法：
   1. 调节 $pH$（**如 $\ce{ Fe^{3+} }$ 可以通过通入 $\ce{NH_3}$ 的方式沉淀**）；

   2. 加沉淀剂；

**元素示例**

- $\ce{Ba^{2+}, Pb^{2+}, Ca^{2+} }$ 用 $\ce{H_{2}SO_{4} }$ 沉淀。
- $\ce{ Ca^{2+}, Mg^{2+}, F^{-} }$ ($pH$ 不应过低，防止生成 $HF$）。
- $\ce{Cu^{2+}, Ag^{+}, Pb^{2+}, Co, Ni^{2+} }$ 用 $\ce{ S^{2-} }$ 沉淀。
- $\ce{Ca^{2+}, Ba^{2+}, Fe^{3+}, Al^{3+} , Ca^{2+} }$ (与 $\ce{Ca^{2+}, Ba^{2+} }$ 形成沉淀，与 $\ce{ Fe^{3+}, Al^{3+} }$ 成氢氧化物)。
- $\ce{Ca^{2+}, Co^{2+}, Ni^{2+} }$ 可溶性草酸盐。

2. 应用：无机物的制备和提纯、废水处理等；

### 沉淀溶解

1. 原理：对于难溶的电解质，如果能设法不断移取生成物，使平衡向右移动，则可以使沉淀溶解；

2. 方法：
   1. 酸/碱溶解法
      $\ce{V_{2}O_{5} }$ 可以被酸溶解，生成 $\ce{VO_{2}^+ }$，也可以溶于强碱
      $\ce{Cr_{2}O_{3} }$、$\ce{Cr(OH)_{3} }$ 有两性，遇碱生成 $\ce{[Cr(OH)_4]^-}$，遇酸生成 $\ce{Cr^3+}$
   2. 盐溶解法；

   3. 生成配合物法
      氨水溶解氢氧化铜：$\ce{Cu(OH)2 +4NH3\cdot H2O \xlongequal{} [Cu(NH3)4]^2+ +2OH- +4H2O}$

   4. 氧化还原法（酸浸不活泼金属时会加入双氧水促进溶解）
      $\ce{Cu +H2O2 +H2SO4 \xlongequal{} CuSO4 +2H2O}$

### 沉淀转化

1. 条件：一般溶解性大的转化为溶解性小的，但有时可以逆向转化；

2. 应用：
   1. 去除水垢；

   2. 化工流程中金属提取。


---

## Original file: index.md

---
description: 本章聚焦化学平衡基础，讲解平衡状态特征、平衡移动及其影响因素，适用于平衡专题的系统复习。
---

# 09 化学平衡

<CCChapterOverview />


---



# Chapter 10 化学反应与能量

Source directory: `10 化学反应与能量`

## Original file: 01 反应热与焓变.md

---
description: "介绍热化学方程式的书写、反应热的概念，以及燃烧热的定义和计算。"
---

# 01 · 反应热与焓变 <Badge type="warning" text="整理中" />

## 一些常见变化的吸放热情况

1. 钢铁生锈、食物腐败：放热

2. 大部分分解反应：吸热（**反例：双氧水、硝酸铵、‌氯酸钾的分解**）

3. $\ce{HF}$溶于水电离：放热（**溶解放热，电离吸热，水合放热，总体放热**）

4. $\ce{CuO + CO}$加热生成$\ce{Cu + CO_2}$：放热

## 热化学方程式

### 热化学方程式

(1)概念：表明反应所释放或吸收的热量的化学方程式。

(2)意义：表明了化学反应中的物质变化和能量变化。

在 $25$ ℃、$101$ kPa下，$\ce{2H2(g)＋O2(g)=2H2O(l)}$ $ΔH＝－571.6$ kJ/mol，其表示在 $25$ ℃、$101$ kPa 下，$2$ mol 气态 $\ce{H2}$ 与 $1$ mol 气态 $\ce{O2}$ 完全反应生成 $2$ mol 液态 $\ce{H2O}$ 时放出 $571.6$ kJ 的热量。

### 书写热化学方程式的注意事项

（1）$ΔH$ 写在方程式右边并用空格隔开，注意**吸热要标注加号，放热要标注减号**

（2）需注明反应时的温度和压强。如不注明，即专指 **$25$ ℃，$101$ kPa**。

（3）不用写加热、加压、催化剂、沉淀、气体等反应条件或符号。**但必须注明各物质的状态：固体—$s$，液体—$l$，气体—$g$，溶液—$aq$**

（4）热化学方程式中化学计量数可**为整数或分数**，其表示参加反应的**各物质的物质的量**，因此 **$ΔH$ 与化学计量数成比例**。

（5）若反应**逆向进行**，则 $ΔH$ 改变符号，但绝对值不变。

（6）若反应为**可逆反应**，$ΔH$ 指的是完全发生反应所吸收或者放出的热量。

## 燃烧热

1.定义：$101$ kPa时，$1$ mol 纯物质完全燃烧生成指定产物时所放出的热量，叫做该物质的燃烧热，单位为kJ/mol。

2.熟记常见元素完全燃烧生成的指定产物

| 元素           | C             | H             | S             | N            |
| -------------- | ------------- | ------------- | ------------- | ------------ |
| 指定产物及状态 | $\ce{CO2(g)}$ | $\ce{H2O(l)}$ | $\ce{SO2(g)}$ | $\ce{N2(g)}$ |

$\ce{CO(g) + \frac{1}{2}O2(g) = CO2(g)}$ $∆H＝−283$ kJ/mol

$\ce{2CO(g) + O2(g)  =   2CO2(g)}$ $∆H＝−566$ kJ/mol

3.$25$ ℃、$101$ kPa时甲烷的燃烧热为 $890.3$ kJ/mol，解释其表示的意义：**表示 $25$ ℃、$101$ kPa 时， $1$ mol $\ce{CH4}$ 完全燃烧生成 $\ce{CO2}$ 气体和液态 $\ce{H2O}$ 时放出 $890.3$ kJ的热量。**

4.燃烧热的热化学方程式
书写燃烧热的热化学方程式时，以燃烧 $1$ mol 可燃物为标准来配平其余物质的化学计量数，同时可燃物要完全燃烧且生成指定产物。
例如：在 $101$ kPa下，汽油的成分之一辛烷（$\ce{C8H18}$）燃烧的热化学方程式为 $\ce{2C8H18(l)＋25O2(g)=16CO2(g)＋18H2O(l)}$ $ΔH＝－11 036$ kJ/mol。则表示辛烷燃烧热的热化学方程式为 $\ce{C8H18(l)＋\frac{25}{2}O2(g) = 8CO2(g)＋9H2O(l)}$ $ΔH=-5 518$ kJ/mol

### 燃烧热的测量

测定原理：将待测物质放在一个充满氧气的密封金属容器（称为氧弹）内，再将此容器置于盛有一定量水的量热计内筒中，通过点火装置使氧弹中物质燃烧，反应放出的热量会使氧弹外面的水温升高。用温度计测量水温的变化，即可计算出此反应放出的热量。

### 中和反应反应热的测定实验

请按照下列步骤，用简易量热计 (如图) 测量盐酸与 $\ce{NaOH}$ 溶液反应前后的温度![alt text](image\img1.png)

1.反应物温度的测量

​ (1) 用量筒量取 $50$ mL $0.50$ mol/L盐酸，打开杯盖，倒入量热计的内筒，盖上杯盖，插入温度计，测量并记录盐酸的温度.用水把温度计上的酸冲洗干净，擦干备用

​ (2) 用另一个量筒量取 $50$ mL $0.55$ mol/L $\ce{NaOH}$ 溶液，用温度计测量并记录 $\ce{NaOH}$ 溶液的温度

​ 2.反应后体系温度的测量打开杯盖，将量筒中的 $\ce{NaOH}$ 溶液迅速倒入量热计的内筒，立即盖上杯盖，插入温度计，用搅拌器匀速搅拌.密切关注温度变化，将最高温度记为反应后体系的温度 ($t_2$)

​ 3.重复上述步骤 1 至步骤 2 两次.

##### 【数据处理】

(1) 取盐酸温度和 $\ce{NaOH}$ 溶液温度的平均值记为反应前体系的温度 ($t_1$).计算温度差 ($t_2-t_1$)，将数据填入下表
|实验次数|起始温度$(\ce{HCl})t_1/^\circ\text{C}$|起始温度$(\ce{NaOH})t_2/^\circ\text{C}$|平均值|终止温度$t_2/^\circ\text{C}$|温度差$(t_2-t_1)/^\circ\text{C}$|
|------|------|------|------|------|------|
|1||||||
|2||||||
|3||||||

(2) 取三次测量所得温度差的平均值作为计算依据

(3) 根据温度差和比热容等计算反应热

(4) 实验数据处理

##### 数据处理计算

​ 1.反应原理：$Q=cm∆t$

​ $Q$ 是中和反应放出的热量
$m$ 是反应混合液的质量
$C$ 是反应混合液的比热容
$Δt$ 是反应前后溶液温度的差值

​ 2.为了计算简便，可以近似地认为实验所用酸、碱稀溶液的密度、比热容与水的相同，并忽略量热计的比热容，

则:① $50$ mL $0.50$ mol/L盐酸的质量 $m_1=50g$，$50$ mL $0.55$ mol/L $\ce{NaOH}$ 溶液的质量 $m_2=50g$.

​ ②反应后生成的溶液的比热容 $c=4.18$ J/(g∙℃)

$Q=4.18×10-3×(50+50)×(t_2-t_1)kJ=0.418(t_2-t_1)kJ$

##### 为了提高测定的准确度，应该采取哪些措施?

1.隔热层、杯盖等的使用是为了减少热量散失，降低实验误差.

2.要使用同一支温度计，避免仪器误差.注意测定一种溶液后必须用水冲洗干净并用滤纸擦干.

3.使用不同的量筒分别量取酸碱溶液

4.正确读取体积和温度，多次试验求平均值时，若有某一组的实验数据有明显偏差，应直接舍去.

5.操作时动作要快，尽量减少热量的散失

6.为了保证盐酸完全被中和，采用稍过量的 $\ce{NaOH}$ 溶液.

### 吸放热反应的判断

依据化学键能量变化：对比反应物断键吸收的能量与生成物成键释放能量的多少（断键吸热 > 成键放热为吸热反应，反之则为放热反应）。

依据物质总能量：反应物总能量 > 生成物总能量为放热反应，反之则为吸热反应。

提示：放热反应与放热过程不同，放热反应有新物质生成（如燃烧），放热过程无新物质生成（如水蒸气液化）。

### 典型的吸热反应与放热反应

典型吸热反应：绝大多数分解反应、铵盐与碱的反应、$\ce{C}$ 与 $\ce{CO₂/CO/H₂O}$ 的反应、弱电解质电离及盐类水解过程。

典型放热反应：燃烧与中和反应、绝大多数化合与氧化还原反应、铝热反应、金属与酸 / 水的置换反应、氯酸钾分解、双氧水分解。


---

## Original file: 02 热化学方程式.md

---
description: "讲解热化学方程式的书写要求，包括状态标注、ΔH表示、计量数等。"
---

# 02 · 热化学方程式 <Badge type="warning" text="整理中" />

## 概念：

能表明反应所释放或吸收的热量的化学方程式。

## 意义：

热化学方程式不仅表明了化学反应中的**物质变化**,也表明了化学反应中的**能量变化**，还说明了物质的量与能量的**关系**。

**例如：**
$$\ce{H2(g) +Cl2(g)=2HCl(g)\qquad\Delta H= -184.6\text{kJ/mol}}$$
表示 $1mol$ 气态 $\ce{H2}$ 和 $1mol$ 气态 $\ce{Cl2}$ 反应生成 $2mol$ 气态 $\ce{HCl}$,放出184.6$\text{kJ}$的热量。

## 书写要求：

1. 标注反应物、生成物聚集状态

   | $s$  | $l$  | $q$  | $aq$   |
   | ---- | ---- | ---- | ------ |
   | 固体 | 液体 | 气体 | 水溶液 |

2. 右端标注$\Delta  H$（放热$\Delta H$<0，吸热$\Delta H$>0），数值与化学计量数成正比。

3. 化学计量数可为整数或分数（表示物质的量），注明反应温度和压强（默认 25℃、101kPa;单位$\text{kJ/mol}$）


---

## Original file: 03 盖斯定律.md

---
description: "介绍盖斯定律的定义和应用方法，用于计算反应热。"
---

# 03 · 盖斯定律 <Badge type="warning" text="整理中" />

### 定义

化学反应的反应热只与反应始末状态有关，与反应路径无关。一步完成或分步完成的反应热相同。

### 应用

部分反应进行很慢，不容易直接发生或是对直接测量反应热造成困难的实验，利用盖斯定律可以**间接**把它们的反应热计算出来。

**例如：**
$\ce{C (s) + 1/2O2 (g) = CO (g)}$ 该反应的 $\Delta H$ 无法直接测得。

但下列两个反应的 $\Delta H$ 可以直接测得：

$\ce{C(s) + O2(g) = CO2(g)}\quad①  \qquad \Delta H_1 = -393.5 \text{ kJ/mol}$

$\ce{CO(g) + 1/2O2(g) = CO2(g)}\quad② \qquad \Delta H_2 = -283.0 \text{ kJ/mol}$

在此温度下，$\ce{C(s) + 1/2O2(g) = CO(g)}$ 反应的 $\Delta H = \Delta H_1 - \Delta H_2 = -110.5 \text{ kJ/mol}$

---

**方程式组装要点：**

| 操作类型 | 方程式变化             | $\Delta H$ 变化                |
| :------- | :--------------------- | :----------------------------- |
| **N 倍** | 各物质系数变为 N 倍    | $\Delta H$ 变为 N 倍           |
| **逆写** | 反应物和生成物互换位置 | 等值异号（数值不变，正负改变） |
| **相加** | 多个方程式相加         | $\Delta H$ 相应相加            |

---

**推导过程：**

② 式逆写为 $\ce{CO2(g)=CO(g) +1/2O2(g)}\quad③\qquad\Delta H_3=+283.0\text{ KJ/mol}$

① 式与 ③ 式相加后，消去 $\ce{CO2(g)}$ 和 $\ce{1/2O2(g)}$ ,

方程式变化为：

$\ce{C(s) +1/2O2(g)=CO(g)}\qquad\Delta H=\Delta H_1+\Delta H_3=\Delta H_1-\Delta H_2=-110.5\text{ KJ/mol}$


---

## Original file: 04 原电池.md

---
description: "介绍化学电池的概念、定义及应用。"
---

# 04 · 原电池 <Badge type="warning" text="整理中" />

## 原电池基本概念

日常电能大多数来自火力发电，化学能通过能量转化，间接转化为电能。

**过程如下：**

化学能 $\xrightarrow{\text{燃料燃烧}}$ 热能 $\xrightarrow{\text{蒸汽轮机}}$ 机械能 $\xrightarrow{\text{发电机}}$ 电能

**缺点：** 步骤多、效率低、环境污染

### 原电池——化学能直接转化为电能

**实验过程：**  
| ![图片](image\原电池.png) | ![图片](image\原电池2.png) |
| :---: | :---: |
| 锌和 $\ce{H2SO4}$ 反应，有气泡生成 | 锌片逐渐溶解 <br> (锌失去的电子经导线流向铜片，溶液中的 $\ce{H^+}$ 在铜片表面得电子生成 $\ce{H_2}$) |
| 铜片无反应 | 铜片上有气泡产生<br>(铜只导电，不和稀硫酸反应) |
| 无电流产生 | 导线中有电流通过 |

**定义：** 利用氧化还原反应原理，将化学能转化为电能的装置

$$
电极名称  \begin{cases}
负极& 电子流出，发生氧化反应的电极\\
正极 & 电子流入，发生还原反应的电极\\
\end{cases}
$$

负极失去电子经外电路流入正极的过程中形成电子流，被人类利用  
电子流：负极$\xrightarrow{}$ 正极  
电流：正极$\xrightarrow{}$ 负极

**原电池离子移动：**  
正正负负（正离子往正离子移动，负离子往负极移动，用于调和左右两边的电荷守恒）

### 构成条件

理论上，自发的氧化还原反应均可构成原电池。

1. 有活动性不同的两个电极
2. 溶液：两电极均插入电解质溶液中
3. 导线：两电极用导线相连，形成闭合回路

### 化学电池

**概念：** 化学电池是根据原电池原理，将化学能转变为电能的装置。

**分类：** 可分为一次电池，二次电池和燃料电池。

1. 一次电池:  
   放电后不能再充电使其复原的电池（内部氧化还原反应无法逆向进行）。
2. 二次电池：  
   又称为充电电池或蓄电池，放电后可以再充电，可以多次重复使用。
3. 燃料电池：  
   利用燃料和氧化剂之间发生氧化还原反应，能连续地将燃料和氧化剂的化学能直接转化为电能的化学电池，如氢氧燃料电池，甲醇燃料电池。

### 设计原电池

<div align="center">
<a href="./image\设计原电池.jpg" target="_blank">
  <img src="./image\设计原电池.jpg" width="300">
</a>

</div>

**盐桥**

1. **组成：** 固定剂是琼脂，电解质溶液常见的有饱和 $\ce{KCI}$ 溶液或饱和 $\ce{KNO3}$ 溶液。
2. **作用：** 连接内电路，形成闭合回路，使溶液电荷守恒，便于源源不断产生电流，避免氧化剂，还原剂直接接触，增大化学能，转化成电能的效率。
3. **离子移动的方向：** 阳离子往正极移动，阴离子往负极移动。

**注意：** 原电池装置不一定有盐桥，但高效的原电池以及氧化剂和还原剂均为溶液的电池，一般需要盐桥连接内电路。

### 电极反应式书写

Ⅰ. 写出正负极架构：

 <div align="center">xx物质在负极失 x 电子后变成xx物质：
 
$$\ce{☐ -?e^-\xrightarrow{}\Delta }$$

</div>

<div align="center">xx物质在正极得 x 电子后变成xx物质：

$$\ce{☐ +?e^-\xrightarrow{}\Delta }$$

</div>

得失电子判断方法：看化合价变化

Ⅱ. 调平电荷：

<div align="center">

酸性溶液：$\ce{H^+}$  
碱性溶液：$\ce{OH^-}$  
中性溶液：$\ce{H^+}$ 或 $\ce{OH^-}$  
(具体题目具体分析)  
**例：** 熔融碳酸盐：$\ce{CO_3^2-}$, 熔融氧化物：$\ce{O^2-}$

</div>

Ⅲ. 调平电子：看氢补水，用氧检查 / 看碳补二氧化碳

（用于帮助配平方程式，反应物氢和生成物水之间原子数目守恒，所以氢原子和氧原子有 $2:1$ 的数量关系，看碳补二氧化碳同理）

以下是例题假设和推导过程（条件是编的，重点看推导）

假设是甲烷（$\ce{CH_4}$）和氧气 ($\ce{O_2}$) 的燃料电池,电解液是酸性水溶液

负极电极反应式书写：

1. **判断负极应失电子被氧化，可推出负极为$\ce{CH_4}$**

   <div align="center">

   根据（Ⅰ）推导： $\ce{CH_4}$ 在负极失 $\ce{n}$ 个电子变成 $\ce{CO_2}$  
   $$\ce{CH_4 -?e^--> CO_2}$$
   </div>

2. **根据化合价判断得失电子：**

   <div align="center">

   $\ce{\overset{-4}{C}H_4 -8e^-->\overset{+4}{C}O_2}$
   </div>

3. **调平电荷：**

   <div align="center">

   由于左侧失 $8$ 个电子，又是酸性水溶液，所以左侧加 $8$ 个 $\ce{H^+}$  
   $\ce{CH_4 -8e^- -> CO_2 + 8H^+}$
   </div>

4. **看氢补水，看碳补二氧化碳：**
   <div align="center">  
   
   由于左侧有 $4$ 个氢原子，右侧 $8$ 个，所以左侧加 $2$ 个 $\ce{H_2O}$
   $\ce{CH_4 -8e^- +2H_2O = CO_2 + 8H^+ }$  
   检查 $\ce{O}$ 原子，左2:右2
   </div>    
正极电极反应式书写：

同理

1. **$\ce{O_2}$ 在正极得 $4$ 个电子，变成 $\ce{H_2O}$**

   <div align="center">

   $\ce{O_2 + 4e^- -> H_2O}$
   </div>

2. **调平电荷：**

   <div align="center">

   （理论上想要守恒要右侧加 $\ce{OH^-}$ ，但这是酸性水溶液，所以只能在左侧加 $\ce{H^+}$）  
   $\ce{O_2 + 4e^- + 4H^+ -> H_2O}$
   </div>

3. **看氢补水，看碳补二氧化碳：**
   <div align="center">  
   
   由于右侧有 $2$ 个氢原子，左侧 $4$ 个，所以右侧加 $\ce{H_2O}$   
   $\ce{O_2 + 4e^- + 4H^+ -> 2H_2O}$  
   这里为了和负极电子数一致，所以正极计量数 ×2  
   $\ce{2O_2 + 8e^- + 8H^+ -> 4H_2O}$
   </div>   
最终，把正极合并，消去电子就是总反应式:  
$$\ce{CH_4 + 2O_2 = CO_2 + 2H_2O}$$   
(可以看出 $\ce{CH_4}$ 和 $\ce{O_2}$ 燃烧电池反应式和 $\ce{CH_4}$ 燃烧一样)  
**由此可知 $\ce{CH_4}$ 燃烧：**  
   
   <div align="center">  
   
   化学能 $\xrightarrow{}$ 光能/热能
   </div>

**而 $\ce{CH_4}$ 燃料电池：**

   <div align="center">  
   
   化学能 $\xrightarrow{}$ 电能
   </div>

<div align="center">【恭喜你，学会了原电池电极反应式的书写】</div>


---

## Original file: 05 电解池.md

---
description: "介绍电解池的概念、定义及应用。"
---

# 05 · 电解池 <Badge type="warning" text="整理中" />

## 电解池基本概念

**定义：** 利用电能使非自发的氧化还原反应发生的装置

**能量转换：**

<div align="center">
电能 → 化学能
</div>

**工作原理：**

1. 阴极：发生还原反应，得电子，与外电源负极相接。
2. 阳极：发生氧化反应，失电子，与外电源正极相接。
3. 离子移动：阴离子往阳极移动，阳离子往阴极移动。

**记忆口诀** 正阳氧，负阴还，阴阳相吸

**构成条件：**

1. 有外加电源（可能是直接的外加电源，也可能是原电池）
2. 有导线的两极（电极只要导电即可，对活泼性无要求）
3. 有电解质环境（内环境可以是电解质溶液，还可以是熔融的电解质）
4. 形成闭合回路

**区分方法：**  
|阳极|阴极|  
|:--:|:--:|  
|物质失电子，发生氧化反应|物质得电子，发生还原反应|
|化合价升高的一极|化合价降低的一极|  
|外电路中电子流出的一极|外电路中电子流入的一极|  
|内电路中阴离子移向的一极|内电路中阳离子移向的一极|  
|电势高的一极|电势低的一极|

**补充：**

1. 阴、阳相互矛盾，由于矛盾的对立性，阴阳极的特征往往相反，为了事半功倍，重点记忆一极的现象即可。
2. 矛盾既对立又统一，阴阳电极分别得失的电子数目相同。
3. 注意学科中的联系，充分利用物理学中的电学知识来理解并掌握电化学知识。
4. 电极还有“活性”与“惰性”之分，活性电极参与反应，惰性电极不参与反应，惰性电极一般包括金、铂、石墨，以及其他特殊材料。
5. **记忆“阳极”口诀：** （正痒痒，失声音，子出解）

**正：** 外加电源的正极连接电解池的阳极。<br>
**痒：** 阳极或阳极周围的活性物质被氧化，发生氧化反应，生成氧化产物。<br>
**痒：** 阳极 <br>
**失：** 阳极失去电子，电子流出阳极进入外电路。<br>
**声：** 阳极化合价升高。<br>
**音：** 溶液中的阴离子往阳极移动。<br>
**子：** 电子<br>
**出：** 从阳极流出<br>
**解：** 阳极若为活性电极（如 $\ce{Zn、Cu、Ag}$ 等金属单质）阳极往往会溶解。

**电解池模型：**（以惰性电极电解氯化钠溶液为例）

<div align="center">
 
 <a href="./image\电解池.png" target="_blank">
 <img src="./image\电解池.png" width="250">
 </a>

</div>  
 
**解决电解问题的思维建模：**  
 1. 先根据外加电源的正负极，确定电解池的阴阳极，若阳极为活性电极必须圈出加以强调。  
 2. 将电解池中的离子归类并排序（阳离子一类按氧化性由强到弱排序，阴离子一类按还原性，由强到弱排序）。  
 3. 根据谁强谁优先，以及电极反应式的通式，书写电极反应式。  
 4. 得失电子守恒的基础上加和阴、阳电极反应，即可获得总反应。  
 5. 完成选择题时，先通过“阳极口诀”，确定阳极特征，排除定性选项，再根据得失电子守恒进行定量计算， PH 的变化以及两极溶液的差值计算尽量用排除法确定。

## 电解池电极反应式的书写

**电解池的电极反应式书写和原电池类似，但需要考虑的因素更多**  
**书写关键：**

1. 除了要准确判断阴阳极外，还需要注意“阳极”是惰性还是活性电极。

- 若阳极是活性材料（除石墨、 $\ce{Pt、Au}$ 以外的金属单质，例： $\ce{Zn、Al、Ag}$ 等）一定要圈出加以强调，因为活性阳极会先于电解质环境中的物质放电。

- 若为惰性电极（如石墨 $\ce{Pt、Au}$ 或题目指定为惰性电极）则电极材料只导电，不反应。
- 但若有题干信息或图像信息，一定要仔细审题，石墨电极也可能会发生改变。

2. 需要熟悉阴阳极的放电顺序（即还原性由强到弱的顺序）：  
   阳极放电顺序（即还原剂的还原性由强到弱的顺序）：

- 金属单质（除 $\ce{Pt、Au}$ ）> $\ce{S^2^-}$ > $\ce{SO_3^2^-}$ > $\ce{I^-}$ > $\ce{Fe^2^+}$ > $\ce{Br^-}$ > $\ce{Cl^-}$ > $\ce{OH^-}$ >最高价含氧酸根（如 $\ce{SO_4^2^-}$ 、NO_3^-、ClO_4^-}$ 等
- 注：阳极放电顺序记忆口诀：金（金属单质）、牛（ $\ce{S^2^-}$ ）、雅( $\ce{SO_3^2-}$ )、典( $\ce{I^-}$ )、地铁( $\ce{Fe^2^+}$ )、袖( $\ce{Br^-}$ )、绿( $\ce{Cl^-}$ )、箭( $\ce{OH^-}$ )

阴极放电顺序（即氧化剂的氧化性由强到弱的顺序）氧化剂得 $\ce{e^-}$ 的能力由强到弱的顺序：

$\ce{Ag^+}$ > $\ce{Fe^3^+}$ > $\ce{Cu^2^+}$ > $\ce{H^+}$ (酸) > $\ce{Fe^2^+}$ > $\ce{Zn^2^+}$ > $\ce{H^+}$ (水) > $\ce{Al^3^+}$ 、 $\ce{Mg^2^+}$ 、 $\ce{Na^+}$ 、 $\ce{Ca^2^+}$ 、 $\ce{K^+}$

由于溶液酸碱性离子浓度的相对大小、电极材料等会影响放电顺序，所以一定要先阅读题干信息，再确定反应的物质。

如果电解水中的 $\ce{K^+}$ 、 $\ce{Ca^+}$ 、 $\ce{Na^+}$ 、 $\ce{Mg^2+}$ 、 $\ce{Al^3^+}$ 、 等离子，阴极电极反应式等同电解 $\ce{H_2O}$ :

<div align="center">

$\ce{2H_2O + 2e^- -> H_2 + 2OH^-}$ (放氢生碱)

</div>

若用“惰性电极”电解水溶液中的 $\ce{SO_4^2^-}$ 、 $\ce{NO_3^-}$ 、 $\ce{ClO_4^-}$ 等最高价含氧酸根，阳极电极反应等同电解 $\ce{H_2O}$ :

<div align="center">

$\ce{H_2O -  e^- \to O_2 + H^+ }$ (放氧生酸)

</div>


---

## Original file: index.md

---
description: 本章梳理化学反应热效应和电化学相关知识，包括反应热与焓变、热化学方程式、盖斯定律原电池及电解池等重点内容。
---

# 10 化学反应与能量

<CCChapterOverview />


---



