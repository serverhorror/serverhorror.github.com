---
layout: post
title: Offer IPv4 connectivity over public IPs to  guest machines - (Virtualization
  with KVM - Part 3)
categories: []
tags:
- sysadmin
status: pending
type: post
published: false
meta: {}
author: 
---
<ul>
<li><del datetime="2010-05-20T11:11:42+00:00"><a href="http://blog.serverhorror.com/2010/05/20/virtualization-with-kvm-part-1/">Get Started! Do the basic setup, verify we have KVM working</a></del></li>
<li><del datetime="2010-06-06T19:41:49+00:00"><a href="http://blog.serverhorror.com/2010/06/06/fully-automated-installations-with-debian-virtualization-with-kvm-part-2">Automated Guest Installations from the direct physical host</a></del></li>
<li><strong>Offer IPv4 connectivity over public IPs to  guest machines</strong></li>
<li>Offer IPv6 and IPv4 connectivity to guest machines</li>
<li>Offer IPv6 as the only connectivity to guest machines</li>
<li>Automagically create new guests with a single command</li>
</ul>
<p>Did you follow closely <a href="http://blog.serverhorror.com/2010/05/20/virtualization-with-kvm-part-1/">the last</a> <a href="http://blog.serverhorror.com/2010/06/06/fully-automated-installations-with-debian-virtualization-with-kvm-part-2">two posts</a>?</p>
<p>If you did so, consider yourself lucky. All we need to do is add two files to our setup. OK I'll admit it I'm lying! Still in essence FAI provides us with the possibility of just creating a single template file and a really short script to deploy a shiny new host with a <del datetime="2010-06-15T20:39:21+00:00">public</del> globally routable IPv4 address</p>
<p>So here's the plan:</p>
<ul>
<li>fine tune the network setup to
<ul>
<li>provide an internal (private) network interface to PXE boot from</li>
<li>provide an external (<del datetime="2010-06-15T20:39:21+00:00">public</del> globally routable) network interface to provide a public IP</li>
</ul>
</li>
<li>create the "template file" in the FAI config space</li>
<li>redeploy</li>
<li>enjoy the public IP</li>
</ul>
<p>Let's fine tune!</p>
<p>First a bit of host network setup, add the following stanza to your <tt>/etc/network/interfaces</tt>:</p>
<pre>auto pxebr0
iface pxebr0 inet static
    bridge_maxwait 2
    # up brctl addbr $IFACE
    address 172.16.0.1
    netmask 255.255.0.0</pre>
<p>and modify the <tt>br0</tt> stanza:</p>
<pre>## device: br0
auto br0
iface br0 inet static
    bridge_ports eth0
    bridge_maxwait 2
    address 192.0.2.2
    netmask 255.255.255.0
    gateway   192.0.2.1</pre>
<p>Now for the only file we actually need to update<br />
<strong><tt>/srv/fai/config/file/etc/network/interfaces/demohost</tt></strong>:</p>
<pre># Loopback device:
auto lo
iface lo inet loopback

## device: eth1
auto  eth1
iface eth1 inet static
  address   192.0.2.3
  netmask   255.255.255.0
  gateway   192.0.2.1</pre>
<p>And the script FAI will use during the installation process<br />
<strong><tt>/srv/fai/config/scripts/demohost/30-interfaces</tt></strong>:</p>
<pre>#! /bin/bash

fcopy -i /etc/resolv.conf
fcopy -iM /etc/network/interfaces /etc/networks
fcopy -iM /etc/network/interfaces</pre>
<p>and <tt>sudo ifdown pxebr0; sudo ifdown br0; sudo ifup pxebr0; sudo ifup br0</tt>. Then expand our <tt>kvm</tt>-command to this:</p>
<pre>NAME="demohost.serverhorror.com"
ETH0_MAC="06:00:06:62:d3:2d"
ETH1_MAC="06:00:06:5b:51:c1"
MEMORY="1024"
VDA="${HOME}/test.img"

sudo /usr/bin/kvm -k en-us \
    -name $NAME \
    -boot order=cn \
    -drive file=$VDA,if=virtio,format=raw,media=disk,boot=on \
    -net nic,macaddr=$ETH0_MAC,vlan=0 -net tap,vlan=0,name=eth0,ifname=pxetap0,script=no,downscript=no \
    -net nic,macaddr=$ETH1_MAC,vlan=1 -net tap,vlan=1,name=eth1,ifname=pubtap0,script=no,downscript=no \
    -usbdevice tablet -watchdog i6300esb \
    -m $MEMORY \
    -vnc none \
    -balloon virtio \
    -pidfile /var/run/$NAME.pid \
    -monitor stdio \
    -S</pre>
<p><strong>Also do not forget to update your host definitions in dhcpd.conf to use the new ethernet address for the fixed-host definition(s)</strong><br />
So what happens here?</p>
<ul>
<li>Define 2 Network interfaces
<ul>
<li>pxetap0 to PXE boot from FAI (eth0 in the guest)</li>
<li>pubtap0 to provide the <del datetime="2010-06-15T20:43:53+00:00">public</del> globally routable address (eth1 in the guest)</li>
</ul>
</li>
<li>"boot" the guest in a stopped state (the <tt>-S</tt>) so we have enough time to set some things up before actually booting</li>
<li>disable vnc by default</li>
</ul>
<p>After you ran the command open up another terminal and bring the interfaces and routes up.</p>
<pre>sudo brctl addif pxebr0 pxetap0
sudo ip link set dev pxetap0 up
sudo ip route add 172.16.0.0/16 dev pxebr0</pre>
<pre>sudo brctl addif br0 pubtap0
sudo ip link set dev pubtap0 up
sudo ip route add 192.0.2.3 dev br0</pre>
<p>Let's set up the options to boot the way we intend to and actually continue the guest process (<strong><tt>c</tt></strong>)</p>
<pre>QEMU 0.12.4 monitor - type 'help' for more information
(qemu) change vnc password
Password: ****
(qemu) change vnc :1
(qemu) boot_set n
boot device list now set to n
(qemu) c</pre>
<p>Now sit back and relax. If you got everything right you should be able to</p>
<ul>
<li>PXE boot</li>
<li>enjoy the FAI installation process</li>
<li>spot the place where the <tt>demohost</tt> class copies the new <tt>/etc/network/interfaces</tt> file</li>
<li>hit enter</li>
<li>watch your guest reboot</li>
<li>enjoy a <del datetime="2010-06-15T21:24:04+00:00">public</del> globally routable IPv4 address</li>
</ul>
<p>So where are we now:</p>
<ul>
<li><del datetime="2010-05-20T11:11:42+00:00"><a href="http://blog.serverhorror.com/2010/05/20/virtualization-with-kvm-part-1/">Get Started! Do the basic setup, verify we have KVM working</a></del></li>
<li><del datetime="2010-06-06T19:41:49+00:00"><a href="http://blog.serverhorror.com/2010/06/06/fully-automated-installations-with-debian-virtualization-with-kvm-part-2">Automated Guest Installations from the direct physical host</a></del></li>
<li><del datetime="2010-06-15T21:27:11+00:00">Offer IPv4 connectivity over public IPs to  guest machines</del></li>
<li>Offer IPv6 and IPv4 connectivity to guest machines</li>
<li>Offer IPv6 as the only connectivity to guest machines</li>
<li>Automagically create new guests with a single command</li>
</ul>
