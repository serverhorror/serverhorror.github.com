---
comments: true
date: 2010-04-28 19:57:53
layout: post
slug: python-psycopg2-postgresql84-and-mac-os-x-snow-leopard
title: Python, psycopg2, postgresql84 and Mac OS X Snow Leopard
wordpress_id: 710
---


	
  * You do some coding in [Python](http://www.pyton.org)?

	
  * You do want to use an [advanced RDBMS](http://www.postgresql.org)?

	
  * You like [Mac OS X](http://www.apple.com/macosx/)?


Look no further here's the simple solution to getting [psycopg2](http://initd.org) to work without placing to much trash on your system.
{% highlight bash %}
virtualenv --no-site-packages .
. bin/activate
easy_install  -U setuptools
easy_install pip
PATH=$PATH:/opt/local/lib/postgresql84/bin/ pip install psycopg2 sqlalchemy
#...lots of compile stuff...
{% endhighlight %}
You are done. Go into your python shell and import the [psycopg2](http://initd.org/psycopg/) module...
{% highlight bash %}
$ python
Python 2.6.1 (r261:67515, Feb 11 2010, 00:51:29) 
[GCC 4.2.1 (Apple Inc. build 5646)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import psycopg2
>>> psycopg2.__version__
'2.2.0 (dt dec release-candidate-1 ext pq3)'
>>> 
{% endhighlight %}

 The solution here is this: {% highlight bash %}
PATH=$PATH:/opt/local/lib/postgresql84/bin/ pip install psycopg2 sqlalchemy
{% endhighlight %}

The path shown here is if you installed postgresql84-server from [macports](http://macports.org). It might differ if you used the [native installer for Mac OS X](http://www.postgresql.org/download/macosx)
