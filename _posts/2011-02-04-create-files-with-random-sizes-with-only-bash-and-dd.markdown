---
comments: true
date: 2011-02-04 11:00:30
layout: post
slug: create-files-with-random-sizes-with-only-bash-and-dd
title: Create files with random sizes with only bash and dd
wordpress_id: 1100
tags:
- bash
- linux
- Randomness
- Shell
- sysadmin
- Unix
- useless math
---

## The Rules


So you need a bunch of files of random size. Say something between 1 MiB and 10 MiB. And you need 3 of them. `bash` to the rescue.



	
  * The variable `$RANDOM` will return an integer between 0 a nd 32,767.

	
  * `$((...))` will do arithmetic expansion for the expression contained within

	
  * The `%`-operator will do a modulo operation


Let me use those 3 simple rules to create

	
  1. 3 files between 1 MiB and 10 MiB

	
  2. 3 files between 15 MiB and 25 MiB


**As a side note: I will be creating sparse files here. Look up `dd(1)` for the details. Your use case might be different anyway.**


## 1 MiB -- 10 MiB files


{% highlight bash %}$(( ($RANDOM % 10) + 1)){% endhighlight %}


## 15 MiB -- 25 MiB files


{% highlight bash %}$(( ($RANDOM % 10) + 15)){% endhighlight %}


## General Solution


{% highlight bash %}
MINSIZE=<number>
MAXSIZE=<number>
$(( ($RANDOM % ($MAXSIZE-$MINSIZE)) + $MINSIZE))
{% endhighlight %}

{% highlight bash %}
MINSIZE=30
MAXSIZE=60
for i in {1..3}
do
    dd if=/dev/zero of=testdata.01-15.${i}.data bs=1m count=0 seek=$(( ($RANDOM % 10) + 1))
    dd if=/dev/zero of=testdata.15-25.${i}.data bs=1m count=0 seek=$(( ($RANDOM % 10) + 15))
    dd if=/dev/zero of=testdata.${MINSIZE}-${MAXSIZE}.${i}.data bs=1m count=0 seek=$(( ($RANDOM % ($MAXSIZE-$MINSIZE)) + $MINSIZE))

done 2>/dev/null \
&& echo 'SUCCESS: Creating data files' \
|| echo 'FAILURE: Creating data files'
{% endhighlight %}

The result looks quite good.

{% highlight bash %}
du -sm testdata.*
10	testdata.01-15.1.data
5	testdata.01-15.2.data
3	testdata.01-15.3.data
17	testdata.15-25.1.data
21	testdata.15-25.2.data
20	testdata.15-25.3.data
31	testdata.30-60.1.data
38	testdata.30-60.2.data
55	testdata.30-60.3.data
{% endhighlight %}

Yes I know this is minor math at best. But still I tend to forget that problems like this are easily solveable, so I'll not it down here. And yes, there's probably a bunch of cases where bash isn't what you want to use. I needed lots of files to test mdadm behaviour so that I can use them as disks and create RAID arrays.
