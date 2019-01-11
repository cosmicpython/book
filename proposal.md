# Proposed Book Title:

* The Clean Architecture in Python?
* Ports and Adapters with Python?
* Enterprise Design Patterns in Python?
* Enterprise Software Architecture in Python?
* Software Architecture in Python?

## Proposed Book Subtitle: 

*How to apply DDD, Ports and Adapters and more enterprise architecture design patterns in a Pythonic way.*

# Author(s): 

Bob Gregory, Harry Percival

> Author title(s) and affiliation(s):

Lead Architect and Software Developer (respectively) at MADE.com

> Preferred mailing address(es): 
> Preferred phone number: 
> Preferred Email address(es):
harry.percival@gmail.com, bob.gregory@made.com
> Author Platform details:
> Author biography and LinkedIn profile: 

https://uk.linkedin.com/in/harry-percival-588a35
https://uk.linkedin.com/in/bobthemighty


> Author public speaking samples (YouTube, etc.):

https://www.youtube.com/watch?v=tFalO9KdCDM
https://skillsmatter.com/skillscasts/12182-event-sourcing-101

> Author Web site/blog/Twitter: 

https://io.made.com/
http://www.obeythetestinggoat.com/


# Why are you the best person to write this book?

Harry has already written one excellent Python book for O'Reilly,  this will make a nice sequel (in fact it covers some of the further reading subjects suggested in the final chapter of said book).
Bob knows more than Harry about the subject matter though.


# Book Summary:

> In one sentence, tell us why the audience will want to buy your book.

The Python world is increasingly interested in software architecture and design, and there are no good Python-specific books on the topic yet.


> Summarize what the book is about, like you would pitch it to a potential reader on the back cover.  What makes your book unique in the marketplace?

As Python grows in popularity as a language, typical projects are getting larger and more complex, and issues of software design and architecture become more salient.  Patterns like "Ports and Adapters", as well Domain-Driven Design, Event-Driven programming, Command-Query Responsibility Segregation, which are well known in more "enterprisey" communities like Java and C#, are generating more interest in the Python community, but it's not always easy to see how these patterns translate into Python.  (reviewing the classic "Gang of Four" design patterns book for example leads to the conclusion that half the patterns are artifacts of the Java/C++ syntax, and are simply not necessary in the more flexible and dynamic world of Python).

In the Python world, we often quote the Zen of Python:  "there should be one--preferably on only one--obvious way to do it".  Unfortunately, as project complexity grows, the most obvious way of doing things isn't always the way that helps you manage complexity and evolving requirements.

This book will provide an introduction to proven architectural design patterns that help you manage complexity, using concrete examples written in Python. It will explain how to avoid some of the unnecessary particularities of Java and C# syntax and implement these patterns in a "Pythonic" way.


# Technology summary.

> How would you characterize the technology’s stage of development? (Put an X in the column next to the stage that best applies.)

In the enterprise world: mature.  In the Python world: developing.


> Briefly explain the technology and why it is important.

Design patterns and software architecture are well established topics in the enterprise software development world, but much less so in the Python world.  As Python matures, translating these topics across is becoming more and more important.



# Audience:

> Explain who the primary audience is for your book. What professional positions does this audience hold? What knowledge do you assume of this audience? What books can you assume they have read? What skills can you assume they have mastered?

This is an intermediate-level book.  It will be of interest to anyone working on codebases of more than moderate complexity, and anyone with an interest in applying architectural patterns common in the C#/Java world to Python.  It will also be of interest to software architects and developers coming from those communities and looking to adapt to the Python world.  Finally the aim will be to make this the most accessible, engaging, and concrete introduction to the architectural concepts involved, such that programmers from any background will turn to it as a first resource.

These people might have read:

- my first book, and be wondering where to go next
- classics like the Evans or Vernon DDD books, or Martin Fowler's "Patterns of Enterprise Application Architecture", and be wondering how to translate those concepts to the Python world

> Please estimate as best you can how many people will use this technology? Please state any applicable statistics (e.g., web searches, web site traffic, blogs) indicating market use or market growth.

