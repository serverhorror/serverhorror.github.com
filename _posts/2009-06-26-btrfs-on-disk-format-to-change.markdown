---
comments: true
date: 2009-06-26 11:00:14
layout: post
slug: btrfs-on-disk-format-to-change
title: BTRFS On-Disk Format to Change
wordpress_id: 182
---

The [Linux Kernel 2.6.31-rc1 (direct git-snapshot download)](http://kernel.org/pub/linux/kernel/v2.6/snapshots/patch-2.6.31-rc1-git1.bz2) has been released.

Among some [Kernel Mode Setting (KMS)](http://en.wikipedia.org/wiki/Mode-setting) enhancements which allow the Kernel to set the "correct" video mode - and thus take some work from X. The most notable change is probably a change in the on-disk format of the [btrfs file system](http://en.wikipedia.org/wiki/Btrfs).

Migration (hopefully) happens automagically upon the filesystem being mounted with the new kernel, there's however no (easy) way back. So **you won't be able to mount the filesystem again with older kernels**.
