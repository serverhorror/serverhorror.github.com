---
layout: post
title: 'Update: Icinga 0.8.1 released'
categories: []
tags: []
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1245787908";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1306079206";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
<p>A short followup on the recent <a href="http://serverhorror.wordpress.com/2009/06/17/icinga-0-8-1-released/">0.8.1 release</a> of <a href="http://www.icinga.org">Icinga</a>. I just found the list of changes from the <a href="https://git.icinga.org/index?p=icinga-core.git;a=blob_plain;f=Changelog;hb=7c5b56d64bfedf7e3a0487e1fc195294df6cb23a">ChangeLog in the git repository</a> of Icinga

{% highlight text %}
0.8.1 - 06/17/2009
------------------
* Archived Logfiles renamed from Icinga-date-syntax.log => icinga-date-syntax.log (capital 'i')
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
* New &quot;important check command&quot; flag for use in service templates, to aid configuration in distributed environments
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
{% endhighlight text %}
