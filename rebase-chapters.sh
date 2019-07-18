#/bin/bash
set -ex

if [[ $# -eq 0 ]] ; then
    echo 'need commit to rebase from'
    exit 0
fi

cd code
git co chapter_10_dependency_injection
git irebase $1

git co master
git reset --hard chapter_10_dependency_injection

cd ..
