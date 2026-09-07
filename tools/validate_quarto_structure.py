#!/usr/bin/env python3
"""Validate Quarto configuration, page headings, links, and public assets."""

from __future__ import annotations

from pathlib import Path
import re
import sys

import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "_quarto.yml"
errors: list[str] = []
warnings: list[str] = []


def flatten_book_entries(entries):
    for entry in entries or []:
        if isinstance(entry, str):
            yield entry
        elif isinstance(entry, dict):
            yield from flatten_book_entries(entry.get("chapters"))


try:
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
except Exception as exc:
    errors.append(f"_quarto.yml cannot be parsed: {exc}")
    config = {}

render_targets = config.get("project", {}).get("render", []) if config else []
book = config.get("book", {}) if config else {}
book_targets = list(flatten_book_entries(book.get("chapters"))) + list(
    flatten_book_entries(book.get("appendices"))
)

for target in render_targets:
    if not (ROOT / target).is_file():
        errors.append(f"missing render target: {target}")

for target in book_targets:
    if not (ROOT / target).is_file():
        errors.append(f"missing book target: {target}")
    if target not in render_targets:
        errors.append(f"book target absent from project.render: {target}")

for target in book_targets:
    path = ROOT / target
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    text_without_fences = re.sub(r"```.*?```|~~~.*?~~~", "", text, flags=re.S)
    if path.suffix == ".md" and re.search(r"(?m)^---\s*$", text_without_fences):
        errors.append(
            f"{target}: bare --- can be misread as Quarto YAML; use *** for a divider"
        )
    h1_count = len(re.findall(r"(?m)^#\s+", text_without_fences))
    if target == "index.qmd":
        if h1_count > 1:
            errors.append(f"{target}: expected at most one H1, found {h1_count}")
    elif h1_count != 1:
        errors.append(f"{target}: expected exactly one H1, found {h1_count}")

for image in ROOT.glob("[0-9][0-9]_*/images/*.png"):
    try:
        with Image.open(image) as loaded:
            loaded.verify()
    except Exception as exc:
        errors.append(f"invalid image {image.relative_to(ROOT)}: {exc}")

for path in [ROOT / "styles.scss", ROOT / "assets/site.html"]:
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"missing site asset: {path.relative_to(ROOT)}")

print(f"Quarto structure errors: {len(errors)}")
for error in errors:
    print("ERROR:", error)
print(f"Quarto structure warnings: {len(warnings)}")
for warning in warnings:
    print("WARNING:", warning)
sys.exit(1 if errors else 0)
