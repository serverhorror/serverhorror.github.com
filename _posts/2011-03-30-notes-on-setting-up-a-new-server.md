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
<h2>A typical Machine</h2>
<h3>Prepare Stuff as root</h3>
<p>{% highlight text %}<br />
passwd -l root<br />
apt-get install sudo<br />
adduser $SYSTEM_USER<br />
adduser $SYSTEM_USER adm<br />
adduser $SYSTEM_USER staff<br />
adduser $SYSTEM_USER sudo<br />
su - $SYSTEM_USER<br />
{% endhighlight %}<br />
{% highlight text %}<br />
sudo -l # verify $SYSTEM_USER can actually use sudo...<br />
exit<br />
{% endhighlight %}<br />
{% highlight text %}<br />
exit<br />
{% endhighlight %}</p>
<h3>Now work with <code>$SYSTEM_USER</code></h3>
<p>{% highlight text %}<br />
sudo apt-get update<br />
sudo apt-get upgrade --yes<br />
sudo apt-get install --yes vim<br />
sudo apt-get remove --purge --yes nano<br />
sudo update-alternatives --display editor|head -n2<br />
sudo apt-get install procps lsof lsb-release bash-completion curl git-core -y<br />
source ./etc/bash_completion<br />
grep -q -i '^PermitRootLogin' /etc/ssh/sshd_config &amp;&amp; sudo sed -i.bak -e 's/^PermitRootLogin (.*)/PermitRootLogin no/' /etc/ssh/sshd_config<br />
sudo pkill -SIGHUP -u root -f /usr/sbin/sshd<br />
{% endhighlight %}</p>
