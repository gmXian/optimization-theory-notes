# Mathematical Programming 学习资料

教材：Melvyn W. Jeter, *Mathematical Programming: An Introduction to Optimization*。

本仓库用于把整本教材整理成适合中文学习、长期复习和 GitHub 发布维护的课程笔记。**最终目标不是教材伴读摘要，而是一套可以脱离教材独立学习的自洽中文课程资料。**

## 仓库结构

每一章固定包含：

- `01_中文笔记.md`：中文主线讲解；必要术语保留英文；定义、定理、结论、证明/推导、算法、完整例题与解答。
- `02_习题与答案_中英双语.md`：按教材原编号整理习题；给出英文忠实重述、中文题意、详细解答、最终答案、验算与易错点。
- `images/`：该章所需图、表、示意图或为理解而重绘的图；Markdown 使用相对路径引用。

## 全书快速导航

| Chapter | 主题 | 中文笔记 | 习题与答案 |
|---|---|---|---|
| 1 | An Introduction to Mathematical Programming | [笔记](01_An_Introduction_to_Mathematical_Programming/01_中文笔记.md) | [习题](01_An_Introduction_to_Mathematical_Programming/02_习题与答案_中英双语.md) |
| 2 | Subspaces, Matrices, Affine/Convex Sets and LP | [笔记](02_Subspaces_Matrices_Affine_Sets_Cones_Convex_Sets_and_the_Linear_Programming_Problem/01_中文笔记.md) | [习题](02_Subspaces_Matrices_Affine_Sets_Cones_Convex_Sets_and_the_Linear_Programming_Problem/02_习题与答案_中英双语.md) |
| 3 | The Primal Simplex Procedure | [笔记](03_The_Primal_Simplex_Procedure/01_中文笔记.md) | [习题](03_The_Primal_Simplex_Procedure/02_习题与答案_中英双语.md) |
| 4 | Duality and the Linear Complementarity Problem | [笔记](04_Duality_and_the_Linear_Complementarity_Problem/01_中文笔记.md) | [习题](04_Duality_and_the_Linear_Complementarity_Problem/02_习题与答案_中英双语.md) |
| 5 | Other Simplex Procedures | [笔记](05_Other_Simplex_Procedures/01_中文笔记.md) | [习题](05_Other_Simplex_Procedures/02_习题与答案_中英双语.md) |
| 6 | Network Programming | [笔记](06_Network_Programming/01_中文笔记.md) | [习题](06_Network_Programming/02_习题与答案_中英双语.md) |
| 7 | Convex and Concave Functions | [笔记](07_Convex_and_Concave_Functions/01_中文笔记.md) | [习题](07_Convex_and_Concave_Functions/02_习题与答案_中英双语.md) |
| 8 | Optimality Conditions | [笔记](08_Optimality_Conditions/01_中文笔记.md) | [习题](08_Optimality_Conditions/02_习题与答案_中英双语.md) |
| 9 | Search Techniques for Unconstrained Optimization | [笔记](09_Search_Techniques_for_Unconstrained_Optimization_Problems/01_中文笔记.md) | [习题](09_Search_Techniques_for_Unconstrained_Optimization_Problems/02_习题与答案_中英双语.md) |
| 10 | Penalty Function Methods | [笔记](10_Penalty_Function_Methods/01_中文笔记.md) | [习题](10_Penalty_Function_Methods/02_习题与答案_中英双语.md) |

根目录重要文件：

