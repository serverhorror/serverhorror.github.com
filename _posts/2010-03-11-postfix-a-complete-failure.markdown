---
comments: true
date: 2010-03-11 18:44:53
layout: post
slug: postfix-a-complete-failure
title: Postfix – A Complete Failure!
wordpress_id: 570
---

Yes this is a rant.



	
  * I used to like postfix

	
  * Until now I never had the need to do deeper analysis of the postfix logs

	
  * I always thought exim was way too complicated


2 of the 3 points above changed right now at this very moment. I still think exim is way to complicated but that's probably because I never had to care about configuring it. However we need to analyze the log data of email deliveries, receptions, failures and whatnot.

"_How hard can it be?_" - at least that was my first thought. **It can be very hard.**

Just compare:



	
  * the **documentation of postfix' log format**: [here](http://readlist.com/lists/postfix.org/postfix-users/2/12192.html) and [here](http://archives.neohapsis.com/archives/postfix/2004-05/1196.html)

	
  * the **documentation of exim's log format**: [here](http://exim.org/exim-html-current/doc/html/spec_html/ch49.html)


Postfix just died for me from this very moment....
