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
<p><!-- YZVNG8ZM3F8R  --><br />
Just a short reminder how to easily create class methods in python. Useful for creating factory methods that return the instance of a certain class.</p>
<p>{% highlight text %}user@localhost:~$ python<br />
Python 2.4.4 (#2, Apr 15 2008, 23:43:20)<br />
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2<br />
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.</p>
<p>&gt;&gt;&gt; class foo(object):<br />
...     def __init__(self, s):<br />
...             self.s = s<br />
...     @classmethod<br />
...     def from_string(cls, in_):<br />
...             return cls(in_)<br />
...     @classmethod<br />
...     def from_int(cls, in_):<br />
...             return cls(int(in_))<br />
...<br />
&gt;&gt;&gt; s = foo.from_string(&quot;foo&quot;)<br />
&gt;&gt;&gt; s = foo.from_int(&quot;foo&quot;)<br />
Traceback (most recent call last):<br />
File &quot;&quot;, line 1, in ?<br />
File &quot;&quot;, line 9, in from_int<br />
ValueError: invalid literal for int(): foo<br />
&gt;&gt;&gt; s = foo.from_int(&quot;2&quot;)<br />
&gt;&gt;&gt; s = foo.from_int(&quot;0x2&quot;)<br />
Traceback (most recent call last):<br />
File &quot;&quot;, line 1, in ?<br />
File &quot;&quot;, line 9, in from_int<br />
ValueError: invalid literal for int(): 0x2<br />
&gt;&gt;&gt; s = foo.from_int(0xe)<br />
&gt;&gt;&gt; s.s<br />
14<br />
{% endhighlight %}</p>
<p>This in fact works quite fine except for one thing:</p>
<p>Python method are first class objects, if you have die above in a module named foo.py you will need the following code:</p>
<p>{% highlight text %}<br />
Python 2.6.4 (r264:77598, Jan 18 2010, 11:44:15)<br />
[GCC 4.3.4] on linux2<br />
&gt;&gt;&gt; import foo<br />
&gt;&gt;&gt; o = foo.foo.from_string(&quot;1&quot;)<br />
&gt;&gt;&gt; o.s<br />
'1'<br />
{% endhighlight %}</p>
<p>Quite a lot of typing, you may want to consider the following:</p>
<p>{% highlight text %}<br />
Python 2.6.4 (r264:77598, Jan 18 2010, 11:44:15)<br />
[GCC 4.3.4] on linux2<br />
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.<br />
&gt;&gt;&gt; import foo<br />
&gt;&gt;&gt; foo.from_string(&quot;a&quot;)<br />
&lt;foo.foo object at 0x7f0c78d94350&gt;<br />
&gt;&gt;&gt; o = foo.from_string(&quot;a&quot;)<br />
&gt;&gt;&gt; o.s<br />
'a'<br />
{% endhighlight %}</p>
<p>A lot less to type isn't it?</p>
<p>To get that working just create a module that looks like this:</p>
<p>{% highlight text %}<br />
def from_string(value):<br />
    return foo(value)</p>
<p>def from_int(value):<br />
    return foo(int(value))</p>
<p>class foo(object):<br />
    def __init__(self, s):<br />
            self.s = s<br />
{% endhighlight %}</p>
