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
<p><strong>NOTICE</strong>:
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
<div class="code">{% highlight text %}
lxc.utsname=vm01 lxc.network.type=empty
lxc.network.flags=up
lxc.mount=/etc/lxc/vm01/fstab
lxc.rootfs=/srv/lxc/vm01
lxc.tty=4 lxc.pts=1024
# LXC Device setup
# only explicitely allowed devices...
lxc.cgroup.devices.deny = a
# /dev/null and zero
lxc.cgroup.devices.allow = c 1:3 rwm
lxc.cgroup.devices.allow = c 1:5 rwm # consoles
lxc.cgroup.devices.allow = c 5:1 rwm
lxc.cgroup.devices.allow = c 5:0 rwm
lxc.cgroup.devices.allow = c 4:0 rwm
lxc.cgroup.devices.allow = c 4:1 rwm
# /dev/{,u}random
lxc.cgroup.devices.allow = c 1:9 rwm
lxc.cgroup.devices.allow = c 1:8 rwm
lxc.cgroup.devices.allow = c 136:* rwm
lxc.cgroup.devices.allow = c 5:2 rwm
# rtc
lxc.cgroup.devices.allow = c 254:0 rwm
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>vim /etc/lxc/vm01/fstab</code>
<div class="CodeRay">
<div class="code">{% highlight text %}
devpts /srv/lxc/vm01/debootstrapped/dev/pts devpts defaults 0 0
proc /srv/lxc/vm01/debootstrapped/proc    proc   defaults 0 0
sysfs /srv/lxc/vm01/debootstrapped/sys     sysfs  defaults 0 0
none /srv/lxc/vm01/debootstrapped/dev/shm tmpfs  defaults 0 0
{% endhighlight %}</p>
</div>
</div>
</li>
<li>Install base system
<div class="CodeRay">
<div class="code">{% highlight text %}
debootstrap --variant=minbase --include=dhcp-client,dialog,ifupdown,iproute,libui-dialog-perl,locales,netbase,net-tools,openssh-server,vim,curl,git-core squeeze /srv/lxc/vm01/ http://cdn.debian.net/debian/
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>/usr/sbin/chroot /srv/lxc/vm01 /usr/bin/passwd -d root</code></li>
<li><code>echo vm01 > /srv/lxc/vm01/etc/hostname</code></li>
<li><code>vim /srv/lxc/vm01/etc/inittab</code>
<div class="CodeRay">
<div class="code">{% highlight text %}
id:3:initdefault:
si::sysinit:/etc/init.d/rcS
l0:0:wait:/etc/init.d/rc 0
l1:1:wait:/etc/init.d/rc 1
l2:2:wait:/etc/init.d/rc 2
l3:3:wait:/etc/init.d/rc 3
l4:4:wait:/etc/init.d/rc 4
l5:5:wait:/etc/init.d/rc 5
l6:6:wait:/etc/init.d/rc 6
# Normally not reached, but fallthrough in case of emergency.
z6:6:respawn:/sbin/sulogin
1:2345:respawn:/sbin/getty 38400 console
c1:12345:respawn:/sbin/getty 38400 tty1 linux
c2:12345:respawn:/sbin/getty 38400 tty2 linux
c3:12345:respawn:/sbin/getty 38400 tty3 linux
c4:12345:respawn:/sbin/getty 38400 tty4 linux
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>vim /srv/lxc/vm01/etc/init.d/hwclockfirst.sh</code>
<div class="CodeRay">
<div class="code">{% highlight text %}
#!/bin/sh
### BEGIN INIT INFO
# Provides:          hwclockfirst
# Required-Start:    mountdevsubfs
# Required-Stop:
# Default-Start:     S
# X-Start-Before:    checkroot
# Default-Stop:
### END INIT INFO
exit 0
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>vim /srv/lxc/vm01/etc/init.d/hwclock.sh</code>
<div class="CodeRay">
<div class="code">{% highlight text %}
#!/bin/sh
### BEGIN INIT INFO
# Provides:          hwclock
# Required-Start:    checkroot
# Required-Stop:     $local_fs
# Default-Start:     S
# Default-Stop:      0 6
### END INIT INFO
exit 0
{% endhighlight %}</p>
</div>
</div>
</li>
<li><code>>/etc/lxc/vm01/log</code></li>
<li><code>lxc-start -n vm01 -f /etc/lxc/vm01/conf -o /etc/lxc/vm01/log --logpriority INFO</code></li>
</ol>
</div>
