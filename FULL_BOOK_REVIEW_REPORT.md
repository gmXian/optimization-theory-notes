# 全书第二轮复审报告 / Full-Book Review Report

> 复审对象：Melvyn W. Jeter, *Mathematical Programming: An Introduction to Optimization* 学习仓库。  
> 复审日期：2026-08-31。  
> 当前结论：**Chapter 1–10 的独立学习版笔记与习题答案均已完成，并完成第二轮复审。**

## 1. 这次“复审”具体检查了什么

本轮复审不是只运行 Markdown 语法检查，而是分成四层：

1. **来源层（source review）**
   - 对照当前教材 PDF 的章节、Section、Example、Exercise 编号与印刷页码；
   - 对高风险页面重新查看页面视觉内容，而不是只相信 OCR；
   - 对缺页、题号跳变、公式符号冲突、题面与提示矛盾建立可追溯记录；
   - 不把模型推测悄悄写成教材原文。

2. **数学层（mathematical review）**
   - 复查定义、定理条件、结论方向、KKT/duality/simplex 符号约定；
   - 对容易受 OCR 影响的指数、根号、分数、不等号方向和矩阵重新核对；
   - 对关键数值题重新代入、求导、解线性系统或独立计算验证；
   - 当扫描题面与数学结论冲突时，同时保留“可见源题面”和“按该题面得到的数学结果”。

3. **独立学习层（self-contained review）**
   - 检查 Chapter 1–10 是否可以不同时打开教材直接学习；
   - 关键概念首次出现时补充术语、直觉、符号和必要前置知识；
   - 教材编号 Example 均进入中文笔记，避免只写“见教材 Example x”；
   - Exercises 均保留编号、中文完整解答，并提供 English answer / concise solution；
   - 教材内容、缺页重建与学习补充保持区分。

4. **GitHub / 仓库层（repository review）**
   - 检查 MathJax 定界符、图片相对路径、目录结构、绝对本地路径和隐藏控制字符；
   - 检查 10 章的固定文件和图片目录；
   - 检查 Exercise / Example 编号覆盖；
   - 新增二级复审脚本 `tools/review_repo.py`，并将其加入 GitHub Actions。

> [!NOTE]
> 自动脚本可以证明“结构和覆盖检查通过”，但不能形式化证明仓库中每一个数学句子都无误。因此，本报告把“自动检查”和“人工/语义数学复审”明确分开。

## 2. 最终覆盖范围

### 2.1 章节

| Chapter | 主题 | 中文笔记 | 习题答案 | 复审 |
|---|---|---|---|---|
| 1 | An Introduction to Mathematical Programming | ✅ | ✅ 1.1–1.10 | ✅ |
| 2 | Subspaces, Matrices, Affine/Convex Sets, LP | ✅ | ✅ 可见题块 / 2.1–2.46 索引 | ✅/⚠️ |
| 3 | The Primal Simplex Procedure | ✅ | ✅ 3.1–3.17 | ✅/⚠️ |
| 4 | Duality and the Linear Complementarity Problem | ✅ | ✅ 4.1–4.33 | ✅/⚠️ |
| 5 | Other Simplex Procedures | ✅ | ✅ 5.1–5.25 | ✅/⚠️ |
| 6 | Network Programming | ✅ | ✅ 6.1–6.26 | ✅/⚠️ |
| 7 | Convex and Concave Functions | ✅ | ✅ 7.1–7.49 | ✅/⚠️ |
| 8 | Optimality Conditions | ✅ | ✅ 8.1–8.28 | ✅ |
| 9 | Search Techniques for Unconstrained Optimization | ✅ | ✅ 9.1–9.43 | ✅/⚠️ |
| 10 | Penalty Function Methods | ✅ | ✅ 10.1–10.15 | ✅/⚠️ |

按教材编号上界统计，当前 Exercise 索引共 **292 个编号**。Chapter 7 在本轮视觉复审时确认还有 Exercise **7.49**，因此早期的 291 已修正为 292。

### 2.2 教材编号 Examples

本仓库检查的教材编号 Example 数量为：

| Chapter | Example 数 |
|---|---:|
| 1 | 7 |
| 2 | 18 |
| 3 | 14 |
| 4 | 8 |
| 5 | 9 |
| 6 | 5 |
| 7 | 5 |
| 8 | 2 |
| 9 | 10 |
| 10 | 5 |

合计 **83 个教材编号 Examples**，均在对应 `01_中文笔记.md` 中出现并纳入讲解。

### 2.3 图片

当前 10 章共包含 **66 个学习图片文件**。v2.0 公开网站化时，原学习版中对网络拓扑、权重、坐标或源题异常高度敏感的 17 张教材局部裁图已全部替换为原创教学重绘或结构化审计图。Markdown 全部使用相对路径，数学公式仍保持 LaTeX 文本而不是截图；逐图范围与已知边界见 `IMAGE_AUDIT.md`。

