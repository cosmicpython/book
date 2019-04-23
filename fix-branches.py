#!/usr/bin/env python

import subprocess
from pathlib import Path
from chapters import CHAPTERS

for chapter in CHAPTERS:
    subprocess.run(
        ['git', '-c', 'pager.show=false', 'show', '-s', '--oneline', f':/{chapter}_ends'],
        cwd=Path(__file__).parent / 'code'
    )
    subprocess.run(
        ['git', 'branch', '-f', chapter, f':/{chapter}_ends'],
        cwd=Path(__file__).parent / 'code'
    )
    subprocess.run(
        ['git', 'diff', chapter, f'origin/{chapter}'],
        cwd=Path(__file__).parent / 'code'
    )

