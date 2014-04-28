---
layout: post
title: '`staff` and `adm` Group on Debian Boxes'
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1248107894";}
  delicious: a:3:{s:5:"count";s:1:"1";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1248107893";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
We had quite a few discussions on our internal usage of the filesystem. Usually we try to keep to the <a href="http://www.pathname.com/fhs/">Linux FHS</a>. That is we use <em><strong>/srv</strong></em><strong> for application data</strong>, <strong><em>/opt</em> for local installations of 3rd party software</strong>. But so far we couldn't get an agreement on how to deal with <em>/usr/local</em>.

One thing that bugged us was: "<strong>What the hell is the `</strong><em><strong>staff</strong></em><strong>` group about anyway</strong>". Well I started investigating a bit.

* what is actually writeable according to the <a href="http://www.debian.org/doc/debian-policy/">Debian Policy</a>
* what is actually writeable (now really)

According to the <a href="http://www.debian.org/doc/debian-policy/">Debian Policy</a> there are 2 groups prepared for a site to use, those are:

* <em>staff</em> and
* <em>adm</em>

The <a href="http://www.debian.org/doc/manuals/securing-debian-howto/">Securing Debian HOWTO</a> mentions it's uses in the FAQ part in chapter 12:

* <a href="http://www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html#s12.1.12.3">What is the difference between the adm and the staff group?</a>

However that wasn't good enough for me, so I fired up a new debian instance and had a look at which files (or directories for that matter) are actually writable by the staff group:

{% highlight bash %}
sudo find / -xdev -group staff -perm +0020 -exec ls -ld {} \;
{% endhighlight text %}

Long story short: It seems only 2 directories are writeable:

* /var/local
* /usr/local

of course that includes all the subdirectories in a default Debian installation. While we're at it we can also check the same for the `adm` group:

{% highlight bash %}
sudo find / -xdev -group adm -perm +0020 -exec ls -ld {} \;
{% endhighlight text %}

Interestingly enough, nothing came back. So let's check what we can read with this group and also what the `staff` group can read:

{% highlight bash %}
sudo find / -xdev -group adm -perm +0010 -exec ls -ld {} \;
sudo find / -xdev -group staff -perm +0010 -exec ls -ld {} \;
{% endhighlight text %}

The `<em>adm</em>` group returned a few hits in the `<em>/var/log</em>` directory while the `<em>staff</em>` group had read access to everything under `<em>/var/local</em>` and `<em>/usr/local`</em>. From my point of view it seems that `<em>staff</em>` and `<em>adm</em>` are perfectly useable for administrators as long as there aren't any critical packages installed by "exploiting" these memberships. I rather see such things installed by creating a proper package and using <em>apt-get</em>.

Of course there should be some testing done on a regular basis that no files or directories are in a place where `<em>staff</em>` or `<em>adm</em>` people shouldn't write to.

Now I just need to completely convince my colleagues to use an existing infrastructure instead of further maintaining our home grown solution.
