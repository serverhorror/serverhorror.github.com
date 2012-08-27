---
comments: true
date: 2011-03-30 12:00:19
layout: post
slug: notes-on-setting-up-a-new-server
title: 'Notes on: Setting up a new Server'
wordpress_id: 1215
tags:
- notes
- Operating Systems
- sysadmin
- Ubuntu
- Unix
---

## A typical Machine




### Prepare Stuff as root


[sourcecode language="bash"]
passwd -l root
apt-get install sudo
adduser $SYSTEM_USER
adduser $SYSTEM_USER adm
adduser $SYSTEM_USER staff
adduser $SYSTEM_USER sudo
su - $SYSTEM_USER
[/sourcecode]
[sourcecode language="bash"]
sudo -l # verify $SYSTEM_USER can actually use sudo...
exit
[/sourcecode]
[sourcecode language="bash"]
exit
[/sourcecode]


### Now work with `$SYSTEM_USER`


[sourcecode language="bash"]
sudo apt-get update
sudo apt-get upgrade --yes
sudo apt-get install --yes vim
sudo apt-get remove --purge --yes nano
sudo update-alternatives --display editor|head -n2
sudo apt-get install procps lsof lsb-release bash-completion curl git-core -y
source ./etc/bash_completion
grep -q -i '^PermitRootLogin' /etc/ssh/sshd_config && sudo sed -i.bak -e 's/^PermitRootLogin (.*)/PermitRootLogin no/' /etc/ssh/sshd_config
sudo pkill -SIGHUP -u root -f /usr/sbin/sshd
[/sourcecode]
