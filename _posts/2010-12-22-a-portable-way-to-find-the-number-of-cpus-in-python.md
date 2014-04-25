---
layout: post
title: A portable way to find the number of CPUs in Python
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  _wpas_done_yup: '1'
  _wpas_done_fb: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1320179097";}
author: 
---
<p>This works in Python to get the number of CPUs in a system:</p>
<p>{% highlight text %}<br />
import os<br />
print os.sysconf('SC_NPROCESSORS_CONF')<br />
print os.sysconf('SC_NPROCESSORS_ONLN') # if different that the above this should be used<br />
{% endhighlight %}</p>
