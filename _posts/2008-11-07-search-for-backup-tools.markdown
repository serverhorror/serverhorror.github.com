---
comments: true
date: 2008-11-07 22:45:00
layout: post
slug: search-for-backup-tools
title: Search for Backup Tools
wordpress_id: 205
tags:
- sysadmin
---

This is a thing that annoys me. Backups should just work, the things I found work best are [Bacula](http://www.bacula.org/) and [amanda](http://www.amanda.org/).

While [Bacula ](http://www.bacula.org/en/)needs quite a setup (database, director and storage -- which you still can install on a single machine), it is indeed easier for me to use than [amanda](http://www.amanda.org/) for me.

[amanda](http://www.amanda.org/) does work once it's set up but I my personal opinion is that it should be a real daemon and not "just a cron job". [Bacula](http://www.bacula.org/en/) runs as a true daemon and can decide when it's best to backup a client. So my suggestion goes for [Bacula](http://www.bacula.org/en/).
