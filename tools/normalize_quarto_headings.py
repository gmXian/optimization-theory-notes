#!/usr/bin/env python3
"""Normalize core content headings for Quarto without changing prose or math.

Each rendered page keeps one H1. Legacy top-level sections become H2, and
their descendants are adjusted only as much as needed to preserve hierarchy.
The transformation is idempotent.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FILES = sorted(ROOT.glob("[0-9][0-9]_*/*.md"))

DUPLICATE_TITLES = {
    "03_The_Primal_Simplex_Procedure/01_中文笔记.md":
        "# 第 3 章：原始单纯形法（The Primal Simplex Procedure）",
    "04_Duality_and_the_Linear_Complementarity_Problem/01_中文笔记.md":
        "# 第 4 章：对偶与线性互补问题（Duality and the Linear Complementarity Problem）",
    "05_Other_Simplex_Procedures/01_中文笔记.md":
        "# 第 5 章：其他单纯形方法（Other Simplex Procedures）",
    "06_Network_Programming/01_中文笔记.md":
        "# 第 6 章：网络规划（Network Programming）",
    "09_Search_Techniques_for_Unconstrained_Optimization_Problems/01_中文笔记.md":
        "# 第 9 章：无约束优化的搜索技术（Search Techniques for Unconstrained Optimization）",
}

HEADING = re.compile(r"^(#{1,6})(\s+.*)$")


def merge_duplicate_title(relative: str, lines: list[str]) -> list[str]:
    title = DUPLICATE_TITLES.get(relative)
    if not title or len(lines) < 2:
        return lines
    if lines[0].startswith("# ") and lines[1].startswith("# "):
        return [title + "\n", "\n", *lines[2:]]
    return lines


def normalize(relative: str, text: str) -> str:
    lines = merge_duplicate_title(relative, text.splitlines(keepends=True))
    is_exercises = relative.endswith("02_习题与答案_中英双语.md")
    seen_h1 = False
    in_fence = False
    legacy_section = False
    legacy_h2_seen = False
    output: list[str] = []

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            output.append(line)
            continue

        match = None if in_fence else HEADING.match(line)
        if not match:
            output.append(line)
            continue

        level = len(match.group(1))
        suffix = match.group(2)

        if level == 1:
            if not seen_h1:
                seen_h1 = True
                legacy_section = False
                legacy_h2_seen = False
                output.append(line)
                continue
            legacy_section = True
            legacy_h2_seen = False
            output.append("##" + suffix)
            continue

        if not legacy_section:
            output.append(line)
            continue

        if is_exercises:
            if level == 2:
                legacy_h2_seen = True
                new_level = 3
            elif level == 3 and not legacy_h2_seen:
                new_level = 3
            else:
                new_level = min(6, level + 1)
        else:
            new_level = min(6, level + 1)

        output.append("#" * new_level + suffix)

    return "".join(output)


def main() -> None:
    changed = 0
    for path in FILES:
        relative = path.relative_to(ROOT).as_posix()
        before = path.read_text(encoding="utf-8")
        after = normalize(relative, before)
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed += 1
    print(f"Normalized {changed} files; checked {len(FILES)} core Markdown files.")


if __name__ == "__main__":
    main()

