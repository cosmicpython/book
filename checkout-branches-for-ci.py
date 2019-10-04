#!/usr/bin/env python

import subprocess
from pathlib import Path
from chapters import CHAPTERS, STANDALONE, NO_EXERCISE

cwd = Path(__file__).parent / 'code'

for chap in CHAPTERS + STANDALONE:
    subprocess.run(['git', 'checkout', chap], cwd=cwd)
    if chap in NO_EXERCISE:
        continue
    subprocess.run(['git', 'checkout', f'{chap}_exercise'], cwd=cwd)

subprocess.run(['git', 'checkout', 'master'], cwd=cwd)
