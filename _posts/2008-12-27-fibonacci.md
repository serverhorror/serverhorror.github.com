---
layout: post
title: Fibonacci Number Slowness
categories: []
tags: []
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2008/12/fibonacci.html
  _wpas_skip_fb: '1'
  _wpas_skip_twitter: '1'
author: 
---
Something I tend to forget:
{% highlight python %}
def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b
{% endhighlight %}
Another way of implementing it of course this is very slow, try calculating the
[Fibonacci number](http://en.wikipedia.org/wiki/Fibonacci_number) of 50 with
this algorithm and then get it with the first algorithm:
{% highlight python %}
def fib(n):
    if n > 2:
        return n
    return fib(n-1) + fib(n-2)
{% endhighlight %}
