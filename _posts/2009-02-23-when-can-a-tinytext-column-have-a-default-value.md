---
layout: post
title: When can a TINYTEXT column have a default value?
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2009/02/when-can-tiny-text-column-have-default.html
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
<a href="http://www.flamingspork.com/blog/2009/02/24/when-can-a-tinytext-column-have-a-default-value/">This</a>:

{% highlight text %}
$ mysql -u root test
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2496
Server version: 5.0.51a-3ubuntu5.4-log (Ubuntu)
Type 'help;' or '\h' for help. Type '\c' to clear the buffer.
mysql> create table t1 (a tinytext default 'fail');
ERROR 1101 (42000): BLOB/TEXT column 'a' can't have a default value
mysql> create table t1 (a tinytext default '');
Query OK, 0 rows affected, 1 warning (0.07 sec)
mysql> show warnings;
+---------+------+-------------------------------------------------+
| Level   | Code | Message                                         |
+---------+------+-------------------------------------------------+
| Warning | 1101 | BLOB/TEXT column 'a' can't have a default value |
+---------+------+-------------------------------------------------+
1 row in set (0.00 sec)
{% endhighlight %}

wouldn't have happened with a <a href="http://www.postgresql.org">real database</a>:

{% highlight text %}
test=# create TABLE xxxx(
test(#  id serial,
test(#  bla text default 'foo'
test(# );
NOTICE:  CREATE TABLE will create implicit sequence "xxxx_id_seq" for serial column "xxxx.id"
CREATE TABLE
test=# INSERT into xxxx (id) values (1);
INSERT 0 1
test=# SELECT * from xxxx;
 id | bla
----+-----
  1 | foo
(1 row)
{% endhighlight %}
