---
layout: post
title: HowTo NILFS2
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1245787862";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1245787862";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
<p>With kernel 2.6.30 there's a shiny new filesystem officially available. <a href="http://www.nilfs.org">NILFS2</a> provides</p>
<ul>
<li>checkpoints at regular intervals (unless there is no change) or  with  synchronous  writings</li>
</ul>
<p>essentially that means that everytime you write a new file you will have a new version of your filesystem just ready to be mounted at a convenient place so that you are able to restore the version of the file from just about 2 seconds ago. Check the <a href="http://en.wikipedia.org/wiki/NILFS">details of NILFS on the wikipedia page</a> for a good overview. This post will be about basic usage and some ideas I have how to put it to actual use in a production environment.</p>
<p>So getting nilfs running on Debian/Squeeze (in that case as I tried it on my workstation) isn't much of a problem. A couple of commands and you are good to go:</p>
<p>[sourcecode language="text"]<br />
$ sudo m-a a-i nilfs2 # compile the modules for the kernel you currently use<br />
$ sudo apt-get install nilfs2-tools<br />
$ sudo lvcreate -L 1000M -n nilfs.test vg00<br />
$ sudo mkfs.nilfs2 /dev/vg00/nilfs.test<br />
$ sudo mount /dev/vg00/nilfs.test /mnt/nilfs/<br />
[/sourcecode]<br />
Now with this you can start using your shiny new nilfs2 2 partition right away, the interesting part comes from the snapshots you are able to use with nilfs2. Use lscp to show how many checkpoints have been created.<br />
[sourcecode language="text"]<br />
$ sudo lscp<br />
        CNO        DATE     TIME  MODE  FLG   NBLKINC       ICNT<br />
         51  2009-06-08 11:42:43   cp    -       1181          6<br />
         52  2009-06-08 11:42:48   cp    -       1168          6<br />
         53  2009-06-08 11:42:53   cp    -       1464          6<br />
         54  2009-06-08 11:42:58   cp    -        551          6<br />
         55  2009-06-08 11:43:03   cp    -        748          6<br />
         56  2009-06-08 11:43:08   cp    -       1505          6<br />
         57  2009-06-08 11:43:13   cp    -        785          6<br />
         58  2009-06-08 11:43:18   cp    -       2155          6<br />
         59  2009-06-08 11:43:23   cp    -        688          6<br />
         60  2009-06-08 11:43:28   cp    -        762          6<br />
         ...<br />
         83  2009-06-08 11:45:30   cp    -       2643          5<br />
         84  2009-06-08 11:47:28   cp    i         10          5<br />
         85  2009-06-08 11:47:40   cp    i         10          5<br />
         86  2009-06-08 11:48:21   cp    i         13          5<br />
[/sourcecode]<br />
Yes I did this from a random directory, lscp will try to find a nilfs2 filesystem by looking at /proc/mounts. Regarding the meaning of the columns I'm pretty sure you can read the manpage yourself. Now let's get a mount from an older version of the filesystem. This involves 3 steps:</p>
<ol>
<li>find the checkpoint you want to mount</li>
<li>make the checkpoint a snapshot</li>
<li>mount it</li>
</ol>
<p>[sourcecode language="text"]<br />
...<br />
# I decided to use no. 65<br />
$ sudo chcp ss 65<br />
$ sudo lscp|grep 65<br />
        65  2009-06-08 11:43:54   ss    -       1563          6<br />
$ mount -t nilfs2 -r -o cp=65 /dev/vg00/nilfs.test /mnt/cp/<br />
$ sudo ls -l /mnt/nilfs/<br />
total 181796<br />
-rw-r--r-- 1 martin martin  43220992 2009-04-14 00:20 debian-501-amd64-businesscard.iso<br />
-rw-r--r-- 1 martin martin 142194688 2009-04-14 00:21 debian-501-amd64-netinst.iso<br />
$ sudo mkdir -p /mnt/cp/<br />
$ sudo ls -l /mnt/cp/<br />
total 0<br />
$ sudo mount -t nilfs2 -r -o cp=65 /dev/vg00/nilfs.test /mnt/cp/<br />
$ sudo ls -l /mnt/cp/<br />
total 117808<br />
-rw-r--r-- 1 martin martin 120151000 2009-06-08 11:43 debian-501-amd64-netinst.iso<br />
-rw-r--r-- 1 martin root           7 2009-06-08 10:50 foo<br />
[/sourcecode]<br />
Aha! Now we have a version from just a couple of minutes before we did something to our filesystem.</p>
<p>How do we put that to actual use now?</p>
<ul>
<li><a href="http://en.wikipedia.org/wiki/Continuous_Data_Protection">Continuous Data Protection</a> - imagine you have some kind of interface where users can mount arbitrary snapshots to restore a file they just destroyed. Forget about those high budget data protection tools</li>
<li>Poor (Wo)Mans Version Control - I do know quite a couple of developers who don't check in to their soruce repo often enough. Could be some help for them</li>
<li>Nicer Backups - quite a couple of server don't have any option without being taken down. Linux LVM snapshots take quite a while to finish, with NILFS2 this takes nearly no time.
<ul>
<li>shutdown # this is probably the part that takes the longest</li>
<li>chcp</li>
<li>startup again</li>
<li>take care of the backup</li>
</ul>
</li>
</ul>
<p>Of course those are just very vague ideas but I hope a richt environment of nice tools will build around it. Of course I'd wish that btrfs would have that feature (or the other way around) because I like the idea of the volume manager being built into the file system. I can't yet exactly say why but to me it just seems to be the right place for it.</p>
<div id="_mcePaste" style="overflow:hidden;position:absolute;left:-10000px;top:764px;width:1px;height:1px;">
<h1 class="firstHeading">Continuous data protection</h1>
</div>
