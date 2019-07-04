#!/usr/bin/env python3
from pathlib import Path
from chapters import CHAPTERS


def fix_word(w):
    if w.upper() == w:
        return w
    if w == 'CSVs':
        return w
    return w.capitalize()

def fix_line(l):
    if not l.startswith('=='):
        return l
    if l == '====':
        return l
    return ' '.join(fix_word(w) for w in l.split())


for chapter in CHAPTERS:
    path = Path(f'{chapter}.asciidoc')
    contents = path.read_text()
    fixed = '\n'.join(
        fix_line(l) for l in contents.splitlines()
    )
    path.write_text(fixed)
