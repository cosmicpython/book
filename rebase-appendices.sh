#/bin/bash
set -ex

cd code
git co appendix_django
git irebase chapter_05_uow

git co appendix_csvs
git irebase chapter_05_uow

git co master
