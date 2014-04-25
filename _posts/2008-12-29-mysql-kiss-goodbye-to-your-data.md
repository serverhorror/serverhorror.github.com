---
layout: post
title: MySQL - kiss goodbye to your data
categories: []
tags: []
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2008/12/mysql-kiss-goodbye-to-your-data.html
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
<p><a href="http://www.planetmysql.org">Planet MySQL</a> had a <a href="http://www.pythian.com/blogs/1422/draft-mind-the-sql_mode-when-running-alter-table#more-1422">blog post about some strange behaviour</a> <a href="http://www.mysql.com">MySQL</a> is showing</p>
<p><strong>Step One</strong>: Create a table with a primary key<br />
[sourcecode language="text"]<br />
mysql&gt; use test;<br />
Database changed<br />
mysql&gt; show tables;<br />
Empty set (0.00 sec)</p>
<p>mysql&gt; create table test_table (id int not null primary key) engine=innodb;<br />
Query OK, 0 rows affected (0.01 sec)</p>
<p>mysql&gt; desc test_table;<br />
+-------+---------+------+-----+---------+-------+<br />
| Field | Type    | Null | Key | Default | Extra |<br />
+-------+---------+------+-----+---------+-------+<br />
| id    | int(11) | NO   | PRI |         |       |<br />
+-------+---------+------+-----+---------+-------+<br />
1 row in set (0.00 sec)</p>
<p>mysql&gt; insert into test_table (id) values (1);<br />
Query OK, 1 row affected (0.00 sec)</p>
<p>mysql&gt; insert into test_table (id) values (2);<br />
Query OK, 1 row affected (0.00 sec)</p>
<p>mysql&gt; insert into test_table (id) values (0);<br />
Query OK, 1 row affected (0.00 sec)</p>
<p>mysql&gt; select * from test_table;<br />
+----+<br />
| id |<br />
+----+<br />
|  0 |<br />
|  1 |<br />
|  2 |<br />
+----+<br />
3 rows in set (0.00 sec)</p>
<p>mysql&gt;<br />
[/sourcecode]<br />
<strong>Step Two</strong>: Alter the table to an auto_increment<br />
[sourcecode language="text"]<br />
mysql&gt; alter table test_table modify id int not null auto_increment, auto_increment=3;<br />
Query OK, 3 rows affected (0.03 sec)<br />
Records: 3  Duplicates: 0  Warnings: 0</p>
<p>mysql&gt; select * from test_table;<br />
+----+<br />
| id |<br />
+----+<br />
|  1 |<br />
|  2 |<br />
|  3 |<br />
+----+<br />
3 rows in set (0.00 sec)</p>
<p>mysql&gt;<br />
[/sourcecode]<br />
<strong>Step Three</strong>: Kiss goodbye to your data</p>
<p>To be fair: There is a solution to this, but personally I think that should be the default, or at least there should be the a warning or error when such a statement is altering your data.<br />
[sourcecode language="text"]<br />
mysql&gt; set sql_mode='NO_AUTO_VALUE_ON_ZERO';<br />
Query OK, 0 rows affected (0.00 sec)</p>
<p>mysql&gt; select @@session.sql_mode;<br />
+-----------------------+<br />
| @@session.sql_mode    |<br />
+-----------------------+<br />
| NO_AUTO_VALUE_ON_ZERO |<br />
+-----------------------+<br />
1 row in set (0.00 sec)<br />
[/sourcecode]</p>