Hard to say.  salesrank data from amazon suggest books like "Buiding evolutionary architectures" (O'Reilly, https://www.novelrank.com/asin/1491986360) and "Patterns of Enterprise Application Architecture" (a classic, https://www.novelrank.com/asin/0321127420) are selling well (compared to my existing book lol)

Other than that, informally, several people have reached out to us in response to our existing 5-part blog post series on the made.com blog, saying how much they'd like to see that content extended to book length, and complaining about the lack of similar resources in the Python world



> Please provide some scenarios that indicate how the audience will use your book. For example, will readers refer to it daily as a reference? Will they read it once to learn the concepts and then refer to it occasionally?

I expect most readers will read it all the way through once.  Some may decide to follow along with the code examples in some or all of the chapters.  Then, they are likely to come back and look at the code examples in more detail as they come to try and implement the various patterns in their day-to-day jobs.

> Use the following table to describe how the audience for your book typically gets information and where it looks for guidance and leadership (list top five choices).

> What web sites or blogs do they read?

my blog, hacker news, /r/python, the made blog, follow on twitter bernhardt, fowler, beck, uncle martin...
 
> What publications do they read (e.g., magazines, journals, newspapers)?

see above.
 
> What conferences do they attend?

pycon(s), oreilly software architecture conference, oscon, fosdem, 
 
 
> Who are the leaders and key influencers in the field who would review or endorse your book?

I could reach out via some contacts at Thoughtworks to see if Martin Fowler might give it a read.  That would be a great name to have on the cover.

In the Python world, Harry's existing Python contacts should be prepared to take a look -- Kenneth Reitz, Gary Bernhanrdt, Michael Foord.

 
 


# Key Topic Coverage:

> What are the top five topics that will be covered in the book? Why are they the top five?

- the dependency inversion principle
- ports and adapters
- domain-driven design (DDD)
- CQRS (command/query responsibility segregation)
- event-driven architectures (and link to microservices)

These are the most popular and recognisable words that people will recognise or have heard of, and appreciate seeing a concrete illustration and discussion of, in the Python world.

> What problems does this book solve for its users?

- How do I deal with increasing complexity as my application grows?
- How can I learn about enterprise software design principles without wading through overcomplicated Java/C++ syntax?
- Where can I find concrete examples rather than abstract discussion?

> List the four or five topics covered or features included that will provide the greatest benefit to readers or will be the most likely to excite them? 

see above, plus:

- How do I separate my domain model from infrastructure and integration layers?
- Concretely, what is a Port and what is an Adapter in Python?  Does the distinction matter?
- What are the expected benefits of this sort of architecture?  When is it worth implementing?
- How do these patterns complement a microservices approach?

> SEO terms for topics covered:

see bullets above, plus "clean architecture", "hexagonal architecture", "functional core imperative shell",...


# Other Book Features and Video Offerings:

> Is there a companion web site? If so, what do you plan to include on the site? Would you be willing to participate in video offerings as well as workshops and training seminars?

- a website with access to source code examples, and follow-on blog posts and materials is likely.
- it could also include "alternative implementations" showing some other ways of achieving the same goals, compared to the examples given in the book.
- not entirely sure that video is the right medium for getting these kinds of concepts across, but up for trying.



# Competition:

> What books or online resources compete with this book? Please list the title and author. In each case, how will your book be different or better in timing, content, coverage, approach, or tone?

<research some books and provide their PageRank?>

DDD book?
patterns of enteprise arch?



# Book Outline (old):

1. the simple approach
2. domain model
3. dependency injection and inversion of control
4. persistence and unit of work
5. commands & events, handlers, message bus
6. (ports and) adapters
7. command-query separation.
8. the proof is in the pudding 1: implementing a new feature
9. the proof is in the pudding 2: refactoring an infrastructure layer
10. comparison with the simple approach
11. conclusions: when to use these patterns
A. appendix: functional core, imperative shell
B. appendix: more design patterns
C. alternatives


# Specs and Schedule:

> How many pages do you expect the book to be?
200-250?

> What use you will make of illustrations or screenshots? Approximately how many illustrations do you anticipate using?

Several code listings per chapter, and maybe a few diagrams which we can produce ourselves...

> What special considerations apply to your plans for the book, including unusual format, use of color, hard-to-get illustrations, or anything else calling for unusual resources?

nothing extraordinary is anticipated
 
> When do you anticipate delivering a complete draft of the manuscript or technical review?

9 months' time?

