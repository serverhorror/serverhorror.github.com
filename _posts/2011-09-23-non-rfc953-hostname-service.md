---
layout: post
title: NON-RFC953 Hostname Service
categories: []
tags:
- Hostname
- Internet Protocol
- Protocols
- Servers
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1316940916";}
  _wpas_mess: NON-RFC953 Hostname Service http://wp.me/pxxjT-l5
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_linkedin: '1'
author: 
---
<ul>
<li>/etc/xinetd.d/<a class="zem_slink" title="Hostname" href="http://en.wikipedia.org/wiki/Hostname" rel="wikipedia">hostname</a></li>
</ul>
<p>[sourcecode]<br />
service hostname {<br />
    disable         = no<br />
    type            = UNLISTED<br />
    id              = hostname<br />
    port            = 101<br />
    socket_type     = stream<br />
    protocol        = tcp<br />
    user            = nobody<br />
    wait            = no<br />
    server          = /bin/hostname<br />
    server_args     = -f<br />
}<br />
[/sourcecode]</p>