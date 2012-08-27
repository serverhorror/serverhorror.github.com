---
comments: true
date: 2011-02-15 12:03:50
layout: post
slug: volatile-debian-org-deprecated-use-squeeze-updates
title: volatile.debian.org deprecated - use squeeze-updates
wordpress_id: 1139
tags:
- Debian
- linux
- sysadmin
---

As of today the [volatile.debian.org](http://www.debian.org/volatile/) is discontinued. Just read [the official announcement](http://lists.debian.org/debian-volatile-announce/2011/msg00000.html).


# Debian/Squeeze


The short version is to got to your `/etc/apt/sources.list` and replace your volatile with

[sourcecode language="text"]
deb http://ftp.debian.org/debian squeeze-updates main
[/sourcecode]

Then run (with your usual procedures of testing that of course):

[sourcecode language="text"]
apt-get update
apt-get upgrade
[/sourcecode]

and you should be fine
