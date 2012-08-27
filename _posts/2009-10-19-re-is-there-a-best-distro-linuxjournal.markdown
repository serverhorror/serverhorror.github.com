---
comments: true
date: 2009-10-19 14:00:45
layout: post
slug: re-is-there-a-best-distro-linuxjournal
title: 'RE: Is there a best distro? (LinuxJournal)'
wordpress_id: 473
tags:
- sysadmin
---

[LinuxJournal is asking for the best Linux Distro](http://www.linuxjournal.com/content/there-best-distro), first I thought

It's actually quite easy to answer (especially to someone who will understand the implications):


## There is no "best Linux"


Just asko what's the best commercial Unix out there. One could
say: "They all start at the same point" it's a kernel and some
toolset you can then use and (re)script to your needs.

The best ist actually the one that meets your requirements best.



	
  * **Cheap?**

	
    * [Debian](http://www.debian.org)

	
    * [Ubuntu](http://www.ubuntu.com)

	
    * [Gentoo](http://www.gentoo.org)

	
    * (any "*non-enterprise distro*")/...




	
  * **Supported?**

	
    * [RHEL](http://www.redhat.com)

	
    * [SuSE](http://www.novell.com/linux/) (hehe, I had to look that one up)

	
    * ...




	
  * **Small?**

	
    * [Grml](http://grml.org/)

	
    * [DSL](http://www.damnsmalllinux.org/)

	
    * ...







## "All of the distributions start from the same point"


I think that's just plain wrong. Yes they do have the same kernel (do they really? - [Debian GNU/kFreeBSD](http://www.debian.org/ports/kfreebsd-gnu/)). But even switching from Ubuntu to Debian or vice versa has a lot of hurdles to take ("/etc/inittab" on Ubuntu?) - Upstart in Debian/Stable?

I'd rather suggest _[FreeBSD](http://www.freebsd.org)__ or __[OpenBSD](http://www.openbsd.org) _(4.6 is just out, I suggest everyone to give it a try) - **or is crucial** because choosing between the 2 is (IMHO) even wider apart than choosing between RHEL and Debian. _Note: I suggest this **[iff](http://en.wikipedia.org/wiki/If_and_only_if)**[sic] you want to stay in an enviroment that stays mostly the same thruought all servers and desktops_

FreeBSD is FreeBSD is FreeBSD - on every box.

Linux is not "just Linux" from that point there's just too much diversity among the distros. Even with a single Distro you can have large differences, of course you can take any BSD apart so that it won't look like the original distribution anymore, but staying within the universe of best practices you won't have as much diversity between FreeBSD installations as between Linux installations within a single distribution.


## Selection of rich applications


The key word here is **Selection**. Compare RHELs selection to Debians selection. You wouldn't think that an enterprise grade distro doesn't even have Nagios in the repositories - aren't the enterprise people monitoring their servers too?


## My choice?


Simple, give me the problem description and I'll have a look which of the distributions (or even non-Linux - read BSDs, or even non-FOSS) solutions will suit best. It doesn't help to get RHEL if they don't support the software you need, but it's neither helpful to stay with Debian if you need proven Enterprise grade support contrancts with 4 hours of maximum time to react. (Btw: [OpenSolaris](http://opensolaris.org) does have the [**option** to buy support from Sun](http://www.opensolaris.com/learn/subscriptions/#opensolaris))

Of course that would be only the start of a discussion with someone who already knows enough about *NIX to discuss on such a Level. As you said dear LinuxJournal:


> This was not someone who is unfamiliar with technology, or UNIX for that matter, but someone who is _one of us_
