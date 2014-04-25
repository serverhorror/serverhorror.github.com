---
layout: post
title: 'HowTo: List open network connections for a certain user'
categories: []
tags:
- lsof
- network
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_yup: '1'
  _wpas_done_twitter: '1'
  _wpas_done_fb: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1319894126";}
author: 
---
<p>Since I always have to look it up in the <a title="LSOF(8) - manpages.debian.net" href="http://manpages.debian.net/cgi-bin/man.cgi?query=lsof">manpage of lsof(8)</a>:</p>
<p>{% highlight text %}<br />
lsof -nP -a -i -u ${USER} # list all network connections for ${USER}<br />
lsof -nP -a -i UDP -u ${USER} # list UDP connections for ${USER}<br />
lsof -nP -a -i TCP -u ${USER} # list TCP connections for ${USER}<br />
lsof -nP -a -i 6 -i TCP -u ${USER} # list IPv6 TCP connections for ${USER}<br />
{% endhighlight %}</p>
<dl>
<dt><code>-n</code></dt>
<dd>don't translate IP addresses to host names</dd>
<dt><code>-P</code></dt>
<dd>don't translate port numbers to names</dd>
<dt><code>-a</code></dt>
<dd>make a logical AND for the following selections</dd>
<dt><code>-i</code></dt>
<dd>without options select EVERYTHING. Other options come in natural</dd>
</dl>
<p>no more <code>grep</code>-ping with <code>lsof</code></p>
<p>[caption id="" align="aligncenter" width="300" caption="Image via Wikipedia"]<a href="http://commons.wikipedia.org/wiki/File:Lsof.JPG"><img title="lsof help output" src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Lsof.JPG/300px-Lsof.JPG" alt="lsof help output" width="300" height="251" /></a>[/caption]</p>
