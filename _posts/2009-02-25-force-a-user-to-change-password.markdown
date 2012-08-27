---
comments: true
date: 2009-02-25 21:41:00
layout: post
slug: force-a-user-to-change-password
title: Force a User to change password
wordpress_id: 253
tags:
- sysadmin
---

How do you force a user to change his/her password on the next login under linux?
{% highlight text %}
passwd -e <user in question>
{% endhighlight %}
