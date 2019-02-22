from pathlib import Path
from lxml import html
import subprocess
import re
# import difflib
from dataclasses import dataclass

def test_chapter_01():
    chapter = 'chapter_01_domain_model'
    for listing in parse_listings(chapter):
        actual_contents = file_contents_for_branch(listing.filename, chapter)
        print('classes', listing.classes)
        actual_lines = actual_contents.split('\n')
        listing_lines = listing.contents.split('\n')
        missing_lines = [l for l in listing_lines if l not in actual_lines]
        if 'noncontinuous' in listing.classes:
            if missing_lines:
                print('\n'.join(missing_lines))
                assert listing_lines == actual_lines

        elif listing.contents not in actual_contents:
            assert listing_lines == actual_lines


@dataclass
class Listing:
    filename: str
    contents: str
    classes: list


def parse_listings(chapter_name):
    raw_contents = Path(f'{chapter_name}.html').read_text()
    parsed_html = html.fromstring(raw_contents)

    for listing_node in parsed_html.cssselect('.exampleblock'):
        [title_node] = listing_node.cssselect('.title')
        filename = re.search(r'.+ \((.+)\)', title_node.text_content()).group(1)

        [block_node] = listing_node.cssselect('.listingblock')
        classes = block_node.get('class').split()

        [code_node] = block_node.cssselect('.content pre')
        yield Listing(filename, contents=code_node.text_content(), classes=classes)


def file_contents_for_branch(filename, chapter_name):
    return subprocess.run(
        ['git', 'show', f'origin/{chapter_name}:{filename}'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()



