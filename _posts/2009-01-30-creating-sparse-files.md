---
layout: post
title: Creating Sparse Files
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2009/01/creating-sparse-files.html
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
<p>This is something I really tend to forget: <strong>How do you create a sparse file in unix?</strong><br />
[sourcecode language="text"]<br />
dd if=/dev/zero of=/tmp/sparsefile.sparse bs=1 count=0 seek=5M<br />
[/sourcecode]<br />
From <a href="http://en.wikipedia.org/wiki/Sparse_file">Wikipedia</a> about what a sparse file is:</p>
<blockquote><p>In <a title="Computer science" href="http://en.wikipedia.org/wiki/Computer_science">computer science</a>, a <strong>sparse file</strong> is a type of <a title="Computer file" href="http://en.wikipedia.org/wiki/Computer_file">computer file</a> that attempts to use <a title="File system" href="http://en.wikipedia.org/wiki/File_system">file system</a> space more efficiently when blocks allocated to the file are mostly empty.</p></blockquote>
