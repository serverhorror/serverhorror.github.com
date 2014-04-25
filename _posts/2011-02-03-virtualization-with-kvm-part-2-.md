---
layout: post
title: Virtualization with KVM (Part 2)
categories: []
tags:
- sysadmin
status: pending
type: post
published: false
meta: {}
author: 
---
<p>Continued from the <a href="http://blog.serverhorror.com/2010/05/20/virtualization-with-kvm-part-1/">last time</a>, let's see where we are:</p>
<ul>
<li><del datetime="2010-05-20T11:11:42+00:00"><a href="http://blog.serverhorror.com/2010/05/20/virtualization-with-kvm-part-1/">Get Started! Do the basic setup, verify we have KVM working</a></del></li>
<li>Automated Guest Installations from the direct physical host</li>
<li>Offer IPv4 connectivity over public IPs to  guest machines</li>
<li>Offer IPv6 and IPv4 connectivity to guest machines</li>
<li>Offer IPv6 as the only connectivity to guest machines</li>
<li>Automagically create new guests with a single command</li>
</ul>
<hr />
<ol>
<li>Use KVM</li>
<li>Manual Configuration
<ol>
<li>Configure Network Bridge</li>
<li>Run Guest without Private IPv4</li>
<li>Run Guest with Public IPv4</li>
<li>Setup SIXXS</li>
<li>Configure IPv6 Bridge/Gateway</li>
<li>Run Guest with IPv6</li>
<li>Install different Guest Systems
<ol>
<li>ArchLinux</li>
<li>CentOS</li>
<li>Debian</li>
<li>Fedora</li>
<li>Gentoo Linux</li>
<li>Ubuntu</li>
<li>OpenSolaris!</li>
</ol>
</li>
</ol>
</li>
<li>Automated Configuration
<ol>
<li>Define available machine types
<ol>
<li>Memory</li>
<li>Disk Space</li>
<li>Host Name</li>
<li>CPU Scheduling?</li>
</ol>
</li>
<li>Define available config options
<ol>
<li>KVM Monitor Access</li>
<li>Available Distros</li>
</ol>
</li>
<li>Automate IP Distribution/Assignement
<ol>
<li>IPv4</li>
<li>IPv6</li>
</ol>
</li>
</ol>
</li>
<li>a</li>
</ol>
<p>﻿﻿﻿http://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine</p>
<p>﻿<a href="http://mediakey.dk/~cc/generate-random-mac-address-for-e-g-xen-guests/">http://mediakey.dk/~cc/generate-random-mac-address-for-e-g-xen-guests/</a></p>
