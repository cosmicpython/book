#!/usr/bin/env python

import subprocess
from pathlib import Path
from chapters import CHAPTERS, STANDALONE

for chap in CHAPTERS + STANDALONE:
    subprocess.run(
        ['git', 'checkout', chap],
        cwd=Path(__file__).parent / 'code'
    )
subprocess.run(
    ['git', 'checkout', 'master'],
    cwd=Path(__file__).parent / 'code'
)

