#!/usr/bin/env python3
"""Generate original, public-safe teaching figures for the Quarto site.

The generated diagrams replace textbook crops while retaining the mathematical
structure required by the surrounding notes. All labels and geometry here are
authored for this repository.
"""

from __future__ import annotations

from pathlib import Path
from math import pi

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


ROOT = Path(__file__).resolve().parents[1]
INK = "#153e52"
TEAL = "#0b6170"
BLUE = "#2d728f"
CYAN = "#63aeb8"
GOLD = "#c78a26"
RED = "#b84a3a"
MUTED = "#6b7f8c"
PALE = "#e8f5f6"
PALE_BLUE = "#edf4fb"
PALE_GOLD = "#fff3cf"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.titleweight": "bold",
        "axes.labelcolor": INK,
        "text.color": INK,
        "axes.edgecolor": MUTED,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


def save(fig: plt.Figure, relative: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def clean_axes(ax, *, equal: bool = False) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#dce7eb", linewidth=0.65, alpha=0.7)
    if equal:
        ax.set_aspect("equal", adjustable="box")


def draw_directed_graph(
    ax,
    positions,
    edges,
    *,
    title="",
    node_text=None,
    node_fill=None,
    highlight_edges=None,
    show_edge_labels=True,
):
    """Draw a compact directed graph.

    edges contains (u, v, label) or (u, v, label, curvature).
    """
    node_text = node_text or {}
    node_fill = node_fill or {}
    highlight_edges = set(highlight_edges or [])

    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    span = max(max(xs) - min(xs), max(ys) - min(ys), 1)
    radius = span * 0.045

    for item in edges:
        u, v, label, *rest = item
        rad = rest[0] if rest else 0.0
        start = np.array(positions[u], dtype=float)
        end = np.array(positions[v], dtype=float)
        color = RED if (u, v) in highlight_edges else BLUE
        width = 2.25 if (u, v) in highlight_edges else 1.35
        arrow = FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=width,
            color=color,
            shrinkA=12,
            shrinkB=12,
            connectionstyle=f"arc3,rad={rad}",
            zorder=1,
        )
        ax.add_patch(arrow)
        if show_edge_labels and label not in (None, ""):
            midpoint = (start + end) / 2
            delta = end - start
            normal = np.array([-delta[1], delta[0]])
            norm = np.linalg.norm(normal)
            if norm:
                normal = normal / norm
            offset = normal * span * (0.035 + 0.12 * rad)
            ax.text(
                *(midpoint + offset),
                str(label),
                ha="center",
                va="center",
                fontsize=8.2,
                color=INK,
                bbox={"boxstyle": "round,pad=0.15", "fc": "white", "ec": "none", "alpha": 0.92},
                zorder=3,
            )

    for node, (x, y) in positions.items():
        fill = node_fill.get(node, "white")
        circle = Circle((x, y), radius, facecolor=fill, edgecolor=INK, linewidth=1.5, zorder=4)
        ax.add_patch(circle)
        ax.text(x, y, node_text.get(node, str(node)), ha="center", va="center", fontsize=8.5, zorder=5)

    ax.set_xlim(min(xs) - span * 0.16, max(xs) + span * 0.16)
    ax.set_ylim(min(ys) - span * 0.18, max(ys) + span * 0.18)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, color=INK, pad=7)


