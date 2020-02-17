#!/usr/bin/env python3
import sys
import tempfile
import subprocess
from pathlib import Path
from lxml import html

IMAGES_DIR = Path(__file__).absolute().parent / 'images'


def all_chapter_names():
    for fn in sorted(Path(__file__).absolute().parent.glob('*.html')):
        chapter_name = fn.name.replace('.html', '')
        if chapter_name == 'book':
            continue
        yield chapter_name

def main(paths):
    if paths:
        chapter_names = [p.replace('.html', '').replace('.asciidoc', '') for p in paths]
    else:
        chapter_names = all_chapter_names()
    for chapter_name in chapter_names:
        render_images(chapter_name)


def render_images(chapter_name):
    print('Rendering images for', chapter_name)
    raw_contents = Path(f'{chapter_name}.html').read_text()
    parsed_html = html.fromstring(raw_contents)

    for image_block in parsed_html.cssselect('.imageblock'):
        [img] = image_block.cssselect('img')
        image_id = img.get('src').replace('images/', '').replace('.png', '')
        print(image_id)

        parent = image_block.getparent()
        next_sibling_pos = parent.index(image_block) + 1
        try:
            next_element = parent[next_sibling_pos]
        except IndexError:
            continue
        if 'image-source' in next_element.classes:
            code = next_element.cssselect('pre')[0].text
            render_image(code, image_id)

INCLUDES = [
    'images/C4_Context.puml',
    'images/C4_Component.puml',
]

def _add_dots(source, image_id):
    lines = source.splitlines()
    assert lines[0].startswith('[')
    assert image_id in lines[0]
    plantuml_cfg = str(Path('plantuml.cfg').absolute())
    lines[0] = lines[0].replace('config=plantuml.cfg', f'config={plantuml_cfg}')
    for ix, l in enumerate(lines):
        if include := next((i for i in INCLUDES if i in l), None):
            lines[ix] = l.replace(include, str(Path(include).absolute()))
    lines.insert(1, '....')
    lines.append('....')
    return '\n'.join(lines)


def render_image(source, image_id):
    source = _add_dots(source, image_id)
    print(source)
    target = Path(f'images/{image_id}.png')
    if target.exists():
        target.unlink()
    tf = Path(tempfile.NamedTemporaryFile().name)
    tf.write_text(source)
    cmd = ['asciidoctor', '-r', 'asciidoctor-diagram', '-a', f'imagesoutdir={IMAGES_DIR}', str(tf)]
    print(' '.join(cmd))
    subprocess.run(cmd, check=True)


if __name__ == '__main__':
    main(sys.argv[1:])
