---
comments: true
date: 2010-03-22 12:00:00
layout: post
slug: python-class-methods
title: Python Class Methods
wordpress_id: 235
---


Just a short reminder how to easily create class methods in python. Useful for creating factory methods that return the instance of a certain class.

{% highlight text %}
user@localhost:~$ python
Python 2.4.4 (#2, Apr 15 2008, 23:43:20)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> class foo(object):
...     def __init__(self, s):
...             self.s = s
...     @classmethod
...     def from_string(cls, in_):
...             return cls(in_)
...     @classmethod
...     def from_int(cls, in_):
...             return cls(int(in_))
...
>>> s = foo.from_string("foo")
>>> s = foo.from_int("foo")
Traceback (most recent call last):
File "", line 1, in ?
File "", line 9, in from_int
ValueError: invalid literal for int(): foo
>>> s = foo.from_int("2")
>>> s = foo.from_int("0x2")
Traceback (most recent call last):
File "", line 1, in ?
File "", line 9, in from_int
ValueError: invalid literal for int(): 0x2
>>> s = foo.from_int(0xe)
>>> s.s
14
{% endhighlight %}


This in fact works quite fine except for one thing:

Python method are first class objects, if you have die above in a module named foo.py you will need the following code:

{% highlight text %}
Python 2.6.4 (r264:77598, Jan 18 2010, 11:44:15)
[GCC 4.3.4] on linux2
>>> import foo
>>> o = foo.foo.from_string("1")
>>> o.s
'1'
{% endhighlight %}


Quite a lot of typing, you may want to consider the following:

{% highlight text %}
Python 2.6.4 (r264:77598, Jan 18 2010, 11:44:15)
[GCC 4.3.4] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import foo
>>> foo.from_string("a")
<foo.foo object at 0x7f0c78d94350>
>>> o = foo.from_string("a")
>>> o.s
'a'
{% endhighlight %}


A lot less to type isn't it?

To get that working just create a module that looks like this:

{% highlight python %}
def from_string(value):
    return foo(value)

def from_int(value):
    return foo(int(value))

class foo(object):
    def __init__(self, s):
            self.s = s
{% endhighlight %}
