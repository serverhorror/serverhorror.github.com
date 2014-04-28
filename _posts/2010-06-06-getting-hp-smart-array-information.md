---
layout: post
title: Getting HP Smart Array information
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_skip_fb: '1'
  _wpas_skip_twitter: '1'
  _wp_old_slug: ''
  _wpas_mess: 'Getting HP Smart Array information:'
  _wpas_skip_yup: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1295290337";}
author: 
---
<p>Just a small note for myself on our hardware.</p>
<p>I tend to forget this everytime I indeed need it. Maybe writing all that down helps</p>
<p>{% highlight text %}
hpacucli ctrl all show detail
hpacucli ctrl slot=0 show config
hpacucli ctrl slot=0 array all show
hpacucli ctrl slot=0 array A show
hpacucli ctrl slot=0 physicaldrive all show
hpacucli ctrl slot=0 physicaldrive 1I:1:1 show
hpacucli ctrl slot=0 logicaldrive all show
hpacucli ctrl slot=0 logicaldrive 1 show
{% endhighlight %}</p>
