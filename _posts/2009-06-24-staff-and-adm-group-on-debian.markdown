---
comments: true
date: 2009-06-24 16:00:23
layout: post
slug: staff-and-adm-group-on-debian
title: '`staff` and `adm` Group on Debian Boxes'
wordpress_id: 160
tags:
- sysadmin
---

We had quite a few discussions on our internal usage of the filesystem. Usually we try to keep to the [Linux FHS](http://www.pathname.com/fhs/). That is we use _**/srv**_** for application data**, **_/opt_ for local installations of 3rd party software**. But so far we couldn't get an agreement on how to deal with _/usr/local_.

One thing that bugged us was: "**What the hell is the `**_**staff**_**` group about anyway**". Well I started investigating a bit.



	
  * what is actually writeable according to the [Debian Policy](http://www.debian.org/doc/debian-policy/)

	
  * what is actually writeable (now really)


According to the [Debian Policy](http://www.debian.org/doc/debian-policy/) there are 2 groups prepared for a site to use, those are:



	
  * _staff_ and

	
  * _adm_


The [Securing Debian HOWTO](http://www.debian.org/doc/manuals/securing-debian-howto/) mentions it's uses in the FAQ part in chapter 12:



	
  * [What is the difference between the adm and the staff group?](http://www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html#s12.1.12.3)


However that wasn't good enough for me, so I fired up a new debian instance and had a look at which files (or directories for that matter) are actually writable by the staff group:

{% highlight text %}
sudo find / -xdev -group staff -perm +0020 -exec ls -ld {} \;
{% endhighlight %}


Long story short: It seems only 2 directories are writeable:



	
  * /var/local

	
  * /usr/local


of course that includes all the subdirectories in a default Debian installation. While we're at it we can also check the same for the `adm` group:

{% highlight text %}
sudo find / -xdev -group adm -perm +0020 -exec ls -ld {} \;
{% endhighlight %}

Interestingly enough, nothing came back. So let's check what we can read with this group and also what the `staff` group can read:

{% highlight text %}
sudo find / -xdev -group adm -perm +0010 -exec ls -ld {} \;
sudo find / -xdev -group staff -perm +0010 -exec ls -ld {} \;
{% endhighlight %}


The `_adm_` group returned a few hits in the `_/var/log_` directory while the `_staff_` group had read access to everything under `_/var/local_` and `_/usr/local`_. From my point of view it seems that `_staff_` and `_adm_` are perfectly useable for administrators as long as there aren't any critical packages installed by "exploiting" these memberships. I rather see such things installed by creating a proper package and using _apt-get_.



Of course there should be some testing done on a regular basis that no files or directories are in a place where `_staff_` or `_adm_` people shouldn't write to.

Now I just need to completely convince my colleagues to use an existing infrastructure instead of further maintaining our home grown solution.
