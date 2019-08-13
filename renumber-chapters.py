#!/usr/bin/env python
import subprocess
from pathlib import Path
MOVES = [
    ('chapter_02B_abstractions', 'chapter_03_abstractions'),
    ('chapter_03_service_layer', 'chapter_04_service_layer'),
    ('chapter_04_uow', 'chapter_05_uow'),
    ('chapter_05_aggregate', 'chapter_06_aggregate'),
    ('chapter_06_events_and_message_bus', 'chapter_07_events_and_message_bus'),
    ('chapter_07_external_events', 'chapter_08_external_events'),
    ('chapter_08_commands', 'chapter_09_commands'),
    ('chapter_09_cqrs', 'chapter_10_cqrs'),
    ('chapter_10_dependency_injection', 'chapter_11_dependency_injection'),
]

for frm, to in MOVES:
    subprocess.run(['git', 'mv', f'{frm}.asciidoc', f'{to}.asciidoc'])

sources = list(Path(__file__).absolute().parent.glob('*.asciidoc'))
for frm, to in MOVES:
    subprocess.run(['sed', '-i', f's/{frm}/{to}/g'] + sources + ['chapters.py', 'atlas.json', 'Readme.md'])

input('base repo done, ready to do submodules')

for frm, to in MOVES[1:]:
    code = Path(__file__).absolute().parent / 'code'
    subprocess.run(['git', 'branch', '-m', frm, to], cwd=code)
    subprocess.run(['git', 'push', 'origin', f':{frm}'], cwd=code)
    subprocess.run(['git', 'checkout', to], cwd=code)
    subprocess.run(['git', 'branch', '--unset-upstream'], cwd=code)
    subprocess.run(['git', 'push', '-u', 'origin', to], cwd=code)
    input(f'{frm}->{to} done in theory')
