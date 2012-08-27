---
comments: true
date: 2009-11-24 15:50:48
layout: post
slug: howto-create-an-opensolaris-zone
title: 'HowTo: Create an OpenSolaris Zone'
wordpress_id: 509
tags:
- sysadmin
---

[digg=http://digg.com/linux_unix/HowTo_Create_an_OpenSolaris_Zone_ServerHorror]

OK this is my first encounter with OpenSolaris Zones, so take all off the following with a grain of salt.

To make it (hopefully) easy to destroy the zone we create a ZFS Filesystem which will hold all of our zones:

[sourcecode langauage="bash"]
pfexec zfs create rpool/zones
pfexec umount /rpool/zones/
pfexec zfs set mountpoint=/zones rpool/zones
pfexec zfs mount rpool/zones
pfexec chmod 0700 /zones/ # Necessary so that a later &quot;verify&quot; doesn't complain...
[/sourcecode]


Great we have a file system to hold our zones, now let's configure a new zone:

[sourcecode langauage="text"]
pfexec zonecfg -z testzone
zonecfg:testzone&gt; create
zonecfg:testzone&gt; commit
zonepath cannot be empty.
Zone testzone failed to verify
testzone: Required resource missing
[sourcecode]
Uh Oh, we failed miserably. So let's set a path where the zone will be living:
[sourcecode langauage=&quot;text&quot;]
zonecfg:testzone&gt; set zonepath=/zones/testzone
zonecfg:testzone&gt; commit
zonecfg:testzone&gt; verify
zonecfg:testzone&gt; end
The end command only makes sense in the resource scope.
zonecfg:testzone&gt;
[/sourcecode]


Looks all nice and fine, let's verify again:

[sourcecode langauage="text"]
$ pfexec zoneadm -z testzone verify
WARNING: /zones/testzone does not exist, so it could not be verified.
When 'zoneadm install' is run, 'install' will try to create
/zones/testzone, and 'verify' will be tried again,
but the 'verify' may fail if:
the parent directory of /zones/testzone is group- or other-writable
or
/zones/testzone overlaps with any other installed zones.
[/sourcecode]


Still some things to do.

[sourcecode langauage="text"]
$pfexec mkdir -p /zones/testzone
$ pfexec zoneadm -z testzone verify
/zones/testzone must not be group readable.
/zones/testzone must not be group executable.
/zones/testzone must not be world readable.
/zones/testzone must not be world executable.
could not verify zonepath /zones/testzone because of the above errors.
zoneadm: zone testzone failed to verify
$ pfexec chmod 0700 /zones/testzone
[/sourcecode]


This looks a lot better now let's install the zone. **Note: We just configured the zone, we didn't yet install it**. So let's start the installation:

[sourcecode langauage="text"]
$ pfexec zoneadm -z testzone  install
A ZFS file system has been created for this zone.
 Publisher: Using opensolaris.org (http://pkg.opensolaris.org/release/).
 Image: Preparing at /zones/testzone/root.
 Cache: Using /var/pkg/download.
Sanity Check: Looking for 'entire' incorporation.
 Installing: Core System (output follows)
DOWNLOAD                                    PKGS       FILES     XFER (MB)
Completed                                  20/20   3021/3021   42.55/42.55

PHASE                                        ACTIONS
Install Phase                              5747/5747
 Installing: Additional Packages (output follows)
DOWNLOAD                                    PKGS       FILES     XFER (MB)
Completed                                  37/37   5598/5598   32.52/32.52

PHASE                                        ACTIONS
Install Phase                              7329/7329

 Note: Man pages can be obtained by installing SUNWman
 Postinstall: Copying SMF seed repository ... done.
 Postinstall: Applying workarounds.
 Done: Installation completed in 2879.333 seconds.

 Next Steps: Boot the zone, then log into the zone console
 (zlogin -C) to complete the configuration process
[/sourcecode]


Looks nice. Even some more instructions. So let's boot the zone:

[sourcecode langauage="text"]
$ pfexec zoneadm -z testzone  boot
[/sourcecode]

All nice and fine, let's try to use the zone (You can escape from this by using "~." - that's a tilde and a dot - just hit "ENTER~."):

[sourcecode langauage="text"]
$ pfexec zlogin -C testzone
[Connected to zone 'testzone' console]
You did not enter a selection.
What type of terminal are you using?
 1) ANSI Standard CRT
