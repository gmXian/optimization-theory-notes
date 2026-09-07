# 教学图片复审报告

> 复审目标：保证“只看网站即可学习/复算”所需的视觉信息完整，同时确保公开版本不直接发布教材扫描图。

## 1. 最终结论

**A 级与 B 级视觉缺口均已补齐；公开构建中的教材裁图数量为 0。**

当前仓库共有 **66 张学习图片**（不计各 `images/README.md`）。原学习版中的 17 张教材 PDF 局部裁图已经全部替换为原创教学重绘或结构化审计图，文件名保持不变，因此正文链接无需迁移。

| Chapter | 图片文件数 | 状态 |
|---|---:|---|
| 1 | 3 | 通过 |
| 2 | 15 | 通过；4 张公开版重绘 |
| 3 | 4 | 通过 |
| 4 | 5 | 通过 |
| 5 | 5 | 通过 |
| 6 | 12 | 通过；6 张公开版重绘 |
| 7 | 7 | 通过；5 张公开版重绘 |
| 8 | 3 | 通过 |
| 9 | 8 | 通过；2 张公开版重绘 |
| 10 | 4 | 通过 |

## 2. 本轮原创重绘清单

### Chapter 2

- `fig_02_12_example16_lp_geometry.png`：可行多边形、五个极点与目标等值线；
- `fig_02_13_hyperplane_halfspaces.png`：二维 half-spaces、三维 hyperplane 与法向量；
- `fig_02_14_simplex_family.png`：1/2/3-simplex 对照；
- `fig_02_15_slack_embedding.png`：不等式可行域到等式平面的 slack embedding。

### Chapter 6

- `fig_06_07_exercise_6_09_networks.png`：四个 transshipment networks；
- `fig_06_08_exercise_6_23_networks.png`：四个 shortest-path networks，并突出最短路径；
- `fig_06_09_exercise_6_25_networks.png`：含负权弧的公开教学重构；
- `fig_06_10_example4_maxflow.png`：最大流网络与流量/容量标签；
- `fig_06_11_example5_shortest_path.png`：最短路网络与最优路径；
- `fig_06_12_exercise_6_13b_source.png`：依据可见节点量和弧方向绘制的结构一致性审计图。

### Chapter 7

- `fig_07_04_epigraph.png`：凸函数 epigraph；
- `fig_07_05_one_sided_derivatives.png`：左右割线斜率关系；
- `fig_07_06_directional_derivative.png`：二维曲面上的方向切片；
- `fig_07_07_convex_starshaped_comparison.png`：非凸 star-shaped 集与 kernel；
- `fig_07_08_quasiconvex_family.png`：quasiconvex / strongly quasiconvex 对照。

### Chapter 9

- `fig_09_07_false_position_newton.png`：false position 与 Newton 几何更新；
- `fig_09_08_powell_dsc_cases.png`：bracketing 与二次插值的三种更新情形。

## 3. 网络题的准确性边界

网络图既是视觉材料，也是题目数据，因此重绘时遵循以下原则：

1. 正文已经明确列出的弧、方向、权重、容量和节点量原样保留；
2. 代表性最优路径使用红色突出，但不删除用于比较的其他可确认弧；
3. Exercise 6.13(b) 不复制教材截图，只呈现证明源数据冲突所需的节点量和弧方向；
4. Exercise 6.25(b)(c) 的原扫描图无法从当前包中可靠恢复，因此公开图只呈现正文可核验的距离标签和代表路径，并在正文中显式说明，不冒充逐弧复原。

## 4. 可复现性

17 张公开版重绘均由 `tools/generate_public_figures.py` 生成。调整主题色、线宽或分辨率后可重新运行脚本，避免手工改图造成数据漂移。

## 5. 验收状态

- 题目依赖图形数据时，网站正文提供对应教学图；
- 关键几何概念有原创可视化；
- 算法几何直觉有对应示意图；
- 所有图片链接使用相对路径；
- 所有 PNG 均通过完整性检查；
- 公开版不包含教材 PDF、整页扫描或教材局部裁图。

> **视觉复审：通过。公开版权清理：通过。已知数据恢复边界：Exercise 6.25(b)(c)，已在正文显式标注。**
