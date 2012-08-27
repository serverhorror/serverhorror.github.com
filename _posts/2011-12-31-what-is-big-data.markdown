---
comments: true
date: 2011-12-31 14:00:44
layout: post
slug: what-is-big-data
title: What is big data?
wordpress_id: 1470
tags:
- Big data
- Data analysis
- Data Warehousing
- Databases
- Hadoop
- Hardware
- PostgreSQL
- Storage
---

It’s actually quite simple: You have [big data](http://en.wikipedia.org/wiki/Big_data) whenever a single host isn’t enough to either store or process your data.


# What does it mean?


Suppose you have a [Postgresql](http://en.wikipedia.org/wiki/PostgreSQL) Database and you run into scaling problems. There’s a choice now, either get _better hardware_ so that you can continue to work on a single host or **split the database to span multiple hosts**.

Suppose you have a file store and all disks are full. You can either buy larger disks or use some distributed storage system where you **just add hosts to expand the total storage capacity**.

**In both cases you are dealing with big data.**

Big data (_for me_) isn’t anything that says X MB of data. It’s simply the case when you need decide to use a distributed system to handle your data.