def figure_02_12() -> None:
    fig, ax = plt.subplots(figsize=(8.4, 5.5))
    vertices = np.array([[0, 0], [0, 5], [4, 7], [7, 2], [4, 0]])
    ax.add_patch(Polygon(vertices, closed=True, facecolor=PALE, edgecolor=TEAL, linewidth=2.2))
    ax.scatter(vertices[:, 0], vertices[:, 1], s=38, color=TEAL, zorder=4)
    labels = ["(0,0)", "(0,5)", "(4,7)", "(7,2)", "(4,0)"]
    offsets = [(0.15, -0.45), (-0.9, 0.1), (-0.1, 0.35), (0.2, 0.15), (-0.25, -0.5)]
    for (x, y), label, (dx, dy) in zip(vertices, labels, offsets):
        ax.text(x + dx, y + dy, label, fontsize=9)

    x = np.linspace(-1, 8.2, 200)
    for mu, alpha in [(-5, 0.55), (0, 0.8), (4, 0.55)]:
        ax.plot(x, x + mu, color=GOLD, linewidth=1.2, alpha=alpha, linestyle="--")
    ax.annotate(
        "decreasing  $-x_1+x_2$",
        xy=(6.65, 1.55),
        xytext=(5.0, 4.3),
        arrowprops={"arrowstyle": "->", "color": GOLD, "lw": 1.5},
        color=GOLD,
        fontsize=9,
    )
    ax.scatter([7], [2], s=125, facecolors="none", edgecolors=RED, linewidths=2.2, zorder=5)
    ax.text(6.0, 2.55, "optimum", color=RED, fontweight="bold")
    ax.set_xlim(-1, 8.4)
    ax.set_ylim(-0.8, 8.2)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$", rotation=0, labelpad=12)
    ax.set_title("Feasible polygon and parallel objective contours")
    clean_axes(ax, equal=True)
    save(fig, "02_Subspaces_Matrices_Affine_Sets_Cones_Convex_Sets_and_the_Linear_Programming_Problem/images/fig_02_12_example16_lp_geometry.png")


def figure_02_13() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    x = np.linspace(-3, 3, 200)
    boundary = 0.65 * x + 0.25
    axes[0].fill_between(x, boundary, 3, color=PALE_BLUE)
    axes[0].fill_between(x, -3, boundary, color=PALE_GOLD)
    axes[0].plot(x, boundary, color=INK, linewidth=2)
    axes[0].annotate("$c$", xy=(0.2, 1.7), xytext=(-0.5, 0.9), arrowprops={"arrowstyle": "->", "color": RED}, color=RED)
    axes[0].text(-2.45, 2.1, "$H^+(c,\\beta)$", color=BLUE, fontweight="bold")
    axes[0].text(1.15, -1.8, "$H^-(c,\\beta)$", color="#8a650f", fontweight="bold")
    axes[0].text(-0.25, 0.0, "$H(c,\\beta)$", rotation=33, color=INK)
    axes[0].set_xlim(-3, 3)
    axes[0].set_ylim(-3, 3)
    axes[0].set_title("A hyperplane separates two half-spaces")
    clean_axes(axes[0], equal=True)

    xx, yy = np.meshgrid(np.linspace(-2.4, 2.4, 30), np.linspace(-2.4, 2.4, 30))
    zz = 0.55 * xx - 0.35 * yy + 0.2
    ax3 = fig.add_subplot(1, 2, 2, projection="3d")
    axes[1].remove()
    ax3.plot_surface(xx, yy, zz, color=CYAN, alpha=0.58, edgecolor="none")
    ax3.quiver(0, 0, 0.2, -0.55, 0.35, 1, color=RED, length=1.25, linewidth=2)
    ax3.text(-0.6, 0.42, 1.55, "$c$", color=RED)
    ax3.set_title("In $\\mathbb{R}^3$: a two-dimensional plane")
    ax3.set_xlabel("$x_1$")
    ax3.set_ylabel("$x_2$")
    ax3.set_zlabel("$x_3$")
    ax3.view_init(elev=24, azim=-55)
    save(fig, "02_Subspaces_Matrices_Affine_Sets_Cones_Convex_Sets_and_the_Linear_Programming_Problem/images/fig_02_13_hyperplane_halfspaces.png")


