---
layout: post
title: 'RE: Is there a best distro? (LinuxJournal)'
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1270743943";}
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1270743930";}
author: 
---
<p><a href="http://www.linuxjournal.com/content/there-best-distro">LinuxJournal is asking for the best Linux Distro</a>, first I thought</p>
<p>It's actually quite easy to answer (especially to someone who will understand the implications):</p>
<h2>There is no "best Linux"</h2>
<p>Just asko what's the best commercial Unix out there. One could
say: "They all start at the same point" it's a kernel and some
toolset you can then use and (re)script to your needs.</p>
<p>The best ist actually the one that meets your requirements best.</p>
<ul>
<li><strong>Cheap?</strong>
<ul>
<li><span style="background-color:#ffffff;"><a href="http://www.debian.org">Debian</a></span></li>
<li><span style="background-color:#ffffff;"><a href="http://www.ubuntu.com">Ubuntu</a></span></li>
<li><span style="background-color:#ffffff;"><a href="http://www.gentoo.org">Gentoo</a></span></li>
<li><span style="background-color:#ffffff;">(any "*non-enterprise distro*")/...</span></li>
</ul>
</li>
<li><strong>Supported?</strong>
<ul>
<li><span style="background-color:#ffffff;"><a href="http://www.redhat.com">RHEL</a></span></li>
<li><span style="background-color:#ffffff;"><a href="http://www.novell.com/linux/">SuSE</a> (hehe, I had to look that one up)</span></li>
<li><span style="background-color:#ffffff;">...</span></li>
</ul>
</li>
<li><strong>Small?</strong>
<ul>
<li><span style="background-color:#ffffff;"><a href="http://grml.org/">Grml</a></span></li>
<li><span style="background-color:#ffffff;"><a href="http://www.damnsmalllinux.org/">DSL</a></span></li>
<li><span style="background-color:#ffffff;">...</span></li>
</ul>
</li>
</ul>
<h2>"All of the distributions start from the same point"</h2>
<p>I think that's just plain wrong. Yes they do have the same kernel (do they really? - <a href="http://www.debian.org/ports/kfreebsd-gnu/">Debian GNU/kFreeBSD</a>). <span style="background-color:#ffffff;">But even switching from Ubuntu to Debian or vice versa has a lot of hurdles to take ("/etc/inittab" on Ubuntu?) - Upstart in Debian/Stable?</span></p>
<p>I'd rather suggest <em><a href="http://www.freebsd.org">FreeBSD</a></em><em> or </em><em><a href="http://www.openbsd.org">OpenBSD</a> </em>(4.6 is just out, I suggest everyone to give it a try) - <strong>or is crucial</strong> because choosing between the 2 is (IMHO) even wider apart than choosing between RHEL and Debian. <em>Note: I suggest this <strong><a href="http://en.wikipedia.org/wiki/If_and_only_if">iff</a></strong>[sic] you want to stay in an enviroment that stays mostly the same thruought all servers and desktops</em></p>
<p>FreeBSD is FreeBSD is FreeBSD - on every box.</p>
<p>Linux is not "just Linux" from that point there's just too much diversity among the distros. Even with a single Distro you can have large differences, of course you can take any BSD apart so that it won't look like the original distribution anymore, but staying within the universe of best practices you won't have as much diversity between FreeBSD installations as between Linux installations within a single distribution.</p>
<h2><span style="background-color:#ffffff;">Selection of rich applications</span></h2>
<p><span style="background-color:#ffffff;">The key word here is <strong>Selection</strong>. Compare RHELs selection to Debians selection. You wouldn't think that an enterprise grade distro doesn't even have Nagios in the repositories - aren't the enterprise people monitoring their servers too?</span></p>
<h2><span style="background-color:#ffffff;">My choice?</span></h2>
<p><span style="background-color:#ffffff;">Simple, give me the problem description and I'll have a look which of the distributions (or even non-Linux - read BSDs, or even non-FOSS) solutions will suit best. It doesn't help to get RHEL if they don't support the software you need, but it's neither helpful to stay with Debian if you need proven Enterprise grade support contrancts with 4 hours of maximum time to react. (Btw: <a href="http://opensolaris.org">OpenSolaris</a> does have the <a href="http://www.opensolaris.com/learn/subscriptions/#opensolaris"><strong>option</strong> to buy support from Sun</a>)</span></p>
<p><span style="background-color:#ffffff;">Of course that would be only the start of a discussion with someone who already knows enough about *NIX to discuss on such a Level. As you said dear LinuxJournal:</span></p>
<blockquote><p><span style="background-color:#ffffff;">This was not someone who is unfamiliar with technology, or UNIX for that matter, but someone who is <em>one of us</em></span></p></blockquote>
