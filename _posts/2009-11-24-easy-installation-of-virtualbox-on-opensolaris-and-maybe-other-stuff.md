---
layout: post
title: Easy Installation of VirtualBox on OpenSolaris (and maybe other stuff)
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1270824424";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1270824435";}
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
  _oembed_01636b13d81cb237d801f2f814e2a19a: '{{unknown}}'
author: 
---
<p>So I was looking how to install <a href="http://www.virtualbox.org/">VirtualBox</a> under <a href="http://www.opensolaris.org">OpenSolaris</a>. My first thought was a simple</p>
<p>{% highlight text %}
pkg install virtualbox
{% endhighlight %}</p>
<p>or similiar would be enough. It isn't :).</p>
<p>Looking around I found that the nice people from Sun provide an easy way to install VirtualBox. Note: I don't really care about the newest and best features to be available but I like it when things are easy to manage - <a href="http://serverhorror.wordpress.com/2009/11/23/running-opensolaris-now-for-better-or-worse-yay/">no really!</a> Here's how to get VirtualBox by simply using pkg with an official IPS repository.</p>
<ol>
<li>Go to <a href="https://pkg.sun.com">https://pkg.sun.com</a></li>
<li>Login with your Sun Account (yes unfortunately you need one) - If you don't have an account register it</li>
<li>You'll be presented with a "Certificate Requests" page, simply choose the OpenSolaris extras repository and request your certificate</li>
<li>Follow the instructions (copy stuff to /var/pkg/ssl, pkg set-authority)</li>
<li>pkg install virtualbox</li>
<li>wait</li>
<li>Be happy with a shiny new VirtualBox installation...</li>
</ol>