def figure_02_14() -> None:
    fig = plt.figure(figsize=(11, 3.9), constrained_layout=True)
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.plot([0, 1], [0, 0], color=TEAL, linewidth=5, solid_capstyle="round")
    ax1.scatter([0, 1], [0, 0], color=INK, s=55, zorder=3)
    ax1.text(0, 0.13, "$v_0$", ha="center")
    ax1.text(1, 0.13, "$v_1$", ha="center")
    ax1.set_xlim(-0.2, 1.2)
    ax1.set_ylim(-0.45, 0.55)
    ax1.set_title("1-simplex · segment")
    ax1.axis("off")

    ax2 = fig.add_subplot(1, 3, 2)
    triangle = np.array([[0, 0], [1, 0], [0.45, 0.9]])
    ax2.add_patch(Polygon(triangle, closed=True, facecolor=PALE, edgecolor=TEAL, linewidth=2.2))
    ax2.scatter(triangle[:, 0], triangle[:, 1], color=INK, s=45, zorder=3)
    for i, (x, y) in enumerate(triangle):
        ax2.text(x, y + 0.09, f"$v_{i}$", ha="center")
    ax2.set_xlim(-0.2, 1.2)
    ax2.set_ylim(-0.2, 1.15)
    ax2.set_aspect("equal")
    ax2.set_title("2-simplex · triangle")
    ax2.axis("off")

    ax3 = fig.add_subplot(1, 3, 3, projection="3d")
    tetra = np.array([[0, 0, 0], [1, 0, 0], [0.35, 0.9, 0], [0.35, 0.3, 0.95]])
    faces = [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]]
    for face in faces:
        verts = tetra[face]
        poly = Poly3DCollection([verts], alpha=0.3, facecolor=CYAN, edgecolor=TEAL)
        ax3.add_collection3d(poly)
    ax3.scatter(tetra[:, 0], tetra[:, 1], tetra[:, 2], color=INK, s=35)
    for i, (x, y, z) in enumerate(tetra):
        ax3.text(x, y, z + 0.08, f"$v_{i}$")
    ax3.set_title("3-simplex · tetrahedron")
    ax3.set_axis_off()
    ax3.view_init(elev=22, azim=-58)
    save(fig, "02_Subspaces_Matrices_Affine_Sets_Cones_Convex_Sets_and_the_Linear_Programming_Problem/images/fig_02_14_simplex_family.png")


def figure_02_15() -> None:
    fig = plt.figure(figsize=(10, 4.5), constrained_layout=True)
    ax1 = fig.add_subplot(1, 2, 1)
    triangle = np.array([[0, 0], [0, 2.2], [3.0, 0]])
    ax1.add_patch(Polygon(triangle, closed=True, facecolor=PALE, edgecolor=TEAL, linewidth=2.2))
    ax1.text(0.75, 0.65, "$F=\\{x:Ax\\leq b,\\ x\\geq0\\}$", color=TEAL)
    ax1.set_xlim(-0.35, 3.4)
    ax1.set_ylim(-0.3, 2.7)
    ax1.set_xlabel("$x_1$")
    ax1.set_ylabel("$x_2$", rotation=0, labelpad=10)
    ax1.set_title("Inequality form")
    clean_axes(ax1)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pts = np.array([[0, 0, 3], [0, 2.2, 0.8], [3, 0, 0]])
    poly = Poly3DCollection([pts], alpha=0.45, facecolor=CYAN, edgecolor=TEAL, linewidth=2)
    ax2.add_collection3d(poly)
    ax2.scatter(pts[:, 0], pts[:, 1], pts[:, 2], color=INK, s=35)
    ax2.text(0.55, 0.5, 2.0, "$Ax+s=b$", color=TEAL)
    ax2.set_xlabel("$x_1$")
    ax2.set_ylabel("$x_2$")
    ax2.set_zlabel("slack $s$")
    ax2.set_title("Equality form: the same feasible set embedded")
    ax2.view_init(elev=23, azim=-53)
    save(fig, "02_Subspaces_Matrices_Affine_Sets_Cones_Convex_Sets_and_the_Linear_Programming_Problem/images/fig_02_15_slack_embedding.png")


