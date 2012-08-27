---
comments: true
date: 2009-06-23 19:15:52
layout: post
slug: nagios-3-1-2-released
title: Nagios 3.1.2 Released
wordpress_id: 136
---

[Nagios 3.1.2 Released](http://www.nagios.org/news/77-news-announcements/205-nagios-312-released) has just been released. I'm not quite sure I want to try it, given the recent fork from [Nagios (Icinga)](http://www.icinga.org), where [all the people who were contributing the interesting plugins and addons](http://www.icinga.org/team/).

Anyway here are the recent notes from the Nagios ChangeLog:
[sourcecode language="text"]
3.1.2 - 06/23/2009
------------------
* Fix for CPU hogging in service and host check scheduling logic

3.1.1 - 06/22/2009
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
* Fix for "Max concurrent service checks (X) has been reached" messages - will now push services 5 + random(10) seconds ahead for
retry
* Fix for removing old HTML files for web frontend that are now replaced with PHP equivalents (index/main/side.html)
* Fix for incorrect service history link text in CGIs
* Fix for useless code loop in netutils.c
* Fix for potential divide by zero in event scheduling code
* Fix for trailing backslash in plugin output causing memory corruption in CGIs
* Fix for bug that could affect host/service scheduling during clock time skew or changes to timeperod definitions between restart
s
* Leading whitespace from continuation lines in configuration files is now stripped out
* Fix for bug where pipe (used by IPC) file descriptors get inherited by child processed (e.g. event handlers) (bug #0000026)
* Fix for failure to daemonize - Nagios now bails (bug #0000011)
* Fix for notifications about flapping starting not processed properly by retention data
* Patch to add transparency to statusmap icons for truecolor images
* Patch to add read-only permissions to extinfo CGI
* Security fix for statuswml.cgi where arbitrary shell injection was possible
[/sourcecode]
