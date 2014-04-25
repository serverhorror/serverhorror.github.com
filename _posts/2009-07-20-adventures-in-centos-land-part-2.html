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
<p>OK let's see what's going on with our <a href="http://serverhorror.wordpress.com/2009/07/19/adventures-in-centos-land-part-1/">CentOS mail host from last time</a>. First let's check that we don't have too much listening on public interfaces after all we only need SSH, SMTPs, IMAPs and HTTPs when everything is set up...<br />
[sourcecode language="text"]<br />
# netstat -tulpen<br />
Active Internet connections (only servers)<br />
Proto Recv-Q Send-Q Local Address     Foreign Address   State   User  Inode  PID/Program name   <br />
tcp        0      0 0.0.0.0:111       0.0.0.0:*         LISTEN  0     54126  19649/portmap       <br />
tcp        0      0 0.0.0.0:818       0.0.0.0:*         LISTEN  0     54249  19716/rpc.statd     <br />
tcp        0      0 127.0.0.1:631     0.0.0.0:*         LISTEN  0     54161  19672/cupsd         <br />
tcp        0      0 127.0.0.1:25      0.0.0.0:*         LISTEN  0     54687  19798/sendmail: acc<br />
tcp        0      0 :::22             :::*              LISTEN  0     4961   1917/sshd           <br />
tcp        0      0 ::1:631           :::*              LISTEN  0     54162  19672/cupsd         <br />
udp        0      0 0.0.0.0:812       0.0.0.0:*                 0     54233  19716/rpc.statd     <br />
udp        0      0 0.0.0.0:815       0.0.0.0:*                 0     54242  19716/rpc.statd     <br />
udp        0      0 0.0.0.0:32825     0.0.0.0:*                 70    54204  19689/avahi-daemon:<br />
udp        0      0 0.0.0.0:5353      0.0.0.0:*                 70    54202  19689/avahi-daemon:<br />
udp        0      0 0.0.0.0:111       0.0.0.0:*                 0     54125  19649/portmap       <br />
udp        0      0 0.0.0.0:631       0.0.0.0:*                 0     54165  19672/cupsd         <br />
udp        0      0 :::32826          :::*                      70    54205  19689/avahi-daemon:<br />
udp        0      0 :::5353           :::*                      70    54203  19689/avahi-daemon:<br />
[/sourcecode]<br />
Quite a lot listening there for a server that is freshly installed. Let's turn of the nastiest stuff in the first place (NFS being public? WTF?).<br />
[sourcecode language="text"]<br />
# service portmap stop<br />
Stopping portmap:                                          [  OK  ]<br />
# service cups stop<br />
Stopping cups:                                             [  OK  ]<br />
# service avahi-daemon stop<br />
Shutting down Avahi daemon:                                [  OK  ]<br />
# service nfslock stop<br />
Stopping NFS statd:                                        [  OK  ]<br />
# service sendmail stop<br />
Shutting down sm-client:                                   [  OK  ]<br />
Shutting down sendmail:                                    [  OK  ]<br />
# service postfix start<br />
Starting postfix:                                          [  OK  ]<br />
# netstat -tulpen<br />
Active Internet connections (only servers)<br />
Proto Recv-Q Send-Q Local Address     Foreign Address  State   User  Inode  PID/Program name<br />
tcp        0      0 0.0.0.0:25        0.0.0.0:*        LISTEN  0     55050  20006/master<br />
tcp        0      0 :::22             :::*             LISTEN  0     4961   1917/sshd<br />
[/sourcecode]<br />
Much better isn't it? Now let's take care of reboots:<br />
[sourcecode language="text"]<br />
# chkconfig --level 345 portmap off<br />
# chkconfig --level 345 cups off<br />
# chkconfig --level 345 avahi-daemon off<br />
# chkconfig --level 345 nfslock off<br />
# chkconfig --level 235 sendmail off<br />
# chkconfig --level 2345 postfix on<br />
# chkconfig --level 2345 sshd on<br />
[/sourcecode]<br />
Just to be on the safe side let's double check that ssh will come up on reboots:<br />
[sourcecode language="text"]<br />
# chkconfig --list sshd<br />
sshd               0:off    1:off    2:on    3:on    4:on    5:on    6:off<br />
[/sourcecode]<br />
Looks all nice. Now <em>shutdown -r now</em> and see if it stays that way...(This is left as an exercise for the reader)</p>
