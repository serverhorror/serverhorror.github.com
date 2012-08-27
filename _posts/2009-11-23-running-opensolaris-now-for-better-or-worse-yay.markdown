---
comments: true
date: 2009-11-23 14:18:50
layout: post
slug: running-opensolaris-now-for-better-or-worse-yay
title: Running OpenSolaris now (for better or worse)! - Yay?
wordpress_id: 493
tags:
- sysadmin
---

So, I just switched to [OpenSolaris](http://www.opensolaris.org) on my workstation. In the sense of "[Eating one's own dog food](http://en.wikipedia.org/wiki/Eating_one%27s_own_dog_food)" I may have a better argumentation on wether I should like it or not. So far everything seems to work althoug I don't quite have a mirrored ZFS root pool in case one disk dies.

I also nearly immediately switched to the "[OpenSolaris Development Release Packaging Repository](http://pkg.opensolaris.org/dev/en/index.shtml)" - actually that's a lie. I'm switching to it right at this very moment....
{% highlight text %}
$ pfexec pkg set-publisher -O http://pkg.opensolaris.org/dev opensolaris.org
$ pfexec pkg image-update
Creating Plan /
{% endhighlight %}
Maybe, just maybe I'll stick to it....
