---
layout: post
title: volatile.debian.org deprecated - use squeeze-updates
categories: []
tags:
- Debian
- linux
- sysadmin
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1319654451";}
  _wpas_done_yup: '1'
  _wpas_done_twitter: '1'
  _wpas_done_fb: '1'
author: 
---
<p>As of today the <a title="The debian-volatile Project" href="http://www.debian.org/volatile/">volatile.debian.org</a> is discontinued. Just read <a title="[VUA 76-1] volatile replaced by new updates suite" href="http://lists.debian.org/debian-volatile-announce/2011/msg00000.html">the official announcement</a>.</p>
<h1>Debian/Squeeze</h1>
<p>The short version is to got to your <code style="display:inline-block;">/etc/apt/sources.list</code> and replace your volatile with</p>
<p>[sourcecode language="text"]<br />
deb http://ftp.debian.org/debian squeeze-updates main<br />
[/sourcecode]</p>
<p>Then run (with your usual procedures of testing that of course):</p>
<p>[sourcecode language="text"]<br />
apt-get update<br />
apt-get upgrade<br />
[/sourcecode]</p>
<p>and you should be fine</p>
