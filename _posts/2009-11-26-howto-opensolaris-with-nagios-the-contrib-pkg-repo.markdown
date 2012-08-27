---
comments: true
date: 2009-11-26 15:00:10
layout: post
slug: howto-opensolaris-with-nagios-the-contrib-pkg-repo
title: 'HowTo: OpenSolaris with Nagios (The contrib pkg repo)'
wordpress_id: 531
tags:
- sysadmin
---

I wanted to get Nagios running on OpenSolaris, honoring the pkg System I tried:

{% highlight text %}

pkg search nagios

{% endhighlight %}

No dice, but I hadn't added the contrib repo yet and didn't know about it up until that point :)

Just add



	
  * [http://pkg.opensolaris.org/contrib](http://pkg.opensolaris.org/contrib)


as a pkg source and then install Nagios. Very nice!
