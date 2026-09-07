# 数学符号与中英术语统一表

> 本文件是全仓库的统一约定。若教材在特定章节使用不同符号，应优先忠实于该章教材，并在该章开头注明局部符号约定。

## 1. 数学符号

| 含义 | 统一写法 | Markdown / LaTeX |
|---|---|---|
| 实数集 | $\mathbb{R}$ | `\mathbb{R}` |
| $n$ 维实向量空间 | $\mathbb{R}^n$ | `\mathbb{R}^n` |
| 向量 | $x$ | `x` |
| 第 $i$ 个分量 | $x_i$ | `x_i` |
| 矩阵 | $A$ | `A` |
| 矩阵元素 | $a_{ij}$ | `a_{ij}` |
| 转置 | $A^\top$ | `A^\top` |
| 逆矩阵 | $A^{-1}$ | `A^{-1}` |
| 单位矩阵 | $I$ | `I` |
| 零向量 | $0$ | `0` |
| 内积 | $x^\top y$ | `x^\top y` |
| 欧氏范数 | $\lVert x\rVert_2$ | `\lVert x\rVert_2` |
| 梯度 | $\nabla f(x)$ | `\nabla f(x)` |
| Hessian | $\nabla^2 f(x)$ | `\nabla^2 f(x)` |
| 属于 | $\in$ | `\in` |
| 子集 | $\subseteq$ | `\subseteq` |
| 非负 | $\ge 0$ | `\ge 0` |
| 非正 | $\le 0$ | `\le 0` |
| 最小化 | $\min$ | `\min` |
| 最大化 | $\max$ | `\max` |
| 求和 | $\sum$ | `\sum` |

## 2. 优化与数学规划核心术语

| 中文 | English | 备注 |
|---|---|---|
| 数学规划 | mathematical programming | 本书标题核心术语 |
| 优化 | optimization | 泛称 |
| 目标函数 | objective function | 教材也使用 cost function |
| 成本函数 | cost function | 依教材语境保留 |
| 决策变量 | decision variable | 学习补充术语时标明 |
| 约束 | constraint |  |
| 可行集 | feasible set | 教材亦表述为 set of feasible solutions |
| 可行解 | feasible solution |  |
| 最优解 | optimal solution |  |
| 全局最优解 | global optimal solution |  |
| 局部最优解 | local optimal solution |  |
| 无约束问题 | unconstrained problem |  |
| 约束问题 | constrained problem |  |
| 线性规划 | linear programming | LP |
| 非线性规划 | nonlinear programming | NLP |
| 整数规划 | integer programming | IP |
| 连续变量 | continuous variable |  |
| 离散变量 | discrete variable |  |
| 非负变量 | nonnegative variable |  |
| 自由变量 / 无限制变量 | unrestricted variable |  |
| 松弛变量 | slack variable | 对 `\le` 约束常见 |
| 剩余变量 | surplus variable | 对 `\ge` 约束常见 |
| 互补变量 | complementary variables |  |
| 互补约束 | complementary constraint |  |
| 二次规划 | quadratic programming | QP |
| 运输问题 | transportation problem |  |
| 指派问题 | assignment problem |  |
| 网络规划 | network programming |  |
| 最大流问题 | maximal / maximum flow problem | 依教材表述 |
| 后最优分析 | post-optimal analysis | 亦称 sensitivity analysis |
| 灵敏度分析 | sensitivity analysis |  |
| 参数规划 | parametric programming |  |
| 模型稳定性 | model stability |  |
| 数值稳定性 | numerical stability |  |

## 3. 线性规划与单纯形法术语

| 中文 | English |
|---|---|
| 基 | basis |
| 基变量 | basic variable |
| 非基变量 | nonbasic variable |
| 基解 | basic solution |
| 基可行解 | basic feasible solution |
| 单纯形法 | simplex procedure / simplex method |
| 原始单纯形法 | primal simplex procedure |
| 对偶单纯形法 | dual simplex procedure |
| 修正单纯形法 | revised simplex procedure |
| 原始-对偶算法 | primal-dual algorithm |
| 人工变量 | artificial variable |
| 两阶段法 | two-phase method |
| 退化 | degeneracy |
| 循环 | cycling |
| 对偶 | duality |
| 互补松弛 | complementary slackness |
| 线性互补问题 | linear complementarity problem |

## 4. 网络规划术语

