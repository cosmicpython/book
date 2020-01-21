#!/usr/bin/env python
import subprocess
from pathlib import Path

MOVES = [
    # change these as desired
    ('chapter_04b_high_gear_low_gear', 'chapter_05_high_gear_low_gear'),
    ('chapter_05_uow', 'chapter_06_uow'),
    ('chapter_06_aggregate', 'chapter_07_aggregate'),
    ("chapter_07_events_and_message_bus", "chapter_08_events_and_message_bus"),
    ("chapter_08_all_messagebus", "chapter_09_all_messagebus"),
    ("chapter_09_commands", "chapter_10_commands"),
    ("chapter_10_external_events", "chapter_11_external_events"),
    ("chapter_11_cqrs", "chapter_12_cqrs"),
    ("chapter_12_dependency_injection", "chapter_13_dependency_injection"),
]

for frm, to in MOVES:
    subprocess.run(['git', 'mv', f'{frm}.asciidoc', f'{to}.asciidoc'], check=True)

sources = list(Path(__file__).absolute().parent.glob('*.asciidoc'))
otherthings = [
    'chapters.py',
    'atlas.json',
    'Readme.md',
    'rebase-chapters.sh',
    'rebase-appendices.sh',
]
for frm, to in MOVES:
    subprocess.run(
        ['sed', '-i', f's/{frm}/{to}/g'] + sources + otherthings,
        check=True,
    )

input('base repo done, ready to do submodules')

for frm, to in MOVES:
    code = Path(__file__).absolute().parent / 'code'
    subprocess.run(['git', 'branch', '-m', frm, to], cwd=code)
    subprocess.run(['git', 'branch', '--unset-upstream', to], cwd=code) # untested
    subprocess.run(['git', 'push', 'origin', f':{frm}'], cwd=code)
    subprocess.run(['git', 'checkout', to], cwd=code)
    subprocess.run(['git', 'push', '-u', 'origin', to], cwd=code)
    from chapters import NO_EXERCISE
    if to not in NO_EXERCISE:
        # untested
        subprocess.run(
            ['git', 'branch', '-m', f'{frm}_exercise', f'{to}_exercise'],
            cwd=code, check=True,
        )

    input(f'{frm}->{to} done in theory')
