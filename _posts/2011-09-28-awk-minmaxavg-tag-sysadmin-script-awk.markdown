---
comments: true
date: 2011-09-28 16:58:13
layout: post
slug: awk-minmaxavg-tag-sysadmin-script-awk
title: Awk min/max/avg
wordpress_id: 1308
tags:
- AWK
- Command-line interface
---



[sourcecode]

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

[/sourcecode]


