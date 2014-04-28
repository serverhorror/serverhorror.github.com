---
layout: post
title: A useful Ticket System
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275723778";}
  _wpas_done_twitter: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1295290317";}
  _wpas_skip_yup: '1'
  _wpas_skip_fb: '1'
author: 
---
<div>This post has been in my queue since 2009-06-01 (¡wow - quite some time¡), now I finally found some time to further refine the draft - which actually consisted of only 2 items in a bulleted list, not that much.</div>
<p>So here it goes I'm missing these things in a bugtracker…</p>
<p><strong>Very very good documentation</strong> - without it everything else is lost. Of course the documentation should be excellent for all the points made below as well.</p>
<p><strong>Lightweight</strong> - yes I know a lot of people don't consider a website served with Perl (<a href="http://bestpractical.com/rt/">Request Tracker</a>) or Python (<a href="http://roundup.sourceforge.net/">roundup</a>) lightweight. Well I don't! For me lightweight isn't about memory usage or the number of components a piece of software depends on. Lightweight is about how easy it is to manage the thing. This includes all aspects: <em>usage, updates, data manipulation, and everything I don't know about yet because I haven't run into it</em>.</p>
<p><strong>Ticket tracker in the first place</strong> - Somehow my impression is that there are just a lot of web interfaces or mail interfaces that process a form (or somewhat customizable form) and place it in a database. I would like to see a description framework where I define what a ticket is. Define the grants and denials on tickets, or any other kind of information I'd like to track. That also include state transitions, actions that should be done and whatnot -- yes I can see how quite a bunch of people will now say "Easy, just use some RDBMS". That is however not what this paragraph means to me.</p>
<p><strong>Well defined API</strong> - this is what makes it really useable. I need to interface with a ticket system every single day of work. I'd even say it is the most vital part of my work. This is the one single point where the information concentrates. It lists things my users find annoying, thiings my servers find annoying (if they can report it), things my monitoring system finds annoying. Just about everything I need (or better want) to know about is collected in the ticket system. That is why I prefer to have an easy to use API available, very easy for me would be something that I can script by using curl, I'd grab some CSV data and create some sheets I can print out and put on my desk (yes <strong>I like to use pen&amp;paper</strong> - just not when someone else has already written everything down), or carry with me when I need more information about a special case ticket.</p>
<p><strong>Extensible API</strong> - This is not quite the same as the point above. By extensible I mean something like a namespace I can create to place my extensions. In a perfect world I wouldn't need to write extensions. I'd simply interface with the API and combine lower level functions to something I find more useful - but even in that case I'd like namespaces.</p>
<p>There are also some things I don't consider to be part of a ticketing system - at least not in the first place. There are mail gateways that try to provide the tickets in near real time to the ticketing system. Personally I don't care about that. I'd rather like to be able to feed tickets from any source in an easy way. Also a web interface isn't really part of issue tracking. That one may need some explanation, after all most customers consider a webpage the access point to something.</p>
<p>Why I don't consider a web interface part of a ticket system in the first place is because there shouldn't be only one web interface there should be several.</p>
<ul>
<li>An interface to submit tickets</li>
<li>An interface to work on (single) tickets
<ul>
<li>Bulk management of tickets</li>
</ul>
</li>
<li>An interface to get reports out of the system (this one may actually be quite hard, different people want different reports)</li>
<li>An interface to reuse solved tickets - where else could you get some F.A.Q in an easier way?</li>
</ul>
<p>I'd really rather see some <em>really really simple</em> web interface. Mantis and roundup have the right direction. Still I'm quite confined in the system (Mantis with PHP, roundup with TAL/METAL). I don't know specifics about JIRA but I'd guess I need a J2EE developer to really customize stuff in it</p>
<p><strong>Conclusion?</strong> Well I don't know which of the ticket systems to use in my eyes they all suck in one point or another. Also don't get me wrong I'm grateful for the systems that are available (Bugzilla, Trac, Redmine, JIRA…to name a few) but in some way or another they just suck…</p>
