---
comments: true
date: 2008-12-27 03:45:00
layout: post
slug: fibonacci
title: Fibonacci Number Slowness
wordpress_id: 241
---

Something I tend to forget:
[sourcecode language="python"]
def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b
[/sourcecode]
Another way of implementing it of course this is very slow, try calculating the [Fibonacci number](http://en.wikipedia.org/wiki/Fibonacci_number) of 50 with this algorithm and then get it with the first algorithm:
[sourcecode language="python"]
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
[/sourcecode]