- [`STUDY_GUIDE.md`](STUDY_GUIDE.md)：逐章学习与整理流程。
- [`SELF_CONTAINED_NOTE_STANDARD.md`](SELF_CONTAINED_NOTE_STANDARD.md)：**独立学习版笔记的最高优先级硬性标准。**
- [`FORMATTING_GUIDE.md`](FORMATTING_GUIDE.md)：GitHub Markdown、MathJax/LaTeX、图片、例题和习题排版规范。
- [`SYMBOLS_AND_TERMS.md`](SYMBOLS_AND_TERMS.md)：全书数学符号和中英术语统一表。
- [`BOOK_AUDIT.md`](BOOK_AUDIT.md)：整本 PDF 的完整性、缺页、OCR 与结构审计。
- [`PAGE_MAP.md`](PAGE_MAP.md)：PDF 页码 ↔ 教材印刷页码映射。
- [`MISSING_PAGES.md`](MISSING_PAGES.md)：缺失页与知识重建登记。
- [`PREREQUISITES.md`](PREREQUISITES.md)：前置知识与补课路线。
- [`EXERCISE_INDEX.md`](EXERCISE_INDEX.md)：全书 Exercise 编号、页码与完成状态索引。
- [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md)：GitHub 公开发布与版权边界。
- [`FULL_BOOK_REVIEW_REPORT.md`](FULL_BOOK_REVIEW_REPORT.md)：全书第二轮复审范围、修订记录、源异常与最终验收结果。
- [`IMAGE_AUDIT.md`](IMAGE_AUDIT.md)：教材必需图片与视觉完整性复审记录。
- [`RELEASE_NOTES.md`](RELEASE_NOTES.md)：版本里程碑与最终收尾记录。
- [`学习进度.md`](学习进度.md)：章节完成状态。
- `tools/validate_repo.py`：基础 Markdown / 公式定界符 / 图片与本地链接路径静态检查。
- `tools/review_repo.py`：Exercise / Example 覆盖、双语答案覆盖、隐藏控制字符与 LaTeX 环境二级复审。
- `QUARTO_GUIDE.md`：本地预览、完整构建与 GitHub Pages 发布说明。
- `.github/workflows/validate-markdown.yml`：上传 GitHub 后自动执行内容与网站结构检查。
- `.github/workflows/publish-quarto.yml`：`main` 分支更新后构建并部署 GitHub Pages。

## 核心原则

1. **独立学习优先**：读者不需要同时查看教材；笔记必须补齐理解所需的背景、定义、符号、推导、证明、例题条件和章节衔接。
2. **以教材为主线而非依赖教材**：章节顺序、概念命名、公式符号、Example / Exercise 编号与教材保持一致，但教材页码仅用于追溯核验。
3. **面向初学者**：新概念先解释“为什么”，再给正式定义、推导和应用。
4. **中英术语并列**：第一次出现写作“可行解（feasible solution）”。
5. **GitHub 原生可渲染**：数学公式统一使用 Markdown + LaTeX，主要采用 `$...$` / `$$...$$`。
6. **公式人工核对**：不直接相信 PDF OCR；关键公式需与教材页面视觉内容逐式核对。
7. **例题完整**：保留所有必要条件，逐步建模/推导/计算，不只给结论。
8. **习题详细**：中文详细解法 + English solution / final answer；证明题给完整逻辑。
9. **图片可维护**：使用相对路径，图片名使用 ASCII；公开版图片均为原创教学重绘或结构化审计图，重绘脚本与边界说明见 `IMAGE_AUDIT.md`。
10. **教材与补充区分**：额外解释统一标为“学习补充”，不混入教材原有论述。
11. **可追溯**：重要定义、定理、例题和习题尽量记录教材印刷页和 PDF 页码。
12. **先审计后整理**：每章开始前核对页码、缺页、Example / Exercise 连续性。
13. **公开发布友好**：公开 GitHub 版本优先使用忠实重述、原创图和自排版公式，避免无必要的大段教材原文或整页扫描。


## 当前进度

> **全书 Chapter 1–10 已全部完成，并完成第二轮复审与 Quarto 网站化。**
> 当前 **v2.0 公开网站版** 共含 66 张学习图片；原有 17 张教材局部裁图已全部替换，公开构建中教材裁图数量为 0。详见 [`IMAGE_AUDIT.md`](IMAGE_AUDIT.md)。

