from pathlib import Path
from lxml import html

def parse_listings(chapter_name):
    raw_contents = Path(f'{chapter_name}.asciidoc').read_text()
    parsed_html = html.fromstring(raw_contents)

    for listing_node in parsed_html.cssselect('.listingblock'):
        [content_node] = listing_node.cssselect('.content')
        yield content_node.text_content()

def test_chapter_01():
    for l in parse_listings('chapter_01_domain_model'):
        assert 'test' in l

