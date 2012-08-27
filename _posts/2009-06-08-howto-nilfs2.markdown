---
comments: true
date: 2009-06-08 12:00:40
layout: post
slug: howto-nilfs2
title: HowTo NILFS2
wordpress_id: 37
tags:
- sysadmin
---

With kernel 2.6.30 there's a shiny new filesystem officially available. [NILFS2](http://www.nilfs.org) provides



	
  * checkpoints at regular intervals (unless there is no change) or  with  synchronous  writings


essentially that means that everytime you write a new file you will have a new version of your filesystem just ready to be mounted at a convenient place so that you are able to restore the version of the file from just about 2 seconds ago. Check the [details of NILFS on the wikipedia page](http://en.wikipedia.org/wiki/NILFS) for a good overview. This post will be about basic usage and some ideas I have how to put it to actual use in a production environment.

So getting nilfs running on Debian/Squeeze (in that case as I tried it on my workstation) isn't much of a problem. A couple of commands and you are good to go:

[sourcecode language="text"]
$ sudo m-a a-i nilfs2 # compile the modules for the kernel you currently use
$ sudo apt-get install nilfs2-tools
$ sudo lvcreate -L 1000M -n nilfs.test vg00
$ sudo mkfs.nilfs2 /dev/vg00/nilfs.test
$ sudo mount /dev/vg00/nilfs.test /mnt/nilfs/
[/sourcecode]
Now with this you can start using your shiny new nilfs2 2 partition right away, the interesting part comes from the snapshots you are able to use with nilfs2. Use lscp to show how many checkpoints have been created.
[sourcecode language="text"]
$ sudo lscp
        CNO        DATE     TIME  MODE  FLG   NBLKINC       ICNT
         51  2009-06-08 11:42:43   cp    -       1181          6
         52  2009-06-08 11:42:48   cp    -       1168          6
         53  2009-06-08 11:42:53   cp    -       1464          6
         54  2009-06-08 11:42:58   cp    -        551          6
         55  2009-06-08 11:43:03   cp    -        748          6
         56  2009-06-08 11:43:08   cp    -       1505          6
         57  2009-06-08 11:43:13   cp    -        785          6
         58  2009-06-08 11:43:18   cp    -       2155          6
         59  2009-06-08 11:43:23   cp    -        688          6
         60  2009-06-08 11:43:28   cp    -        762          6
         ...
         83  2009-06-08 11:45:30   cp    -       2643          5
         84  2009-06-08 11:47:28   cp    i         10          5
         85  2009-06-08 11:47:40   cp    i         10          5
         86  2009-06-08 11:48:21   cp    i         13          5
[/sourcecode]
Yes I did this from a random directory, lscp will try to find a nilfs2 filesystem by looking at /proc/mounts. Regarding the meaning of the columns I'm pretty sure you can read the manpage yourself. Now let's get a mount from an older version of the filesystem. This involves 3 steps:



	
  1. find the checkpoint you want to mount

	
  2. make the checkpoint a snapshot

	
  3. mount it


[sourcecode language="text"]
...
# I decided to use no. 65
$ sudo chcp ss 65
$ sudo lscp|grep 65
        65  2009-06-08 11:43:54   ss    -       1563          6
$ mount -t nilfs2 -r -o cp=65 /dev/vg00/nilfs.test /mnt/cp/
$ sudo ls -l /mnt/nilfs/
total 181796
-rw-r--r-- 1 martin martin  43220992 2009-04-14 00:20 debian-501-amd64-businesscard.iso
-rw-r--r-- 1 martin martin 142194688 2009-04-14 00:21 debian-501-amd64-netinst.iso
$ sudo mkdir -p /mnt/cp/
$ sudo ls -l /mnt/cp/
total 0
$ sudo mount -t nilfs2 -r -o cp=65 /dev/vg00/nilfs.test /mnt/cp/
$ sudo ls -l /mnt/cp/
total 117808
-rw-r--r-- 1 martin martin 120151000 2009-06-08 11:43 debian-501-amd64-netinst.iso
-rw-r--r-- 1 martin root           7 2009-06-08 10:50 foo
[/sourcecode]
Aha! Now we have a version from just a couple of minutes before we did something to our filesystem.

How do we put that to actual use now?

	
  * [Continuous Data Protection](http://en.wikipedia.org/wiki/Continuous_Data_Protection) - imagine you have some kind of interface where users can mount arbitrary snapshots to restore a file they just destroyed. Forget about those high budget data protection tools

	
  * Poor (Wo)Mans Version Control - I do know quite a couple of developers who don't check in to their soruce repo often enough. Could be some help for them

	
  * Nicer Backups - quite a couple of server don't have any option without being taken down. Linux LVM snapshots take quite a while to finish, with NILFS2 this takes nearly no time.

	
    * shutdown # this is probably the part that takes the longest

	
    * chcp

	
    * startup again

	
    * take care of the backup





Of course those are just very vague ideas but I hope a richt environment of nice tools will build around it. Of course I'd wish that btrfs would have that feature (or the other way around) because I like the idea of the volume manager being built into the file system. I can't yet exactly say why but to me it just seems to be the right place for it.





# Continuous data protection



