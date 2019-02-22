from pathlib import Path
from lxml import html

def parse_listings(chapter_name):
    raw_contents = Path(filename + '.asciidoc').read_text()
    parsed_html = html.fromstring(raw_contents)
    listing_nodes = parsed_html.cssselect('.listingblock')

def test_chapter_01():
    listings = parse_listings('chapter_01_domain_model')
    assert 0

