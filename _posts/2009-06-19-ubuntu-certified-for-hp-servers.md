---
layout: post
title: Ubuntu certified for HP servers
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1246166792";}
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1246166791";}
author: 
---
<p><a href="http://www.ubuntu.com">Ubuntu</a> just announced a <a href="http://www.ubuntu.com/news/hp-proliant-servers-certified-ubuntu">certification for the server version 9.04 on HP Proliant G6 servers</a> (see also <a href="http://h18004.www1.hp.com/products/servers/platforms/new.html?psn=servers">HP Press release about this</a>).</p>
<p>It seems I finally have to consider Ubuntu for our servers. <strong>Not something I'm too pleased with</strong> as my previous experience has been less than good. <a href="https://launchpad.net/ubuntu/+source/cyrus-imapd-2.2/+bug/67111">One bug I ran into</a> burned itself into my memory.</p>
<p>The bug was a cyrus-imapd linked to a version of libdb it wasn't compiled against. As a result you could nicely see it segfault but that was it. The real tragedy in this bug was actually a couple of things:</p>
<ul>
<li>it was an LTS (Long-Term-Support) Release</li>
<li>cyrus-imapd was in main</li>
<li>the bug was not fixed for nearly  7 months</li>
</ul>
<p>I can understand that things like these can happen - even in an LTS release, even in main - but the time it took to repair the trivial issue just doesn't make me feel comfortable with Ubuntu on our servers.</p>
<p>Fortunately <a href="http://h20219.www2.hp.com/services/cache/442406-0-0-225-121.html">Debian is also supported on HP Proliant servers</a>, and has even been supported for much longer than the just <a href="http://h18006.www1.hp.com/products/servers/platforms/new.html">recently released G6 Family</a> of HP's servers. Hopefully HP won't drop support for Debian that would be a real pita.</p>
