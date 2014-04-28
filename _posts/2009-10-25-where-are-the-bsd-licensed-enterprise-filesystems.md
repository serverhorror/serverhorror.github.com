---
layout: post
title: Where are the BSD Licensed "Enterprise Filesystems"?
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1270743930";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1270743940";}
  _wpas_skip_fb: '1'
author: 
---
<p>A very simple question.</p>
<blockquote><p>Where is the "Enterprise Filesystem" licensed in a pure BSD way?</p></blockquote>
<p>I know <a href="http://en.wikipedia.org/wiki/Zfs">ZFS</a> has been implemented by OpenSolaris (well yeah...that's the origin of ZFS) as well as <a href="http://www.freebsd.org">FreeBSD</a> but the <a href="http://en.wikipedia.org/wiki/Common_Development_and_Distribution_License">CDDL</a> is not without critique in the BSD community. The <a href="http://www.openbsd.org">OpenBSD</a> <a href="http://marc.info/?l=openbsd-tech&amp;m=110806948606417&amp;w=2">people consider the CDDL even more restrivtive than GNU/GPL</a>.</p>
<p>So a question to all the guys and girls who are able to create a filesystem (I can't my coding skills are nowhere near to be able to create one), where is the BSD licensed filesystem with all the new features that make a hype?</p>
<p>I'm thinking about stuff like this (thou maybe not complete, somebody may have an absolutely usefull new idea that obsoletes all these features</p>
<ul>
<li><a href="http://en.wikipedia.org/wiki/Snapshot_(computer_storage)">Snapshots</a> (<a href="http://en.wikipedia.org/wiki/Btrfs">BTRFS</a>, ZFS)
<ul>
<li><a href="http://en.wikipedia.org/wiki/Versioning_file_system">Continous Snapshots (Versioning File System)</a> (<a href="http://en.wikipedia.org/wiki/Nilfs">NILFS</a>)</li>
</ul>
</li>
<li><a href="http://en.wikipedia.org/wiki/Copy_on_write">COW (Copy on Write)</a> (BTRFS, ZFS)</li>
<li><a href="http://en.wikipedia.org/wiki/Logical_volume_management">Volume Management built-in</a> (BTRFS, ZFS)</li>
<li><a href="http://en.wikipedia.org/wiki/RAID">RAID (like) features built-in the filesystem</a> (BTRFS, ZFS)</li>
<li>Really large maximum filesizes and<sup>*</sup></li>
<li>Really large maximum filesystem sizes<sup>*</sup></li>
</ul>
<p><sup><strong>*</strong></sup>This may not be a Problem now, but I do get why Sun chose to make ZFS a 128-bit filesystem</p>
