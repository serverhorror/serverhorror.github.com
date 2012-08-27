---
comments: true
date: 2011-06-02 13:25:25
layout: post
slug: notes-on-lxc
title: Notes on LXC
wordpress_id: 1282
tags:
- Device file
- linux
- Logical Volume Manager (Linux)
- LXC
- Mkdir
- Operating Systems
- Sysfs
- Ubuntu
---



**NOTICE**:
Despite looking like copy/paste commands. **These are not copy/paste commands**. Use your brain!

Minor notes on how to set up a host and a first container for [LXC](http://en.wikipedia.org/wiki/Lxc). This will not give you networking. Those are just the basics…


## Assumptions





	
  * You have an [LVM](http://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux) configured that is named `lxc`

	
  * [LXC](http://en.wikipedia.org/wiki/Lxc) containers will be deployed to `/srv/lxc/$utsname`

	
  * LXC containers will be configured from `/etc/lxc/$utsname/{config,fstab}`




## Do It!





	
  1. `apt-get install debian`

	
  2. `apt-get install vim git-core lxc bash-completion`

	
  3. `. /etc/bash-completion`

	
  4. `mkdir -p /srv/lxc/vm01`

	
  5. `lvcreate -n vm01 -L 5G lxc`

	
  6. `mkfs.ext4 /dev/lxc/vm01`

	
  7. `mount /dev/lxc/vm01 /srv/lxc/vm01`

	
  8. `mkdir -p /etc/lxc/vm01`

	
  9. `vim /etc/lxc/vm01/conf`





[sourcecode]
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
{% endhighlight %}







	
  10. `vim /etc/lxc/vm01/fstab`





[sourcecode]
devpts /srv/lxc/vm01/debootstrapped/dev/pts devpts defaults 0 0
proc /srv/lxc/vm01/debootstrapped/proc    proc   defaults 0 0
sysfs /srv/lxc/vm01/debootstrapped/sys     sysfs  defaults 0 0
none /srv/lxc/vm01/debootstrapped/dev/shm tmpfs  defaults 0 0
{% endhighlight %}







	
  11. Install base system





[sourcecode]
debootstrap --variant=minbase --include=dhcp-client,dialog,ifupdown,iproute,libui-dialog-perl,locales,netbase,net-tools,openssh-server,vim,curl,git-core squeeze /srv/lxc/vm01/ http://cdn.debian.net/debian/
{% endhighlight %}







	
  12. `/usr/sbin/chroot /srv/lxc/vm01 /usr/bin/passwd -d root`

	
  13. `echo vm01 > /srv/lxc/vm01/etc/hostname`

	
  14. `vim /srv/lxc/vm01/etc/inittab`





[sourcecode]
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
{% endhighlight %}







	
  15. `vim /srv/lxc/vm01/etc/init.d/hwclockfirst.sh`





[sourcecode]
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
{% endhighlight %}







	
  16. `vim /srv/lxc/vm01/etc/init.d/hwclock.sh`





[sourcecode]
#!/bin/sh
### BEGIN INIT INFO
# Provides:          hwclock
# Required-Start:    checkroot
# Required-Stop:     $local_fs
# Default-Start:     S
# Default-Stop:      0 6
### END INIT INFO
exit 0
{% endhighlight %}







	
  17. `>/etc/lxc/vm01/log`

	
  18. `lxc-start -n vm01 -f /etc/lxc/vm01/conf -o /etc/lxc/vm01/log --logpriority INFO`



