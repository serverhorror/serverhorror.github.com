---
comments: true
date: 2010-05-20 12:00:40
layout: post
published: true
slug: virtualization-with-kvm-part-1
title: Virtualization with KVM (Part 1)
wordpress_id: 739
---

So [Kernel-based Virtual Machine (KVM)](http://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine) is something _everybody wants to use_(TM). Let's define a (not so) small private project to make it useful. Since XEN will never (and should never - IMHO) be in the mainline kernel, let's do some KVM!

First of our final requirements (in random order):



	
  * Get Started! Do the basic setup, verify we have KVM working

	
  * Automated Guest Installations from the direct physical host

	
  * Offer IPv4 connectivity over public IPs to  guest machines

	
  * Offer IPv6 and IPv4 connectivity to guest machines

	
  * Offer IPv6 as the only connectivity to guest machines

	
  * Automagically create new guests with a single command


Since my private resources are limited this will run on a [hosting provider](http://www.hetzner.de/). The initial "problem" with this is their network setup, it will however not be a problem when diving deeper once this is set up.


# Network Configuration




## Bridging the Gap


The host will be running Debian/Squeeze and what you get after installing is this:

{% highlight text %}
# Loopback device:
auto lo
iface lo inet loopback

# device: eth0
auto  eth0
    iface eth0 inet static
    address 192.0.2.195
    broadcast 192.0.2.255
    netmask 255.255.255.192
    gateway 192.0.2.193
    default route to access subnet

# default route to access subnet
up route add -net 192.0.2.192 netmask 255.255.255.192 gw 192.0.2.193 br0
{% endhighlight %}

Let's make a bridge which will later on be used to route the traffic from our guests to the world:

{% highlight text %}
# Loopback device:
auto lo
iface lo inet loopback

## device: br0
auto br0
iface br0 inet static
    bridge_ports eth0 dummy0
    bridge_maxwait 2
    address 192.0.2.195
    netmask 255.255.255.192
    gateway   192.0.2.193

# default route to access subnet
up route add -net 192.0.2.192 netmask 255.255.255.192 gw 192.0.2.193 eth0
{% endhighlight %}

Let's look at the output of iproute2 now.

{% highlight text %}
$ ip link list
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff
3: br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff
4: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN
    link/ether 92:0e:c3:fe:5f:ae brd ff:ff:ff:ff:ff:ff
{% endhighlight %}

All nice and fine, we have a br0 interface eth0 and dummy0. What about the assigned addresses?

{% highlight text %}
$ ip address list
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::224:21ff:feb4:3626/64 scope link
       valid_lft forever preferred_lft forever
3: br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN
    link/ether 00:24:21:b4:36:26 brd ff:ff:ff:ff:ff:ff
    inet 192.0.2.195/26 brd 188.40.110.255 scope global br0
    inet6 fe80::224:21ff:feb4:3626/64 scope link
       valid_lft forever preferred_lft forever
4: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN
    link/ether 92:0e:c3:fe:5f:ae brd ff:ff:ff:ff:ff:ff
    inet6 fe80::900e:c3ff:fefe:5fae/64 scope link
       valid_lft forever preferred_lft forever
{% endhighlight %}

All nice and fine, br0 has the IP configured eth0 and dummy0 don't have an IPv4 address. This looks quite good. Let's see how the routing table works:

{% highlight text %}
$ ip route list
192.0.2.192/26 dev br0  proto kernel  scope link  src 192.0.2.195
default via 192.0.2.193 dev br0
{% endhighlight %}

This doesn't look so good. In the /etc/network/interfaces file we told debian to route thru eth0 but ended up routing thru br0 what happened?

Actually nothing too serious. Our Linux kernel knows that eth0 doesn't have an address and thus uses br0 instead. Which actually is what whe told it to do in the definition of iface br0 inet static. What about our bridge config?

{% highlight text %}
$ sudo brctl show
[sudo] password for sysmaint:
bridge name	bridge id		STP enabled	interfaces
br0		8000.002421b43626	no		    dummy0
                                                              eth0
{% endhighlight %}

{% highlight text %}
$ sudo brctl showmacs br0
port no	mac addr		        is local?	ageing timer
  1	        00:23:9c:17:34:23	no		   0.00
  1	        00:24:21:b4:36:26	yes		   0.00
  2	        92:0e:c3:fe:5f:ae	yes		   0.00
{% endhighlight %}

All nice and fine, our bridge is here, and has the members we defined.


# Virtualize!


It's time to run our first virtualized machine. For testing purposes we'll simply install Debian/Stable with the default network config that KVM uses. It has nothing to do with the bridge setup since it uses an internal DHCP server and NAT services. So here are the ToDos:



	
  1. Create the image

	
  2. Run the guest

	
  3. Install Debian/Stable to verify we have connectivity


{% highlight text %}
$ qemu-img create test.img 10G
{% endhighlight %}

{% highlight text %}
sudo /usr/bin/kvm \
    -k en \
    -name test \
    -boot order=cd,once=d \
    -drive file=$HOME/test.img,if=virtio,format=raw,media=disk \
    -drive file=$HOME/debian-504-amd64-netinst.iso,if=ide,media=cdrom \
    -usbdevice tablet \
    -watchdog i6300esb \
    -m 1024 \
    -vnc :1 \
    -balloon virtio \
    -pidfile /var/run/kvm.test
{% endhighlight %}

The command above does the following:

	
  * Tell KVM to use the english keymap

	
  * Name the guest test

	
  * Define a boot order of: disk,cdrom; but on the first boot use cdrom

	
  * Define a hard disk image, it's location and tell it to use the virtualized IO

	
  * Define a cdrom disk image, it's location and tell it to use the IDE IO

	
  * Set up a USB Device so that the SDL interaction VNC works more smoothly

	
  * Provide a watchdog hardware device

	
  * Provide 1024MiB of memory

	
  * Start a VNC Server on display one (port 5901)

	
  * Use the balloon driver

	
  * Tell KVM to create a PID file


When this is running just fire up a VNC Viewer and connect to the host

{% highlight text %}
$ vncviewer 192.2.0.195:1
{% endhighlight %}

If you have your Debian ISO image in the correct place you should be presented with the boot screen of the Debian ISO image. Just click thru and install. Since we used the netinst ISO image a successful installation means you have basic connectivity to the outside world.

In the next installment we'll further refine this to provide a DHCP and TFTP server thru the user mode networking so that we can automagically install our guests without further interaction.

This is our status as of now:


	
  * <del>Get Started! Do the basic setup, verify we have KVM working</del>

	
  * Automated Guest Installations from the direct physical host

	
  * Offer IPv4 connectivity over public IPs to  guest machines

	
  * Offer IPv6 and IPv4 connectivity to guest machines

	
  * Offer IPv6 as the only connectivity to guest machines

	
  * Automagically create new guests with a single command