def figure_06_07() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 8.2), constrained_layout=True)
    pos_a = {1: (0, 1), 2: (1.4, 2), 3: (1.4, 1.25), 4: (1.4, 0.5), 5: (0.2, 0), 6: (2.8, 1.2), 7: (2.8, 0.25)}
    edges_a = [(1,2,1),(1,3,1),(1,5,1),(1,7,1),(2,3,1),(2,7,1),(3,4,1),(3,6,1),(3,7,1),(4,3,1,0.22),(4,7,1),(5,2,1),(5,3,1),(5,6,1),(5,7,1),(6,7,1)]
    draw_directed_graph(axes[0,0], pos_a, edges_a, title="(a)  $b=(50,0,0,0,0,0,-50)$", highlight_edges={(1,7)})

    pos_b = {1:(0,2),2:(0,1),3:(0,0),4:(2.5,2.1),5:(2.5,1.4),6:(2.5,0.65),7:(2.5,-0.1)}
    edges_b = [(1,4,2),(1,5,3),(2,4,2),(2,5,1),(2,6,3),(2,7,4),(3,6,1),(3,7,1)]
    draw_directed_graph(axes[0,1], pos_b, edges_b, title="(b) sources 1–3, sinks 4–7")

    pos_c = {1:(0,1),2:(1.3,2),3:(1.3,0),4:(2.6,1)}
    edges_c = [(1,2,3),(1,3,4),(2,3,-1,-0.12),(3,2,2,-0.12),(2,4,1),(3,4,1)]
    draw_directed_graph(axes[1,0], pos_c, edges_c, title="(c) transshipment with a negative arc", highlight_edges={(1,2),(2,3),(3,4)})

    pos_d = {1:(0,2),2:(0,1),3:(0,0),4:(2.7,2),5:(2.7,1),6:(2.7,0)}
    edges_d = [(i,j,1 if (i,j) in {(1,4),(2,5),(3,6)} else 2) for i in (1,2,3) for j in (4,5,6)]
    draw_directed_graph(axes[1,1], pos_d, edges_d, title="(d) complete transportation network", highlight_edges={(1,4),(2,5),(3,6)})
    fig.suptitle("Exercise 6.9 · Original teaching redraw", fontsize=14, fontweight="bold", color=INK)
    save(fig, "06_Network_Programming/images/fig_06_07_exercise_6_09_networks.png")


def figure_06_08() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 8.5), constrained_layout=True)
    pos_a = {1:(0,1),2:(1,2),4:(1,0),3:(2.4,2),5:(2.4,0),6:(3.4,1)}
    edges_a = [(1,2,1),(1,4,3),(1,3,5),(2,3,4),(2,4,2),(2,5,2),(3,4,1),(4,5,1),(5,3,1),(3,6,1),(5,6,2)]
    draw_directed_graph(axes[0,0],pos_a,edges_a,title="(a) shortest 1→2→5→6 = 5",highlight_edges={(1,2),(2,5),(5,6)})

    pos_b = {1:(0,1),2:(0.9,2),5:(0.9,0),3:(2,2.5),6:(2,0),4:(3.1,2),7:(3.1,0.45),8:(4,1.25)}
    edges_b = [(1,2,1),(1,5,1),(2,3,3),(2,6,1),(2,7,4),(5,3,1),(5,6,1),(6,3,2),(3,4,2),(6,4,3),(6,7,4),(4,7,1),(4,8,1),(7,8,1)]
    draw_directed_graph(axes[0,1],pos_b,edges_b,title="(b) shortest 1→5→3→4→8 = 5",highlight_edges={(1,5),(5,3),(3,4),(4,8)})

    pos_c = {1:(0,2),3:(0,0),2:(1.2,0.85),5:(2.3,0.85),4:(3.5,2),6:(3.5,0)}
    edges_c = [(1,4,3),(1,3,2),(1,2,2),(3,2,1),(4,5,1),(5,2,2),(5,6,1),(4,6,3),(3,6,4)]
    draw_directed_graph(axes[1,0],pos_c,edges_c,title="(c) shortest 1→4→5→6 = 5",highlight_edges={(1,4),(4,5),(5,6)})

    pos_d = {1:(0,1),2:(1,2),4:(1,0),6:(1.8,1),3:(2.6,2),7:(2.6,1),5:(2.6,0),8:(3.7,1)}
    edges_d = [(1,2,3),(1,4,2),(2,3,1),(2,6,1),(6,4,3),(3,7,2),(7,6,1),(7,5,1),(3,8,4),(4,5,5),(5,8,2)]
    draw_directed_graph(axes[1,1],pos_d,edges_d,title="(d) shortest 1→2→3→8 = 8",highlight_edges={(1,2),(2,3),(3,8)})
    fig.suptitle("Exercise 6.23 · Directed shortest-path networks", fontsize=14, fontweight="bold", color=INK)
    save(fig, "06_Network_Programming/images/fig_06_08_exercise_6_23_networks.png")


