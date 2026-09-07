> **归档说明：** 本文件记录 Chapter 1–6 制作阶段的历史路线，现全书 Chapter 1–10 已完成并复审；仅保留用于追溯，不再作为当前工作清单。

# Chapter 1–6 逐步完成路线图


> **历史阶段说明（2026-08-31）**：本文件记录最初“先完成 Chapter 1–6”的阶段路线。该阶段已全部完成；随后 Chapter 7–10 也已完成并经过全书复审。当前最终状态请以 [`学习进度.md`](学习进度.md) 与 [`FULL_BOOK_REVIEW_REPORT.md`](FULL_BOOK_REVIEW_REPORT.md) 为准。

> 目标：在不依赖教材同步阅读的前提下，把前六章整理成可以独立学习、复习和做题的中文课程资料。为了保障数学正确性，不采用“批量生成后一次性宣布完成”的方式，而是按章节与习题组逐批验收。

## 验收标准

一章只有同时满足以下条件才标记为 `✅ 已完成并核对`：

- `01_中文笔记.md` 可脱离教材独立学习；
- 教材核心定义、定理、推导、Example 均已覆盖；
- `02_习题与答案_中英双语.md` 覆盖该章全部可确认编号的 Exercise；
- 关键公式与教材视觉页面核对；
- 需要的几何图/网络图/算法图已保存到 `images/`；
- Markdown/MathJax/图片相对路径通过仓库静态检查；
- 若教材存在缺页、误号或扫描异常，已在审计文件中登记。

## 当前批次

| 阶段 | 内容 | 状态 |
|---|---|---|
| 1A | Chapter 1 独立学习版 V2 | ✅ 已完成 |
| 1B | Chapter 2 中文笔记独立学习版 V1 | ✅ 已完成 |
| 1C | Chapter 2 Exercises 2.1–2.46 | ✅ 当前 PDF 可确认题面全部完成；⚠️ 2.32/2.33 编号映射待核验 |
| 1D | Chapter 3 中文笔记独立学习版 V1 | ✅ 已完成 |
| 1E | Chapter 3 Exercises 3.1–3.17 | ✅ 已完成；⚠️ 3.4(b) 源题一致性异常已登记 |
| 2A | Chapter 4 — Duality and LCP | ✅ 已完成；⚠️ 4.16 Hint RHS 冲突已登记 |
| 2B | Chapter 5 — Other Simplex Procedures | ✅ 已完成；⚠️ 5.18/5.19 源题一致性异常已登记 |
| 2C | Chapter 6 — Network Programming | ✅ 已完成；⚠️ 6.13(b) 源网络数据/方向一致性异常已登记 |

## 后续章节顺序

### Chapter 3 — The Primal Simplex Procedure ✅ 已完成

1. Primal simplex tableau 与 BFS 移动；
2. entering/leaving variable、ratio test、optimality test；
3. artificial variables / artificial cost coefficients；
4. two-phase method；
5. 全部 Examples；
6. Exercises 3.1–3.17 分组完成并验算。

### Chapter 4 — Duality and the Linear Complementarity Problem ✅ 已完成

1. primal/dual 构造；
2. dual 的经济解释与 sensitivity；
3. post-optimal analysis；
4. dual simplex；
5. complementary slackness；
6. linear complementarity problem；
7. Lemke complementary pivoting；
8. Exercises 4.1–4.33。

### Chapter 5 — Other Simplex Procedures ✅ 已完成

1. tableau revisited；
2. revised simplex；
3. product form / elimination form of inverse；
4. primal-dual algorithm；
5. parametric LP；
6. degeneracy/cycling；
7. decomposition/reinversion；
8. Exercises 5.1–5.25。

### Chapter 6 — Network Programming ✅ 已完成

1. network flow LP formulation；
2. graph theory 最小前置知识；
3. network simplex / transshipment；
4. maximal flow 与 max-flow min-cut；
5. primal-dual network procedures、shortest path、Dijkstra、Hungarian method；
6. Exercises 6.1–6.26 全部完成；
7. 6 张原创网络/算法图；
8. Exercise 6.13(b) 的当前扫描网络数据与可见弧方向存在一致性异常，已按源文件可见内容登记，不擅自修题。

## Chapter 1–6 阶段结论

截至当前版本，Chapter 1–6 已全部达到本路线图定义的独立学习验收标准。仍存在的 2.32/2.33、3.4(b)、4.16、5.18/5.19、6.13(b) 等项目属于**源教材/扫描版本核验项**，不是仓库遗漏；对应答案均保留当前可见题面并显式说明冲突。

## 为什么按这种粒度推进

前六章并不是六篇互不相关的摘要：Chapter 2 的基本解和凸几何是 Chapter 3 单纯形法的底层语言；Chapter 3 的表结构又直接进入 Chapter 4–5；Chapter 6 则是对 LP 结构的网络化专门化。若前面的符号、基矩阵、BFS、约化成本等概念写得含糊，后续章节会连锁出错。因此仓库采用“完成一组—核对一组—再向前推进”的方式。
