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
<p>Something I tend to forget:<br />
[sourcecode language="python"]<br />
def fibonacci():<br />
    a, b = 1, 2<br />
    while True:<br />
        yield a<br />
        a, b = b, a + b<br />
[/sourcecode]<br />
Another way of implementing it of course this is very slow, try calculating the <a href="http://en.wikipedia.org/wiki/Fibonacci_number">Fibonacci number</a> of 50 with this algorithm and then get it with the first algorithm:<br />
[sourcecode language="python"]<br />
def fib(n):<br />
    if n &lt; 2:<br />
        return n<br />
    return fib(n-1) + fib(n-2)<br />
[/sourcecode]</p>
