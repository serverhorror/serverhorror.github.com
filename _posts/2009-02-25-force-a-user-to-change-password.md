---
layout: post
title: Force a User to change password
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2009/02/force-user-to-change-password.html
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
How do you force a user to change his/her password on the next login under linux?

{% highlight bash %}
passwd -e $OTHER_USER
{% endhighlight bash %}
