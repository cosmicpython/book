from pathlib import Path
from lxml import html
import subprocess
import re
import difflib

def test_chapter_01():
    chapter = 'chapter_01_domain_model'
    for filename, listing in parse_listings(chapter):
        actual_contents = file_contents_for_branch(filename, chapter)
        if listing not in actual_contents:
            raise_with_helpful_diff(filename, listing, actual_contents)

def parse_listings(chapter_name):
    raw_contents = Path(f'{chapter_name}.html').read_text()
    parsed_html = html.fromstring(raw_contents)

    for listing_node in parsed_html.cssselect('.exampleblock'):
        [content_node] = listing_node.cssselect('.listingblock .content pre')
        [title_node] = listing_node.cssselect('.title')
        filename = re.search(r'.+ \((.+)\)', title_node.text_content()).group(1)
        yield filename, content_node.text_content()


def file_contents_for_branch(filename, chapter_name):
    return subprocess.run(
        ['git', 'show', f'origin/{chapter_name}:{filename}'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()


def raise_with_helpful_diff(filename, listing, actual_contents):
    assert listing.split('\n') == actual_contents.split('\n')

