---
layout: post
title: Python Class Methods
categories: []
tags: []
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2008/11/python-class-methods.html
  _wpas_done_twitter: '1'
  _wpas_done_fb: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275723777";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1275723777";}
  _wpas_skip_yup: '1'
author: 
---
<p><!-- YZVNG8ZM3F8R  -->
Just a short reminder how to easily create class methods in python. Useful for creating factory methods that return the instance of a certain class.</p>
<p>{% highlight text %}user@localhost:~$ python
Python 2.4.4 (#2, Apr 15 2008, 23:43:20)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.</p>
<p>&gt;&gt;&gt; class foo(object):
...     def __init__(self, s):
...             self.s = s
...     @classmethod
...     def from_string(cls, in_):
...             return cls(in_)
...     @classmethod
...     def from_int(cls, in_):
...             return cls(int(in_))
...
&gt;&gt;&gt; s = foo.from_string(&quot;foo&quot;)
&gt;&gt;&gt; s = foo.from_int(&quot;foo&quot;)
Traceback (most recent call last):
File &quot;&quot;, line 1, in ?
File &quot;&quot;, line 9, in from_int
ValueError: invalid literal for int(): foo
&gt;&gt;&gt; s = foo.from_int(&quot;2&quot;)
&gt;&gt;&gt; s = foo.from_int(&quot;0x2&quot;)
Traceback (most recent call last):
File &quot;&quot;, line 1, in ?
File &quot;&quot;, line 9, in from_int
ValueError: invalid literal for int(): 0x2
&gt;&gt;&gt; s = foo.from_int(0xe)
&gt;&gt;&gt; s.s
14
{% endhighlight %}</p>
<p>This in fact works quite fine except for one thing:</p>
<p>Python method are first class objects, if you have die above in a module named foo.py you will need the following code:</p>
<p>{% highlight text %}
Python 2.6.4 (r264:77598, Jan 18 2010, 11:44:15)
[GCC 4.3.4] on linux2
&gt;&gt;&gt; import foo
&gt;&gt;&gt; o = foo.foo.from_string(&quot;1&quot;)
&gt;&gt;&gt; o.s
'1'
{% endhighlight %}</p>
<p>Quite a lot of typing, you may want to consider the following:</p>
<p>{% highlight text %}
Python 2.6.4 (r264:77598, Jan 18 2010, 11:44:15)
[GCC 4.3.4] on linux2
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.
&gt;&gt;&gt; import foo
&gt;&gt;&gt; foo.from_string(&quot;a&quot;)
&lt;foo.foo object at 0x7f0c78d94350&gt;
&gt;&gt;&gt; o = foo.from_string(&quot;a&quot;)
&gt;&gt;&gt; o.s
'a'
{% endhighlight %}</p>
<p>A lot less to type isn't it?</p>
<p>To get that working just create a module that looks like this:</p>
<p>{% highlight text %}
def from_string(value):
    return foo(value)</p>
<p>def from_int(value):
    return foo(int(value))</p>
<p>class foo(object):
    def __init__(self, s):
            self.s = s
{% endhighlight %}</p>
