import pytest
import re
import subprocess
from dataclasses import dataclass
from lxml import html
from pathlib import Path

CHAPTERS = [
    'chapter_01_domain_model',
    'chapter_02_repository',
    "chapter_03_flask_api_and_service_layer",
    "appendix_project_structure",
]


def git_log(chapter):
    return subprocess.run(
        ['git', 'log', f'origin/{chapter}', '--oneline', '--decorate'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()

@pytest.fixture(scope='session')
def master_log():
    return git_log('master')

@pytest.mark.parametrize('chapter', CHAPTERS)
def test_master_has_all_chapters_in_its_history(master_log, chapter):
    assert f'origin/{chapter}' in master_log


@pytest.mark.parametrize('chapter', CHAPTERS)
def test_each_chapter_follows_the_last(chapter):
    chapter_no = CHAPTERS.index(chapter)
    if chapter_no == 0:
        return
    previous = CHAPTERS[chapter_no - 1]
    assert f'origin/{previous}' in git_log(chapter), f'{chapter} did not follow {previous}'


@pytest.mark.parametrize('chapter', CHAPTERS)
def test_chapter(chapter):
    for listing in parse_listings(chapter):
        check_listing(listing, chapter)


def check_listing(listing, chapter):
    if 'skip' in listing.classes:
        return
    actual_contents = file_contents_for_branch(listing.filename, chapter)
    actual_lines = actual_contents.split('\n')
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

    callouts = re.compile(r'  #?\(\d\)$', flags=re.MULTILINE)
    callouts_alone = re.compile(r'^\(\d\)$')

    @property
    def fixed_contents(self):
        fixed = self.contents
        fixed = self.callouts.sub('', fixed)
        fixed = '\n'.join(
            l for l in fixed.splitlines()
            if not self.callouts_alone.match(l)
        )
        return fixed

    @property
    def lines(self):
        return self.fixed_contents.split('\n')


def parse_listings(chapter_name):
    raw_contents = Path(f'{chapter_name}.html').read_text()
    parsed_html = html.fromstring(raw_contents)

    for listing_node in parsed_html.cssselect('.exampleblock'):
        [block_node] = listing_node.cssselect('.listingblock')
        classes = block_node.get('class').split()

        [title_node] = listing_node.cssselect('.title')
        print('found listing', title_node.text_content())
        try:
            filename = re.search(r'.+ \((.+)\)', title_node.text_content()).group(1)
        except AttributeError as e:
            if 'skip' in classes:
                filename = None
            else:
                raise AssertionError(f'Could not find filename in title {title_node.text_content()}') from e

        [code_node] = block_node.cssselect('.content pre')
        yield Listing(filename, contents=code_node.text_content(), classes=classes)


def file_contents_for_branch(filename, chapter_name):
    return subprocess.run(
        ['git', 'show', f'origin/{chapter_name}:{filename}'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()

