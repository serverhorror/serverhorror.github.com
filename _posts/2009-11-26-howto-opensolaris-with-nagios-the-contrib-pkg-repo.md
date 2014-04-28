---
layout: post
title: 'HowTo: OpenSolaris with Nagios (The contrib pkg repo)'
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1295290318";}
  _wpas_done_twitter: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275723779";}
  _wpas_skip_fb: '1'
  _oembed_15dbb68ab1388bb4cebb7a88403e2ed7: '{{unknown}}'
author: 
---
I wanted to get Nagios running on OpenSolaris, honoring the pkg System I tried:

{% highlight text %}
pkg search nagios
{% endhighlight %}

No dice, but I hadn't added the contrib repo yet and didn't know about it up until that point :)

Just add

* <a href="http://pkg.opensolaris.org/contrib">http://pkg.opensolaris.org/contrib</a>

as a pkg source and then install Nagios. Very nice!
