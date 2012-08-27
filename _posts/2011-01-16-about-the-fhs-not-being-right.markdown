---
comments: true
date: 2011-01-16 11:39:14
layout: post
slug: about-the-fhs-not-being-right
title: About the FHS not being right...
wordpress_id: 922
tags:
- fhs
- filesystem
- linux
- srv
- standard
- sysadmin
- var
---

[Chris Siebenmann](http://utcc.utoronto.ca/~cks/) wrote about the [FHS not being right](http://utcc.utoronto.ca/~cks/space/blog/linux/FHSNotAlwaysRight). Well I can't say I disagree completely but the points he makes aren't quite the points I dislike about the FHS.


> Dear Chris,

Err...have you read about /srv ([http://www.pathname.com/fhs/pub/fhs-2.3.html#SRVDATAFORSERVICESPROVIDEDBYSYSTEM](http://www.pathname.com/fhs/pub/fhs-2.3.html#SRVDATAFORSERVICESPROVIDEDBYSYSTEM))?
Seems to me that it's not /var you should target with your comments but rather /srv. Then again I haven't seen any package management that does soemthing to /srv - which in my opinion whould make the critic pointless (correct me if I'm wrong). Actually _I never even considered putting site-local data into the /var hierarchy_ exactly because I consider it to be the space where my distribution does it's things.

On a side note I just wish that there was a site alternative for /etc.
