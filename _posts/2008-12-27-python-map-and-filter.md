---
layout: post
title: Python, map and filter.
categories: []
tags: []
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2008/12/python-map-and-filter.html
author: 
---
<p>Just another note to myself for some useful python stuff:</p>
<pre style="padding-left:30px;">Python 2.4.4 (#2, Oct 22 2008, 20:20:22)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; def multby3(elem):
...     return elem * 3
...
&gt;&gt;&gt; map(multby3, (1, 2, 3, ))
[3, 6, 9]
&gt;&gt;&gt; def even(elem):
...     return not elem % 2
...
&gt;&gt;&gt; filter(even, (1, 2, 3, ))
(2,)
&gt;&gt;&gt; map(multby3, filter(even, (1, 2, 3, )))
[6]
&gt;&gt;&gt;</pre>
