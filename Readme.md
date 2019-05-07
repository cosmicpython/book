# Book repo

| Book | Code |
| ---- | ---- |
| [![Book Build Status](https://travis-ci.org/python-leap/book.svg?branch=master)](https://travis-ci.org/python-leap/book) | [![Code build status](https://travis-ci.org/python-leap/code.svg?branch=master)](https://travis-ci.org/python-leap/code) |


## Table of Contents

O'Reilly have generously allowed us to publish this book under a [CC license](license.txt),
and while it's still under construction you can read it here.  In return, pull requests,
typofixes, and more substantial feedback + suggestions are enthusiastically solicited.

| Chapter |       |
| ------- | ----- |
| [Preface](preface.asciidoc) | |
| [Prologue](prologue.asciidoc)| |
| [Chapter 1: Domain Model](chapter_01_domain_model.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_01_domain_model)](https://travis-ci.org/python-leap/code) |
| [Chapter 2: Repository](chapter_02_repository.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_02_repository)](https://travis-ci.org/python-leap/code) |
| [Chapter 3: Flask API and Service Layer](chapter_03_flask_api_and_service_layer.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_03_flask_api_and_service_layer)](https://travis-ci.org/python-leap/code) |
| [Chapter 4: Unit of Work](chapter_04_uow.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_04_uow)](https://travis-ci.org/python-leap/code) |
| [Chapter 5: Aggregates](chapter_05_aggregate.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_05_aggregate)](https://travis-ci.org/python-leap/code) |
| [Chapter 6: Events and the Message Bus](chapter_06_events_and_message_bus.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_06_events_and_message_bus)](https://travis-ci.org/python-leap/code) |
| [Chapter 7: Event-Driven Architecture](chapter_07_external_events.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_07_external_events)](https://travis-ci.org/python-leap/code) |
| [Appendix A: Abstractions](appendix_abstractions.asciidoc) | |
| [Appendix B: Project Structure](appendix_project_structure.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=appendix_project_structure)](https://travis-ci.org/python-leap/code) |
| [Appendix C: A major infrastructure change, made easy](appendix_csvs.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=appendix_csvs)](https://travis-ci.org/python-leap/code) |
| [Appendix D: Django](appendix_django.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=appendix_django)](https://travis-ci.org/python-leap/code) |




Below is just instructions for me and bob really.

## Dependencies:

* asciidoctor
* Pygments (for syntax higlighting)

```sh
gem install asciidoctor
python2 -m pip install --user pygments
gem install pygments.rb
```


## Commands

```sh
make html  # builds local .html versions of each chapter
make test  # does a sanity-check of the code listings
```

