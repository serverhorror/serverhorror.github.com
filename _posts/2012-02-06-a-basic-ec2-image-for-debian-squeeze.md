---
layout: post
title: A Basic EC2 Image for Debian/Squeeze
categories: []
tags: []
status: draft
type: post
published: false
meta: {}
author: 
---
<p>{% highlight text %}
dd if=/dev/zero of=ec2-debian-squeeze-x64.img bs=1 count=0 seek=10G
sudo mkfs.ext3 -F -Odir_index ec2-debian-squeeze-x64.img
mkdir ec2
sudo mount -oloop ec2-debian-squeeze-x64.img ec2
sudo debootstrap --include=sudo,vim,bzip2,rsync,mtr-tiny,openssh-server,git-core,bash-completion,curl,dnsutils,git,xz-utils,xz-lzma,curl,makedev,locales --exclude=nano --arch amd64 squeeze ec2/ http://ftp.de.debian.org/debian
{% endhighlight %}</p>
