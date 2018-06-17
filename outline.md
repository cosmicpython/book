# Proposed Book Title:

* The Clean Architecture in Python?
* Ports and Adapters with Python?
* Enterprise Design Patterns in Python?

## Proposed Book Subtitle: 



# Author(s): 

Bob Gregory, Harry Percival

> Author title(s) and affiliation(s):

Software Developer and Architect (respectively) at MADE.com

> Preferred mailing address(es): 
> Preferred phone number: 
> Preferred Email address(es):  harry.percival@gmail.com, bob.gregory@made.com
> Author Platform details:
> Author biography and LinkedIn profile: 

https://uk.linkedin.com/in/harry-percival-588a35
https://uk.linkedin.com/in/bobthemighty

> Author Web site/blog/Twitter: 

https://io.made.com/
http://www.obeythetestinggoat.com/


# Why are you the best person to write this book?

Harry has already written one excellent Python book for O'Reilly,  this will make a nice sequel.
Bob knows more than Harry about the subject matter though.


# Book Summary:

> In one sentence, tell us why the audience will want to buy your book.

The Python world is increasingly interested in software architecture and design, and there are no good Python-specific books on the topic yet.


> Summarize what the book is about, like you would pitch it to a potential reader on the back cover.  What makes your book unique in the marketplace?

As Python grows in popularity as a language, typical projects are getting larger and more complex, and issues of software design and architecture become more salient.  Patterns like "Ports and Adapters", as well Domain-Driven Design, Event-Driven programming, Command-Query separation, which are well known in more "enterprisey" communities like Java and C#, are generating more interest in the Python community, but it's not always easy to see how these patterns translate into Python.  (reviewing the classic "Gang of Four" design patterns book for example leads to the conclusion that half the patterns are artifacts of the Java/C++ syntax, and are simply not necessary in the more flexible and dynamic world of Python).

This book will provide an introduction to architectural topics using concrete examples written in Python. It will explaining how to avoid some of the particularities of Java and C# syntax and implement these patterns in a "Pythonic" way.


> Briefly explain the technology and why it is important.


# Audience:

> Explain who the primary audience is for your book. What skills can you assume they have mastered?

This is an intermediate-level book.  It will be of interest to anyone working on codebases of more than moderate complexity, and anyone with an interest in applying architectural patterns common in the C#/Java world to Python.  It will also be of interest to software architects and developers coming from those communities and looking to adapt to the Python world.  Finally the aim will be to make this the most accessible, engaging, and concrete introduction to the architectural concepts involved, such that programmers from any background will turn to it as a first resource.

> Please estimate as best you can how many people will use this technology? Please state any applicable statistics (e.g., web searches, web site traffic, blogs) indicating market use or market growth.


> Please provide some scenarios that indicate how the audience will use your book. For example, will readers refer to it daily as a reference? Will they read it once to learn the concepts and then refer to it occasionally?


# Key Topic Coverage:

> What problems does this book solve for its users?

- How do I deal with increasing complexity as my application grows?
- How can I learn about enterprise software design principles without wading through overcomplicated Java/C++ syntax?
- Where can I find concrete examples rather than abstract discussion?

> List the four or five topics covered or features included that will provide the greatest benefit to readers or will be the most likely to excite them? 

- How do I separate my domain model from infrastructure and integration layers?
- Concretely, what is a Port and what is an Adapter in Python?
- What are the expected benefits of this sort of architecture?  When is it worth implementing?


# Other Book Features and Video Offerings:

> Is there a companion web site? If so, what do you plan to include on the site? Would you be willing to participate in video offerings as well as workshops and training seminars?

- a website with access to source code examples, and follow-on blog posts and materials is likely.
- not entirely sure that video is the right medium for getting these kinds of concepts across, but up for trying.



# Competition:

> What books or online resources compete with this book? Please list the title and author. In each case, how will your book be different or better in timing, content, coverage, approach, or tone?

<research some books and provide their PageRank?>

DDD book?
patterns of enteprise arch?



# Book Outline (chapter level is fine):

1. the simple approach
2. domain model
3. dependency injection and inversion of control
4. persistence and unit of work
5. event-driven architecture: commands & queries, handlers, message bus
6. (ports and) adapters
7. the proof is in the pudding 1: implementing a new feature
8. the proof is in the pudding 2: refactoring an infrastructure layer
9. comparison with the simple approach
10. conclusions: when to use this pattern
A. appendix: functional core, imperative shell
B. appendix: more design patterns
C. alternatives




# Specs and Schedule:

> How many pages do you expect the book to be?
200-250?

> How long do you expect it to take you to write the book?
9 months - 1yr
