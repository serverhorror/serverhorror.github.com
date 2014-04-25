---
layout: post
title: Nagios 3.1.2 Released
categories: []
tags: []
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1246166789";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1306079203";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
<p><a href="http://www.nagios.org/news/77-news-announcements/205-nagios-312-released">Nagios 3.1.2 Released</a> has just been released. I'm not quite sure I want to try it, given the recent fork from <a href="http://www.icinga.org">Nagios (Icinga)</a>, where <a href="http://www.icinga.org/team/">all the people who were contributing the interesting plugins and addons</a>.</p>
<p>Anyway here are the recent notes from the Nagios ChangeLog:<br />
[sourcecode language="text"]<br />
3.1.2 - 06/23/2009<br />
------------------<br />
* Fix for CPU hogging in service and host check scheduling logic</p>
<p>3.1.1 - 06/22/2009<br />
------------------<br />
* New &quot;important check command&quot; flag for use in service templates, to aid configuration in distributed environments<br />
* Fix for nagios validation error when no services defined<br />
* Fix for stylesheet link<br />
* Fix for extinfo.cgi error message when cgi.cfg doesn't exist<br />
* Fix for notifications.cgi where Update button on right didn't retain host information when no host= was in query parameters<br />
* Fix for potential bug where a contactgroup with no members could cause parsing errors<br />
* Fix for W3 validation for history.cgi<br />
* Fix for W3 validation for extinfo.cgi<br />
* Fix for nagiostats to return non-zero with failures in MRTG mode<br />
* Added t/ directory for tests. Use make test to run. Requires perl on development server<br />
* Fix for duplicate event_id attributes in status and retention data<br />
* Fix for duplicate unlink() during check processing<br />
* Added missing check period column to host config display (CGI)<br />
* Fix for embedded Perl initialization under FreeBSD<br />
* Fix for incorrect re-initialization of mutext after program restart<br />
* Fix for incorrect weighting in host flap detection logic<br />
* Added libtap to distribution. Use ./configure --enable-libtap to compile<br />
* nagios.log permissions are now kept after log rotation<br />
* Fix for &quot;Max concurrent service checks (X) has been reached&quot; messages - will now push services 5 + random(10) seconds ahead for<br />
retry<br />
* Fix for removing old HTML files for web frontend that are now replaced with PHP equivalents (index/main/side.html)<br />
* Fix for incorrect service history link text in CGIs<br />
* Fix for useless code loop in netutils.c<br />
* Fix for potential divide by zero in event scheduling code<br />
* Fix for trailing backslash in plugin output causing memory corruption in CGIs<br />
* Fix for bug that could affect host/service scheduling during clock time skew or changes to timeperod definitions between restart<br />
s<br />
* Leading whitespace from continuation lines in configuration files is now stripped out<br />
* Fix for bug where pipe (used by IPC) file descriptors get inherited by child processed (e.g. event handlers) (bug #0000026)<br />
* Fix for failure to daemonize - Nagios now bails (bug #0000011)<br />
* Fix for notifications about flapping starting not processed properly by retention data<br />
* Patch to add transparency to statusmap icons for truecolor images<br />
* Patch to add read-only permissions to extinfo CGI<br />
* Security fix for statuswml.cgi where arbitrary shell injection was possible<br />
[/sourcecode]</p>
