---
comments: true
date: 2009-02-23 21:30:00
layout: post
slug: when-can-a-tinytext-column-have-a-default-value
title: When can a TINYTEXT column have a default value?
wordpress_id: 252
tags:
- sysadmin
---

[This](http://www.flamingspork.com/blog/2009/02/24/when-can-a-tinytext-column-have-a-default-value/):
[sourcecode language="text"]
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
[/sourcecode]
wouldn't have happened with a [real database](http://www.postgresql.org):
[sourcecode language="text"]
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
[/sourcecode]