def figure_06_09() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.4), constrained_layout=True)
    pos_a = {1:(0,1),3:(1,0.25),2:(1,1.75),5:(2,0),4:(2.5,1.5),6:(3.5,0.8)}
    edges_a = [(1,2,4),(1,3,1),(3,2,-2),(2,4,3),(3,4,1),(3,5,4),(5,4,-3),(4,6,2),(5,6,3)]
    draw_directed_graph(axes[0],pos_a,edges_a,title="(a)  $d=(0,-1,1,2,5,4)$",highlight_edges={(1,3),(3,2),(3,4),(4,6)})

    pos_b = {1:(0,1),2:(1,1.8),3:(1,0.25),4:(2,1.8),5:(2.7,1.1),6:(3.5,0.25),7:(3.7,1.8)}
    edges_b = [(1,2,10),(1,3,8),(2,4,5),(3,5,3),(4,5,-4),(5,6,5),(4,7,3)]
    draw_directed_graph(axes[1],pos_b,edges_b,title="(b)  shortest-distance labels",highlight_edges={(1,2),(2,4),(4,5),(1,3)})
    axes[1].text(1.9,-0.35,"$d=(0,10,8,15,11,16,18)$",ha="center",fontsize=9,color=MUTED)

    pos_c = {1:(0,1),3:(1.2,1.8),5:(1.2,0.2),4:(2.4,1.8),2:(2.4,1),6:(2.4,0.2)}
    edges_c = [(1,3,4),(3,4,-5),(4,2,1),(1,5,4),(5,6,-6)]
    draw_directed_graph(axes[2],pos_c,edges_c,title="(c)  negative arcs, no negative cycle",highlight_edges={(1,3),(3,4),(4,2),(1,5),(5,6)})
    axes[2].text(1.25,-0.35,"$d=(0,0,4,-1,4,-2)$",ha="center",fontsize=9,color=MUTED)
    fig.suptitle("Exercise 6.25 · Public teaching reconstruction", fontsize=14, fontweight="bold", color=INK)
    save(fig, "06_Network_Programming/images/fig_06_09_exercise_6_25_networks.png")


def figure_06_10() -> None:
    fig, ax = plt.subplots(figsize=(8.5, 4.3))
    pos = {1:(0,1),2:(1.2,2),3:(1.2,0),4:(2.5,0),5:(2.5,2)}
    edges = [(1,2,"0/10"),(1,3,"0/4"),(2,5,"0/5"),(2,4,"0/5"),(3,5,"0/5"),(4,3,"0/3"),(4,5,"0/3")]
    draw_directed_graph(ax,pos,edges,title="Example 4 · Maximum-flow network (flow / capacity)")
    ax.annotate("source",xy=(-0.1,1),xytext=(-0.75,1),arrowprops={"arrowstyle":"->","color":TEAL},ha="right",va="center",color=TEAL)
    ax.annotate("sink",xy=(2.6,2),xytext=(3.25,2),arrowprops={"arrowstyle":"->","color":TEAL},ha="left",va="center",color=TEAL)
    save(fig, "06_Network_Programming/images/fig_06_10_example4_maxflow.png")


def figure_06_11() -> None:
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    pos = {1:(0,0.8),2:(1,1.7),3:(2.1,0.25),4:(2.2,1.8),5:(3.4,0.95)}
    edges = [(1,2,1),(1,3,5),(2,4,1),(2,3,4),(4,3,2),(4,5,4),(3,5,1)]
    path = {(1,2),(2,4),(4,3),(3,5)}
    draw_directed_graph(ax,pos,edges,title="Example 5 · Shortest path 1→2→4→3→5",highlight_edges=path)
    ax.text(1.7,-0.25,"highlighted length: 1 + 1 + 2 + 1 = 5",ha="center",color=RED,fontweight="bold")
    save(fig, "06_Network_Programming/images/fig_06_11_example5_shortest_path.png")


