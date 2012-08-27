---
comments: true
date: 2012-08-17 22:45:31
layout: post
slug: create-a-self-signed-x509-cert-with-a-single-openssl-command
title: create a self signed x509 cert with a single openssl command
wordpress_id: 1538
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
---






This is how you create a nice **self signed x509 cert with a single openssl command**:

_openssl req -newkey rsa:2048 -keyout server.key -out server.crt -nodes -x509_

{% highlight bash %}
openssl req -newkey rsa:2048 -keyout server.key -out server.crt -nodes -x509  -subj /CN=www.example.com
{% endhighlight %}

Now it'll just take another couple of months to finally read up on how to write a config file for that :)











