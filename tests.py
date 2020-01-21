# pylint: disable=redefined-outer-name
import re
import subprocess
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from lxml import html
import pytest
from chapters import CHAPTERS, BRANCHES, STANDALONE, NO_EXERCISE



def all_branches():
    return subprocess.run(
        ['git', 'branch', '-a'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode().split()

def git_log(chapter):
    return subprocess.run(
        ['git', 'log', chapter, '--oneline', '--decorate'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()

@pytest.fixture(scope='session')
def master_log():
    return git_log('master')

@pytest.mark.parametrize('chapter', CHAPTERS)
def test_master_has_all_chapters_in_its_history(master_log, chapter):
    if chapter in BRANCHES:
        return
    assert f'{chapter})' in master_log

@pytest.mark.parametrize('chapter', CHAPTERS)
def test_exercises_for_reader(chapter):
    exercise_branch = f'{chapter}_exercise'
    branches = all_branches()
    if chapter in NO_EXERCISE:
        if exercise_branch in branches:
            pytest.fail(f'looks like there is an exercise for {chapter} after all!')
        else:
            pytest.xfail(f'{chapter} has no exercise yet')
        return
    assert exercise_branch in branches
    assert f'{chapter})' in git_log(exercise_branch), f'Exercise for {chapter} not up to date'

def previous_chapter(chapter):
    chapter_no = CHAPTERS.index(chapter)
    if chapter_no == 0:
        return None
    previous = CHAPTERS[chapter_no - 1]
    if previous in BRANCHES:
        previous = CHAPTERS[chapter_no - 2]
    return previous

@pytest.mark.parametrize('chapter', CHAPTERS)
def test_each_chapter_follows_the_last(chapter):
    previous = previous_chapter(chapter)
    if previous is None:
        return
    assert f'{previous})' in git_log(chapter), f'{chapter} did not follow {previous}'


@pytest.mark.parametrize('chapter', CHAPTERS + STANDALONE)
def test_chapter(chapter):
    for listing in parse_listings(chapter):
        check_listing(listing, chapter)


@contextmanager
def checked_out(chapter):
    subprocess.run(
        ['git', 'checkout', f'{chapter}'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    )
    try:
        yield

    finally:
        subprocess.run(
            ['git', 'checkout', '-'],
            cwd=Path(__file__).parent / 'code',
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=True
        )


def tree_for_branch(chapter_name):
    with checked_out(chapter_name):
        return subprocess.run(
            ['tree', '-v', '-I', '__pycache__|*.egg-info'],
            cwd=Path(__file__).parent / 'code',
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=True
        ).stdout.decode()


def check_listing(listing, chapter):
    if 'tree' in listing.classes:
        actual_contents = tree_for_branch(chapter)
    elif 'non-head' in listing.classes:
        actual_contents = file_contents_for_tag(
            listing.filename, chapter, listing.tag,
        )
    elif 'existing' in listing.classes:
        actual_contents = file_contents_for_previous_chapter(
            listing.filename, chapter,
        )
    elif listing.is_diff:
        actual_contents = diff_for_tag(
            listing.filename, chapter, listing.tag,
        )

    else:
        actual_contents = file_contents_for_branch(listing.filename, chapter)
    actual_lines = actual_contents.split('\n')

    if '...' in listing.contents:
        for section in re.split(r'#?\.\.\.', listing.fixed_contents):
            lines = section.splitlines()
            if section.strip() not in actual_contents:
                assert lines == actual_lines, \
                        f'section from [{listing.tag}] not found within actual'

    elif listing.fixed_contents not in actual_contents:
        assert listing.lines == actual_lines, \
                f'listing [{listing.tag}] not found within actual'



@dataclass
class Listing:
    filename: str
    tag: str
    contents: str
    classes: list
    is_diff: bool

    callouts = re.compile(r'  #?(\(\d\) ?)+$', flags=re.MULTILINE)
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
        if 'skip' in classes:
            continue

        if 'tree' in classes:
            filename = None
        else:
            [title_node] = listing_node.cssselect('.title')
            title = title_node.text_content()
            print('found listing', title)
            try:
                filename = re.search(r'.+ \((.+)\)', title).group(1)
            except AttributeError as e:
                raise AssertionError(f'Could not find filename in title {title}') from e

        is_diff = bool(listing_node.cssselect('code[data-lang="diff"]'))
        tag = listing_node.get('id')

        [code_node] = block_node.cssselect('.content pre')
        yield Listing(
            filename, tag, contents=code_node.text_content(), classes=classes,
            is_diff=is_diff
        )


def file_contents_for_branch(filename, chapter_name):
    return subprocess.run(
        ['git', 'show', f'{chapter_name}:{filename}'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()

def file_contents_for_previous_chapter(filename, chapter_name):
    previous = previous_chapter(chapter_name)
    return file_contents_for_branch(filename, previous)

def file_contents_for_tag(filename, chapter_name, tag):
    output = subprocess.run(
        ['git', 'show', f'{chapter_name}^{{/\\[{tag}\\]}}:{filename}'],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()
    assert output.strip(), f'no commit found for [{tag}]'
    return output

def diff_for_tag(filename, chapter_name, tag):
    if tag.endswith('_diff'):
        tag = tag[:-5]
    output = subprocess.run(
        ['git', 'show', f'{chapter_name}^{{/\\[{tag}\\]}}', '--', filename],
        cwd=Path(__file__).parent / 'code',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True
    ).stdout.decode()
    assert output.strip(), f'no commit found for [{tag}]'
    return '\n'.join(l.rstrip() for l in output.splitlines())
