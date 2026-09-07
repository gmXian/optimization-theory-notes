#!/usr/bin/env python3
"""Check rendered HTML entrypoints and local links after `quarto render`."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_book"
errors: list[str] = []


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(("href", attrs["href"]))
        if tag in {"img", "script"} and attrs.get("src"):
            self.links.append(("src", attrs["src"]))
        if tag == "link" and attrs.get("href"):
            self.links.append(("href", attrs["href"]))


if not (SITE / "index.html").is_file():
    errors.append("_book/index.html is missing")

html_files = sorted(SITE.rglob("*.html")) if SITE.is_dir() else []
for html in html_files:
    parser = LinkParser()
    parser.feed(html.read_text(encoding="utf-8", errors="replace"))
    for attribute, raw in parser.links:
        if raw.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
            continue
        parsed = urlsplit(raw)
        if not parsed.path or parsed.path.startswith("/"):
            continue
        if attribute == "href" and parsed.path.lower().endswith((".md", ".qmd")):
            errors.append(
                f"{html.relative_to(SITE)}: source document leaked into rendered link: {raw}"
            )
            continue
        target = (html.parent / unquote(parsed.path)).resolve()
        if parsed.path.endswith("/"):
            target = target / "index.html"
        try:
            target.relative_to(SITE.resolve())
        except ValueError:
            errors.append(f"{html.relative_to(SITE)}: link escapes site: {raw}")
            continue
        if not target.exists():
            errors.append(f"{html.relative_to(SITE)}: missing {attribute} target: {raw}")

print(f"Rendered HTML files: {len(html_files)}")
print(f"Rendered site errors: {len(errors)}")
for error in errors[:100]:
    print("ERROR:", error)
if len(errors) > 100:
    print(f"... and {len(errors) - 100} more")
sys.exit(1 if errors else 0)
