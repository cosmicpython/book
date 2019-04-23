#!/usr/bin/env python

import subprocess
from pathlib import Path
from chapters import CHAPTERS

for chap in CHAPTERS:
    subprocess.run(
        ['git', '-c', 'pager.show=false', 'show', '-s', '--oneline', f':/{chap}_ends'],
        cwd=Path(__file__).parent / 'code'
    )
    subprocess.run(
        ['git', 'branch', '-f', chap, f':/{chap}_ends'],
        cwd=Path(__file__).parent / 'code'
    )

