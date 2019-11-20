# Book repo

| Book | Code |
| ---- | ---- |
| [![Book Build Status](https://travis-ci.org/cosmicpython/book.svg?branch=master)](https://travis-ci.org/cosmicpython/book) | [![Code build status](https://travis-ci.org/cosmicpython/code.svg?branch=master)](https://travis-ci.org/cosmicpython/code) |


## Table of Contents

O'Reilly have generously said that we will be able to publish this book under a [CC license](license.txt),
In the meantime, pull requests, typofixes, and more substantial feedback + suggestions are enthusiastically solicited.

| Chapter |       |
| ------- | ----- |
| [Preface](preface.asciidoc) | |
| [Introduction: Why do our designs go wrong?](introduction.asciidoc)| ||
| [**Part 1 Intro**](part1.asciidoc) | |
| [Chapter 1: Domain Model](chapter_01_domain_model.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_01_domain_model)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 2: Repository](chapter_02_repository.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_02_repository)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 3: Interlude: Abstractions](chapter_03_abstractions.asciidoc) | |
| [Chapter 4: Service Layer (and Flask API)](chapter_04_service_layer.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_04_service_layer)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 5: Unit of Work](chapter_05_uow.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_05_uow)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 6: Aggregates](chapter_06_aggregate.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_06_aggregate)](https://travis-ci.org/cosmicpython/code) |
| [**Part 2 Intro**](part2.asciidoc) | |
| [Chapter 7: Domain Events and a Simple Message Bus](chapter_07_events_and_message_bus.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_07_events_and_message_bus)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 8: Going to Town on the MessageBus](chapter_08_all_messagebus.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_08_all_messagebus)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 9: Commands](chapter_09_commands.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_09_commands)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 10: External Events for Integration](chapter_10_external_events.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_10_external_events)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 11: CQRS](chapter_11_cqrs.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_11_cqrs)](https://travis-ci.org/cosmicpython/code) |
| [Chapter 12: Dependency Injection](chapter_12_dependency_injection.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=chapter_12_dependency_injection)](https://travis-ci.org/cosmicpython/code) |
| [Epilogue: How do I get there from here?](epilogue_1_how_to_get_there_from_here.asciidoc) | |
| [Appendix B: Project Structure](appendix_project_structure.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=appendix_project_structure)](https://travis-ci.org/cosmicpython/code) |
| [Appendix C: A major infrastructure change, made easy](appendix_csvs.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=appendix_csvs)](https://travis-ci.org/cosmicpython/code) |
| [Appendix D: Django](appendix_django.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=appendix_django)](https://travis-ci.org/cosmicpython/code) |
| [Appendix E: Bootstrap](appendix_bootstrap.asciidoc) | [![Build Status](https://travis-ci.org/cosmicpython/code.svg?branch=appendix_bootstrap)](https://travis-ci.org/cosmicpython/code) |
| [Appendix F: Validation](appendix_validation.asciidoc) | |




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

