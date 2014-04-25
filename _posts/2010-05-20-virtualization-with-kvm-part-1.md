---
layout: post
title: Virtualization with KVM (Part 1)
categories: []
tags: []
status: pending
type: post
published: false
meta: {}
author: 
---
<p>So <a href="http://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine">Kernel-based Virtual Machine (KVM)</a> is something <em>everybody wants to use</em>(TM). Let's define a (not so) small private project to make it useful. Since XEN will never (and should never - IMHO) be in the mainline kernel, let's do some KVM!</p>
<p>First of our final requirements (in random order):</p>
<ul>
<li>Get Started! Do the basic setup, verify we have KVM working</li>
<li>Automated Guest Installations from the direct physical host</li>
<li>Offer IPv4 connectivity over public IPs to  guest machines</li>
<li>Offer IPv6 and IPv4 connectivity to guest machines</li>
<li>Offer IPv6 as the only connectivity to guest machines</li>
<li>Automagically create new guests with a single command</li>
</ul>
<p>Since my private resources are limited this will run on a <a href="http://www.hetzner.de/">hosting provider</a>. The initial "problem" with this is their network setup, it will however not be a problem when diving deeper once this is set up.</p>
<h1>Network Configuration</h1>
<h2>Bridging the Gap</h2>
<p>The host will be running Debian/Squeeze and what you get after installing is this:</p>
<p>[sourcecode language="text"]<br />
# Loopback device:<br />
auto lo<br />
iface lo inet loopback</p>
<p># device: eth0<br />
auto  eth0<br />
    iface eth0 inet static<br />
    address 192.0.2.195<br />
    broadcast 192.0.2.255<br />
    netmask 255.255.255.192<br />
    gateway 192.0.2.193<br />
    default route to access subnet</p>
<p># default route to access subnet<br />
up route add -net 192.0.2.192 netmask 255.255.255.192 gw 192.0.2.193 br0<br />
[/sourcecode]</p>
<p>Let's make a bridge which will later on be used to route the traffic from our guests to the world:</p>
<p>[sourcecode language="text"]<br />
# Loopback device:<br />
auto lo<br />
iface lo inet loopback</p>
<p>## device: br0<br />
auto br0<br />
iface br0 inet static<br />
    bridge_ports eth0 dummy0<br />
    bridge_maxwait 2<br />
    address 192.0.2.195<br />
    netmask 255.255.255.192<br />
    gateway   192.0.2.193</p>
<p># default route to access subnet<br />
up route add -net 192.0.2.192 netmask 255.255.255.192 gw 192.0.2.193 eth0<br />
[/sourcecode]</p>
<p>Let's look at the output of <tt>iproute2</tt> now.</p>
<p>[sourcecode language="text"]<br />
$ ip link list<br />
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 16436 qdisc noqueue state UNKNOWN<br />
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00<br />
2: eth0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000<br />
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff<br />
3: br0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue state UNKNOWN<br />
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff<br />
4: dummy0: &lt;BROADCAST,NOARP,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue state UNKNOWN<br />
    link/ether 92:0e:c3:fe:5f:ae brd ff:ff:ff:ff:ff:ff<br />
[/sourcecode]</p>
<p>All nice and fine, we have a <tt>br0</tt> interface <tt>eth0</tt> and <tt>dummy0</tt>. What about the assigned addresses?</p>
<p>[sourcecode language="text"]<br />
$ ip address list<br />
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 16436 qdisc noqueue state UNKNOWN<br />
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00<br />
    inet 127.0.0.1/8 scope host lo<br />
    inet6 ::1/128 scope host<br />
       valid_lft forever preferred_lft forever<br />
2: eth0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000<br />
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff<br />
    inet6 fe80::224:21ff:feb4:3626/64 scope link<br />
       valid_lft forever preferred_lft forever<br />
3: br0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue state UNKNOWN<br />
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff<br />
    inet 192.0.2.195/26 brd 188.40.110.255 scope global br0<br />
    inet6 fe80::224:21ff:feb4:3626/64 scope link<br />
       valid_lft forever preferred_lft forever<br />
4: dummy0: &lt;BROADCAST,NOARP,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue state UNKNOWN<br />
    link/ether 92:0e:c3:fe:5f:ae brd ff:ff:ff:ff:ff:ff<br />
    inet6 fe80::900e:c3ff:fefe:5fae/64 scope link<br />
       valid_lft forever preferred_lft forever<br />