def figure_06_12() -> None:
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    pos = {1:(0,1),2:(1.2,2.2),3:(2.7,2.2),4:(3.8,1),5:(2.7,0),6:(1.2,0)}
    balances = {1:8,2:-18,3:-16,4:-10,5:2,6:34}
    labels = {i:f"{i}\n$b={balances[i]}$" for i in pos}
    edges = [(2,1,None),(3,1,None),(5,1,None),(1,6,None),(2,3,None),(2,6,None),(2,4,None),(3,5,None),(4,3,None),(4,6,None),(4,5,None),(5,6,None)]
    draw_directed_graph(ax,pos,edges,title="Exercise 6.13(b) · Structural consistency audit",node_text=labels,node_fill={6:"#fff0ee"},show_edge_labels=False)
    ax.annotate(
        "positive supply but no outgoing arc",
        xy=pos[6],
        xytext=(2.3,-0.75),
        arrowprops={"arrowstyle":"->","color":RED,"lw":1.8},
        color=RED,
        ha="center",
        fontweight="bold",
    )
    save(fig, "06_Network_Programming/images/fig_06_12_exercise_6_13b_source.png")


def figure_07_04() -> None:
    fig, ax = plt.subplots(figsize=(8, 5.2))
    x = np.linspace(-3, 3, 400)
    f = 0.38 * x**2 + 0.8
    ax.fill_between(x, f, 5, color=PALE_BLUE, alpha=0.95)
    ax.plot(x, f, color=TEAL, linewidth=2.6, label="$y=f(x)$")
    ax.text(0.9,3.35,"$\\operatorname{epi}(f)=\\{(x,t):t\\geq f(x)\\}$",color=BLUE,fontweight="bold")
    ax.annotate("boundary $f$",xy=(-1.75,1.95),xytext=(-2.65,3),arrowprops={"arrowstyle":"->","color":TEAL},color=TEAL)
    ax.set_xlim(-3,3)
    ax.set_ylim(0,5)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$t$",rotation=0,labelpad=12)
    ax.set_title("Epigraph of a convex function")
    clean_axes(ax)
    save(fig, "07_Convex_and_Concave_Functions/images/fig_07_04_epigraph.png")


def figure_07_05() -> None:
    fig, ax = plt.subplots(figsize=(8.5, 5.1))
    x = np.linspace(-2.4, 2.4, 400)
    y = 0.35*x**2 + 0.35
    a,b,c = -1.55,0,1.7
    pts = [(a,0.35*a*a+0.35),(b,0.35),(c,0.35*c*c+0.35)]
    ax.plot(x,y,color=TEAL,linewidth=2.4)
    ax.scatter(*zip(*pts),color=INK,s=45,zorder=4)
    ax.plot([a,b],[pts[0][1],pts[1][1]],color=GOLD,linewidth=2,label="left secant slope")
    ax.plot([b,c],[pts[1][1],pts[2][1]],color=BLUE,linewidth=2,label="right secant slope")
    for xx,yy,label in [(a,pts[0][1],"$a$"),(b,pts[1][1],"$b$"),(c,pts[2][1],"$c$")]:
        ax.text(xx, -0.05, label, ha="center")
    ax.text(-1.95,2.5,"left slope $\\leq$ right slope",color=INK,fontweight="bold")
    ax.set_xlim(-2.45,2.45)
    ax.set_ylim(-0.2,3.1)
    ax.set_title("One-sided slopes of a convex function")
    ax.legend(frameon=False,loc="upper right")
    clean_axes(ax)
    save(fig, "07_Convex_and_Concave_Functions/images/fig_07_05_one_sided_derivatives.png")


def figure_07_06() -> None:
    fig = plt.figure(figsize=(8, 5.7))
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(-1.8,1.8,45)
    y = np.linspace(-1.8,1.8,45)
    xx,yy=np.meshgrid(x,y)
    zz=0.35*xx**2+0.2*yy**2
    ax.plot_surface(xx,yy,zz,cmap="GnBu",alpha=0.62,edgecolor="none")
    t=np.linspace(-1.25,1.25,80)
    lx=0.4+t
    ly=-0.15+0.6*t
    lz=0.35*lx**2+0.2*ly**2
    ax.plot(lx,ly,lz,color=RED,linewidth=3)
    x0,y0=0.4,-0.15
    z0=0.35*x0*x0+0.2*y0*y0
    ax.scatter([x0],[y0],[z0],color=INK,s=50)
    ax.quiver(x0,y0,z0,0.9,0.54,0.23,color=RED,linewidth=2,arrow_length_ratio=0.13)
    ax.text(x0+0.92,y0+0.56,z0+0.25,"direction $v$",color=RED)
    ax.text(x0-0.25,y0-0.18,z0+0.2,"$\\bar{x}$",color=INK)
    ax.set_title("Directional derivative: restrict $f$ to a line through $\\bar{x}$")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$f(x)$")
    ax.view_init(elev=25,azim=-55)
    save(fig, "07_Convex_and_Concave_Functions/images/fig_07_06_directional_derivative.png")


