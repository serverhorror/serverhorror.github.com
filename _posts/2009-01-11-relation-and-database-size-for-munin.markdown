---
comments: true
date: 2009-01-11 17:15:00
layout: post
slug: relation-and-database-size-for-munin
title: Relation and Database size for munin
wordpress_id: 247
tags:
- sysadmin
---

Since we are running into some minor scaling problems at work and [Munin](http://munin.projects.linpro.no/) doesn't provide the necessary information out of the box I created a small script that let's you see the relation size total relation size and also the database size of a [PostgreSQL](http://www.postgresql.org/) database.

The necessary information is quite easy to find in the [PostgreSQL documentation](http://www.postgresql.org/docs/current/interactive/functions-admin.html#FUNCTIONS-ADMIN-DBSIZE). And with [Python](http://www.python.org/) at hand you have a tool that let's you easily create the [necessary script, available at my github repository](http://github.com/mm/munin-plugins/tree/master/pg_dbsize_.py).

The usage is simple just copy the script to a suitable place - personally I'd suggest either a directory under /opt oder /usr/local/bin - as my understanding of the [Linux FHS](http://www.pathname.com/fhs/) is that this is just the right place.

When you're done make the script executable and symlink it to:



	
  * pg_dbsize_ or

	
  * pg_relation_size_ or

	
  * pg_total_relation_size_ (this includes [TOAST](http://www.postgresql.org/docs/current/interactive/storage-toast.html#STORAGE-TOAST) and indexes)


The latter two require to configure munin with at least a PG_DB environment variable so that the relation name is qualified and the functions used in the script will find the relation. The first form should just work.

Get the script here:



	
  * [http://github.com/mm/munin-plugins/tree/master/pg_dbsize_.py](http://github.com/mm/munin-plugins/tree/master/pg_dbsize_.py)