[/sourcecode]</p>
<p>All nice and fine, <tt>br0</tt> has the IP configured <tt>eth0</tt> and <tt>dummy0</tt> don't have an IPv4 address. This looks quite good. Let's see how the routing table works:</p>
<p>[sourcecode language="text"]<br />
$ ip route list<br />
192.0.2.192/26 dev br0  proto kernel  scope link  src 192.0.2.195<br />
default via 192.0.2.193 dev br0<br />
[/sourcecode]</p>
<p>This doesn't look so good. In the <tt>/etc/network/interfaces</tt> file we told debian to route thru <tt>eth0</tt> but ended up routing thru <tt>br0</tt> what happened?</p>
<p>Actually nothing too serious. Our Linux kernel knows that <tt>eth0</tt> doesn't have an address and thus uses <tt>br0</tt> instead. Which actually is what whe told it to do in the definition of <tt>iface br0 inet static</tt>. What about our bridge config?</p>
<p>[sourcecode language="text"]<br />
$ sudo brctl show<br />
[sudo] password for sysmaint:<br />
bridge name	bridge id		STP enabled	interfaces<br />
br0		8000.002421b43626	no		    dummy0<br />
                                                              eth0<br />
[/sourcecode]</p>
<p>[sourcecode language="text"]<br />
$ sudo brctl showmacs br0<br />
port no	mac addr		        is local?	ageing timer<br />
  1	        00:23:9c:17:34:23	no		   0.00<br />
  1	        00:24:21:b4:36:26	yes		   0.00<br />
  2	        92:0e:c3:fe:5f:ae	yes		   0.00<br />
[/sourcecode]</p>
<p>All nice and fine, our bridge is here, and has the members we defined.</p>
<h1>Virtualize!</h1>
<p>It's time to run our first virtualized machine. For testing purposes we'll simply install Debian/Stable with the default network config that KVM uses. It has nothing to do with the bridge setup since it uses an internal DHCP server and NAT services. So here are the ToDos:</p>
<ol>
<li>Create the image</li>
<li>Run the guest</li>
<li>Install Debian/Stable to verify we have connectivity</li>
</ol>
<p>[sourcecode language="text"]<br />
$ qemu-img create test.img 10G<br />
[/sourcecode]</p>
<p>[sourcecode language="text"]<br />
sudo /usr/bin/kvm \<br />
    -k en \<br />
    -name test \<br />
    -boot order=cd,once=d \<br />
    -drive file=$HOME/test.img,if=virtio,format=raw,media=disk \<br />
    -drive file=$HOME/debian-504-amd64-netinst.iso,if=ide,media=cdrom \<br />
    -usbdevice tablet \<br />
    -watchdog i6300esb \<br />
    -m 1024 \<br />
    -vnc :1 \<br />
    -balloon virtio \<br />
    -pidfile /var/run/kvm.test<br />
[/sourcecode]</p>
<p>The command above does the following:</p>
<ul>
<li>Tell KVM to use the english keymap</li>
<li>Name the guest test</li>
<li>Define a boot order of: disk,cdrom; but on the first boot use cdrom</li>
<li>Define a hard disk image, it's location and tell it to use the virtualized IO</li>
<li>Define a cdrom disk image, it's location and tell it to use the IDE IO</li>
<li>Set up a USB Device so that the SDL interaction VNC works more smoothly</li>
<li>Provide a watchdog hardware device</li>
<li>Provide 1024MiB of memory</li>
<li>Start a VNC Server on display one (port 5901)</li>
<li>Use the balloon driver</li>
<li>Tell KVM to create a PID file</li>
</ul>
<p>When this is running just fire up a VNC Viewer and connect to the host</p>
<p>[sourcecode language="text"]<br />
$ vncviewer 192.2.0.195:1<br />
[/sourcecode]</p>
<p>If you have your Debian ISO image in the correct place you should be presented with the boot screen of the Debian ISO image. Just click thru and install. Since we used the netinst ISO image a successful installation means you have basic connectivity to the outside world.</p>
<p>In the next installment we'll further refine this to provide a DHCP and TFTP server thru the user mode networking so that we can automagically install our guests without further interaction.</p>
<p>This is our status as of now:</p>
<ul>
<li><del datetime="2010-05-20T11:11:42+00:00">Get Started! Do the basic setup, verify we have KVM working</del></li>
<li>Automated Guest Installations from the direct physical host</li>
<li>Offer IPv4 connectivity over public IPs to  guest machines</li>
<li>Offer IPv6 and IPv4 connectivity to guest machines</li>
<li>Offer IPv6 as the only connectivity to guest machines</li>
<li>Automagically create new guests with a single command</li>
</ul>
