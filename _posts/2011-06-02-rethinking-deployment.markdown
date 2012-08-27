---
comments: true
date: 2011-06-02 20:52:26
layout: post
slug: rethinking-deployment
title: Rethinking Deployment
wordpress_id: 1284
tags:
- Application programming interface
- Google AppEngine
- Hello world program
- Heroku
- Java
- Python
- Web application
- Web Server Gateway Interface
---




# Rethinking [Deployment](http://en.wikipedia.org/wiki/Software_deployment)


Probably everyone knows something about one of the following environment:



	
  * [Google AppEngine](https://appengine.google.com/) (runs [Python](http://www.python.org), [Java](http://www.java.com/) and recently also [Go](http://golang.org))

	
  * [ep.io](http://www.ep.io) (runs [Python](http://www.python.org))

	
  * [Engine Yard](http://www.engineyard.com/) or [Heroku](http://www.heroku.com) (runs [Ruby](http://www.ruby-lang.org))


What you usually get from services like these is easy deployment and kind of a _namespace for your app_. By namespace I mean some kind of container that keeps your app from crashing because someone else did something bad on the server and vice versa. This is naturally what you want because you run in a hosted environment, that means you don’t actually have control about what kinds of apps run on the servers or even how many apps run on the server. Please keep in mind that hosted doesn’t necessarily mean that you pay a third party for hosting your stuff. It might as well be some service within the very own company.

Not a bad thing in and on itself. Just something to get used to.

Of course there are some things to keep in mind with that kind of automated deployment. One of the more problematic things will be how to ensure that only working apps will get deployed.

After all you don’t want some fancy, easy to use deployment mechanism just to take your main site down every 15 minutes. Of course you could then just easily deploy the last version again and be up and running. Still this is not a desireable solution.

We now know a few requirements:



	
  * easy deployment (more on that later)

	
  * versioned deployment




## Versioned Deployment


Versioned deployment means that the same app must be deployable multiple times. Somehow the deployment system must be able to differentiate between the same app deployed multiple times. It’s only natural (at least to me) to use a version number. This actually brings in another requirement:



	
  * semantic version numbers


What does that mean? Don’t just use some random string, there needs to be a notion of comparison between versions. In simple Terms it must support the following operations:

	
  * is larger than

	
  * is smaller than

	
  * is equal to


There’s the nice [semver.org](http://semver.org) site that tries to _standardize_. Personally I agree with the spec, except for the _special version number_, I just don’t see a need for it. I’m perfectly fine without it.

Another quite simple version number would be a unix timestamp or the date and time of the release. I suggest something like 201105261324 — but to be honest; just staying with the spec from [semver.org](http://semver.org) is perfectly fine. **It’s defined, it’s there; no need to reinvent the wheel!**


## Easy Deployment





	
  * [http://pivotallabs.com/talks/30-next-generation-application-deployment](http://pivotallabs.com/talks/30-next-generation-application-deployment)


Easy deployment actually means that developers have to live with quite a lot of constraints. I can’t imagine a system that allows you to do anything you can think of and still have a notion of easy deployment.

Contraints (or rather restrictions) have a bad side taste. Maybe I can’t write to disk. Maybe I can’t configure my logging the way I want. Maybe I don’t have the possibility of accessing the database I like best.

These kinds of contraints come in varying sizes and tastes. The most basic thing that won’t be available is random access to the file system. Or even the expectation that whatever you write to the file system may be there in half an hour.

To [quote myself](http://serverhorror.eu/rethinking-compliance) (yeah, I know…):


> You want that people accept the system, hell they shouldn’t just accept it — it should be natural to them to use the whatever compliant services are provided. Because the are easy to use and because they do the job at least well.

If you want to have compliance and you do it in a way that users don’t like they will find ways around it.


What this actually means is that for every expectation (or at least most of them) people have regarding a system, there needs to be a solution. This solution must be well thought of. I couldn’t just throw some bad API at the users and expect that people will use the deployment system.

The most basic requirements to deploy (web) software are:



	
  * Application _Entry Points_

	
  * Application Configuration

	
  * Have a _caching API_

	
  * Have a _persistence API_

	
  * Have a _data query API_ (specifically not resctricted to SQL)

	
  * Have a _logging API_

	
  * Have at _least very good documentation_ for all of the above


This is what needs to be available to write some app against a restricted environment. Much of this is actually just what [Google AppEngine](https://appengine.google.com/) provides.

Let me construct a system that has the basic properties mentioned above. We’ll restrict to the following:



	
  * Python [Web Applications](http://en.wikipedia.org/wiki/Web_application) that are accessed thru an `application` object that is a [WSGI](http://www.python.org/dev/peps/pep-0333/) instance

	
  * You will run on [python2.5](http://www.python.org)

	
  * The application needs to be self contained

	
    * this implies that if you use [web.py](http://webpy.org) you need to make sure that it’s importable from within you application. You cannot expect [web.py](http://webpy.org) to be somehow magically available

	
    * this also means that you can only use pure python modules





I’ll ber very unspecific here. I hope nobody expects me to to use a magic hat and just pull out a solution. I hope the basic idea will still come through.


### Entry Points


I just implicitely defined that above. Just make a WSGI application, a simple one like the [`web.py` cookbook sample](http://webpy.org/cookbook/mod_wsgi-apache) is enough:







    
    import web  urls = ( '/.*', 'hello', )  class hello: def GET(self): return "<a href="http://en.wikipedia.org/wiki/Hello_world_program" class="zem_slink" rel="wikipedia" title="Hello world program">Hello, world</a>."  application = web.application(urls, globals()).wsgifunc()










### Application Configuration


This mostly about data that shouldn’t be the default. For web application this means:



	
  * cookie/session secret

	
  * API credentials (which may be different for different [APIs](http://en.wikipedia.org/wiki/Application_programming_interface))

	
  * other data that is not under the direct control of a user




### Caching API


**Note**: Stealing from [`memcached`](http://memcached.org/) here. You might want to read up on [the memcached protocol](http://code.sixapart.com/svn/memcached/trunk/server/doc/protocol.txt)

Some assumptions that need to be dealt with:



	
  * Cached items may expire at any time

	
  * `set`ing something doesn’t mean that the next time I want to retrieve it it’s still there (yes this is actually **very, very, very bad** – just trying to simplify)


Basic idea:







    
    [bytes]  set   get










### Persistence API


This should be nothing special. Just `write(bytes)` and `read(identifier)`. I like the notion of content-addressed storage for that part so I’m biased. But the `identifier` could be anything. A path a sha1-sum, really anything.

Again stealing from above (and yes, this works in the real world – just look at [riak](http://www.basho.com)).

There’s something go keep in mind here: I want to make sure nobody writes vast amounts of data, either in a single object or by issuing a multitude of `write`s that’ll take down the system. I want some kind of quote. Say 100 GiB per application.

Basic idea:







    
    [bytes]  write   read










### Data Query API


This get’s a bit more tricky. Usually as soon as I take away SQL from some kind of data query I hear screams. I’m not saying SQl is bad or wrong in any way. But as soon as there aren’t dedicated DBAs involved that will take care of largish databases most servers run into a problem.

For the sake of simplicity let’s stay with a nice simple (for certain definitions of simple) SQL database. I’d allow people to:



	
  * `CREATE TABLE`,

	
  * `DROP TABLE`,

	
  * `CREATE VIEW`,

	
  * `SELECT`,

	
  * `INSERT`,

	
  * `DELETE`


Maybe even:

	
  * `CREATE INDEX`,

	
  * `DROP INDEX`.


Things I specifically wouldn’t allow (speaking in MySQL permissions here):

	
  * `CREATE TEMPORARY TABLES`

	
  * `SELECT INTO OUTFILE`

	
  * `COPY FROM FILE`


Basically I’d let everyone talk to his/her own database with basic usage rights. But especially deny everything that would need access to the filesystem or something near that.


### Logging API


This is a special case. All of the above were external things. External in the sense that there’s no problem by only allowing communication to run thru some sort of tcp connection. Logging however would should be available as a “_local_” API call. I’d just stay with the standard python logging library.

The important point would be that users must not set up their own Handlers. Basically people are allowed to either use a `StreamHandler` or a `NullHandler`.

A `StreamHandler` would be exactly what any other log system does. Provide a stream of events. An event isn’t necessarily something that ends with a newline. But the point is that writing something to the filesystem through the logging API sets up expectatiions that these log events will later be available. This assumption is wrong. The only events that will be available will be the ones that have been emitted through the `StreamHandler`s provided by the system.

What’s the point in providing a NullHandler? To be honest I can’t think of one. But hey! There’s gotta be some choice :)


### Documentation


I’m a believer of learning by example. This has 2 advantages:



	
  * diving in is easy

	
  * by writing examples I will be a user


The last point is a “_eat your own dogfood_” argument. But it will inflict the same pain on me that the users of the system have. Thus it will get better “_real soon now_”™.

Jokes aside. There’s a third point to it. Libraries will pop up for free. By writing code against the carefully designed APIs I will automagically create libraries to make my life easier, I will then either publish these libraries or incorporate the libraries in the existing API thus making everyone elses life easier.

The valid point of “If you need to create a library it’s not good enough” has a shortcoming here. If the API is just some HTTP-Restful API this API could be very good. But why not just create a library that will do directly in Python (or Ruby, Java, [Go](http://golang.org)), after all nearly everyone will be using these libraries and by providing them I have the potential to take serverload away by optimizing a single library and updating it on the server.

Original Post: http://serverhorror.eu/rethinking-deployment New Blog Location: http://serverhorror.eu


