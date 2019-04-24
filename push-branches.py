#!/usr/bin/env python

import subprocess
from pathlib import Path
from chapters import CHAPTERS

for chapter in CHAPTERS:
    subprocess.run(
        ['git', 'push', '--force-with-lease', 'origin', chapter],
        cwd=Path(__file__).parent / 'code'
    )
subprocess.run(
    ['git', 'push', '--force-with-lease', 'origin', 'master'],
    cwd=Path(__file__).parent / 'code'
)

