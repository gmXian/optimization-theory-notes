# PREREQUISITES - 前置知识与补课路线

> 这本书不是“完全零数学基础”的教材。作者在 Preface 中明确假定读者学过 **一学期线性代数**，并完成到 **多元微积分（multivariable calculus）** 的微积分序列。Chapter 2 Section 1 会复习部分线性代数，但并不能替代完整基础课。

本文件的目标是：当某个知识点卡住时，知道应该补什么，而不是硬背优化算法。

## 1. 必备线性代数

开始 Chapter 2-6 前至少应能理解：

- 向量与矩阵（vector, matrix）
- 矩阵乘法与转置
- 线性方程组 $Ax=b$
- 初等行变换（elementary row operations）
- Gaussian elimination / Gauss-Jordan elimination
- 向量空间、子空间（vector space, subspace）
- 线性组合、张成（span）
- 线性无关（linear independence）
- 基与维数（basis, dimension）
- 可逆矩阵（nonsingular / invertible matrix）

Chapter 2 还会复习并使用：

- basic solution / basic feasible solution
- LU decomposition
- affine set / convex set 的线性代数基础

### 自测

如果下面问题无法独立完成，应在对应章节前补课：

- [ ] 能把一个 $3\times3$ 线性方程组写成 $Ax=b$。
- [ ] 能用 Gaussian elimination 求解。
- [ ] 能判断一组向量是否线性无关。
- [ ] 能解释“基”为什么既要求张成又要求线性无关。
- [ ] 能理解矩阵乘法的维度规则。

## 2. 必备微积分

Chapter 7-10 前至少应掌握：

- 单变量导数、极值、一阶/二阶条件
- 多变量偏导数（partial derivatives）
- 梯度（gradient）
- 二阶偏导与 Hessian matrix
- 多元 Taylor expansion 的基本思想
- chain rule
- 连续性、极限、开集/闭集的基本直觉

### 自测

- [ ] 能求 $f(x_1,x_2)$ 的 $\nabla f(x)$。
- [ ] 能构造 $\nabla^2 f(x)$。
- [ ] 能解释驻点不一定是最优点。
- [ ] 能用一阶与二阶导数判断单变量局部极值。

## 3. 建议但非硬性要求

- Python / MATLAB / Julia 中任一种基础编程能力。
- 能写简单循环和函数。
- 能画二维函数/可行域。
- 基础数值计算常识：舍入误差、收敛、停止准则。

作者特别强调 Chapter 9-10 的非线性搜索计算量较大；现代学习中建议用 Python 实现算法，而不是机械重复大量手算。

## 4. 按章节的依赖路线

```text
线性代数基础
   │
   ├── Chapter 1  数学规划建模概念
   │
   └── Chapter 2  线性代数复习 + affine / convex geometry
          │
          ├── Chapter 3  primal simplex
          │      │
          │      ├── Chapter 4  duality / complementary slackness
          │      │      │
          │      │      └── Chapter 5  revised / primal-dual simplex
          │      │
          │      └── Chapter 6  network programming
          │
          └── Chapter 7  convex / concave functions
                 │
                 └── Chapter 8  optimality / Kuhn-Tucker
                        │
                        ├── Chapter 9  unconstrained search
                        │
                        └── Chapter 10 penalty / barrier / multipliers
```

## 5. 面向初学者的笔记补充规则

正式笔记中遇到以下情况，必须补充解释：

- 教材直接使用但未展开的线性代数概念；
- “为什么要引入这个变量/约束”；
- 矩阵维度为什么匹配；
- 定理条件缺一不可的原因；
- 算法每一步的几何意义；
- 推导中省略的代数步骤。

补充内容统一标记为 `💡 学习补充`，避免与教材原论述混淆。