| 中文 | English | 备注 |
|---|---|---|
| 网络 / 图 | network / graph | Chapter 6 教材近似作同义词使用 |
| 节点 | node | 也可称 vertex；正文优先 node |
| 弧 | arc | 有向边 |
| 节点–弧关联矩阵 | node–arc incidence matrix | 每列通常含一个 $+1$ 与一个 $-1$ |
| 源点 / 供应节点 | source / supply node | 教材约定 $b_i>0$ |
| 汇点 / 需求节点 | sink / demand node | 教材约定 $b_i<0$ |
| 中转节点 | intermediate / transshipment node | $b_i=0$ |
| 容量 | capacity | 常记为 $u_{ij}$ |
| 最小费用网络流 | minimal-cost network flow | 教材表述 |
| 转运问题 | transshipment problem | 无容量上界的最小费用网络流特例 |
| 路径 | path | 所有弧方向与行进方向一致 |
| 链 | chain | 可含 forward / reverse arcs |
| 圈 | cycle | 首尾相接的 chain |
| 回路 | circuit | 教材中指方向一致的 cycle |
| 树 | tree | connected and acyclic |
| 生成树 | spanning tree | 覆盖网络全部节点 |
| 节点势 | node potential | 网络单纯形中的 dual variables |
| 割 | cut / cutset | 分离 source 与 sink |
| 割容量 | cut capacity | 穿过割的正向弧容量之和 |
| 增广链 | flow-augmenting chain | 与当前流相对的可增广 chain |
| 最大流最小割定理 | max-flow min-cut theorem | 最大流值 = 最小割容量 |
| 最短路 | shortest path | Chapter 6 作为 network LP / primal-dual 特例 |
| Dijkstra 算法 | Dijkstra's algorithm | 教材用于非负弧成本 |
| 匈牙利法 | Hungarian method | assignment problem 的 primal-dual 特化 |

## 5. 凸分析与非线性优化术语

| 中文 | English |
|---|---|
| 仿射集 | affine set |
| 锥 | cone |
| 凸集 | convex set |
| 凸函数 | convex function |
| 凹函数 | concave function |
| 拟凸函数 | quasiconvex function |
| 严格拟凸函数 | strictly quasiconvex function |
| 伪凸函数 | pseudoconvex function |
| 星形集 | star-shaped set |
| 正定 / 半正定 | positive definite / positive semidefinite |
| 负定 / 半负定 | negative definite / negative semidefinite |
| 主子式 | principal minor |
| 最优性条件 | optimality conditions |
| 一阶必要条件 | first-order necessary condition |
| 二阶必要 / 充分条件 | second-order necessary / sufficient condition |
| 活跃约束 | active constraint |
| 约束资格条件 | constraint qualification |
| 拉格朗日函数 | Lagrangian |
| 拉格朗日乘子 | Lagrange multiplier |
| Kuhn–Tucker 条件 | Kuhn–Tucker conditions |
| 鞍点 | saddle point |
| 线搜索 | line search |
| 单峰函数 | unimodal function |
| Fibonacci 搜索 | Fibonacci search |
| 黄金分割搜索 | golden-section search |
| 二次插值 | quadratic interpolation |
| Powell 方法 | Powell's method |
| Davies–Swann–Campey 方法 | Davies–Swann–Campey (DSC) method |
| Newton 方法 | Newton's method |
| 最速下降法 | steepest-descent method |
| 共轭方向 | conjugate directions |
| 共轭梯度法 | conjugate-gradient method |
| Fletcher–Reeves 方法 | Fletcher–Reeves method |
| Davidon–Fletcher–Powell 方法 | Davidon–Fletcher–Powell (DFP) method |
| 拟 Newton 方法 | quasi-Newton method |
| 外罚函数 | exterior penalty function |
| 二次罚函数 | quadratic penalty function |
| 障碍函数 | barrier function |
| 倒数障碍函数 | reciprocal barrier function |
| 对数障碍函数 | logarithmic barrier function |
| 增广拉格朗日函数 | augmented Lagrangian |
| 乘子法 | method of multipliers |
| 罚参数 | penalty parameter |
| 障碍参数 | barrier parameter |

## 6. 翻译原则

1. 第一次出现：中文 + English，例如“可行解（feasible solution）”。
2. 后续正文以中文为主，公式变量与算法标准英文名保留。
3. 若教材使用的英文术语与现代常用写法略有差异，正文优先解释教材术语，再在“学习补充”中说明现代写法。
4. 不擅自把教材中的符号体系整体替换成现代记法；为了可读性做改写时必须说明。