## 3. 第二轮复审的重要修订

下面只列会实质影响学习结论或仓库质量的修订，不枚举纯措辞和排版调整。

### Chapter 1

- 继续保留并明确标记教材印刷页 **pp.14–15** 缺失；
- 缺失部分仍采用“知识性重建”，不声称逐字恢复原页；
- Chapter 1 V2 保持“脱离教材可学习”的前置知识、Example、图示和自测结构。

### Chapter 2

- 再次核对第一道习题扫描显示为 `1.2` 的源编号异常；仓库按章节连续性记作 2.1，同时保留说明；
- 2.32 / 2.33 的当前扫描仍不能安全恢复精确题号映射：可见未编号 polyhedron 题块已经求解，但**不人为把两个编号强配给某两道题**；
- 为此前只含中文的后半段习题补充 `English concise solutions`，保持“中文详细 + 英文结论”的双语标准。

### Chapter 3

- 3.4(b) 保留源题“应有 infinitely many solutions”与可见公式实际给出唯一最优点之间的冲突；
- 补齐 Exercise 3.13 的 English answer；
- Big-M、two-phase、post-optimal 的符号和判据继续与前文统一。

### Chapter 4

- 把原先依赖 Chapter 3 上下文的 Example 1 补成**自包含版本**，在本章直接给出 primal、basis、$B^{-1}$、dual vector 和 objective equality；
- 4.16 的可见题面 RHS=16 与 Hint RHS=20 冲突继续显式登记；
- 新增完整 `English concise solutions — Exercises 4.1–4.33`，使整章习题真正满足中英双语要求。

### Chapter 5

- 复核 revised simplex / product form / elimination form / primal-dual / parametric LP 的关系；
- 5.18 当前扫描的第三式与“必然 cycling”叙述无法同时成立，保留可见公式并说明；
- 5.19 按可见方程组会得到不可行性，与 “can cycle” 叙述冲突，继续作为源教材异常保留；
- 原有 `English concise solutions — Exercises 5.1–5.25` 保留。

### Chapter 6

- 复查 node–arc incidence matrix、tree–basis 对应、network simplex reduced cost、max-flow/min-cut、shortest path、Hungarian method 的符号一致性；
- 6.13(b) 当前网络图的可见弧方向与 $b_6>0$ 数据存在可验证冲突，不补画不存在的弧；
- 26/26 编号 Exercise 和图片路径完整。

### Chapter 7

- 确认教材习题实际到 **7.49**，补入答案与索引；
- 把 Examples 1–5 扩成自包含例题，重新核对二次型、Hessian、strict convexity 和 Example 5 顶点/目标值；
- 修正 7.47(b) 的严格拟凸反例；
- 重写 7.48(b)(c) 的逻辑，使 pseudoconvex → strictly quasiconvex → quasiconvex 的证明更严谨；
- 对 7.45(a) 做来源一致性复审：按教材给出的 quasiconvex 定义，题面“若局部最小非全局，则在整个 neighborhood 恒定”过强。答案给出反例，并保留可可靠证明的较弱结论（例如 strict local minimum 必为 global minimum）。

### Chapter 8

- 恢复并复核教材真正的 Examples 1–2，而不是用学习补充例子替代教材 Example；
- 复核 Exercise 8.23 四个 quadratic-programming 数值矩阵与解；
- 统一 KKT、Lagrangian、saddle point、QP → LCP 的符号和最大/最小化约定；
- 新增完整 `English concise solutions — Exercises 8.1–8.28`。

### Chapter 9

- 对 10 个教材 Examples 逐一保留，并对一维搜索中的高风险根号、分数指数、区间和导数重新核验；
- 9.15 修正为可见四次多项式，得到 $x^*=-1,f^*=-11$；
- 9.16 复核 $x^{1/3}(x-7)^2$ 的最大点 $x=1$；
- 9.20 区分教材有限步数值近似与真正驻点数值；
- 9.24 明确：可见题面要求 **minimize** $x\cos x$ on $[0,2]$，内部根约 $0.86033$ 实为最大点，字面最小值在端点 $x=2$；
- 9.26 修正先前错误因式分解，正确最小点为 $(7-\sqrt{17})/4$；
- 9.28 登记 “see Example 7” 与实际 Example 6 的交叉引用异常；
- 新增完整 `English concise solutions — Exercises 9.1–9.43`。

### Chapter 10

- 复核 exterior penalty、barrier、quadratic penalty、method of multipliers / augmented Lagrangian 的参数与符号；
- Exercise 10.5(f) 重新完整求解。源题为
  $$
  \min x_1x_2+\ln x_3
  $$
  在给定球约束、$x_2+x_3^4=4$、$x_1\ge0,x_3\ge1$ 下，旧答案 $(0,3,1)$ 并非最优；重新约化后数值最优约为
  $$
  x\approx(6.97774110,-6.92858485,1.81819719),
  $$
  $$
  f^*\approx-47.74802587.
  $$
