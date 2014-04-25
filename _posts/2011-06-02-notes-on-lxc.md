---
layout: post
title: Notes on LXC
categories: []
tags:
- Device file
- linux
- Logical Volume Manager (Linux)
- LXC
- Mkdir
- Operating Systems
- Sysfs
- Ubuntu
status: publish
type: post
published: true
meta:
  _wpas_mess: 'Fixed formatting: "Notes on LXC http://wp.me/pxxjT-kG"'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1307092069";}
  _wpas_done_twitter: '1'
  _wpas_done_linkedin: '1'
  _wpas_skip_fb: '1'
author: 
---
<div class="posterous_autopost">
<p><strong>NOTICE</strong>:<br />
Despite looking like copy/paste commands. <strong>These are not copy/paste commands</strong>. Use your brain!</p>
<p>Minor notes on how to set up a host and a first container for <a href="http://en.wikipedia.org/wiki/Lxc">LXC</a>. This will not give you networking. Those are just the basics…</p>
<h2>Assumptions</h2>
<ul>
<li>You have an <a href="http://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux">LVM</a> configured that is named <code>lxc</code></li>
<li><a href="http://en.wikipedia.org/wiki/Lxc">LXC</a> containers will be deployed to <code>/srv/lxc/$utsname</code></li>
<li>LXC containers will be configured from <code>/etc/lxc/$utsname/{config,fstab}</code></li>
</ul>
<h2>Do It!</h2>
<ol>
<li><code>apt-get install debian</code></li>
<li><code>apt-get install vim git-core lxc bash-completion</code></li>
<li><code>. /etc/bash-completion</code></li>
<li><code>mkdir -p /srv/lxc/vm01</code></li>
<li><code>lvcreate -n vm01 -L 5G lxc</code></li>
<li><code>mkfs.ext4 /dev/lxc/vm01</code></li>
<li><code>mount /dev/lxc/vm01 /srv/lxc/vm01</code></li>
<li><code>mkdir -p /etc/lxc/vm01</code></li>
<li><code>vim /etc/lxc/vm01/conf</code>
<div class="CodeRay">
<div class="code">{% highlight text %}<br />
lxc.utsname=vm01 lxc.network.type=empty<br />
lxc.network.flags=up<br />
lxc.mount=/etc/lxc/vm01/fstab<br />
lxc.rootfs=/srv/lxc/vm01<br />
lxc.tty=4 lxc.pts=1024<br />
# LXC Device setup<br />
# only explicitely allowed devices...<br />
lxc.cgroup.devices.deny = a<br />
# /dev/null and zero<br />
lxc.cgroup.devices.allow = c 1:3 rwm<br />
lxc.cgroup.devices.allow = c 1:5 rwm # consoles<br />
lxc.cgroup.devices.allow = c 5:1 rwm<br />
lxc.cgroup.devices.allow = c 5:0 rwm<br />
lxc.cgroup.devices.allow = c 4:0 rwm<br />
lxc.cgroup.devices.allow = c 4:1 rwm<br />
# /dev/{,u}random<br />
lxc.cgroup.devices.allow = c 1:9 rwm<br />
lxc.cgroup.devices.allow = c 1:8 rwm<br />
lxc.cgroup.devices.allow = c 136:* rwm<br />
lxc.cgroup.devices.allow = c 5:2 rwm<br />
# rtc<br />
lxc.cgroup.devices.allow = c 254:0 rwm<br />
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>vim /etc/lxc/vm01/fstab</code>
<div class="CodeRay">
<div class="code">{% highlight text %}<br />
devpts /srv/lxc/vm01/debootstrapped/dev/pts devpts defaults 0 0<br />
proc /srv/lxc/vm01/debootstrapped/proc    proc   defaults 0 0<br />
sysfs /srv/lxc/vm01/debootstrapped/sys     sysfs  defaults 0 0<br />
none /srv/lxc/vm01/debootstrapped/dev/shm tmpfs  defaults 0 0<br />
{% endhighlight %}</p>
</div>
</div>
</li>
<li>Install base system
<div class="CodeRay">
<div class="code">{% highlight text %}<br />
debootstrap --variant=minbase --include=dhcp-client,dialog,ifupdown,iproute,libui-dialog-perl,locales,netbase,net-tools,openssh-server,vim,curl,git-core squeeze /srv/lxc/vm01/ http://cdn.debian.net/debian/<br />
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>/usr/sbin/chroot /srv/lxc/vm01 /usr/bin/passwd -d root</code></li>
<li><code>echo vm01 &gt; /srv/lxc/vm01/etc/hostname</code></li>
<li><code>vim /srv/lxc/vm01/etc/inittab</code>
<div class="CodeRay">
<div class="code">{% highlight text %}<br />
id:3:initdefault:<br />
si::sysinit:/etc/init.d/rcS<br />
l0:0:wait:/etc/init.d/rc 0<br />
l1:1:wait:/etc/init.d/rc 1<br />
l2:2:wait:/etc/init.d/rc 2<br />
l3:3:wait:/etc/init.d/rc 3<br />
l4:4:wait:/etc/init.d/rc 4<br />
l5:5:wait:/etc/init.d/rc 5<br />
l6:6:wait:/etc/init.d/rc 6<br />
# Normally not reached, but fallthrough in case of emergency.<br />
z6:6:respawn:/sbin/sulogin<br />
1:2345:respawn:/sbin/getty 38400 console<br />
c1:12345:respawn:/sbin/getty 38400 tty1 linux<br />
c2:12345:respawn:/sbin/getty 38400 tty2 linux<br />
c3:12345:respawn:/sbin/getty 38400 tty3 linux<br />
c4:12345:respawn:/sbin/getty 38400 tty4 linux<br />
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>vim /srv/lxc/vm01/etc/init.d/hwclockfirst.sh</code>
<div class="CodeRay">
<div class="code">{% highlight text %}<br />
#!/bin/sh<br />
### BEGIN INIT INFO<br />
# Provides:          hwclockfirst<br />
# Required-Start:    mountdevsubfs<br />
# Required-Stop:<br />
# Default-Start:     S<br />
# X-Start-Before:    checkroot<br />
# Default-Stop:<br />
### END INIT INFO<br />
exit 0<br />
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>vim /srv/lxc/vm01/etc/init.d/hwclock.sh</code>
<div class="CodeRay">
<div class="code">{% highlight text %}<br />
#!/bin/sh<br />
### BEGIN INIT INFO<br />
# Provides:          hwclock<br />
# Required-Start:    checkroot<br />
# Required-Stop:     $local_fs<br />
# Default-Start:     S<br />
# Default-Stop:      0 6<br />
### END INIT INFO<br />
exit 0<br />
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>&gt;/etc/lxc/vm01/log</code></li>
<li><code>lxc-start -n vm01 -f /etc/lxc/vm01/conf -o /etc/lxc/vm01/log --logpriority INFO</code></li>
</ol>
</div>
