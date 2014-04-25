---
layout: post
title: Adventures in CentOS-Land (Part 2)
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1259053359";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1259053359";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
<p>OK let's see what's going on with our <a href="http://serverhorror.wordpress.com/2009/07/19/adventures-in-centos-land-part-1/">CentOS mail host from last time</a>. First let's check that we don't have too much listening on public interfaces after all we only need SSH, SMTPs, IMAPs and HTTPs when everything is set up...

{% highlight text %}
# netstat -tulpen
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address     Foreign Address   State   User  Inode  PID/Program name   
tcp        0      0 0.0.0.0:111       0.0.0.0:*         LISTEN  0     54126  19649/portmap       
tcp        0      0 0.0.0.0:818       0.0.0.0:*         LISTEN  0     54249  19716/rpc.statd     
tcp        0      0 127.0.0.1:631     0.0.0.0:*         LISTEN  0     54161  19672/cupsd         
tcp        0      0 127.0.0.1:25      0.0.0.0:*         LISTEN  0     54687  19798/sendmail: acc
tcp        0      0 :::22             :::*              LISTEN  0     4961   1917/sshd           
tcp        0      0 ::1:631           :::*              LISTEN  0     54162  19672/cupsd         
udp        0      0 0.0.0.0:812       0.0.0.0:*                 0     54233  19716/rpc.statd     
udp        0      0 0.0.0.0:815       0.0.0.0:*                 0     54242  19716/rpc.statd     
udp        0      0 0.0.0.0:32825     0.0.0.0:*                 70    54204  19689/avahi-daemon:
udp        0      0 0.0.0.0:5353      0.0.0.0:*                 70    54202  19689/avahi-daemon:
udp        0      0 0.0.0.0:111       0.0.0.0:*                 0     54125  19649/portmap       
udp        0      0 0.0.0.0:631       0.0.0.0:*                 0     54165  19672/cupsd         
udp        0      0 :::32826          :::*                      70    54205  19689/avahi-daemon:
udp        0      0 :::5353           :::*                      70    54203  19689/avahi-daemon:
{% endhighlight text %}

Quite a lot listening there for a server that is freshly installed. Let's turn of the nastiest stuff in the first place (NFS being public? WTF?).

{% highlight text %}
# service portmap stop
Stopping portmap:                                          [  OK  ]
# service cups stop
Stopping cups:                                             [  OK  ]
# service avahi-daemon stop
Shutting down Avahi daemon:                                [  OK  ]
# service nfslock stop
Stopping NFS statd:                                        [  OK  ]
# service sendmail stop
Shutting down sm-client:                                   [  OK  ]
Shutting down sendmail:                                    [  OK  ]
# service postfix start
Starting postfix:                                          [  OK  ]
# netstat -tulpen
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address     Foreign Address  State   User  Inode  PID/Program name
tcp        0      0 0.0.0.0:25        0.0.0.0:*        LISTEN  0     55050  20006/master
tcp        0      0 :::22             :::*             LISTEN  0     4961   1917/sshd
{% endhighlight text %}

Much better isn't it? Now let's take care of reboots:

{% highlight text %}
# chkconfig --level 345 portmap off
# chkconfig --level 345 cups off
# chkconfig --level 345 avahi-daemon off
# chkconfig --level 345 nfslock off
# chkconfig --level 235 sendmail off
# chkconfig --level 2345 postfix on
# chkconfig --level 2345 sshd on
{% endhighlight text %}

Just to be on the safe side let's double check that ssh will come up on reboots:

{% highlight text %}
# chkconfig --list sshd
sshd               0:off    1:off    2:on    3:on    4:on    5:on    6:off
{% endhighlight text %}

Looks all nice. Now <em>shutdown -r now</em> and see if it stays that way...(This is left as an exercise for the reader)</p>
