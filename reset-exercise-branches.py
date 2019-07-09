#!/usr/bin/env python
import subprocess
from pathlib import Path
from chapters import CHAPTERS


def run(cmds):
    print(' '.join(cmds))
    p = subprocess.run(
        cmds,
        cwd=Path(__file__).parent / 'code',
        capture_output=True,
    )
    if p.returncode:
        raise Exception(p.stderr.decode())
    output = p.stdout.decode()
    print(output)
    return output


all_branches = run(['git', 'branch', '-a'],)

for chapter in CHAPTERS:
    exercise_chapter = f'{chapter}_exercise'
    if exercise_chapter not in all_branches:
        continue
    run(['git', 'checkout', exercise_chapter])
    run(['git', 'reset', '--hard', f'origin/{exercise_chapter}'])
run(['git', 'checkout', 'master'])
