---
comments: true
date: 2011-03-01 10:55:25
layout: post
slug: howto-list-open-network-connections-for-a-certain-user
title: 'HowTo: List open network connections for a certain user'
wordpress_id: 1172
tags:
- lsof
- network
- sysadmin
---

Since I always have to look it up in the [manpage of lsof(8)](http://manpages.debian.net/cgi-bin/man.cgi?query=lsof):

{% highlight bash %}
lsof -nP -a -i -u ${USER} # list all network connections for ${USER}
lsof -nP -a -i UDP -u ${USER} # list UDP connections for ${USER}
lsof -nP -a -i TCP -u ${USER} # list TCP connections for ${USER}
lsof -nP -a -i 6 -i TCP -u ${USER} # list IPv6 TCP connections for ${USER}
{% endhighlight %}



`-n`
    don't translate IP addresses to host names
`-P`
    don't translate port numbers to names
`-a`
    make a logical AND for the following selections
`-i`
    without options select EVERYTHING. Other options come in natural
no more `grep`-ping with `lsof`

[caption id="" align="aligncenter" width="300" caption="Image via Wikipedia"][![lsof help output](http://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Lsof.JPG/300px-Lsof.JPG)](http://commons.wikipedia.org/wiki/File:Lsof.JPG)[/caption]
