from pathlib import Path
from lxml import html
import re

def parse_listings(chapter_name):
    raw_contents = Path(f'{chapter_name}.html').read_text()
    parsed_html = html.fromstring(raw_contents)

    for listing_node in parsed_html.cssselect('.exampleblock'):
        [content_node] = listing_node.cssselect('.listingblock .content pre')
        [title_node] = listing_node.cssselect('.title')
        filename = re.search(r'.+ \((.+)\)', title_node.text_content()).group(1)
        yield filename, content_node.text_content()


def test_chapter_01():
    for filename, listing in parse_listings('chapter_01_domain_model'):
        assert 'test' in listing

