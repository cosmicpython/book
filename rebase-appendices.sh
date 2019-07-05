#/bin/bash
set -ex

cd code
git co appendix_django
git irebase chapter_04_uow

git co appendix_csvs
git irebase chapter_04_uow

git co appendix_bootstrap
git irebase chapter_10_dependency_injection

git co master
