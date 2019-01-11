# Outline

## Preface/Intro

Who are we, why we are writing this book
(all the args from the proposal, python's popularity, communicating well-understood patterns from the Java/C#/Enterprise world to a wider audience with nice, readable, pythonic code examples)

> As Python grows in popularity as a language, typical projects are getting larger and more complex, and issues of software design and architecture become more salient.  Patterns like "Ports and Adapters", as well Domain-Driven Design, Event-Driven programming, Command-Query Responsibility Segregation, which are well known in more "enterprisey" communities like Java and C#, are generating more interest in the Python community, but it's not always easy to see how these patterns translate into Python.  (reviewing the classic "Gang of Four" design patterns book for example leads to the conclusion that half the patterns are artifacts of the Java/C++ syntax, and are simply not necessary in the more flexible and dynamic world of Python).

> In the Python world, we often quote the Zen of Python:  "there should be one--preferably on only one--obvious way to do it".  Unfortunately, as project complexity grows, the most obvious way of doing things isn't always the way that helps you manage complexity and evolving requirements.

> This book will provide an introduction to proven architectural design patterns that help you manage complexity, using concrete examples written in Python. It will explain how to avoid some of the unnecessary particularities of Java and C# syntax and implement these patterns in a "Pythonic" way.

An overview of the central argument:

> Layer your system so that the low-level details depend on the high-level abstractions, not the other way around.


## Chapter 1: Domain modelling, and why do we always make it so hard for ourselves?

Every so often someone says "where shall I put this new logic", and we all know the right answer: it should live in the domain model.  So why does it always somehow end up in some gigantic controller function that's closely coupled with your web framework and database and third party apis and god knows what else?

Let's see what happens if we build everything around making sure our domain model is easy to work with and change.

* Talk about domain modelling and DDD, work through an example (allocate-order)
* Example code
* crazy idea: Bob and I will record a video of (part of?) the allocate-order code writing as a TDD "kata", to illustrate how easy it is to do this stuff when you have no dependencies on databases, frameworks, etc (this will also save us from having to go slowly thru what tdd is in the book)

code examples / patterns:  some domain model objects (python3.7 dataclasses maybe?), a domain service / use case function, some "proper" unit tests.

related post from existing blog: https://io.made.com/introducing-command-handler/



## Chapter 2: persistence and the repository pattern

The main ORM tool in the Python world is SQLAlchemy, and if you follow the default tutorial, you end up writing your model objects inheriting from `sqlalchemy.Table`, and soon your domain model is tightly coupled to your DB.

But you don't have to!  Demonstrate the alternative way to do metadata/mapping.

==> our ORM depends on the domain model, and not the other way around. an illustration of one of our key patterns/principles, the  _Dependency Inversion Principle_ (the D in SOLID)

Also: repository pattern.  choosing a simple abstraction (it's a dictionary)
Also: first integration test

code examples / patterns: sqlalchemy metadata/mapping, repository pattern

related post from existing blog: https://io.made.com/repository-and-unit-of-work-pattern-in-python/ 



## Chapter 3: making ourselves available via a web API.  Flask as a port (as in ports-and-adapters). Our first use case.  Orchestration. Service layer

We have a use case in mind, and a domain model that can do it, but how do we make it available to the outside world?

start with a naive flask controller.  evolve it to flask being an adapter to a use case function in our service/orchestration layer.

* happy path, show the basic use case moving parts:  create a database session, initialise our repository, load some objects, invoke our domain function, commit.
* first acceptance test
* handle error case, eg product does not exist.  handle `KeyError` from repository, flask returns a 400 with nice erro json
* but what if we have more error cases at this orchestration level? it'll be annoying to test everything with acceptance tests, and hard to unit test.

==> introduce service layer.  flask becomes an adapter.  flask depends on the service layer, rather than the other way around (DIP once again)

(later in the book we'll swap flask for asyncio, and show how easy it is)

patterns: use case, service layer, port/adapter pattern for web,

related post from existing blog: https://io.made.com/repository-and-unit-of-work-pattern-in-python/ 



## Chapter 4: data integrity concerns 1: unit of work pattern

What happens if we encounter an error during our allocation?  eg out of stock, a domain error?  We'd like to wrap our work up so that, either the entire order is allocated, or we abort and leave things in a "clean" state if anything goes wrong -- a classic case for a transaction/rollback.

What's a Pythonic way of "doing transactions"?  A context manager.  demonstrate the _Unit of Work Pattern_ and show how it fits with _Repository_
But we also want a nice, Pythonic way of "doing transactions", of wrapping a block of code up into an atomic whole.

discuss different options of unit of work, explicit/implicit rollbacks, dependency-inject uow.

code examples / patterns: Unit Of Work (using a context manager)

related post from existing blog: https://io.made.com/repository-and-unit-of-work-pattern-in-python/ 


## Chapter 5: data integrity concerns 2: choosing the right consistency boundary (Aggregate pattern)

While we're thinking about data integrity, we now realise that our `allocate(order, shipments)` implementation which depends on all the shipments in the world won't scale if every order needs to lock the whole shipments table.   We should only look at shipments that matter to that order.

Moreover, we only need to allocate the order one line at a time (although maybe we want to roll back all the lines if we fail any one of them).

This leads us on to discussing the _Aggregate_ pattern - by choosing `Product` as our aggregate, we choose a consistency boundary that allows us to be more clever about transactions.

Also demonstrate how easy it is to refactor a domain model if it's not intermixed with infrastructure concerns.

code examples / patterns:  Aggregate



## Chapter 6: CQRS

The business comes along and supplies a new requirement:  a dashboard showing the current allocation state of all shipments.  Discuss how using the ORM naively leads to the _SELECT N+1_ antipattern, and use it as an opportunity to demonstrate _Command-Query-Responsiblity-Segregation (CQRS)_ -- read-only parts of our architecture can be implemented quite differently from the write side

code examples / patterns:  CQRS / raw sql queries

related post from existing blog: https://io.made.com/commands-and-queries-handlers-and-views/



## Chapter 7: event-driven architecture part 1: events and the message bus

Another new requirement:  when allocation succeeds, someone should be emailed.  But we don't want to have email-sending code be a potential cause of bugs/failures in our core model/state changes.  introduce domain events and a message bus as a pattern for kicking off related work after a use case is complete.

* discuss SRP, use case shouldn't have an _and_. leads naturally to events.

code examples / patterns: events, handlers, message bus

related post from existing blog: https://io.made.com/why-use-domain-events/



## Chapter 8: event-driven architecture part 2: domain events

currently events are raised at the service layer.  but what about something like "out of stock"?  maybe that's an event that really belongs inside our domain, something that has business logic, not just orchestration.

code examples / patterns:  domain events raised by aggregate, unit of work with event tracking/ message bus integration

related post from existing blog: https://io.made.com/why-use-domain-events/



## Chapter 9: event-driven architecture part 3: a second use case, cancel_shipment -- command handler pattern

now we want to be able to cancel a shipment.  maybe a boat sank and all the orders allocated to it need re-allocating.  but we don't want to do the reallocation and the cancellation in the same transaction.  So a command "cancel shipment" that raises a number of independent "reallocate" commands makes sense


We also decide we don't need a web api for this, a command-line interface makes sense.  but what's a sensible abstraction that gives use access to our use cases from both the command-line and a flask api?  commands.  we've been talking about them for a while, time to make them into a real thing.

==> show how commands can be put on the message bus just like events.

code examples / patterns: reuse message bus for commands

related post from existing blog: https://io.made.com/introducing-command-handler/


## Chapter 10: event-driven architecture part 4: reactive microservices

We've got a microservice, but we've so far glossed over how it actually gets data about the outside world -- how does it know about new shipments?
Show how the event-driven system we've built so far is a great way of integrating between separate applications:  our logistics app can emit events about new shipments, and our app can consume them in exactly the same way that it consumes its internal events and commands.

code examples / patterns: events as a microservices integration platform

 

## Appendix 1: swapping out flask for asyncio

demonstrate how our layered architecture makes it easy to do infrastructure changes whilst keeping our business logic intact

this could be an exercise for the reader tbh.  or a video


## Appendix 2: patterns for dependency injection

with + without framework, `@inject`, and bob's crazy, heretical, unclean type-hints based one.

related post from existing blog: https://io.made.com/dependency-injection-with-type-signatures-in-python/

