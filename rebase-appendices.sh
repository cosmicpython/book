#/bin/bash
set -ex

cd code
git co appendix_django
git irebase chapter_06_uow

git co appendix_csvs
git irebase chapter_06_uow

git co master
