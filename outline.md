# Outline

## Preface/Intro

Who are we, why we are writing this book
(all the args from the proposal, python's popularity, communicating well-understood patterns from the Java/C#/Enterprise world to a wider audience with nice, readable, pythonic code examples)

An overview of the central argument:

> Layer your system so that the low-level details depend on the high-level abstractions, not the other way around.


## Chapter 1: Domain modelling, and why do we always make it so hard for ourselves?

Every so often someone says "where shall I put this new logic", and we all know the right answer: it should live in the domain model.  So why does it always somehow end up in some gigantic controller function that's closely coupled with your web framework?

* Talk about domain modelling and DDD, work through an example (allocate-order)
* Example code
* crazy idea: Bob and I will record a video of (part of?) the allocate-order code writing as a TDD "kata", to illustrate how easy it is to do this stuff when you have no dependencies on databases, frameworks, etc (this will also save us from having to go slowly thru what tdd is in the book)

code examples:  some domain model objects (python3.7 dataclasses maybe?), a domain service / use case function, some "proper" unit tests.


## Chapter 2: persistence and the repository pattern

The main ORM tool in the Python world is SQLAlchemy, and if you follow the default tutorial, you end up writing your model objects inheriting from `sqlalchemy.Table`, and soon your domain model is tightly coupled to your DB.

But you don't have to!  Demonstrate the alternative way to do metadata/mapping.

==> our ORM depends on the domain model, and not the other way around. an illustration of one of our key patterns/principles, the  _Dependency Inversion Principle_ (the D in SOLID)

Also: repository pattern.  choosing a simple abstraction (it's a dictionary)

code examples: sqlalchemy metadata/mapping, repository pattern


## Chapter 3: making ourselves available via a web API.  Flask as a port (as in ports-and-adapters)

Show how flask becomes a thin wrapper that talks to the use cases provided by our domain model
Contrast this to the way it's usually done the other way around -- the use cases are defined in the flask controller/view functions, and are tightly coupled to them
(later in the book we'll swap flask for asyncio, and show how easy it is)

patterns: port/adapter pattern for web


## Chapter 4: data integrity concerns 1: unit of work pattern

What happens if we encounter an error during our allocation?  We'd like to wrap our work up so that, either the entire order is allocated, or we abort and leave things in a "clean" state if anything goes wrong -- a classic case for a transaction/rollback.

What's a Pythonic way of "doing transactions"?  A context manager.  demonstrate the _Unit of Work Pattern_ and show how it fits with _Repository_
But we also want a nice, Pythonic way of "doing transactions", of wrapping a block of code up into an atomic whole.

code examples: Unit Of Work (using a context manager)


## Chapter 5: data integrity concerns 2: choosing the right consistency boundary (Aggregate pattern)

While we're thinking about data integrity, we now realise that our `allocate(order, shipments)` implementation which depends on all the shipments in the world won't scale if every order needs to lock the whole shipments table.   We should only look at shipments that matter to that order.

Moreover, we only need to allocate the order one line at a time (although maybe we want to roll back all the lines if we fail any one of them).

This leads us on to discussing the _Aggregate_ pattern - by choosing `Product` as our aggregate, we choose a consistency boundary that allows us to be more clever about transactions.

Also demonstrate how easy it is to refactor a domain model if it's not intermixed with infrastructure concerns.

code examples:  Aggregate


## Chapter 6: CQRS

The business comes along and supplies a new requirement:  a dashboard showing the current allocation state of all shipments.  Discuss how using the ORM naively leads to the _SELECT N+1_ antipattern, and use it as an opportunity to demonstrate _Command-Query-Responsiblity-Segregation (CQRS)_ -- read-only parts of our architecture can be implemented quite differently from the write side

code examples:  CQRS / raw sql queries


## Chapter 7: event-driven architecture part 1: domain events and the message bus

Another new requirement:  when allocation succeeds, someone should be emailed.  But we don't want to have email-sending code be a potential cause of bugs/failures in our core model/state changes.  introduce domain events and a message bus as a pattern for kicking off async/retriable events after a use case is complete.

code examples: domain events, handlers, message bus


## Chapter 8: event-driven architecture part 2: a second use case, cancel_shipment -- command handler pattern

now we want to be able to cancel a shipment.  maybe a boat sank and all the orders allocated to it need re-allocating.  but we don't want to do the reallocation and the cancellation in the same transaction.  So a command "cancel shipment" that raises a number of independent "reallocate" commands makes sense

We also decide we don't need a web api for this, a command-line interface makes sense.  but what's a sensible abstraction that gives use access to our use cases from both the command-line and a flask api?  commands.

code examples: commands


## Chapter 9: event-driven architecture part 3: reactive microservices

We've got a microservice, but we've so far glossed over how it actually gets data about the outside world -- how does it know about new shipments?
Show how the event-driven system we've built so far is a great way of integrating between separate applications:  our logistics app can emit events about new shipments, and our app can consume them in exactly the same way that it consumes its internal events and commands.

code examples: eventstore as a microservices integration platform

 

## Appendix 1: swap out the database for the filesystem

demonstrate how our layered arhitecture makes it easy to do infrastructure changes whilst keeping our business logic intact

this could be an exercise for the reader tbh.  or a video

## Appendix 2: swap out flask for asyncio

## Appendix 3: patterns for dependency injection

with + without framework, `@inject`, and bob's crazy, heretical, unclean type-hints based one.

