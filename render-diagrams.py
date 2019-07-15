#!/usr/bin/env python3
import tempfile
import subprocess
from pathlib import Path
from lxml import html
from chapters import CHAPTERS

IMAGES_DIR = Path(__file__).resolve().parent / 'images'

def render_images(chapter_name):
    raw_contents = Path(f'{chapter_name}.html').read_text()
    parsed_html = html.fromstring(raw_contents)

    for image_block in parsed_html.cssselect('.imageblock'):
        [img] = image_block.cssselect('img')

        parent = image_block.getparent()
        next_sibling_pos = parent.index(image_block) + 1
        try:
            next_element = parent[next_sibling_pos]
        except IndexError:
            continue
        if 'Comment' in str(next_element.tag) and next_element.text.strip().startswith('IMAGE SOURCE'):
            print(next_element.text)
            image_id = img.get('src').lstrip('images/').rstrip('.png')
            assert f'[ditaa, {image_id}]' in next_element.text
            render_image(next_element.text.strip().lstrip('IMAGE SOURCE'))

def render_image(source):
    tf = Path(tempfile.NamedTemporaryFile().name)
    tf.write_text(source)
    cmd = ['asciidoctor', '-r', 'asciidoctor-diagram', '-a', f'imagesoutdir={IMAGES_DIR}', str(tf)]
    print(' '.join(cmd))
    subprocess.run(cmd)

render_images('prologue')
