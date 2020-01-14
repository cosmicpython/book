#!/usr/bin/env python
import sys
import subprocess
from pathlib import Path


def run(cmds):
    print(' '.join(cmds))
    p = subprocess.run(
        cmds,
        cwd=Path(__file__).parent / 'code',
        capture_output=True,
        check=True
    )
    if p.returncode:
        raise Exception(p.stderr.decode())
    output = p.stdout.decode()
    print(output)
    return output

all_branches = run(['git', 'branch', '-a'],)


def main(chapter):
    exercise_chapter = f'{chapter}_exercise'
    assert exercise_chapter in all_branches

    run(['git', 'checkout', exercise_chapter])
    commits = list(reversed(run([
        'git', 'log', '--pretty=%h',
        f'{exercise_chapter}^{{/{chapter}_ends}}..{exercise_chapter}',
    ]).split()))
    run(['git', 'reset', '--hard', chapter])
    run(['git', 'cherry-pick', *commits])
    run(['git', 'checkout', 'master'])

if __name__ == '__main__':
    main(sys.argv[1])
