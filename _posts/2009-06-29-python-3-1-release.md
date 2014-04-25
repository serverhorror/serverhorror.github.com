---
layout: post
title: Python 3.1 Release
categories: []
tags: []
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1306079199";}
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1250068346";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
<p>Great news: 2 days ago Python 3.1 has been released.</p>
<p>You can find the <a href="http://svn.python.org/projects/python/tags/r31/Misc/NEWS">ChangeLog here</a>. Personally I find these fixes great (not any specific order):

{% highlight text %}
- Issue #1655: Make imaplib IPv6-capable. Patch by Derek Morr.
- Issue #1664: Make nntplib IPv6-capable. Patch by Derek Morr.
- Issue #4868: utf-8, utf-16 and latin1 decoding are now 2x to 4x faster. The common cases are optimized thanks to a dedicated fast path and a moderate amount of loop unrolling.
- Issue #4874: Most builtin decoders now reject unicode input.
- Issue #3959: The ipaddr module has been added to the standard library. Contributed by Google.
- The json module now works exclusively with str and not bytes.
{% endhighlight text %}

I nearly missed it but my RSS Reader was kind enough to remind me, first <a href="http://sayspy.blogspot.com/2009/06/python-31-is-out.html">found it on this blog post</a></p>
