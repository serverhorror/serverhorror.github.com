---
layout: post
title: 'Notes on: Setting up a new Server'
categories: []
tags:
- notes
- Operating Systems
- sysadmin
- Ubuntu
- Unix
status: publish
type: post
published: true
meta:
  _wpas_done_yup: '1'
  _wpas_done_twitter: '1'
  _wpas_done_fb: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1320179127";}
author: 
---
## A typical Machine
### Prepare Stuff as root
{% highlight bash %}
passwd -l root
apt-get install sudo
adduser $SYSTEM_USER
adduser $SYSTEM_USER adm
adduser $SYSTEM_USER staff
adduser $SYSTEM_USER sudo
su - $SYSTEM_USER
{% endhighlight %}
{% highlight bash %}
sudo -l # verify $SYSTEM_USER can actually use sudo...
exit
{% endhighlight %}
{% highlight bash %}
exit
{% endhighlight %}
### Now work with `$SYSTEM_USER`
{% highlight bash %}
sudo apt-get update
sudo apt-get upgrade --yes
sudo apt-get install --yes vim
sudo apt-get remove --purge --yes nano
sudo update-alternatives --display editor|head -n2
sudo apt-get install procps lsof lsb-release bash-completion curl git-core -y
source ./etc/bash_completion
grep -q -i '^PermitRootLogin' /etc/ssh/sshd_config &amp;&amp; sudo sed -i.bak -e 's/^PermitRootLogin (.*)/PermitRootLogin no/' /etc/ssh/sshd_config
sudo pkill -SIGHUP -u root -f /usr/sbin/sshd
{% endhighlight %}
