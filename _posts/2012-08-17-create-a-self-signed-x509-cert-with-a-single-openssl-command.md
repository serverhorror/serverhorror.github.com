---
layout: post
title: create a self signed x509 cert with a single openssl command
categories: []
tags:
- apache
- gnutls
- HTTP
- https
- openssl
- secure
- ssl
- tls
- x509
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  _wpas_skip_facebook: '1'
  _wpas_skip_linkedin: '1'
author: 
---
This is how you create a nice **self signed x509 cert with a single openssl command**:

{% highlight bash %}
openssl req -newkey rsa:2048 -keyout server.key -out server.crt -nodes -x509  -subj /CN=www.example.com
{% endhighlight %}
