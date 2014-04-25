---
layout: post
title: 'HowTo: Create an OpenSolaris Zone'
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1270824422";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1295290319";}
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
<p>[digg=http://digg.com/linux_unix/HowTo_Create_an_OpenSolaris_Zone_ServerHorror]</p>
<p>OK this is my first encounter with OpenSolaris Zones, so take all off the following with a grain of salt.</p>
<p>To make it (hopefully) easy to destroy the zone we create a ZFS Filesystem which will hold all of our zones:</p>
<p>{% highlight text %}<br />
pfexec zfs create rpool/zones<br />
pfexec umount /rpool/zones/<br />
pfexec zfs set mountpoint=/zones rpool/zones<br />
pfexec zfs mount rpool/zones<br />
pfexec chmod 0700 /zones/ # Necessary so that a later &amp;quot;verify&amp;quot; doesn't complain...<br />
{% endhighlight %}</p>
<p>Great we have a file system to hold our zones, now let's configure a new zone:</p>
<p>{% highlight text %}<br />
pfexec zonecfg -z testzone<br />
zonecfg:testzone&amp;gt; create<br />
zonecfg:testzone&amp;gt; commit<br />
zonepath cannot be empty.<br />
Zone testzone failed to verify<br />
testzone: Required resource missing<br />
{% endhighlight text %}<br />
Uh Oh, we failed miserably. So let's set a path where the zone will be living:<br />
{% highlight text %}
zonecfg:testzone&amp;gt; set zonepath=/zones/testzone<br />
zonecfg:testzone&amp;gt; commit<br />
zonecfg:testzone&amp;gt; verify<br />
zonecfg:testzone&amp;gt; end<br />
The end command only makes sense in the resource scope.<br />
zonecfg:testzone&amp;gt;<br />
{% endhighlight %}</p>
<p>Looks all nice and fine, let's verify again:</p>
<p>{% highlight text %}<br />
$ pfexec zoneadm -z testzone verify<br />
WARNING: /zones/testzone does not exist, so it could not be verified.<br />
When 'zoneadm install' is run, 'install' will try to create<br />
/zones/testzone, and 'verify' will be tried again,<br />
but the 'verify' may fail if:<br />
the parent directory of /zones/testzone is group- or other-writable<br />
or<br />
/zones/testzone overlaps with any other installed zones.<br />
{% endhighlight %}</p>
<p>Still some things to do.</p>
<p>{% highlight text %}<br />
$pfexec mkdir -p /zones/testzone<br />
$ pfexec zoneadm -z testzone verify<br />
/zones/testzone must not be group readable.<br />
/zones/testzone must not be group executable.<br />
/zones/testzone must not be world readable.<br />
/zones/testzone must not be world executable.<br />
could not verify zonepath /zones/testzone because of the above errors.<br />
zoneadm: zone testzone failed to verify<br />
$ pfexec chmod 0700 /zones/testzone<br />
{% endhighlight %}</p>
<p>This looks a lot better now let's install the zone. <strong>Note: We just configured the zone, we didn't yet install it</strong>. So let's start the installation:</p>
<p>{% highlight text %}<br />
$ pfexec zoneadm -z testzone  install<br />
A ZFS file system has been created for this zone.<br />
 Publisher: Using opensolaris.org (http://pkg.opensolaris.org/release/).<br />
 Image: Preparing at /zones/testzone/root.<br />
 Cache: Using /var/pkg/download.<br />
Sanity Check: Looking for 'entire' incorporation.<br />
 Installing: Core System (output follows)<br />
DOWNLOAD                                    PKGS       FILES     XFER (MB)<br />
Completed                                  20/20   3021/3021   42.55/42.55</p>
<p>PHASE                                        ACTIONS<br />
Install Phase                              5747/5747<br />
 Installing: Additional Packages (output follows)<br />
DOWNLOAD                                    PKGS       FILES     XFER (MB)<br />
Completed                                  37/37   5598/5598   32.52/32.52</p>
<p>PHASE                                        ACTIONS<br />
Install Phase                              7329/7329</p>
<p> Note: Man pages can be obtained by installing SUNWman<br />
 Postinstall: Copying SMF seed repository ... done.<br />
 Postinstall: Applying workarounds.<br />
 Done: Installation completed in 2879.333 seconds.</p>
<p> Next Steps: Boot the zone, then log into the zone console<br />
 (zlogin -C) to complete the configuration process<br />
{% endhighlight %}</p>
<p>Looks nice. Even some more instructions. So let's boot the zone:</p>
<p>{% highlight text %}<br />
$ pfexec zoneadm -z testzone  boot<br />
{% endhighlight %}</p>
<p>All nice and fine, let's try to use the zone (You can escape from this by using "~." - that's a tilde and a dot - just hit "ENTER~."):</p>
<p>{% highlight text %}<br />
$ pfexec zlogin -C testzone<br />
[Connected to zone 'testzone' console]<br />
You did not enter a selection.<br />
What type of terminal are you using?<br />
 1) ANSI Standard CRT<br />
