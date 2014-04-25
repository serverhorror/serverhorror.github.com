---
layout: post
title: Create .dmg Images for OS X on Linux
categories: []
tags:
- Disk image
- linux
- Mac OS X
- os x
- osx
status: publish
type: post
published: true
meta:
  _wpas_done_fb: '1'
  _wpas_done_yup: '1'
  _wpas_done_twitter: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1319696121";}
author: 
---
<p>Those are the kinds of gems hidden in bugreports:</p>
<blockquote><p>If you cant create the image on a mac because of the build process, here is how you can do it under linux:</p>
<ol>
<li>Create a image file, the size is fixed. (<code>dd if=/dev/zero of=/root/eclipse.dmg bs=1M count=130</code>)</li>
<li>Get the <code>hfsutils</code> (for redhat or suse: <code>hfsutils-3.2.6-1.i386.rpm</code> from rpmfind.net) and install them.</li>
<li>Format the image file: <code>hformat -l Eclipse /root/eclipse.dmg</code></li>
<li>Mount the image: <code>mount -t hfs -o loop /root/eclipse.dmg /mnt/test</code></li>
<li>Copy files into the volume</li>
<li>Unmount the volume: <code>umount /mnt/test</code></li>
<li>Thats it.</li>
</ol>
</blockquote>
<p>via <a href="https://bugs.eclipse.org/bugs/show_bug.cgi?id=106350#c0">Bug 106350 – Feature Request: distributing eclipse.dmg instead of .tar.gz for the mac platform</a>.</p>
<p>Applying these instructions to your distro is left as an exercise for the reader.</p>
