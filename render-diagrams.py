#!/usr/bin/env python3
import tempfile
import subprocess
from pathlib import Path
from lxml import html

IMAGES_DIR = Path(__file__).absolute().parent / 'images'


def main():
    for fn in Path(__file__).absolute().parent.glob('*.html'):
        chapter_name = fn.name.replace('.html', '')
        if chapter_name == 'book':
            continue
        print('Rendering images for', chapter_name)
        render_images(chapter_name)


def render_images(chapter_name):
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
            print(code)
            render_image(code, image_id)

def render_image(source, image_id):
    tf = Path(tempfile.NamedTemporaryFile().name)
    tf.write_text(f'[ditaa,{image_id}]\n....\n{source}\n....\n')
    cmd = ['asciidoctor', '-r', 'asciidoctor-diagram', '-a', f'imagesoutdir={IMAGES_DIR}', str(tf)]
    print(' '.join(cmd))
    subprocess.run(cmd)

if __name__ == '__main__':
    main()
