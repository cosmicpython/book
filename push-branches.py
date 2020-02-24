#!/usr/bin/env python

import subprocess
from pathlib import Path
from chapters import CHAPTERS, NO_EXERCISE, STANDALONE

processes = []

for chapter in CHAPTERS + STANDALONE:
    print('pushing', chapter)
    processes.append(subprocess.Popen(
        ['git', 'push', '-v', '--force-with-lease', 'origin', chapter],
        cwd=Path(__file__).parent / 'code',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    ))
    if chapter in NO_EXERCISE:
        continue
    exercise_branch = f'{chapter}_exercise'
    print('pushing', exercise_branch)
    processes.append(subprocess.Popen(
        ['git', 'push', '-v', '--force-with-lease', 'origin', exercise_branch],
        cwd=Path(__file__).parent / 'code',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    ))

print('pushing master')
processes.append(subprocess.Popen(
    ['git', 'push', '-v', '--force-with-lease', 'origin', 'master'],
    cwd=Path(__file__).parent / 'code',
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
))

for p in processes:
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)
