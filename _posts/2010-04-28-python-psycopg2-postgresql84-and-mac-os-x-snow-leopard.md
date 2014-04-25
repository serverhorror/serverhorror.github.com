---
layout: post
title: Python, psycopg2, postgresql84 and Mac OS X Snow Leopard
categories: []
tags: []
status: publish
type: post
published: true
meta:
  _wpas_mess: 'Python, psycopg2, postgresql84 and Mac OS X Snow Leopard: http://wp.me/pxxjT-bs'
  _wpas_done_fb: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275723774";}
  _wpas_done_twitter: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1275723775";}
  _wpas_skip_yup: '1'
author: 
---
<ul>
<li>You do some coding in <a href="http://www.pyton.org">Python</a>?</li>
<li>You do want to use an <a href="http://www.postgresql.org">advanced RDBMS</a>?</li>
<li>You like <a href="http://www.apple.com/macosx/">Mac OS X</a>?</li>
</ul>
<p>Look no further here's the simple solution to getting <a href="http://initd.org">psycopg2</a> to work without placing to much trash on your system.
{% highlight text %}
virtualenv --no-site-packages .
. bin/activate
easy_install  -U setuptools
easy_install pip
PATH=$PATH:/opt/local/lib/postgresql84/bin/ pip install psycopg2 sqlalchemy
#...lots of compile stuff...
{% endhighlight %}
You are done. Go into your python shell and import the <a href="http://initd.org/psycopg/">psycopg2</a> module...
{% highlight text %}
$ python
Python 2.6.1 (r261:67515, Feb 11 2010, 00:51:29)
[GCC 4.2.1 (Apple Inc. build 5646)] on darwin
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.
&gt;&gt;&gt; import psycopg2
&gt;&gt;&gt; psycopg2.__version__
'2.2.0 (dt dec release-candidate-1 ext pq3)'
&gt;&gt;&gt;
{% endhighlight %}</p>
<p> The solution here is this: {% highlight text %}
PATH=$PATH:/opt/local/lib/postgresql84/bin/ pip install psycopg2 sqlalchemy
{% endhighlight %}</p>
<p>The path shown here is if you installed postgresql84-server from <a href="http://macports.org">macports</a>. It might differ if you used the <a href="http://www.postgresql.org/download/macosx">native installer for Mac OS X</a></p>
