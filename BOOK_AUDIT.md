# BOOK_AUDIT - 教材完整性与可用性审计

> 审计对象：Melvyn W. Jeter, *Mathematical Programming: An Introduction to Optimization*（当前学习用 PDF）。  
> 本文件用于记录 **PDF 本身的结构问题**。它不是教材内容摘要，也不把 OCR 文本视为权威原文。

## 1. 审计结论摘要

- PDF 总页数：**361 页**。
- 教材正文从 **PDF 第 20 页 = 教材印刷页 p.1** 开始。
- 正文与索引阶段的页码映射保持稳定：**教材印刷页 = PDF 页码 - 19**。
- 当前自动检测 + 页面视觉复核发现：**教材印刷页 pp.14-15（PDF pp.33-34）正文缺失**，现有 PDF 中这两页被 Taylor & Francis 占位页替代。
- 除 pp.14-15 外，正文/索引范围未发现其他“整页空白或占位替换”的明显缺页候选。
- 前置页中的 PDF pp.13、17、19 属于版式/出版空白页，不计入教材正文缺页。
- 本 PDF 有 OCR/文本层，但数学公式、下标、不等号、希腊字母、Exercise 编号存在识别错误；**后续笔记禁止直接复制 OCR 公式**。

> [!IMPORTANT]
> “未发现其他明显整页缺失”不等于“全书所有公式、图表、局部扫描都无损”。每章正式整理前仍需要做 **章节级逐页复核**。

## 2. 审计方法

本次预检使用了三种互补方式：

1. **PDF 结构检查**：页数、书签/Outline、页面可打开性。
2. **文本层检查**：逐页提取文本长度，寻找正文阶段异常空页。
3. **视觉密度检查**：低分辨率渲染后统计非白像素比例，避免把“只有图片/表格但 OCR 很少”的页面误判为空白页。

正文阶段视觉/文本双重异常候选只有：

| PDF 页 | 教材印刷页 | 文本长度 | 视觉非白密度 | 结论 |
|---:|---:|---:|---:|---|
| 33 | 14 | 0 | 0.0132 | 缺失正文 / 出版社占位页 |
| 34 | 15 | 0 | 0.0132 | 缺失正文 / 出版社占位页 |

## 3. 已确认缺失内容

详见 [`MISSING_PAGES.md`](MISSING_PAGES.md)。当前确认：

- **MP-001：Chapter 1，印刷页 pp.14-15 / PDF pp.33-34**。

判断依据：

- 印刷页 p.13（PDF p.32）的 Example 7 在句子中途结束；
- PDF pp.33-34 均为 Taylor & Francis 占位页；
- 目录/书签显示 Section 3 `Global and Local Solutions` 应从印刷页 p.14 开始；
- 印刷页 p.16（PDF p.35）正文直接从点集拓扑术语继续，并开始 Section 4。

因此这里不是普通空白页，而是 **两页正文内容丢失**。

> 进展（2026-08-30）：Chapter 1 的知识性重建已完成，详见 `MISSING_PAGES.md` 与 Chapter 1 正式笔记；仍不声称恢复缺页逐字原文。

## 4. Exercise 编号与 OCR 异常

当前预检发现若干“编号层异常”，它们不一定代表正文缺失：

