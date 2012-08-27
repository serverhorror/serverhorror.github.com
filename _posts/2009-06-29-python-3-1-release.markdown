---
comments: true
date: 2009-06-29 09:00:52
layout: post
slug: python-3-1-release
title: Python 3.1 Release
wordpress_id: 189
---

Great news: 2 days ago Python 3.1 has been released.

You can find the [ChangeLog here](http://svn.python.org/projects/python/tags/r31/Misc/NEWS). Personally I find these fixes great (not any specific order):
[sourcecode language="text"]
- Issue #1655: Make imaplib IPv6-capable. Patch by Derek Morr.
- Issue #1664: Make nntplib IPv6-capable. Patch by Derek Morr.
- Issue #4868: utf-8, utf-16 and latin1 decoding are now 2x to 4x faster. The common cases are optimized thanks to a dedicated fast path and a moderate amount of loop unrolling.
- Issue #4874: Most builtin decoders now reject unicode input.
- Issue #3959: The ipaddr module has been added to the standard library. Contributed by Google.
- The json module now works exclusively with str and not bytes.
[/sourcecode]
I nearly missed it but my RSS Reader was kind enough to remind me, first [found it on this blog post](http://sayspy.blogspot.com/2009/06/python-31-is-out.html)
