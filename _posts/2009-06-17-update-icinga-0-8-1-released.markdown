---
comments: true
date: 2009-06-17 15:49:28
layout: post
slug: update-icinga-0-8-1-released
title: 'Update: Icinga 0.8.1 released'
wordpress_id: 100
---

A short followup on the recent [0.8.1 release](http://serverhorror.wordpress.com/2009/06/17/icinga-0-8-1-released/) of [Icinga](http://www.icinga.org). I just found the list of changes from the [ChangeLog in the git repository](https://git.icinga.org/index?p=icinga-core.git;a=blob_plain;f=Changelog;hb=7c5b56d64bfedf7e3a0487e1fc195294df6cb23a) of Icinga
{% highlight text %}
0.8.1 - 06/17/2009
------------------
* Archived Logfiles renamed from Icinga-date-syntax.log =&gt; icinga-date-syntax.log (capital 'i')
* cherry picked latest Nagios Patches (see Nagios Changelog below)
* new ido2db command switch: '-f' don't daemonize the ido2db
* ido2db will now prints out available database drivers
* fix ido2db segfault when try to access non existing tables
* DocBook v5 conversion
* Fix menu frameset cols width<!--more-->
{% endhighlight %}
Here is the ChangeLog for Nagios referenced above:
{% highlight text %}
3.1.1 - 02/??/2009
------------------
* New "important check command" flag for use in service templates, to aid configuration in distributed environments
* Fix for nagios validation error when no services defined
* Fix for stylesheet link
* Fix for extinfo.cgi error message when cgi.cfg doesn't exist
* Fix for notifications.cgi where Update button on right didn't retain host information when no host= was in query parameters
* Fix for potential bug where a contactgroup with no members could cause parsing errors
* Fix for W3 validation for history.cgi
* Fix for W3 validation for extinfo.cgi
* Fix for nagiostats to return non-zero with failures in MRTG mode
* Added t/ directory for tests. Use make test to run. Requires perl on development server
* Fix for duplicate event_id attributes in status and retention data
* Fix for duplicate unlink() during check processing
* Added missing check period column to host config display (CGI)
* Fix for embedded Perl initialization under FreeBSD
* Fix for incorrect re-initialization of mutext after program restart
* Fix for incorrect weighting in host flap detection logic
* Added libtap to distribution. Use ./configure --enable-libtap to compile
* nagios.log permissions are now kept after log rotation
{% endhighlight %}