- Chapter 2 第一组习题的第一题，在当前扫描图像上显示为 **`1.2`**，但根据所在章节及后续 `2.2, 2.3, ...` 的连续性，仓库索引统一规范为 **Exercise 2.1**，并保留来源异常说明。
- Chapter 2 Section 3 的习题起始处，当前扫描在 `Exercises` 后出现一个未显示题号的题块，随后直接出现 `2.34`。因此 **2.32 / 2.33 的编号与内容对应关系暂不能仅凭当前 PDF 安全确定**，已在 `EXERCISE_INDEX.md` 标为待外部版本核验。
- Exercise 10.9 在 OCR 文本层中被误识别为类似 `^0.9`，但上下文连续，属于 OCR 错误，不视为缺题。
- Chapter 3 Exercise 3.4 的总要求称两个小题都应有 infinitely many optimal solutions；但当前扫描件 3.4(b) 可见约束按字面求解得到唯一最优点 $(30/17,10/17)$、最优值 20。当前仓库将其登记为 **题面/版本一致性异常**，不擅自修改不等号或成本系数。
- Chapter 4 Exercise 4.16 的题面写作 $3x_1+6x_2-x_5=16$，但同题 Hint 又要求将其“改写”为 $3x_1+6x_2-x_5+x_8=20$；两式并不等价，而且紧随其后的 Exercise 4.17 才明确使用右端项 20。仓库因此将 **4.16 的 Hint 右端项冲突**登记为源教材/版本一致性异常：4.16 按可见题面 RHS=16 求解，同时在答案中保留冲突说明，不擅自把题面改为 20。
- Chapter 5 Exercise 5.18 的当前扫描图像明确显示第三个等式为 $x_3+x_7=0$，但题目紧接着声称按指定 pivot rule “basis matrices will cycle”。按该可见题面逐式计算，原点是最优解且指定规则并不能复现其“必然 cycling”断言。仓库因此按 **当前扫描字面题面** 给出答案，同时把该不一致登记为源教材/版本异常，不擅自把 RHS 改成经典 cycling 示例中的其他数值。
- Chapter 5 Exercise 5.19 的当前扫描方程组按字面消元得到 $x_2=(x_4-1)/8$ 与 $x_3=(3-27x_4)/8$，非负性要求同时 $x_4\ge1$ 与 $x_4\le1/9$，因此当前题面不可行；但教材随后又写 “This problem ... can cycle.”。仓库将其登记为 **题面/文字说明一致性异常**，不修改可见公式。
- Chapter 6 Exercise 6.13(b) 的当前扫描网络图与题面数据存在可验证的一致性异常：按教材本章约定 $b_i>0$ 表示 source（净流出），图中节点 6 的可见数据为 $b_6=34>0$，但当前扫描图中没有可供其净流出的可见出弧，因此按字面数据无法满足 $Ax=b$。仓库将其登记为 **源网络数据/弧方向一致性异常**；正式答案不擅自反转全体 $b$ 的符号、补画弧或改变弧方向，只在“核验说明”中讨论可能的版本差异。
- Chapter 7 的习题实际延伸到 **Exercise 7.49**（印刷页 p.245 / PDF p.264）。早期索引只统计到 7.48，复审后已补入 7.49，因此全书按最大题号统计的 Exercise 总数由 291 修正为 **292**。
- Chapter 7 Exercise 7.45(a) 的可见题面声称 quasiconvex 函数的 relative minimum 若非 global minimum，则函数在该点某个 neighborhood 内为常数。按教材本章给出的标准 quasiconvex 定义，仅能推出“沿通向更低点的充分短线段为平台 / strict local minimum 必为 global minimum”；“整个 neighborhood 恒定”在现有假设下存在反例。仓库已在答案中给出一维 quasiconvex 反例，并将该条登记为 **源命题假设/结论一致性问题**，不把过强结论当成已证明事实。
- Chapter 9 Exercise 9.24 的扫描题面明确要求用 false-position method 在 $[0,2]$ 上 **minimize** $f(x)=x\cos x$；但区间内唯一导数零点 $x\approx0.860333589$ 是局部最大点，字面最小值实际出现在端点 $x=2$。仓库保留 `minimize` 原文事实，并在答案中要求 stationary-point 分类与端点比较；不静默改成 `maximize`。
- Chapter 9 Exercise 9.28 的扫描题尾写 “see Example 7”，但相同函数 $x\sqrt{2+x}$ 实际是本章 **Example 6** 的内容。该处作为交叉引用编号异常登记，不影响题面求解。
- Chapter 10 Exercise 10.6 的可见题面使用 $f-(1/\beta_k)b$，而 Section 2 / Theorem 2 的 barrier subproblem 使用 $f+(1/\beta_k)b$，且教材定义的 reciprocal barrier 在边界趋于 $+\infty$。两者符号作用相反。仓库按 Theorem 2 一致的正号版本给出标准证明，同时明确保留扫描负号冲突。
- Chapter 10 Exercise 10.7(a) 要求对等式约束 $x_1^2+x_2=10$ 使用 barrier method；但 Section 2 明确只处理 $g_i(x)\le0$ 且具有非空严格内部的模型，并明确排除 equality constraints。仓库将其登记为 **方法适用域/题面一致性问题**，给出原问题正确解，并把“将等式近似为双边窄带后使用 barrier”仅标作学习补充。
- Chapter 10 Exercise 10.12(b) 的扫描件明确写 “problems in Exercise 9.5”。Chapter 9 Exercise 9.5 是无约束一维搜索题，与 method of multipliers 的上下文不匹配。仓库不擅自把它替换成 `10.5`，按可见交叉引用解释其退化含义，并登记为 **跨章引用异常**。


## 5. PDF 书签与章节结构

PDF 自带书签较完整，可用于章节定位。下表列出正文中的 Chapter / Section 起始位置：

