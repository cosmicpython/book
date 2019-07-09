# Book repo

| Book | Code |
| ---- | ---- |
| [![Book Build Status](https://travis-ci.org/python-leap/book.svg?branch=master)](https://travis-ci.org/python-leap/book) | [![Code build status](https://travis-ci.org/python-leap/code.svg?branch=master)](https://travis-ci.org/python-leap/code) |


## Table of Contents

O'Reilly have generously said that we will be able to publish this book under a [CC license](license.txt),
In the meantime, pull requests, typofixes, and more substantial feedback + suggestions are enthusiastically solicited.

| Chapter |       |
| ------- | ----- |
| [Preface](preface.asciidoc) | |
| [Acknowledgements](acknowledgements.asciidoc) | |
| [**Part 1 Intro**](part1.asciidoc) | |
| [Prologue: Why do our designs go wrong?](prologue.asciidoc)| |
| [Chapter 1: Domain Model](chapter_01_domain_model.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_01_domain_model)](https://travis-ci.org/python-leap/code) |
| [Chapter 2: Repository](chapter_02_repository.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_02_repository)](https://travis-ci.org/python-leap/code) |
| [Interlude: Abstractions](chapter_02B_abstractions.asciidoc) | |
| [Chapter 3: Service Layer (and Flask API)](chapter_03_service_layer.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_03_service_layer)](https://travis-ci.org/python-leap/code) |
| [Chapter 4: Unit of Work](chapter_04_uow.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_04_uow)](https://travis-ci.org/python-leap/code) |
| [Chapter 5: Aggregates](chapter_05_aggregate.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_05_aggregate)](https://travis-ci.org/python-leap/code) |
| [**Part 2 Intro**](part2.asciidoc) | |
| [Chapter 6: Events and the Message Bus](chapter_06_events_and_message_bus.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_06_events_and_message_bus)](https://travis-ci.org/python-leap/code) |
| [Chapter 7: Event-Driven Architecture](chapter_07_external_events.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_07_external_events)](https://travis-ci.org/python-leap/code) |
| [Chapter 8: Commands](chapter_08_commands.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_08_commands)](https://travis-ci.org/python-leap/code) |
| [Chapter 9: CQRS](chapter_09_cqrs.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_09_cqrs)](https://travis-ci.org/python-leap/code) |
| [Chapter 10: Dependency Injection](chapter_10_dependency_injection.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=chapter_10_dependency_injection)](https://travis-ci.org/python-leap/code) |
| [Epilogue 1: How do I get there from here?](epilogue_1_how_to_get_there_from_here.asciidoc) | |
| [Appendix B: Project Structure](appendix_project_structure.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=appendix_project_structure)](https://travis-ci.org/python-leap/code) |
| [Appendix C: A major infrastructure change, made easy](appendix_csvs.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=appendix_csvs)](https://travis-ci.org/python-leap/code) |
| [Appendix D: Django](appendix_django.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=appendix_django)](https://travis-ci.org/python-leap/code) |
| [Appendix E: Bootstrap](appendix_bootstrap.asciidoc) | [![Build Status](https://travis-ci.org/python-leap/code.svg?branch=appendix_bootstrap)](https://travis-ci.org/python-leap/code) |




Below is just instructions for me and bob really.

## Dependencies:

* asciidoctor
* Pygments (for syntax higlighting)
* asciidoctor-diagram (to render images from the text sources in [`./images`](./images))

```sh
gem install asciidoctor
python2 -m pip install --user pygments
gem install pygments.rb
gem install asciidoctor-diagram
```


## Commands

```sh
make html  # builds local .html versions of each chapter
make test  # does a sanity-check of the code listings
```

