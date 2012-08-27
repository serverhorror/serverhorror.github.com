---
comments: true
date: 2012-01-03 14:00:33
layout: post
slug: golang-package-cappedqueue
title: golang package cappedqueue
wordpress_id: 1502
tags:
- github
- Go
- Google
---

Just finished the first few lines of hopefully somewhat usable go code. The code is available on github in case someone indeed is brave enough to use it...





	
  * [http://github.com/serverhorror/cappedqueue](http://github.com/serverhorror/cappedqueue)


To quote the README.rst file:


> 

> 
> # cappedqueue
> 
> 
cappedqueue is a simple package to make sure you can submit to a queue. Losing items is on purpose so that **you can rely on not accidentally blocking or filling up your memory**

see the `cappedqueue_test.go` file for details on the usage...

/serverhorror
