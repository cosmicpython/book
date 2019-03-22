# Book repo

| Book | Code |
| ---- | ---- |
| [![Book Build Status](https://travis-ci.org/python-leap/book.svg?branch=master)](https://travis-ci.org/python-leap/book) | [![Code build status](https://travis-ci.org/python-leap/code.svg?branch=master)](https://travis-ci.org/python-leap/code) |


## Table of Contents

* [Preface](preface.asciidoc)
* [Prologue](prologue.asciidoc)
* [chapter 1: Domain Model](chapter_01_domain_model.asciidoc)
* [chapter 2: Repository](chapter_02_repository.asciidoc)
* [chapter 3: Flask API and Service Layer](chapter_03_flask_api_and_service_layer.asciidoc)
* [chapter 4: Unit of Work](chapter_04_uow.asciidoc)
* [appendix A: Project Structure](appendix_project_structure.asciidoc)
* [appendix B: A major infrastructure change, made easy](appendix_csvs.asciidoc)


## Dependencies:

* asciidoctor
* coderay (for syntax higlighting)

```sh
gem install asciidoctor
gem install coderay
```


## Commands

```sh
make html  # builds local .html versions of each chapter
make test  # does a sanity-check of the code listings
make html test # does both
```