- 10.6 可见练习中的 barrier 符号与本章 Theorem 2 的符号作用冲突；答案按定理一致的标准 barrier 证明，并明确标出扫描冲突；
- 10.7(a) 的 equality constraint 与 Section 2 的 strict-interior inequality barrier 框架不兼容；不给出“假装可直接套用”的解法；
- 10.12(b) 可见交叉引用 `Exercise 9.5` 与 multiplier-method 上下文明显不匹配，保留而不擅自改成 `10.5`。

## 4. 已知源教材 / 扫描异常

这些项目**不是仓库未完成项**，而是当前 PDF 本身无法在不猜测的情况下唯一修复的地方。完整证据见 [`BOOK_AUDIT.md`](BOOK_AUDIT.md)。

1. Chapter 1：印刷 pp.14–15 缺失；
2. Chapter 2：首题扫描显示 `1.2`；2.32/2.33 题号映射不确定；
3. Chapter 3：3.4(b) 与题目“infinitely many”说明冲突；
4. Chapter 4：4.16 RHS=16 / Hint RHS=20；
5. Chapter 5：5.18、5.19 的可见公式与 cycling 文字冲突；
6. Chapter 6：6.13(b) 网络可见弧方向与节点净供给数据冲突；
7. Chapter 7：7.45(a) 在教材当前假设下结论过强；
8. Chapter 9：9.24 的 “minimize” 与内部驻点类型冲突；9.28 Example 交叉引用编号异常；
9. Chapter 10：10.6 barrier 符号冲突；10.7(a) 方法适用域冲突；10.12(b) 跨章引用异常。

处理原则统一为：**保留可见来源 + 给出可验证数学结论 + 显式说明冲突，不静默改题。**

## 5. 双语完整性复审

用户要求习题答案为中英文版。复审发现早期部分章节虽然标题写“中英双语”，但实际有些习题只有中文详细推导。此次已经统一处理：

- Chapter 1：每题已有 English answer；
- Chapter 2：1–12 原有英文部分，13–46 补充 consolidated English concise solutions；2.32/2.33 用英文明确说明源编号无法安全映射；
- Chapter 3：补齐遗漏的 3.13 English answer；
- Chapter 4：新增 4.1–4.33 全套 English concise solutions；
- Chapter 5：保留原有 5.1–5.25 English concise solutions；
- Chapter 6：每题已有 English answer；
- Chapter 7：每题已有 English answer；
- Chapter 8：新增 8.1–8.28 全套 English concise solutions；
- Chapter 9：新增 9.1–9.43 全套 English concise solutions；
- Chapter 10：每题已有 English concise answer / final answer。

英文部分采用“**concise solution / final answer**”而中文部分保持详细初学者推导，避免为了双语而把整份答案机械重复一遍。

## 6. GitHub 与自动检查

仓库提供两级检查：

```bash
python tools/validate_repo.py
python tools/review_repo.py
```

`validate_repo.py` 负责基础 Markdown / MathJax / 图片路径 / 目录检查。  
`review_repo.py` 额外检查：

- 隐藏控制字符；
- 公式块定界符；
- 10 章目录结构；
- 292 个 Exercise 编号覆盖；
- 每个 Exercise 的英文答案覆盖；
- 83 个教材编号 Example 覆盖；
- 全书复审报告等根目录文件是否存在。

`.github/workflows/validate-markdown.yml` 已更新为在 GitHub Actions 中同时运行两级检查。

## 7. 如何理解“完成”

本仓库的“完成”含义是：

- Chapter 1–10 都已有正式中文独立学习笔记；
- 教材编号 Example 已纳入笔记；
- 教材 Exercise 编号已纳入答案文件，且中文详细解答 + English concise answer 的双语要求已落实；
- 高风险数学和扫描歧义经过第二轮复查；
- 图片、MathJax 和仓库结构经过自动验证；
- 当前 PDF 无法唯一修复的源异常被保留为公开审计项。

“完成”**不**意味着把源教材矛盾强行修成某个猜测版本，也不意味着自动脚本可以替代形式化数学证明检查。后续若获得另一版/纸质版教材，最有价值的第三轮工作不是重写整仓库，而是专门核验 [`BOOK_AUDIT.md`](BOOK_AUDIT.md) 中的 ⚠️ 项。

## 8. 最终自动验收结果

在最终打包前执行：

```text
$ python tools/validate_repo.py
Errors: 0
Warnings: 0

$ python tools/review_repo.py
Coverage errors: 0
Coverage warnings: 0
```

此外，仓库级 placeholder 扫描未发现 `TODO`、`TBD`、`待补`、`待完成` 等遗留占位标记。最终 ZIP 还会单独执行压缩完整性测试。
