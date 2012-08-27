---
comments: true
date: 2010-02-22 10:00:50
layout: post
slug: a-useful-ticket-system
title: A useful Ticket System
wordpress_id: 7
tags:
- sysadmin
---



[digg=http://digg.com/programming/A_useful_Ticket_System_Server_Horror]






This post has been in my queue since 2009-06-01 (¡wow - quite some time¡), now I finally found some time to further refine the draft - which actually consisted of only 2 items in a bulleted list, not that much.


So here it goes I'm missing these things in a bugtracker…

**Very very good documentation** - without it everything else is lost. Of course the documentation should be excellent for all the points made below as well.

**Lightweight** - yes I know a lot of people don't consider a website served with Perl ([Request Tracker](http://bestpractical.com/rt/)) or Python ([roundup](http://roundup.sourceforge.net/)) lightweight. Well I don't! For me lightweight isn't about memory usage or the number of components a piece of software depends on. Lightweight is about how easy it is to manage the thing. This includes all aspects: _usage, updates, data manipulation, and everything I don't know about yet because I haven't run into it_.

**Ticket tracker in the first place** - Somehow my impression is that there are just a lot of web interfaces or mail interfaces that process a form (or somewhat customizable form) and place it in a database. I would like to see a description framework where I define what a ticket is. Define the grants and denials on tickets, or any other kind of information I'd like to track. That also include state transitions, actions that should be done and whatnot -- yes I can see how quite a bunch of people will now say "Easy, just use some RDBMS". That is however not what this paragraph means to me.

**Well defined API** - this is what makes it really useable. I need to interface with a ticket system every single day of work. I'd even say it is the most vital part of my work. This is the one single point where the information concentrates. It lists things my users find annoying, thiings my servers find annoying (if they can report it), things my monitoring system finds annoying. Just about everything I need (or better want) to know about is collected in the ticket system. That is why I prefer to have an easy to use API available, very easy for me would be something that I can script by using curl, I'd grab some CSV data and create some sheets I can print out and put on my desk (yes **I like to use pen&paper** - just not when someone else has already written everything down), or carry with me when I need more information about a special case ticket.

**Extensible API** - This is not quite the same as the point above. By extensible I mean something like a namespace I can create to place my extensions. In a perfect world I wouldn't need to write extensions. I'd simply interface with the API and combine lower level functions to something I find more useful - but even in that case I'd like namespaces.

There are also some things I don't consider to be part of a ticketing system - at least not in the first place. There are mail gateways that try to provide the tickets in near real time to the ticketing system. Personally I don't care about that. I'd rather like to be able to feed tickets from any source in an easy way. Also a web interface isn't really part of issue tracking. That one may need some explanation, after all most customers consider a webpage the access point to something.

Why I don't consider a web interface part of a ticket system in the first place is because there shouldn't be only one web interface there should be several.



	
  * An interface to submit tickets

	
  * An interface to work on (single) tickets

	
    * Bulk management of tickets




	
  * An interface to get reports out of the system (this one may actually be quite hard, different people want different reports)

	
  * An interface to reuse solved tickets - where else could you get some F.A.Q in an easier way?


I'd really rather see some _really really simple_ web interface. Mantis and roundup have the right direction. Still I'm quite confined in the system (Mantis with PHP, roundup with TAL/METAL). I don't know specifics about JIRA but I'd guess I need a J2EE developer to really customize stuff in it

**Conclusion?** Well I don't know which of the ticket systems to use in my eyes they all suck in one point or another. Also don't get me wrong I'm grateful for the systems that are available (Bugzilla, Trac, Redmine, JIRA…to name a few) but in some way or another they just suck…
