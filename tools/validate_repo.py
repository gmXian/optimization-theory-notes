#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]

def strip_code(text:str)->str:
    text=re.sub(r'```.*?```','',text,flags=re.S)
    text=re.sub(r'`[^`\n]*`','',text)
    return text

for md in root.rglob('*.md'):
    raw=md.read_text(encoding='utf-8')
    t=strip_code(raw)
    # Block math delimiter count outside code.
    if t.count('$$')%2:
        errors.append(f'{md.relative_to(root)}: unmatched $$ delimiter')
    if '/mnt/data/' in t or 'sandbox:/mnt/data/' in t:
        errors.append(f'{md.relative_to(root)}: contains local/sandbox absolute path')
    # Markdown image refs outside code.
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)',t):
        target=m.group(1).strip().split()[0].strip('<>')
        if re.match(r'^[a-z]+://',target):
            continue
        target=target.split('#',1)[0]
        path=(md.parent/target).resolve()
        try: path.relative_to(root.resolve())
        except Exception:
            errors.append(f'{md.relative_to(root)}: image escapes repository: {target}')
            continue
        if not path.exists():
            errors.append(f'{md.relative_to(root)}: missing image: {target}')

    # Ordinary Markdown links outside code (local repository targets only).
    for m in re.finditer(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', t):
        target=m.group(1).strip().split()[0].strip('<>')
        if not target or target.startswith('#') or re.match(r'^(?:[a-z]+:)?//',target) or target.startswith('mailto:'):
            continue
        target=target.split('#',1)[0]
        if not target:
            continue
        path=(md.parent/target).resolve()
        try: path.relative_to(root.resolve())
        except Exception:
            errors.append(f'{md.relative_to(root)}: link escapes repository: {target}')
            continue
        if not path.exists():
            errors.append(f'{md.relative_to(root)}: missing local link target: {target}')

# Chapter fixed structure for existing chapter dirs only.
for ch in sorted(root.glob('[0-9][0-9]_*')):
    if not ch.is_dir(): continue
    for req in ['01_中文笔记.md','02_习题与答案_中英双语.md','images']:
        if not (ch/req).exists(): errors.append(f'{ch.name}: missing {req}')
    imgdir=ch/'images'
    if imgdir.exists():
        for f in imgdir.iterdir():
            if f.is_file() and not re.fullmatch(r'[A-Za-z0-9_.-]+',f.name):
                warnings.append(f'{ch.name}: non-ASCII image filename {f.name}')

print(f'Errors: {len(errors)}')
for e in errors: print('ERROR:',e)
print(f'Warnings: {len(warnings)}')
for w in warnings: print('WARNING:',w)
sys.exit(1 if errors else 0)
