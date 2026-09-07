# MISSING_PAGES - 缺失页与重建登记

> 原则：**不伪造原文，不把推断写成教材逐字内容。**
> 
> 缺页处理分为：`原版核验恢复` / `高置信度知识重建` / `学习补充`。所有重建内容在章节笔记中必须显式标记。

## 状态说明

- `🔴 已确认缺页`：PDF 中对应印刷页正文确实不存在。
- `🟨 重建中`：已确定知识边界，正在根据前后文和可靠来源重建。
- `🟦 知识重建完成`：知识链已补齐并可用于学习，但未声称恢复缺失页逐字原文。
- `🟩 已核验`：已找到可靠版本或充分证据完成重建并复核。
- `⚪ 待核验`：怀疑异常，但当前证据不足。

## MP-001 - Chapter 1 pp.14-15

| 项目 | 内容 |
|---|---|
| 状态 | 🔴 已确认缺页；🟦 知识重建完成（未恢复逐字原文） |
| 教材印刷页 | pp.14-15 |
| PDF 页 | pp.33-34 |
| PDF 当前内容 | Taylor & Francis 占位页 |
| 所属章节 | Chapter 1 - An Introduction to Mathematical Programming |
| 涉及小节 | Example 7 收尾；Section 3 `Global and Local Solutions` |
| 置信度 | “缺页事实”高；“具体原文字句”未知 |

### 可由当前教材直接支持的边界信息

- 印刷页 p.13 的 Example 7 讲 quadratic programming / portfolio selection，并在说明投资比例与风险时中途断开。
- 目录说明 Section 3 `Global and Local Solutions` 从 p.14 开始，Section 4 从 p.16 开始。
- p.16 一开始继续讨论集合相关概念，包括 boundary point、closed set、accumulation point，说明 pp.14-15 中已经引入了为局部最优定义服务的邻域/集合基础概念。
- Chapter 1 Exercise 1.8 要求证明线性规划的局部最优解必为全局最优解；Exercises 1.9-1.10 考查 interior、boundary、open/closed、accumulation point 等概念。

### 重建结果（2026-08-30）

- 已在 Chapter 1 `01_中文笔记.md` 中补齐 Example 7 的知识续接、global/local optimum、neighborhood、interior/open set，以及与 p.16 连续的 boundary/closed/accumulation point 概念。
- 已完成 Exercises 1.8–1.10 的完整证明/解答。
- 已生成全局/局部最优与集合拓扑自绘图。
- 当前仍不声称恢复了 pp.14–15 的逐字原文；若以后找到完整合法版本，可进一步逐项核对。

### 重建规则

Chapter 1 正式笔记中：

1. 先恢复 **知识链**，不声称逐字恢复原教材；
2. 所有重建段落使用 `🧩 缺失页重建` 标签；
3. 若使用其他版本/公开预览核验，记录来源与核验日期；
4. 若原教材证明不可得，补充证明统一标为 `💡 学习补充`；
5. 不把出版社占位页截图上传到公开仓库。

## 待继续监控的非缺页异常

这些问题目前不登记为“缺页”，但在正式章节整理时必须处理：

- Chapter 2 Exercise 2.1 的扫描编号异常（图像显示 `1.2`）。
- Chapter 2 Section 3 Exercises 起始编号存在未显示/不清晰现象，2.32 与 2.33 需外部版本核验。
- OCR 中大量公式符号与 Exercise 10.9 等编号存在识别错误。