2) DEC VT100<br />
3) PC Console<br />
4) Sun Command Tool<br />
5) Sun Workstation<br />
6) X Terminal Emulator (xterms)<br />
7) Other<br />
Type the number of your choice and press Return: 6</p>
<p>Creating new rsa public/private host key pair<br />
Creating new dsa public/private host key pair<br />
{% endhighlight %}</p>
<p>Shock! There's some curses (or whatever OpenSolaris uses) interface popping up! It will ask about hostname, time zone and root password. Enter the gritty details and try ESC-2 if it doesn't continue with F2 (I chose "X Terminal Emulator (xterms)" - seems to be a bad choice).</p>
<p>{% highlight text %}<br />
Configuring network interface addresses:.<br />
System identification is completed.</p>
<p>testzone.local console login: root<br />
Password:<br />
Nov 24 07:40:41 testzone.local login: ROOT LOGIN /dev/console<br />
Sun Microsystems Inc.   SunOS 5.11      snv_111b        November 2008<br />
root@testzone.local:~# uptime<br />
 7:40am  up 5 min(s),  1 user,  load average: 0.17, 0.18, 0.18<br />
root@testzone.local:~# ifconfig -a<br />
lo0:1: flags=2001000849&amp;lt;UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL&amp;gt; mtu 8232 index 1<br />
 inet 127.0.0.1 netmask ff000000<br />
lo0:1: flags=2002000849&amp;lt;UP,LOOPBACK,RUNNING,MULTICAST,IPv6,VIRTUAL&amp;gt; mtu 8252 index 1<br />
 inet6 ::1/128<br />
root@testzone.local:~# netstat -f tcp -an<br />
tcp: unknown address family.<br />
root@testzone.local:~# netstat -f inet -an</p>
<p>UDP: IPv4<br />
 Local Address        Remote Address      State<br />
-------------------- -------------------- ----------<br />
 *.111                               Idle<br />
 *.*                                 Unbound<br />
 *.64049                             Idle<br />
 *.111                               Idle<br />
 *.*                                 Unbound<br />
 *.38336                             Idle</p>
<p>TCP: IPv4<br />
 Local Address        Remote Address    Swind Send-Q Rwind Recv-Q    State<br />
-------------------- -------------------- ----- ------ ----- ------ -----------<br />
 *.111                *.*                0      0 49152      0 LISTEN<br />
 *.*                  *.*                0      0 49152      0 IDLE<br />
 *.111                *.*                0      0 49152      0 LISTEN<br />
 *.*                  *.*                0      0 49152      0 IDLE<br />
 *.22                 *.*                0      0 49152      0 LISTEN<br />
root@testzone.local:~# pkg search telnet<br />
pkg: Some servers failed to respond appropriately:<br />
 http://pkg.opensolaris.org/release/: node name or service name not known<br />
{% endhighlight %}</p>
<p>Again to escape from the zlogin stuff hit: "ENTER~." - that's ENTER, tide, dot.</p>
<p>Very nice so far. We have uptime, a hostname and an IP Address, well kind of :). Stay tuned for when I try to get network connectivity, which will hopefully be in the not too distant future.</p>
<p>A few minor notes on other tools that could be usefull:</p>
<p>Installing took quite a while on my system, since I could do some work in parallel I didn't investigate. But I found the following command nice to see the status:</p>
<p>{% highlight text %}<br />
$ zoneadm -z testzone list -v<br />
 ID NAME             STATUS     PATH                           BRAND    IP<br />
 - testzone         incomplete /zones/testzone                ipkg     shared<br />
{% endhighlight %}</p>
<p>So let's set up a nice terminal that watches the STATUS of our zone (the incomplete will go away as soon as the installation is finished). Of course we could watch the original terminal simply returning, but that would be kind of boring - wouldn't it?</p>
<p>{% highlight text %}<br />
$ while true; do clear;zoneadm -z testzone list -v; zoneadm list -iv;sleep .8; done<br />
{% endhighlight %}</p>
<p>Also the state of the zone after booting it:</p>
<p>{% highlight text %}<br />
$ zoneadm -z testzone list -v<br />
ID NAME             STATUS     PATH                           BRAND    IP<br />
1 testzone         running    /zones/testzone                ipkg     shared<br />
{% endhighlight %}</p>
<p>Shutting the zone down cleanly:</p>
<p>{% highlight text %}<br />
$ pfexec zlogin testzone shutdown # from the outside<br />
# shutdown -y -i 0 # from inside the zone<br />
{% endhighlight %}</p>
<p>Then looks like this:</p>
<p>{% highlight text %}<br />
$ zoneadm -z testzone list -v<br />
ID NAME             STATUS     PATH                           BRAND    IP<br />
- testzone         installed  /zones/testzone                ipkg     shared<br />
{% endhighlight %}</p>
<p>Happy working with your zone.</p>
