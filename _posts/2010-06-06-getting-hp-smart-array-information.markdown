---
comments: true
date: 2010-06-06 08:05:39
layout: post
slug: getting-hp-smart-array-information
title: Getting HP Smart Array information
wordpress_id: 791
tags:
- sysadmin
---

Just a small note for myself on our hardware.

I tend to forget this everytime I indeed need it. Maybe writing all that down helps

{% highlight bash %}
hpacucli ctrl all show detail
hpacucli ctrl slot=0 show config
hpacucli ctrl slot=0 array all show
hpacucli ctrl slot=0 array A show
hpacucli ctrl slot=0 physicaldrive all show
hpacucli ctrl slot=0 physicaldrive 1I:1:1 show
hpacucli ctrl slot=0 logicaldrive all show
hpacucli ctrl slot=0 logicaldrive 1 show
{% endhighlight %}
