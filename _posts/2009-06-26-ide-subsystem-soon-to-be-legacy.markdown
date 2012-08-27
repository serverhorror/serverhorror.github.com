---
comments: true
date: 2009-06-26 09:00:50
layout: post
slug: ide-subsystem-soon-to-be-legacy
title: IDE-Subsystem soon to be legacy?
wordpress_id: 174
tags:
- sysadmin
---

It seems the Kernel Maintainers of the IDE-subsystem are "giving up". A recent thread thread on the Linux Kernel Mailing List (LKML) fired up a discussion about the IDE-subsystem. The discussion arised because the former maintainer Bartlomiej Zolnierkiewicz made a few changes to the subsystem and a user of a SPARC system reported undesired behaviour.

Zolnierkiewicz mentioned being quite tired about the "hostile environment" (_I'm really tired of this kind of hostility towards IDE changes[...]_) he feels to be in, so he suggested to David Miller to take over maintainership of the subsystem who immediately accepted.

However David Milleralso noted that he will tread the IDE-subsystem as a pure legacy (_I'm going to treat IDE as pure legacy [...]_). Linus Torvalds also took part in the discussion and told Miller and Zolnierkiewicz to invest more time in the subsystem to iron out the problems it has.

Here are some links to key points in the discussion (hosted on gmane):



	
  * [http://thread.gmane.org/gmane.linux.ports.sparc/11845](http://thread.gmane.org/gmane.linux.ports.sparc/11845)

	
  * [http://thread.gmane.org/gmane.linux.ports.sparc/11845/focus=11864](http://thread.gmane.org/gmane.linux.ports.sparc/11845)

	
  * [http://thread.gmane.org/gmane.linux.ports.sparc/11845/focus=11867](http://thread.gmane.org/gmane.linux.ports.sparc/11845)


