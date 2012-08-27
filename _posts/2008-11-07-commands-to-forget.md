---
comments: true
date: 2008-11-07 21:45:00
layout: post
slug: commands-to-forget
title: Commands to forget
wordpress_id: 202
tags:
- sysadmin
---

Commands I always forget (mostly this is [Linux](http://www.kernel.org/) only, or at least [GNU Tools](http://www.gnu.org/)):


* gzip input from stdin to a file: [ ](http://manpages.debian.net/cgi-bin/man.cgi?query=cat&sektion=1)
    {% highlight bash %}
    cat <sourcefile> | gzip > <targetfile>
    {% endhighlight %}
* get the number of threads for a given process name
    {% highlight bash %}
    ps -C <processname> -L
    {% endhighlight %}



