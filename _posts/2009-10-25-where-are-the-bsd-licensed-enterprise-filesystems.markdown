---
comments: true
date: 2009-10-25 17:28:51
layout: post
slug: where-are-the-bsd-licensed-enterprise-filesystems
title: Where are the BSD Licensed "Enterprise Filesystems"?
wordpress_id: 479
tags:
- sysadmin
---

[digg=http://digg.com/linux_unix/Where_are_the_BSD_Licensed_Enterprise_Filesystems]

A very simple question.


> Where is the "Enterprise Filesystem" licensed in a pure BSD way?


I know [ZFS](http://en.wikipedia.org/wiki/Zfs) has been implemented by OpenSolaris (well yeah...that's the origin of ZFS) as well as [FreeBSD](http://www.freebsd.org) but the [CDDL](http://en.wikipedia.org/wiki/Common_Development_and_Distribution_License) is not without critique in the BSD community. The [OpenBSD](http://www.openbsd.org) [people consider the CDDL even more restrivtive than GNU/GPL](http://marc.info/?l=openbsd-tech&m=110806948606417&w=2).

So a question to all the guys and girls who are able to create a filesystem (I can't my coding skills are nowhere near to be able to create one), where is the BSD licensed filesystem with all the new features that make a hype?

I'm thinking about stuff like this (thou maybe not complete, somebody may have an absolutely usefull new idea that obsoletes all these features



	
  * [Snapshots](http://en.wikipedia.org/wiki/Snapshot_(computer_storage)) ([BTRFS](http://en.wikipedia.org/wiki/Btrfs), ZFS)

	
    * [Continous Snapshots (Versioning File System)](http://en.wikipedia.org/wiki/Versioning_file_system) ([NILFS](http://en.wikipedia.org/wiki/Nilfs))




	
  * [COW (Copy on Write)](http://en.wikipedia.org/wiki/Copy_on_write) (BTRFS, ZFS)

	
  * [Volume Management built-in](http://en.wikipedia.org/wiki/Logical_volume_management) (BTRFS, ZFS)

	
  * [RAID (like) features built-in the filesystem](http://en.wikipedia.org/wiki/RAID) (BTRFS, ZFS)

	
  * Really large maximum filesizes and*

	
  * Really large maximum filesystem sizes*


*****This may not be a Problem now, but I do get why Sun chose to make ZFS a 128-bit filesystem