def figure_07_07() -> None:
    fig, axes = plt.subplots(1,2,figsize=(10.5,4.6),constrained_layout=True)
    angles=np.linspace(0,2*pi,11)[:-1]
    radii=np.array([1.0,0.45]*5)
    star=np.c_[radii*np.cos(angles+pi/2),radii*np.sin(angles+pi/2)]
    axes[0].add_patch(Polygon(star,closed=True,facecolor=PALE_BLUE,edgecolor=BLUE,linewidth=2))
    kernel=np.array([[-0.18,-0.15],[0.18,-0.15],[0.25,0.12],[0,0.28],[-0.25,0.12]])
    axes[0].add_patch(Polygon(kernel,closed=True,facecolor=PALE_GOLD,edgecolor=GOLD,linewidth=1.5))
    center=np.array([0,0.04])
    axes[0].scatter(*center,color=RED,s=45,zorder=4)
    for point in star[::2]:
        axes[0].plot([center[0],point[0]],[center[1],point[1]],color=RED,alpha=0.45,linewidth=1)
    axes[0].text(0,-1.2,"kernel = valid star centers",ha="center",color=GOLD,fontweight="bold")
    axes[0].set_title("Nonconvex star set with a kernel")
    axes[0].set_aspect("equal"); axes[0].axis("off")

    t=np.linspace(0,2*pi,500)
    r=1-0.28*np.cos(2*t)
    x=r*np.cos(t); y=0.8*r*np.sin(t)
    axes[1].fill(x,y,color=PALE,edgecolor=TEAL,linewidth=2)
    c=np.array([0.18,0])
    axes[1].scatter(*c,color=RED,s=45,zorder=4)
    for idx in [45,120,215,330]:
        axes[1].plot([c[0],x[idx]],[c[1],y[idx]],color=RED,alpha=0.48,linewidth=1.1)
    axes[1].annotate("star center",xy=c,xytext=(0.65,0.85),arrowprops={"arrowstyle":"->","color":RED},color=RED)
    axes[1].set_title("Every point can see the chosen center")
    axes[1].set_aspect("equal"); axes[1].axis("off")
    fig.suptitle("Star-shaped does not mean convex",fontsize=14,fontweight="bold",color=INK)
    save(fig, "07_Convex_and_Concave_Functions/images/fig_07_07_convex_starshaped_comparison.png")


def figure_07_08() -> None:
    fig, axes = plt.subplots(1,2,figsize=(10,4.2),constrained_layout=True)
    x=np.linspace(0,6,500)
    y=np.piecewise(x,[x<1.6,(x>=1.6)&(x<=3.4),x>3.4],[lambda z:(1.6-z)**2+1,1,lambda z:0.45*(z-3.4)**2+1])
    axes[0].plot(x,y,color=TEAL,linewidth=2.6)
    axes[0].axhline(1,color=GOLD,linestyle="--",linewidth=1)
    axes[0].text(2.5,1.12,"flat minimum",ha="center",color=GOLD)
    axes[0].set_title("Quasiconvex, not strongly quasiconvex")
    axes[0].set_xlabel("$x$"); axes[0].set_ylabel("$f(x)$")
    clean_axes(axes[0])

    y2=np.exp(0.32*x)
    axes[1].plot(x,y2,color=BLUE,linewidth=2.6)
    axes[1].scatter([0.7,5.2],np.exp(0.32*np.array([0.7,5.2])),color=INK,s=35)
    axes[1].text(3.1,1.2,"strict interior improvement",ha="center",color=BLUE)
    axes[1].set_title("Strongly quasiconvex example")
    axes[1].set_xlabel("$x$"); axes[1].set_ylabel("$f(x)$")
    clean_axes(axes[1])
    save(fig, "07_Convex_and_Concave_Functions/images/fig_07_08_quasiconvex_family.png")


