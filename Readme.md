# Book repo

| Book | Code |
| ---- | ---- |
| [![Book Build Status](https://travis-ci.org/python-leap/book.svg?branch=master)](https://travis-ci.org/python-leap/book) | [![Code build status](https://travis-ci.org/python-leap/code.svg?branch=master)](https://travis-ci.org/python-leap/code) |


## Table of Contents

O'Reilly have generously allowed us to publish this book under a [CC license](license.txt),
and while it's still under construction you can read it here.  In return, pull requests,
typofixes, and more substantial feedback + suggestions are enthusiastically solicited.

* [Preface](preface.asciidoc)
* [Prologue](prologue.asciidoc)
* [Chapter 1: Domain Model](chapter_01_domain_model.asciidoc)
* [Chapter 2: Repository](chapter_02_repository.asciidoc)
* [Chapter 3: Flask API and Service Layer](chapter_03_flask_api_and_service_layer.asciidoc)
* [Chapter 4: Unit of Work](chapter_04_uow.asciidoc)
* [Chapter 5: Aggregates](chapter_05_aggregate.asciidoc)
* [Appendix A: Project Structure](appendix_project_structure.asciidoc)
* [Appendix B: A major infrastructure change, made easy](appendix_csvs.asciidoc)


Below is just instructions for me and bob really.

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
```