| 层级 | 标题 | PDF 页 | 教材印刷页 |
|---|---|---:|---:|
| Chapter | Chapter 1: AN INTRODUCTION TO MATHEMATICAL PROGRAMMING | 20 | 1 |
| Section | 1. The Mathematical Programming Problem | 20 | 1 |
| Section | 2. Examples of Mathematical Programming Problems | 21 | 2 |
| Section | 3. Global and Local Solutions | 33 | 14 |
| Section | 4. Post-Optimal Analysis, Parametric Programming, and Stability | 35 | 16 |
| Section | 5. Some Historical Comments | 42 | 23 |
| Section | References | 44 | 25 |
| Chapter | Chapter 2: SUBSPACES, MATRICES, AFFINE SETS, CONES, CONVEX SETS, AND THE LINEAR PROGRAMMING PROBLEM | 46 | 27 |
| Section | 1. A Review of Elementary Linear Algebra | 47 | 28 |
| Section | 2. Affine and Convex Sets | 70 | 51 |
| Section | 3. The Linear Programming Problem | 84 | 65 |
| Section | References | 99 | 80 |
| Chapter | Chapter 3: THE PRIMAL SIMPLEX PROCEDURE | 100 | 81 |
| Section | 1. The Primal Simplex Procedure | 100 | 81 |
| Section | 2. Artificial Variables and Artificial Cost Coefficients | 118 | 99 |
| Section | 3. Artificial Variables and the Two-Phase Method | 128 | 109 |
| Section | References | 136 | 117 |
| Chapter | Chapter 4: DUALITY AND THE LINEAR COMPLEMEN- TARITY PROBLEM | 137 | 118 |
| Section | 1. Dual Linear Programming Problems | 137 | 118 |
| Section | 2. Interpretation of the Dual Problem (Post-Optimal Analysis) | 145 | 126 |
| Section | 3. Post-Optimal Analysis | 145 | 126 |
| Section | 4. The Dual Simplex Procedure | 149 | 130 |
| Section | 5. Complementary Slackness | 154 | 135 |
| Section | 6. The Linear Complementarity Problem | 155 | 136 |
| Section | 7. Lemke’s Complementary Pivoting Algorithm | 156 | 137 |
| Section | References | 161 | 142 |
| Chapter | Chapter 5: OTHER SIMPLEX PROCEDURES | 163 | 144 |
| Section | 1. The Primal Simplex Tableau Revisited | 163 | 144 |
| Section | 2. The Revised Simplex Procedure | 165 | 146 |
| Section | 3. The Product Form of the Inverse | 167 | 148 |
| Section | 4. The Elimination Form of the Inverse | 169 | 150 |
| Section | 5. The Primal-Dual Algorithm | 174 | 155 |
| Section | 6. Parametric Linear Programming | 180 | 161 |
| Section | 7. Degeneracy and Cycling | 188 | 169 |
| Section | 8. Decomposition | 189 | 170 |
| Section | 9. Reinversion | 190 | 171 |
| Section | References | 193 | 174 |
| Chapter | Chapter 6: NETWORK PROGRAMMING | 195 | 176 |
| Section | 1. Linear Network Flow Problems | 195 | 176 |
| Section | 2. Some Basic Graph Theory | 200 | 181 |
| Section | 3. The Network Simplex Procedure for the Transshipment Problem | 204 | 185 |
| Section | 4. The Maximal Flow Problem | 216 | 197 |
| Section | 5. Primal Dual Procedures for Network Flow Problems | 223 | 204 |
| Section | References | 232 | 213 |
| Chapter | Chapter 7: CONVEX AND CONCAVE FUNCTIONS | 234 | 215 |
| Section | 1. Introduction | 234 | 215 |
| Section | 2. Convex Functions of One Real Variable | 242 | 223 |
| Section | 3. Some Topics from Calculus | 246 | 227 |
| Section | 4. Convex Functions of Several Variables | 249 | 230 |
| Section | 5. Optimization of Convex Functions | 254 | 235 |
| Section | 6. Quasiconvex Functions and Other Generalizations | 260 | 241 |
| Section | References | 265 | 246 |
| Chapter | Chapter 8: OPTIMALITY CONDITIONS | 266 | 247 |
| Section | 1. Unconstrained Problems | 266 | 247 |
| Section | 2. Nonnegative Variables | 268 | 249 |
| Section | 3. Equality Constraints | 270 | 251 |
| Section | 4. Nonnegative Variables and Equality Constraints | 274 | 255 |
| Section | 5. Nonnegative Variables and Inequality Constraints | 275 | 256 |
| Section | 6. The Kuhn-Tucker Theorem | 279 | 260 |
| Section | References | 285 | 266 |
| Chapter | Chapter 9: SEARCH TECHNIQUES FOR UNCONSTRAINED OPTIMIZATION PROBLEMS | 287 | 268 |
| Section | 1. One-Dimensional Linear Search Techniques | 287 | 268 |
| Section | 2. Linear Search Techniques by Curve Fitting | 304 | 285 |
| Section | 3. Linear Search Techniques for Differential Functions by Curve Fitting | 313 | 294 |
| Section | 4. Multidimensional Search Techniques | 319 | 300 |
| Section | References | 333 | 314 |
| Chapter | Chapter 10: PENALTY FUNCTION METHODS | 334 | 315 |
| Section | 1. Introduction | 335 | 316 |
| Section | 2. Barrier Function Methods | 342 | 323 |
| Section | 3. The Quadratic Penalty Function Method | 347 | 328 |
| Section | References | 355 | 336 |

## 6. 后续章节级审计规则

正式写某章笔记前，必须再检查：

- 印刷页码是否连续；
- Example 是否跨页被截断；
- 定理/证明是否在页首或页尾突然断裂；
- 公式编号是否出现无法解释的跳号；
- Exercises 是否存在编号缺失、OCR 误号或跨页漏题；
- 图、表、网络图、几何图是否完整；
- 页面视觉内容与 OCR 文本是否一致。

发现新问题后先更新本文件与 `MISSING_PAGES.md`，再继续写笔记。
