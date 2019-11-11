#!/usr/bin/env python3
import re
from pathlib import Path
from titlecase import titlecase
from chapters import CHAPTERS

SPECIAL = {
    'CSVs', 'To/From', 'UoW', 'AKA', 'SELECT',
}

LOWERCASE = {
    'with',
}



def specialcases(w, **_):
    if w.lower() in LOWERCASE:
        return w.lower()
    if w.lower() in {s.lower() for s in SPECIAL}:
        return next(special for special in SPECIAL if special.lower() == w.lower())
    if  '_' in w:
        return w
    return None


def fix_line(l):
    if not l.startswith('=='):
        return l
    if l == '====':
        return l
    if l == '.':
        return l
    prefix, rest = re.match(r'(=+ |\.)(.+)', l).groups()
    return prefix + titlecase(rest, callback=specialcases)


def main():
    for chapter in CHAPTERS:
        path = Path(f'{chapter}.asciidoc')
        contents = path.read_text()
        fixed = '\n'.join(
            fix_line(l) for l in contents.splitlines()
        )
        path.write_text(fixed)

if __name__ == '__main__':
    main()

import pytest

def test_lowercases_short_words():
    assert fix_line('=== What Is A Domain Model') == '=== What Is a Domain Model'

def test_fix_line_handles_quotes_and_slashes():
    assert fix_line('=== Foo "bar" baz') == '=== Foo "Bar" Baz'

def test_fix_line_leaves_small_words_alone_except_at_beginning():
    assert fix_line('=== This is a line') == '=== This Is a Line'
    assert fix_line('=== The initial the is fine') == '=== The Initial the Is Fine'

@pytest.mark.skip
def test_dotstarters():
    assert fix_line('.A sidebar title') == '.A Sidebar Title'

def test_hyphens():
    assert fix_line('=== A wrap-up') == '=== A Wrap-Up'

def test_uow():
    assert fix_line('=== A Uow') == '=== A UoW'

def test_underscores():
    assert fix_line('=== A special_method') == '=== A special_method'
