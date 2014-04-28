---
layout: post
title: Adventures in CentOS-Land (Part 1)
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1259053359";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1259053360";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
<p>So I have to set up a dedicated mail server for my boss' private use. Since we wanted to completely seperate this private use server from our infrastructure "we" (actually our billing department) decided to get a GoDaddy server (a dedicated one). The account was set up and the details were forwarded to us - as happy admins of mostly debian we don't have to deal with non-debian system too often so we were not exactly happy to find only <a href="http://www.fedoraproject.org/">Fedora</a>, <a href="http://www.redhat.com/rhel/">RHEL</a> or <a href="http://www.centos.org/">CentOS</a> as available <a href="http://www.kernel.org/">Linux</a> options. Anyway the account had already been paid for so we went to set it up.</p>
<p>Here are the requirements:</p>
<ul>
<li>nagios for monitoring of
<ul>
<li>disk space</li>
<li>system load</li>
<li>service availability</li>
<li>...</li>
</ul>
</li>
<li>openLDAP (v3 only and TLS only)</li>
<li>SMTP with Sender Authentication over TLS only</li>
<li>IMAPs (only, and only over TLS)</li>
<li>an HTTPs (only) interface to the outside world for our user(s)
<ul>
<li>the Nagios Webinterface for the Administrator(s)</li>
<li>a webmail interface for easy access from anywhere - also TLS only</li>
</ul>
</li>
</ul>
<p>Let's see if your required software is available:

{% highlight text %}
# yum search nagios
Excluding Packages from CentOS-5 - Base
Finished
Excluding Packages from CentOS-5 - Updates
Finished
Excluding Packages from CentOS-5 - Plus
Finished
Reducing CentOS-5 - Plus to included packages only
Finished
Excluding Packages from CentOS-5 - Addons
Finished
Excluding Packages from CentOS-5 - Extras
Finished
No Matches found
{% endhighlight text %}

Shoot nothing here..., let's see where we can find the repo. The <a href="http://wiki.centos.org/AdditionalResources/Repositories">CentOS Wiki Page on Repositories</a> is the first hint. It leads us to the description on <a href="http://wiki.centos.org/AdditionalResources/Repositories/RPMForge">how to enable the rpmforge repository</a>. Let's see what happens after the setup process:

{% highlight text %}
# yum check-update
rpmforge                  100% |=========================| 1.1 kB    00:00
Excluding Packages from CentOS-5 - Base
Finished
Excluding Packages from CentOS-5 - Updates
Finished
Excluding Packages from CentOS-5 - Plus
Finished
Reducing CentOS-5 - Plus to included packages only
Finished
Excluding Packages from CentOS-5 - Addons
Finished
Excluding Packages from CentOS-5 - Extras
Finished</p>
<p>lftp.i386                                3.7.14-1.el5.rf        rpmforge
mtr.i386                                 2:0.75-1.el5.rf        rpmforge
pdns.i386                                2.9.21.1-1.el5.rf      rpmforge
perl-BSD-Resource.i386                   1.2901-1.el5.rf        rpmforge
perl-Compress-Zlib.noarch                2.015-1.el5.rf         rpmforge
perl-Convert-ASN1.noarch                 0.22-1.el5.rf          rpmforge
perl-Crypt-SSLeay.i386                   0.57-1.el5.rf          rpmforge
perl-DBI.i386                            1.609-1.el5.rf         rpmforge
perl-Digest-SHA1.i386                    2.12-1.el5.rf          rpmforge
perl-HTML-Parser.i386                    3.61-1.el5.rf          rpmforge
perl-HTML-Tagset.noarch                  3.20-1.el5.rf          rpmforge
perl-IO-Socket-SSL.noarch                1.26-1.el5.rf          rpmforge
perl-Net-DNS.i386                        0.65-1.el5.rf          rpmforge
perl-Net-SSLeay.i386                     1.35-1.el5.rf          rpmforge
perl-XML-NamespaceSupport.noarch         1.10-1.el5.rf          rpmforge
perl-XML-Parser.i386                     2.36-1.el5.rf          rpmforge
perl-XML-SAX.noarch                      0.96-1.el5.rf          rpmforge
perl-XML-Twig.noarch                     3.32-1.el5.rf          rpmforge
rsync.i386                               3.0.6-1.el5.rf         rpmforge
subversion.i386                          1.6.3-0.1.el5.rf       rpmforge
syslinux.i386                            3.82-1.el5.rf          rpmforge
{% endhighlight text %}

Ouch again, quite a few packages to update. Where did the priority stuff go described in the setup process? After some Googling I found that the Priority Plugin itself is indeed enabled, but the plugin infrastructure that yum has is not there: Doh!</p>
<p>Let's enable the plugin infrastructure..

{% highlight text %}
# vim /etc/yum.conf
{% endhighlight text %}

and let's check the contents:

{% highlight text %}
[main]
cachedir=/var/cache/yum
debuglevel=2
logfile=/var/log/yum.log
pkgpolicy=newest
distroverpkg=redhat-release
tolerant=1
exactarch=1
retries=20
obsoletes=1
gpgcheck=1
metadata_expire=1800
#plugins=1</p>
<p># PUT YOUR REPOS HERE OR IN separate files named file.repo
# in /etc/yum.repos.d
{% endhighlight text %}

