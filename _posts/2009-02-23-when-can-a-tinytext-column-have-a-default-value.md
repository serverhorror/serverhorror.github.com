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
<p><a href="http://www.flamingspork.com/blog/2009/02/24/when-can-a-tinytext-column-have-a-default-value/">This</a>:<br />
[sourcecode language="text"]<br />
$ mysql -u root test<br />
Welcome to the MySQL monitor.  Commands end with ; or \g.<br />
Your MySQL connection id is 2496<br />
Server version: 5.0.51a-3ubuntu5.4-log (Ubuntu)</p>
<p>Type 'help;' or '\h' for help. Type '\c' to clear the buffer.</p>
<p>mysql&gt; create table t1 (a tinytext default 'fail');<br />
ERROR 1101 (42000): BLOB/TEXT column 'a' can't have a default value<br />
mysql&gt; create table t1 (a tinytext default '');<br />
Query OK, 0 rows affected, 1 warning (0.07 sec)</p>
<p>mysql&gt; show warnings;<br />
+---------+------+-------------------------------------------------+<br />
| Level   | Code | Message                                         |<br />
+---------+------+-------------------------------------------------+<br />
| Warning | 1101 | BLOB/TEXT column 'a' can't have a default value |<br />
+---------+------+-------------------------------------------------+<br />
1 row in set (0.00 sec)<br />
[/sourcecode]<br />
wouldn't have happened with a <a href="http://www.postgresql.org">real database</a>:<br />
[sourcecode language="text"]<br />
test=# create TABLE xxxx(<br />
test(#  id serial,<br />
test(#  bla text default 'foo'<br />
test(# );<br />
NOTICE:  CREATE TABLE will create implicit sequence &quot;xxxx_id_seq&quot; for serial column &quot;xxxx.id&quot;<br />
CREATE TABLE<br />
test=# INSERT into xxxx (id) values (1);<br />
INSERT 0 1<br />
test=# SELECT * from xxxx;<br />
 id | bla<br />
----+-----<br />
  1 | foo<br />
(1 row)<br />
[/sourcecode]</p>
