import pytest
import re
import subprocess
from dataclasses import dataclass
from lxml import html
from pathlib import Path

@pytest.mark.parametrize('chapter', [
    'chapter_01_domain_model',
    'chapter_02_repository',
])
def test_chapter(chapter):
    for listing in parse_listings(chapter):
        check_listing(listing, chapter)

def check_listing(listing, chapter):
    actual_contents = file_contents_for_branch(listing.filename, chapter)
    actual_lines = actual_contents.split('\n')
    if 'skip' in listing.classes:
        return
    if 'noncontinuous' in listing.classes:
        missing_lines = [l for l in listing.lines if l not in actual_lines]
        if missing_lines:
            print('\n'.join(missing_lines))
            assert listing.lines == actual_lines

    elif listing.fixed_contents not in actual_contents:
        assert listing.lines == actual_lines


@dataclass
class Listing:
    filename: str
    contents: str
    classes: list

    @property
    def fixed_contents(self):
        return re.sub(r'  \(\d\)$', '', self.contents, flags=re.MULTILINE)

    @property
    def lines(self):
        return self.fixed_contents.split('\n')


def parse_listings(chapter_name):
    raw_contents = Path(f'{chapter_name}.html').read_text()
    parsed_html = html.fromstring(raw_contents)

    for listing_node in parsed_html.cssselect('.exampleblock'):
        [title_node] = listing_node.cssselect('.title')
        try:
            filename = re.search(r'.+ \((.+)\)', title_node.text_content()).group(1)
        except AttributeError as e:
            raise AssertionError(f'Could not find filename in title {title_node.text_content()}') from e

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



