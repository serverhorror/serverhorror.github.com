---
comments: true
date: 2011-09-23 14:20:47
layout: post
slug: non-rfc953-hostname-service
title: NON-RFC953 Hostname Service
wordpress_id: 1307
tags:
- Hostname
- Internet Protocol
- Protocols
- Servers
---


	
  * /etc/xinetd.d/[hostname](http://en.wikipedia.org/wiki/Hostname)


[sourcecode]
service hostname {
    disable         = no
    type            = UNLISTED
    id              = hostname
    port            = 101
    socket_type     = stream
    protocol        = tcp
    user            = nobody
    wait            = no
    server          = /bin/hostname
    server_args     = -f
}
[/sourcecode]
