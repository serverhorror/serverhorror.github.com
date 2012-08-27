---
comments: true
date: 2009-11-24 15:00:09
layout: post
slug: easy-installation-of-virtualbox-on-opensolaris-and-maybe-other-stuff
title: Easy Installation of VirtualBox on OpenSolaris (and maybe other stuff)
wordpress_id: 502
tags:
- sysadmin
---

So I was looking how to install [VirtualBox](http://www.virtualbox.org/) under [OpenSolaris](http://www.opensolaris.org). My first thought was a simple

{% highlight text %}
pkg install virtualbox
{% endhighlight %}


or similiar would be enough. It isn't :).

Looking around I found that the nice people from Sun provide an easy way to install VirtualBox. Note: I don't really care about the newest and best features to be available but I like it when things are easy to manage - [no really!](http://serverhorror.wordpress.com/2009/11/23/running-opensolaris-now-for-better-or-worse-yay/) Here's how to get VirtualBox by simply using pkg with an official IPS repository.



	
  1. Go to [https://pkg.sun.com](https://pkg.sun.com)

	
  2. Login with your Sun Account (yes unfortunately you need one) - If you don't have an account register it

	
  3. You'll be presented with a "Certificate Requests" page, simply choose the OpenSolaris extras repository and request your certificate

	
  4. Follow the instructions (copy stuff to /var/pkg/ssl, pkg set-authority)

	
  5. pkg install virtualbox

	
  6. wait

	
  7. Be happy with a shiny new VirtualBox installation...


