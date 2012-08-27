---
comments: true
date: 2009-01-30 23:15:00
layout: post
slug: creating-sparse-files
title: Creating Sparse Files
wordpress_id: 249
tags:
- sysadmin
---

This is something I really tend to forget: **How do you create a sparse file
in unix?**

{% highlight bash %}
dd if=/dev/zero of=/tmp/sparsefile.sparse bs=1 count=0 seek=5M
{% endhighlight %}

From [Wikipedia](http://en.wikipedia.org/wiki/Sparse_file) about what a
sparse file is:


> In [computer science](http://en.wikipedia.org/wiki/Computer_science), a
> **sparse file** is a type of [computer
> file](http://en.wikipedia.org/wiki/Computer_file) that attempts to use
> [file system](http://en.wikipedia.org/wiki/File_system) space more
> efficiently when blocks allocated to the file are mostly empty.
