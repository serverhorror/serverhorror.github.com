---
comments: true
date: 2011-02-07 00:01:38
layout: post
slug: mysql-tab-completion
title: MySQL tab completion (which sucks anyway)
wordpress_id: 1129
tags:
- Database
- MySQL
- sysadmin
---

Since the [MySQL](http://www.mysql.com) tab completion sucks anyway, but I usually forget how to enable it here's how:

{% highlight ini %}
[mysql]
#no-auto-rehash # faster start of mysql but no tab completion
auto-rehash
{% endhighlight %}

If you can't control the server and [`auto-rehash`](http://dev.mysql.com/doc/refman/5.1/en/mysql-command-options.html#option_mysql_auto-rehash) isn't enabled:

{% highlight sql %}
rehash; -- rehash the database/table names for this session (from this point in time)
{% endhighlight %}