Aha! The <em>plugins=1</em> line was missing. Check again that it is indeed working:

{% highlight text %}
# yum check-update
Loading "priorities" plugin
Loading "fastestmirror" plugin
Loading mirror speeds from cached hostfile
 * rpmforge: apt.sw.be
 * base: p3mirror01.prod.phx3.secureserver.net
 * updates: p3mirror01.prod.phx3.secureserver.net
 * contrib: pubmirrors.reflected.net
 * centosplus: p3mirror01.prod.phx3.secureserver.net
 * addons: p3mirror01.prod.phx3.secureserver.net
 * extras: p3mirror01.prod.phx3.secureserver.net
rpmforge                  100% |=========================| 1.1 kB    00:00     
base                      100% |=========================| 1.1 kB    00:00     
updates                   100% |=========================|  951 B    00:00     
contrib                   100% |=========================|  951 B    00:00     
centosplus                100% |=========================|  951 B    00:00     
addons                    100% |=========================|  951 B    00:00     
extras                    100% |=========================| 1.1 kB    00:00     
Excluding Packages from CentOS-5 - Base
Finished
Excluding Packages from CentOS-5 - Updates
Finished
Excluding Packages from CentOS-5 - Plus
Finished
Reducing CentOS-5 - Plus to included packages only
Finished
Excluding Packages from CentOS-5 - Addons
Finished
Excluding Packages from CentOS-5 - Extras
Finished
416 packages excluded due to repository priority protections
{% endhighlight text %}

Success! No updates available from the rpmforge repository. Now let's check wether we got something like nagios (and nrpe for that matter):

{% highlight text %}
# yum list nagios nrpe dovecot postfix openldap-servers openldap-clients openldap
Loading "priorities" plugin
Loading "fastestmirror" plugin
Loading mirror speeds from cached hostfile
 * rpmforge: apt.sw.be
 * base: p3mirror01.prod.phx3.secureserver.net
 * updates: p3mirror01.prod.phx3.secureserver.net
 * contrib: pubmirrors.reflected.net
 * centosplus: p3mirror01.prod.phx3.secureserver.net
 * addons: p3mirror01.prod.phx3.secureserver.net
 * extras: p3mirror01.prod.phx3.secureserver.net
Excluding Packages from CentOS-5 - Base
Finished
Excluding Packages from CentOS-5 - Updates
Finished
Excluding Packages from CentOS-5 - Plus
Finished
Reducing CentOS-5 - Plus to included packages only
Finished
Excluding Packages from CentOS-5 - Addons
Finished
Excluding Packages from CentOS-5 - Extras
Finished
416 packages excluded due to repository priority protections
Installed Packages
dovecot.i386                             1.0.7-2.el5            installed
openldap.i386                            2.3.27-8.el5_2.4       installed
openldap-clients.i386                    2.3.27-8.el5_2.4       installed
openldap-servers.i386                    2.3.27-8.el5_2.4       installed
postfix.i386                             2:2.3.3-2.el5.centos.m installed
Available Packages
nagios.i386                              3.0.6-1.el5.rf         rpmforge
postfix.i386                             2:2.3.3-2              base
{% endhighlight text %}

Success (again)! Tons of nagios and nrpe packages available. Yes I already installed some packages because I thought all I need was available, CentOS is a RHEL clone after all and claims to be Enterprise. How much enterprise can you be if the standard monitoring tool isn't available in the official repositories?</p>
<p>So much for basic package availability in CentOS...see you next time dear CentOS (or rather RHEL)

{% highlight text %}
yum install nagios
Loading "priorities" plugin
Loading "fastestmirror" plugin
Loading mirror speeds from cached hostfile
* rpmforge: ftp-stud.fht-esslingen.de
* base: p3mirror01.prod.phx3.secureserver.net
* updates: p3mirror01.prod.phx3.secureserver.net
* contrib: pubmirrors.reflected.net
* centosplus: p3mirror01.prod.phx3.secureserver.net
* addons: p3mirror01.prod.phx3.secureserver.net
* extras: p3mirror01.prod.phx3.secureserver.net
Excluding Packages from CentOS-5 - Base
Finished
Excluding Packages from CentOS-5 - Updates
Finished
Excluding Packages from CentOS-5 - Plus
Finished
Reducing CentOS-5 - Plus to included packages only
Finished
Excluding Packages from CentOS-5 - Addons
Finished
Excluding Packages from CentOS-5 - Extras
Finished
416 packages excluded due to repository priority protections
Setting up Install Process
Parsing package install arguments
Resolving Dependencies
--> Running transaction check
---> Package nagios.i386 0:3.0.6-1.el5.rf set to be updated
--> Finished Dependency Resolution</p>
<p>Dependencies Resolved</p>
<p>=============================================================================
Package                 Arch       Version          Repository        Size
=============================================================================
Installing:
nagios                  i386       3.0.6-1.el5.rf   rpmforge          3.6 M</p>
<p>Transaction Summary
=============================================================================
Install      1 Package(s)
Update       0 Package(s)
Remove       0 Package(s)</p>
<p>Total download size: 3.6 M
Is this ok [y/N]: N
Exiting on user Command
Complete!
{% endhighlight text %}

