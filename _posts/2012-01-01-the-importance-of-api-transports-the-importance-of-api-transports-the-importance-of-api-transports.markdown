---
comments: true
date: 2012-01-01 14:00:52
layout: post
slug: the-importance-of-api-transports-the-importance-of-api-transports-the-importance-of-api-transports
title: The Importance of API “Transports”
wordpress_id: 1476
tags:
- Application programming interface
- Database
- Facebook
- HTTP
- Hypertext Transfer Protocol
- NoSQL
- Relational database management system
- SQL
---

## SQL [Databases](http://en.wikipedia.org/wiki/Database) are dead




> 

> 
> There I said it. I jumped the [NoSQL](http://en.wikipedia.org/wiki/NoSQL) waggon and I refuse to use anything that is remotely uncool and old.
> 
> 



Of course the above is a lie. Well kind of. In reality I do think that the interface by which you communicate with a [SQL database](http://en.wikipedia.org/wiki/SQL) is dead (or rather should be, but so should [FTP](http://en.wikipedia.org/wiki/File_Transfer_Protocol) -- another story -- still there are a few people left using it).

I’m not really talking about the query language itself, I’m talking about the “transport” (lacking a better word).


## So is (nearly) any other protocol


I’ll leave the _kool new aid road_ now and talk about the transport stuff a bit.

My problem with [API](http://en.wikipedia.org/wiki/Application_programming_interface) interfaces currently is that the usage of these interfaces is quite annoying. Let’s look at the products that people use all over the web.

Say you go to Facebook or Google and what to use their API to do something with the social networks represented by the data. On the API page of Facebook you’ll find some source package that implements a [transport protocol](http://en.wikipedia.org/wiki/Transport_Layer), a [domain specific language](http://en.wikipedia.org/wiki/Domain-specific_language) and to complicate things a bit further also a certain data representation.

Reality is that right now to use some service on the Internet there is only a single transport protocol. HTTP, maybe add SSL on top of that but the transport is HTTP. I’m not saying that the [HTTP protocol](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is the ultimate protocol. It’s shortcomings are quite well known.

The point is that you can solve a whole set of problems all in one go and be done with it.


## Back to the SQL Example


So you have this cool new project and decided to use some relational database system. Now you also decide to use a framework that relies on interactions with other systems being non-blocking. So you run around the web and look for some non-blocking driver for you [RDBMS](http://en.wikipedia.org/wiki/Relational_database_management_system) of choice.

Then you run around the web and look for some non-blocking driver for you storage part, then you run around the web...(you get the idea).

Now if all your satellite systems would be exposed oder HTTP you’d...run around the web and look for a non-blocking HTTP client and be done with this category of problems.


## Just don’t use HTTP...please!


Please, please, please...don’t just use HTTP because I used it as an example here. A unified (or generalized) transport really needs some serious thinking.

Of course you can just run away now and scream what kind of idiot I am, but the next time you run around the web and and look for a driver because the transport of services isn’t generalized enough to be reusable.

Also please don’t confuse the transport with the represenation -- which should be considered equally important and would solve another stack of problems.

And if you go that last route, that still doesn’t say that should be only a single language per domain, having a single language per domain would be not that good without wasting further thoughts about those last two statements.


> /serverhorror