| 阶段 | 章节 | 状态 | 核心内容 |
|---|---|---|---|
| 线性规划基础 | Chapter 1–2 | ✅ | 数学规划建模、线性代数、仿射/凸集、LP 几何基础 |
| 单纯形与对偶 | Chapter 3–5 | ✅ | primal simplex、artificial variables、duality、dual simplex、LCP、revised/primal-dual/parametric simplex |
| 网络优化 | Chapter 6 | ✅ | network flow、network simplex、max-flow/min-cut、shortest path、Hungarian method |
| 凸分析与最优性 | Chapter 7–8 | ✅ | convex/concave/quasiconvex、Hessian、全局性、Lagrange/KKT、saddle point、QP/LCP |
| 数值优化 | Chapter 9–10 | ✅ | Fibonacci/golden/Powell/DSC/Newton、steepest descent、CG/FR/DFP、penalty/barrier/multiplier methods |

全书 Exercise 索引现覆盖 **292 个编号**；Chapter 7 复审时确认原书还有 Exercise 7.49，已补入索引与答案。每章的教材编号 Examples 均已纳入中文独立学习笔记。详见 [`EXERCISE_INDEX.md`](EXERCISE_INDEX.md) 与 [`学习进度.md`](学习进度.md)。

### 复审中保留的源教材异常

当前扫描源本身存在少数缺页、题号或题面/文字冲突，例如 Chapter 1 pp.14–15 缺失、Chapter 2 的 2.32/2.33 编号映射、3.4(b)、4.16、5.18/5.19、6.13(b)、7.45(a)、9.24、10.6/10.7(a)/10.12(b) 等。仓库原则是：

- 能从视觉页确认的内容按可见源内容处理；
- 源文件自己矛盾时显式标记，不悄悄改题；
- 缺失内容只做“知识性重建”，不冒充原文逐字恢复；
- 数学上可独立检验的结果另外进行验算，并在与源描述冲突时同时保留说明。

完整记录见 [`BOOK_AUDIT.md`](BOOK_AUDIT.md)；本轮复审和修订摘要见 [`FULL_BOOK_REVIEW_REPORT.md`](FULL_BOOK_REVIEW_REPORT.md)。

## GitHub 数学公式规范

最基本写法：

```markdown
设 $x \in \mathbb{R}^n$。

$$
\begin{aligned}
\min \quad & c^\top x \\
\text{s.t.}\quad & Ax \ge b, \\
& x \ge 0.
\end{aligned}
$$
```

完整要求见 [`FORMATTING_GUIDE.md`](FORMATTING_GUIDE.md)。

## 推荐学习方式

1. 先读每章 `01_中文笔记.md` 的“学习目标”和“核心术语”。
2. 按教材小节顺序阅读定义、结论、推导和例题。
3. 遮住答案尝试完成 Example / Exercise。
4. 对照 `02_习题与答案_中英双语.md` 检查。
5. 用“知识地图 + 一页速记”进行第一次复习。
6. 一周后重做代表性习题。

## 本地检查

在仓库根目录运行：

```bash
python tools/validate_repo.py
python tools/review_repo.py
python tools/validate_quarto_structure.py
quarto render
python tools/validate_rendered_site.py
```

两级脚本会检查：

- 块级 `$$` 是否成对；
- 是否出现仓库规范外的数学定界符；
- 本地图片是否存在；
- 是否误写 `/mnt/data`、`sandbox:` 或本机绝对路径；
- 每章固定文件是否完整；
- 图片文件名是否满足建议规范；
- 292 个 Exercise 编号与 English answer 覆盖；
- 83 个教材编号 Example 覆盖；
- 常用 LaTeX 环境是否成对。

这些脚本只能做结构/静态检查，**不能代替数学正确性和教材原页核对**。数学与来源复审记录见 [`FULL_BOOK_REVIEW_REPORT.md`](FULL_BOOK_REVIEW_REPORT.md)。

## 说明

本仓库是学习型二次整理。后续每章内容应明确区分：

- **教材主线**：从教材内容忠实整理而来；
- **学习补充**：为了帮助初学者理解而增加的解释、例子或推导；
- **教学图**：公开版使用原创重绘图或结构化审计图解释数学关系；数据来源、重绘范围和保真边界在 `IMAGE_AUDIT.md` 登记。
