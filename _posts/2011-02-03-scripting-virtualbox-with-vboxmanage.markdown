---
comments: true
date: 2011-02-03 10:24:53
layout: post
slug: scripting-virtualbox-with-vboxmanage
title: Scripting VirtualBox with VBoxManage
wordpress_id: 1037
tags:
- automation
- Mac OS X
- Operating system
- sysadmin
- Virtual machine
- virtualbox
- virtualization
---

Well **not really scripting**. Merely a note on the basic usage of `VBoxManage` so that I can remember how to quickly create guest machines with lots of disks.


## Get Basic Info About What We Need


[sourcecode]
VBoxManage list
VBoxManage list ostypes
{% endhighlight %}


## Create a Guest and Register it to be visible in the GUI


[sourcecode]
VBoxManage createvm --name clitest --ostype Linux26_64
VBoxManage registervm ~/VirtualBox\ VMs/clitest/clitest.vbox
VBoxManage list vms
{% endhighlight %}


## Adjust the settings


[sourcecode]
VBoxManage modifyvm clitest --vram 16
VBoxManage modifyvm clitest --memory 1024
VBoxManage modifyvm clitest --boot1 dvd --boot2 disk --boot3 none
VBoxManage modifyvm clitest --acpi on --ioapic on
VBoxManage modifyvm clitest --nictype1 virtio --nic1 bridged
# This is on Mac OS X so you might need to fiddle around with the name of --bridgeadapter1
VBoxManage modifyvm clitest --bridgeadapter1 en0:\ Ethernet --cableconnected1 on
VBoxManage modifyvm clitest --chipset ich9
VBoxManage modifyvm clitest --firmware bios
{% endhighlight %}


## Create a disk to boot from


[sourcecode]
VBoxManageo vbm createhd --filename ~/VirtualBox\ VMs/clitest/root.vdi --size $((2**10 * 5))
{% endhighlight %}


## Create a SATA Controller


[sourcecode]
VBoxManage storagectl clitest --name SATA\ Controller --add sata --sataportcount 2 --bootable on
{% endhighlight %}


## Attach an ISO image and disk to the Guest


[sourcecode]
VBoxManage storageattach clitest --storagectl SATA\ Controller --port 0 --device 0 --type dvddrive --medium ~/ISOs/Fedora-13-x86_64-netinst.iso
VBoxManage storageattach clitest --storagectl SATA\ Controller --port 1 --device 0 --type hdd --medium clitest/root.vdi
{% endhighlight %}


## Boot it


[sourcecode]
VBoxManage startvm clitest --type gui
{% endhighlight %}
