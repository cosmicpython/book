#!/usr/bin/env python

import subprocess
from pathlib import Path
from chapters import CHAPTERS, NO_EXERCISE

for chapter in CHAPTERS:
    print('pushing', chapter, end=': ', flush=True)
    subprocess.run(
        ['git', 'push', '--force-with-lease', 'origin', chapter],
        cwd=Path(__file__).parent / 'code'
    )
    if chapter in NO_EXERCISE:
        continue
    exercise_branch = f'{chapter}_exercise'
    print('pushing', exercise_branch, end=': ', flush=True)
    subprocess.run(
        ['git', 'push', '--force-with-lease', 'origin', exercise_branch],
        cwd=Path(__file__).parent / 'code'
    )

subprocess.run(
    ['git', 'push', '--force-with-lease', 'origin', 'master'],
    cwd=Path(__file__).parent / 'code'
)