2) DEC VT100
3) PC Console
4) Sun Command Tool
5) Sun Workstation
6) X Terminal Emulator (xterms)
7) Other
Type the number of your choice and press Return: 6

Creating new rsa public/private host key pair
Creating new dsa public/private host key pair
[/sourcecode]


Shock! There's some curses (or whatever OpenSolaris uses) interface popping up! It will ask about hostname, time zone and root password. Enter the gritty details and try ESC-2 if it doesn't continue with F2 (I chose "X Terminal Emulator (xterms)" - seems to be a bad choice).

[sourcecode langauage="text"]
Configuring network interface addresses:.
System identification is completed.

testzone.local console login: root
Password:
Nov 24 07:40:41 testzone.local login: ROOT LOGIN /dev/console
Sun Microsystems Inc.   SunOS 5.11      snv_111b        November 2008
root@testzone.local:~# uptime
 7:40am  up 5 min(s),  1 user,  load average: 0.17, 0.18, 0.18
root@testzone.local:~# ifconfig -a
lo0:1: flags=2001000849&lt;UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL&gt; mtu 8232 index 1
 inet 127.0.0.1 netmask ff000000
lo0:1: flags=2002000849&lt;UP,LOOPBACK,RUNNING,MULTICAST,IPv6,VIRTUAL&gt; mtu 8252 index 1
 inet6 ::1/128
root@testzone.local:~# netstat -f tcp -an
tcp: unknown address family.
root@testzone.local:~# netstat -f inet -an

UDP: IPv4
 Local Address        Remote Address      State
-------------------- -------------------- ----------
 *.111                               Idle
 *.*                                 Unbound
 *.64049                             Idle
 *.111                               Idle
 *.*                                 Unbound
 *.38336                             Idle

TCP: IPv4
 Local Address        Remote Address    Swind Send-Q Rwind Recv-Q    State
-------------------- -------------------- ----- ------ ----- ------ -----------
 *.111                *.*                0      0 49152      0 LISTEN
 *.*                  *.*                0      0 49152      0 IDLE
 *.111                *.*                0      0 49152      0 LISTEN
 *.*                  *.*                0      0 49152      0 IDLE
 *.22                 *.*                0      0 49152      0 LISTEN
root@testzone.local:~# pkg search telnet
pkg: Some servers failed to respond appropriately:
 http://pkg.opensolaris.org/release/: node name or service name not known
[/sourcecode]


Again to escape from the zlogin stuff hit: "ENTER~." - that's ENTER, tide, dot.

Very nice so far. We have uptime, a hostname and an IP Address, well kind of :). Stay tuned for when I try to get network connectivity, which will hopefully be in the not too distant future.

A few minor notes on other tools that could be usefull:

Installing took quite a while on my system, since I could do some work in parallel I didn't investigate. But I found the following command nice to see the status:

[sourcecode langauage="text"]
$ zoneadm -z testzone list -v
 ID NAME             STATUS     PATH                           BRAND    IP
 - testzone         incomplete /zones/testzone                ipkg     shared
[/sourcecode]


So let's set up a nice terminal that watches the STATUS of our zone (the incomplete will go away as soon as the installation is finished). Of course we could watch the original terminal simply returning, but that would be kind of boring - wouldn't it?

[sourcecode langauage="text"]
$ while true; do clear;zoneadm -z testzone list -v; zoneadm list -iv;sleep .8; done
[/sourcecode]


Also the state of the zone after booting it:

[sourcecode langauage="text"]
$ zoneadm -z testzone list -v
ID NAME             STATUS     PATH                           BRAND    IP
1 testzone         running    /zones/testzone                ipkg     shared
[/sourcecode]


Shutting the zone down cleanly:

[sourcecode langauage="text"]
$ pfexec zlogin testzone shutdown # from the outside
# shutdown -y -i 0 # from inside the zone
[/sourcecode]


Then looks like this:

[sourcecode langauage="text"]
$ zoneadm -z testzone list -v
ID NAME             STATUS     PATH                           BRAND    IP
- testzone         installed  /zones/testzone                ipkg     shared
[/sourcecode]


Happy working with your zone.
