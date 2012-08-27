---
comments: true
date: 2009-06-19 10:04:00
layout: post
slug: ubuntu-certified-for-hp-servers
title: Ubuntu certified for HP servers
wordpress_id: 112
tags:
- sysadmin
---

[Ubuntu](http://www.ubuntu.com) just announced a [certification for the server version 9.04 on HP Proliant G6 servers](http://www.ubuntu.com/news/hp-proliant-servers-certified-ubuntu) (see also [HP Press release about this](http://h18004.www1.hp.com/products/servers/platforms/new.html?psn=servers)).

It seems I finally have to consider Ubuntu for our servers. **Not something I'm too pleased with** as my previous experience has been less than good. [One bug I ran into](https://launchpad.net/ubuntu/+source/cyrus-imapd-2.2/+bug/67111) burned itself into my memory.

The bug was a cyrus-imapd linked to a version of libdb it wasn't compiled against. As a result you could nicely see it segfault but that was it. The real tragedy in this bug was actually a couple of things:



	
  * it was an LTS (Long-Term-Support) Release

	
  * cyrus-imapd was in main

	
  * the bug was not fixed for nearly  7 months


I can understand that things like these can happen - even in an LTS release, even in main - but the time it took to repair the trivial issue just doesn't make me feel comfortable with Ubuntu on our servers.

Fortunately [Debian is also supported on HP Proliant servers](http://h20219.www2.hp.com/services/cache/442406-0-0-225-121.html), and has even been supported for much longer than the just [recently released G6 Family](http://h18006.www1.hp.com/products/servers/platforms/new.html) of HP's servers. Hopefully HP won't drop support for Debian that would be a real pita.
