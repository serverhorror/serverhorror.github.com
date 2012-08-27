---
comments: true
date: 2010-12-22 19:14:15
layout: post
slug: a-portable-way-to-find-the-number-of-cpus-in-python
title: A portable way to find the number of CPUs in Python
wordpress_id: 901
tags:
- sysadmin
---

This works in Python to get the number of CPUs in a system:

{% highlight python %}
import os
print os.sysconf('SC_NPROCESSORS_CONF')
print os.sysconf('SC_NPROCESSORS_ONLN') # if different that the above this should be used
{% endhighlight %}
