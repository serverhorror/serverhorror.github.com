---
comments: true
date: 2011-02-26 17:17:52
layout: post
slug: create-dmg-images-for-os-x-on-linux
title: Create .dmg Images for OS X on Linux
wordpress_id: 1161
tags:
- Disk image
- linux
- Mac OS X
- os x
- osx
---

Those are the kinds of gems hidden in bugreports:


> If you cant create the image on a mac because of the build process, here is how you can do it under linux:

> 
> 
	
>   1. Create a image file, the size is fixed. (`dd if=/dev/zero of=/root/eclipse.dmg bs=1M count=130`)
> 
	
>   2. Get the `hfsutils` (for redhat or suse: `hfsutils-3.2.6-1.i386.rpm` from rpmfind.net) and install them.
> 
	
>   3. Format the image file: `hformat -l Eclipse /root/eclipse.dmg`
> 
	
>   4. Mount the image: `mount -t hfs -o loop /root/eclipse.dmg /mnt/test`
> 
	
>   5. Copy files into the volume
> 
	
>   6. Unmount the volume: `umount /mnt/test`
> 

>   7. Thats it.
> 




via [Bug 106350 – Feature Request: distributing eclipse.dmg instead of .tar.gz for the mac platform](https://bugs.eclipse.org/bugs/show_bug.cgi?id=106350#c0).

Applying these instructions to your distro is left as an exercise for the reader.
