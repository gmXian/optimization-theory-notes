#!/usr/bin/env python3
"""Second-level repository review checks.

This script complements validate_repo.py. It checks content coverage, bilingual
exercise-answer coverage, basic repository hygiene, and review artifacts. It
cannot prove mathematical correctness; source-page and numerical review remain
manual/semantic tasks documented in FULL_BOOK_REVIEW_REPORT.md.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

EXERCISES = {1:10, 2:46, 3:17, 4:33, 5:25, 6:26, 7:49, 8:28, 9:43, 10:15}
EXAMPLES = {1:7, 2:18, 3:14, 4:8, 5:9, 6:5, 7:5, 8:2, 9:10, 10:5}


def chapter_dir(ch: int) -> Path:
    matches = sorted(ROOT.glob(f"{ch:02d}_*"))
    if len(matches) != 1:
        ERRORS.append(f"Chapter {ch}: expected exactly one directory, found {len(matches)}")
        return ROOT / f"{ch:02d}_MISSING"
    return matches[0]


def strip_code(text: str) -> str:
    """Remove fenced and inline code before Markdown/MathJax checks."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def exercise_blocks(text: str, ch: int):
    """Return first top-level-ish heading block for each numbered exercise."""
    pat = re.compile(
        rf"(?m)^(#{{1,4}})\s+(?:Exercise\s+)?{ch}\.(\d+)(?!\d)[^\n]*"
    )
    starts = []
    seen = set()
    for m in pat.finditer(text):
        n = int(m.group(2))
        if n not in seen:
            starts.append((n, m.start()))
            seen.add(n)
    starts.sort(key=lambda x: x[1])
    blocks = {}
    for i, (n, pos) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else len(text)
        blocks[n] = text[pos:end]
    return blocks


# Global Markdown hygiene.
for md in ROOT.rglob("*.md"):
    raw = md.read_text(encoding="utf-8")
    bad = sorted({ord(c) for c in raw if ord(c) < 32 and c not in "\n\r\t"})
    if bad:
        ERRORS.append(f"{md.relative_to(ROOT)}: control characters {bad}")

    text = strip_code(raw)
    if text.count("$$") % 2:
        ERRORS.append(f"{md.relative_to(ROOT)}: unmatched $$ outside code")
    if re.search(r"(?<!\\)\\\(|(?<!\\)\\\[", text):
        WARNINGS.append(
            f"{md.relative_to(ROOT)}: contains \\( or \\[ outside code; prefer $/$$"
        )
    for env in ("aligned", "bmatrix", "pmatrix", "cases", "array", "matrix"):
        b = text.count(f"\\begin{{{env}}}")
        e = text.count(f"\\end{{{env}}}")
        if b != e:
            ERRORS.append(
                f"{md.relative_to(ROOT)}: unbalanced LaTeX environment {env} ({b} begin / {e} end)"
            )

# Chapter structure, exercise coverage, bilingual answers, examples.
for ch, max_ex in EXERCISES.items():
    d = chapter_dir(ch)
    note = d / "01_中文笔记.md"
    ans = d / "02_习题与答案_中英双语.md"
    img = d / "images"
    for p in (note, ans):
        if not p.exists():
            ERRORS.append(f"Chapter {ch}: missing {p.name}")
    if not img.is_dir():
        ERRORS.append(f"Chapter {ch}: missing images directory")
        continue

    if ans.exists():
        s = ans.read_text(encoding="utf-8")
        missing = [
            n for n in range(1, max_ex + 1)
            if not re.search(rf"(?<!\d){ch}\.{n}(?!\d)", s)
        ]
        if missing:
            ERRORS.append(f"Chapter {ch}: missing exercise identifiers {missing}")

        # Bilingual answer coverage. Accept either an English/英文 subsection in
        # the exercise block, or a consolidated English concise-solutions section
        # that explicitly includes the exercise number.
        blocks = exercise_blocks(s, ch)
        eng_idx = re.search(r"(?im)^#{1,4}\s+English\s+concise\s+solutions\b", s)
        eng_suffix = s[eng_idx.start():] if eng_idx else ""
        missing_english = []
        for n in range(1, max_ex + 1):
            in_block = bool(
                n in blocks and re.search(r"(?i)\bEnglish\b|英文", blocks[n])
            )
            in_summary = bool(
                eng_suffix and re.search(rf"(?im)^#{{1,4}}\s+Exercise\s+{ch}\.{n}(?!\d)", eng_suffix)
            )
            if not (in_block or in_summary):
                missing_english.append(n)
        if missing_english:
            ERRORS.append(
                f"Chapter {ch}: exercises without an English answer {missing_english}"
            )

    if note.exists():
        s = note.read_text(encoding="utf-8")
        max_example = EXAMPLES[ch]
        missing_examples = [
            n for n in range(1, max_example + 1)
            if not re.search(rf"(?i)example\s*{n}\b", s)
        ]
        if missing_examples:
            ERRORS.append(f"Chapter {ch}: missing Example identifiers {missing_examples}")

# Root review artifacts.
for required in [
    "README.md", "BOOK_AUDIT.md", "EXERCISE_INDEX.md", "学习进度.md",
    "SELF_CONTAINED_NOTE_STANDARD.md", "FORMATTING_GUIDE.md",
    "FULL_BOOK_REVIEW_REPORT.md",
]:
    if not (ROOT / required).exists():
        ERRORS.append(f"root: missing {required}")

print(f"Coverage errors: {len(ERRORS)}")
for e in ERRORS:
    print("ERROR:", e)
print(f"Coverage warnings: {len(WARNINGS)}")
for w in WARNINGS:
    print("WARNING:", w)

sys.exit(1 if ERRORS else 0)