def figure_09_07() -> None:
    fig,axes=plt.subplots(1,2,figsize=(10.5,4.3),constrained_layout=True)
    x=np.linspace(0.2,2.2,500)
    g=x**2-2
    root=np.sqrt(2)
    axes[0].plot(x,g,color=TEAL,linewidth=2.5)
    a,b=0.65,2.0
    ga,gb=a*a-2,b*b-2
    xsec=(a*gb-b*ga)/(gb-ga)
    axes[0].plot([a,b],[ga,gb],color=GOLD,linewidth=2)
    axes[0].scatter([a,b,xsec],[ga,gb,0],color=[INK,INK,RED],s=40,zorder=4)
    axes[0].axhline(0,color=MUTED,linewidth=1)
    axes[0].annotate("secant estimate",xy=(xsec,0),xytext=(0.85,1.25),arrowprops={"arrowstyle":"->","color":RED},color=RED)
    axes[0].set_title("False position keeps a bracket")
    clean_axes(axes[0])

    axes[1].plot(x,g,color=BLUE,linewidth=2.5)
    xk=1.9; gk=xk*xk-2; slope=2*xk
    tangent=gk+slope*(x-xk)
    xnew=xk-gk/slope
    axes[1].plot(x,tangent,color=GOLD,linewidth=2)
    axes[1].scatter([xk,xnew],[gk,0],color=[INK,RED],s=40,zorder=4)
    axes[1].axhline(0,color=MUTED,linewidth=1)
    axes[1].annotate("$x_{k+1}$",xy=(xnew,0),xytext=(0.75,1.2),arrowprops={"arrowstyle":"->","color":RED},color=RED)
    axes[1].set_title("Newton uses a tangent")
    clean_axes(axes[1])
    fig.suptitle("Solving $f'(x)=0$: two geometric updates",fontsize=14,fontweight="bold",color=INK)
    save(fig, "09_Search_Techniques_for_Unconstrained_Optimization_Problems/images/fig_09_07_false_position_newton.png")


def figure_09_08() -> None:
    fig,axes=plt.subplots(1,3,figsize=(12.5,4),constrained_layout=True)
    cases=[(-0.5,"discard left"),(0,"accept tighter bracket"),(0.55,"discard right")]
    x=np.linspace(-2.2,2.2,400)
    for ax,(shift,label) in zip(axes,cases):
        y=(x-shift)**2+0.2
        ax.plot(x,y,color=TEAL,linewidth=2.3)
        points=np.array([-1.7,-0.4,1.55])
        vals=(points-shift)**2+0.2
        ax.scatter(points,vals,color=INK,s=38,zorder=4)
        for idx,(px,py) in enumerate(zip(points,vals),1):
            ax.text(px,py+0.25,f"$x_{idx}$",ha="center")
        coeff=np.polyfit(points,vals,2)
        xq=-coeff[1]/(2*coeff[0])
        yq=np.polyval(coeff,xq)
        ax.scatter([xq],[yq],color=RED,s=55,zorder=5)
        ax.text(xq,yq-0.48,"$x_q$",ha="center",color=RED,fontweight="bold")
        ax.axvspan(points[0],points[-1],color=PALE_BLUE,alpha=0.45)
        ax.set_title(label)
        ax.set_xticks([]); ax.set_yticks([])
        clean_axes(ax)
    fig.suptitle("Powell / DSC · bracket then refine by quadratic interpolation",fontsize=14,fontweight="bold",color=INK)
    save(fig, "09_Search_Techniques_for_Unconstrained_Optimization_Problems/images/fig_09_08_powell_dsc_cases.png")


def main() -> None:
    generators = [
        figure_02_12,
        figure_02_13,
        figure_02_14,
        figure_02_15,
        figure_06_07,
        figure_06_08,
        figure_06_09,
        figure_06_10,
        figure_06_11,
        figure_06_12,
        figure_07_04,
        figure_07_05,
        figure_07_06,
        figure_07_07,
        figure_07_08,
        figure_09_07,
        figure_09_08,
    ]
    for generator in generators:
        generator()
    print(f"Generated {len(generators)} public-safe teaching figures.")


if __name__ == "__main__":
    main()
