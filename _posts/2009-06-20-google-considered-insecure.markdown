---
comments: true
date: 2009-06-20 18:15:49
layout: post
slug: google-considered-insecure
title: Google considered insecure
wordpress_id: 116
---

A [group of 38 experts researchers](http://www.cloudprivacy.net/letter/#signers) wrote an [open letter to Google](http://www.cloudprivacy.net/letter/) claiming - according to recent news - that Google is insecure.

After reading the original PDF sent to [Eric Schmidt (PhD)](http://www.google.com/corporate/execs.html#eric) I can't quite follow why the common opinion states that _Google is insecure_. I do understand that from a security point of view it is - without doubts - a lot better to use an SSL encrypted connection by default. Let's get into the details.

The researchers claim that **Google Apps is insecure by default**, because (in essence):



	
  * Google uses an authentication cookie

	
  * once authenticated to any of Google's services (Docs, iGoogle, Mail, Blogger,...) users are able to log in without providing any password to services visited later on

	
  * the options to activate SSL secured connection to Google is hard to find

	
  * the **default is not to use secure connections** by using encryption


I read up a bit on how authentication cookies generally work and that seems to be a real problem. A short thought about how many PCs out there are probably a member of some kind of botnet, the botnet operators could rather easily gain access to such a cookie and authenticate to any of Google's services.

On the other hand a compromised PC has no guarantee at all that it doesn't send all keystrokes to the operators anyway. So asking for the username and password for any service provided by Google won't add much to security anyway. For a PC that is not some kind of Zombie but for some reason let's anyone access all data on disk the problem with authentication cookies still is valid.

The reasoning that the option to enable encrypted connections is something I can't quite follow. Actually I find it very easy to reach. Just login to your Google account and click "_Settings_" at the top right (excuse the quality of the graphics, I'm just not compatible with graphics or anything that should be appealing to the eye).

![settings](http://serverhorror.files.wordpress.com/2009/06/settings.jpg?w=300)

You'll be taken to the General settings page, scroll down near the end and you'll find the option to encrypt all your traffic.

![https](http://serverhorror.files.wordpress.com/2009/06/https.jpg?w=300)Give, the naming of the option could be better for the casual user, something like "Prevent 3rd parties from eavesdropping my data" - but there are probably smarter people than me to choose a nice, non-technical wording for that.

Finally the last option is indeed valid. The connection should be secured by default, but this is Google and they have a lot of resources so [an answer didn't take too long](http://googlepublicpolicy.blogspot.com/2009/06/https-security-for-web-applications.html) (see also the original on the [Google Online Security Blog](http://googleonlinesecurity.blogspot.com/2009/06/https-security-for-web-applications.html) - resembling the same content).

The canonical answer from Google seems to be that they are investigation the impact of switching to HTTPS by default will have, so they are not really opposed to switch to a secure by default configuration.
