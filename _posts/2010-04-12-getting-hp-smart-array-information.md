---
layout: post
title: Getting HP Smart Array information
categories: []
tags: []
status: draft
type: post
published: false
meta: {}
author: 
---
<p>{% highlight text %}</p>
<p>hpacucli ctrl all show detail
hpacucli ctrl slot=0 show config
hpacucli ctrl slot=0 array all show
hpacucli ctrl slot=0 array A show
hpacucli ctrl slot=0 physicaldrive all show
hpacucli ctrl slot=0 physicaldrive 1I:1:1 show
hpacucli ctrl slot=0 logicaldrive all show
hpacucli ctrl slot=0 logicaldrive 1 show
{% endhighlight %}</p>
