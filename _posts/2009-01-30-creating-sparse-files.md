---
layout: post
title: Creating Sparse Files
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2009/01/creating-sparse-files.html
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
This is something I really tend to forget: **How do you create a sparse file in unix?**

{% highlight bash %}
dd if=/dev/zero of=/tmp/sparsefile.sparse bs=1 count=0 seek=5M
{% endhighlight %}

From [Wikipedia](http://en.wikipedia.org/wiki/Sparse_file) about what a sparse file is:
> In [computer science](http://en.wikipedia.org/wiki/Computer_science), a
> **sparse file** is a type of [computer file](http://en.wikipedia.org/wiki/Computer_file)
> that attempts to use [file system](http://en.wikipedia.org/wiki/File_system)
> space more efficiently when blocks allocated to the file are mostly empty.
