---
layout: post
title: Relation and Database size for munin
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2009/01/relation-and-database-size-for-munin.html
author: 
---
<p>Since we are running into some minor scaling problems at work and <a href="http://munin.projects.linpro.no/">Munin</a> doesn't provide the necessary information out of the box I created a small script that let's you see the relation size total relation size and also the database size of a <a href="http://www.postgresql.org/">PostgreSQL</a> database.</p>
<p>The necessary information is quite easy to find in the <a href="http://www.postgresql.org/docs/current/interactive/functions-admin.html#FUNCTIONS-ADMIN-DBSIZE">PostgreSQL documentation</a>. And with <a href="http://www.python.org/">Python</a> at hand you have a tool that let's you easily create the <a href="http://github.com/mm/munin-plugins/tree/master/pg_dbsize_.py">necessary script, available at my github repository</a>.</p>
<p>The usage is simple just copy the script to a suitable place - personally I'd suggest either a directory under <span style="font-style:italic;">/opt</span> oder <span style="font-style:italic;">/usr/local/bin</span> - as my understanding of the <a href="http://www.pathname.com/fhs/">Linux FHS</a> is that this is just the right place.</p>
<p>When you're done make the script executable and symlink it to:</p>
<ul>
<li><span style="font-style:italic;">pg_dbsize_</span> or</li>
<li><span style="font-style:italic;">pg_relation_size_</span> or</li>
<li><span style="font-style:italic;">pg_total_relation_size_</span> (this includes <a href="http://www.postgresql.org/docs/current/interactive/storage-toast.html#STORAGE-TOAST">TOAST</a> and indexes)</li>
</ul>
<p>The latter two require to configure munin with at least a <span style="font-style:italic;">PG_DB</span> environment variable so that the relation name is qualified and the functions used in the script will find the relation. The first form should just work.</p>
<p>Get the script here:</p>
<ul>
<li><a href="http://github.com/mm/munin-plugins/tree/master/pg_dbsize_.py">http://github.com/mm/munin-plugins/tree/master/pg_dbsize_.py</a></li>
</ul>
