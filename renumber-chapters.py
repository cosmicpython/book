#!/usr/bin/env python
import subprocess
from pathlib import Path

MOVES = [
    # change these as desired
    ('chapter_09B_external_events', 'chapter_10_external_events'),
    ('chapter_10_cqrs', 'chapter_11_cqrs'),
    ('chapter_11_dependency_injection', 'chapter_12_dependency_injection'),
]

for frm, to in MOVES:
    subprocess.run(['git', 'mv', f'{frm}.asciidoc', f'{to}.asciidoc'])

sources = list(Path(__file__).absolute().parent.glob('*.asciidoc'))
for frm, to in MOVES:
    subprocess.run(
        ['sed', '-i', f's/{frm}/{to}/g'] + sources + ['chapters.py', 'atlas.json', 'Readme.md'],
        check=True,
    )

input('base repo done, ready to do submodules')

for frm, to in MOVES[1:]:
    code = Path(__file__).absolute().parent / 'code'
    subprocess.run(['git', 'branch', '-m', frm, to], cwd=code)
    subprocess.run(['git', 'push', 'origin', f':{frm}'], cwd=code)
    subprocess.run(['git', 'checkout', to], cwd=code)
    subprocess.run(['git', 'branch', '--unset-upstream'], cwd=code)
    subprocess.run(['git', 'push', '-u', 'origin', to], cwd=code)
    input(f'{frm}->{to} done in theory')
