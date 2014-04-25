---
layout: post
title: Awk min/max/avg
categories: []
tags:
- AWK
- Command-line interface
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1322875060";}
author: 
---
<div class="posterous_autopost">
<p>{% highlight text %}</p>
<p>#!/usr/bin/awk -f
BEGIN
{
 minimum=0;
 maximum=0;
 sum=0;
}</p>
<p>{
 if($3&gt;maximum)
 {
 maximum=$3;
 }
 if($3<minimum)
 {
 minimum=$3;
 }
 sum+=$3;
}</p>
<p>END
{
 print &quot;Average = &quot;,sum/NR;
 print &quot;Max = &quot;,maximum;
 print &quot;Min = &quot;,minimum;
}</p>
<p>{% endhighlight %}</p>
</div>
