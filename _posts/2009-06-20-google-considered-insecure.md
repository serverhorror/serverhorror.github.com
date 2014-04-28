---
layout: post
title: Google considered insecure
categories: []
tags: []
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1246166791";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1306079204";}
  _wpas_skip_yup: '1'
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
A <a href="http://www.cloudprivacy.net/letter/#signers">group of 38 <span style="text-decoration:line-through;">experts</span> researchers</a> wrote an <a href="http://www.cloudprivacy.net/letter/">open letter to Google</a> claiming - according to recent news - that Google is insecure.

After reading the original PDF sent to <a href="http://www.google.com/corporate/execs.html#eric">Eric Schmidt (PhD)</a> I can't quite follow why the common opinion states that <em>Google is insecure</em>. I do understand that from a security point of view it is - without doubts - a lot better to use an SSL encrypted connection by default. Let's get into the details.

The researchers claim that <strong>Google Apps is insecure by default</strong>, because (in essence):

* Google uses an authentication cookie
* once authenticated to any of Google's services (Docs, iGoogle, Mail, Blogger,...) users are able to log in without providing any password to services visited later on
* the options to activate SSL secured connection to Google is hard to find
* the <strong>default is not to use secure connections</strong> by using encryption

I read up a bit on how authentication cookies generally work and that seems to be a real problem. A short thought about how many PCs out there are probably a member of some kind of botnet, the botnet operators could rather easily gain access to such a cookie and authenticate to any of Google's services.

On the other hand a compromised PC has no guarantee at all that it doesn't send all keystrokes to the operators anyway. So asking for the username and password for any service provided by Google won't add much to security anyway. For a PC that is not some kind of Zombie but for some reason let's anyone access all data on disk the problem with authentication cookies still is valid.

The reasoning that the option to enable encrypted connections is something I can't quite follow. Actually I find it very easy to reach. Just login to your Google account and click "<em>Settings</em>" at the top right (excuse the quality of the graphics, I'm just not compatible with graphics or anything that should be appealing to the eye).

![settings](http://serverhorror.files.wordpress.com/2009/06/settings.jpg)

You'll be taken to the *General Settings* page, scroll down near the end and you'll find the option to encrypt all your traffic.

![https](http://serverhorror.files.wordpress.com/2009/06/https.jpg)

Give, the naming of the option could be better for the casual user, something like "Prevent 3rd parties from eavesdropping my data" - but there are probably smarter people than me to choose a nice, non-technical wording for that.

Finally the last option is indeed valid. The connection should be secured by default, but this is Google and they have a lot of resources so <a href="http://googlepublicpolicy.blogspot.com/2009/06/https-security-for-web-applications.html">an answer didn't take too long</a> (see also the original on the <a href="http://googleonlinesecurity.blogspot.com/2009/06/https-security-for-web-applications.html">Google Online Security Blog</a> - resembling the same content).

The canonical answer from Google seems to be that they are investigation the impact of switching to HTTPS by default will have, so they are not really opposed to switch to a secure by default configuration.
