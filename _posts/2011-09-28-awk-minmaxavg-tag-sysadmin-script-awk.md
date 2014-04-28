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
{% highlight awk %}
#!/usr/bin/awk -f
BEGIN
{
 minimum=0;
 maximum=0;
 sum=0;
}
{
 if($3>maximum)
 {
  maximum=$3;
 }
 if($3<minimum)
 {
  minimum=$3;
 }
 sum+=$3;
}
END
{
 print "Average = ",sum/NR;
 print "Max = ",maximum;
 print "Min = ",minimum;
}
{% endhighlight %}
