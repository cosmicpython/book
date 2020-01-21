#!/usr/bin/env python
from pathlib import Path
import re

for path in sorted(Path(__file__).absolute().parent.glob('*.asciidoc')):
    images = re.findall(r'::images/(\w+\.png)', path.read_text())
    if not images:
        continue
    chapter_no = re.search(r'chapter_(\d\d)', str(path))
    if chapter_no:
        chapter_no = str(int(chapter_no.group(1)))
    else:
        chapter_no = '??'
    print(path.name)
    for ix, image in enumerate(images):
        print(f'  Figure {chapter_no}.{ix+1}: {image}')
