# Book repo

| Book | Code |
| ---- | ---- |
| [![Book Build Status](https://travis-ci.org/python-leap/book.svg?branch=master)](https://travis-ci.org/python-leap/book) | [![Code build status](https://travis-ci.org/python-leap/code.svg?branch=master)](https://travis-ci.org/python-leap/code) |


## Table of Contents

* [preface](preface.asciidoc)

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

