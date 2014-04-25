---
layout: post
title: Scripting VirtualBox with VBoxManage
categories: []
tags:
- automation
- Mac OS X
- Operating system
- sysadmin
- Virtual machine
- virtualbox
- virtualization
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1319931925";}
  _wpas_done_yup: '1'
  _wpas_done_twitter: '1'
  _wpas_done_fb: '1'
author: 
---
<p>Well <strong>not really scripting</strong>. Merely a note on the basic usage of <code>VBoxManage</code> so that I can remember how to quickly create guest machines with lots of disks.</p>
<h2>Get Basic Info About What We Need</h2>
<p>{% highlight text %}<br />
VBoxManage list<br />
VBoxManage list ostypes<br />
{% endhighlight %}</p>
<h2>Create a Guest and Register it to be visible in the GUI</h2>
<p>{% highlight text %}<br />
VBoxManage createvm --name clitest --ostype Linux26_64<br />
VBoxManage registervm ~/VirtualBox\ VMs/clitest/clitest.vbox<br />
VBoxManage list vms<br />
{% endhighlight %}</p>
<h2>Adjust the settings</h2>
<p>{% highlight text %}<br />
VBoxManage modifyvm clitest --vram 16<br />
VBoxManage modifyvm clitest --memory 1024<br />
VBoxManage modifyvm clitest --boot1 dvd --boot2 disk --boot3 none<br />
VBoxManage modifyvm clitest --acpi on --ioapic on<br />
VBoxManage modifyvm clitest --nictype1 virtio --nic1 bridged<br />
# This is on Mac OS X so you might need to fiddle around with the name of --bridgeadapter1<br />
VBoxManage modifyvm clitest --bridgeadapter1 en0:\ Ethernet --cableconnected1 on<br />
VBoxManage modifyvm clitest --chipset ich9<br />
VBoxManage modifyvm clitest --firmware bios<br />
{% endhighlight %}</p>
<h2>Create a disk to boot from</h2>
<p>{% highlight text %}<br />
VBoxManageo vbm createhd --filename ~/VirtualBox\ VMs/clitest/root.vdi --size $((2**10 * 5))<br />
{% endhighlight %}</p>
<h2>Create a SATA Controller</h2>
<p>{% highlight text %}<br />
VBoxManage storagectl clitest --name SATA\ Controller --add sata --sataportcount 2 --bootable on<br />
{% endhighlight %}</p>
<h2>Attach an ISO image and disk to the Guest</h2>
<p>{% highlight text %}<br />
VBoxManage storageattach clitest --storagectl SATA\ Controller --port 0 --device 0 --type dvddrive --medium ~/ISOs/Fedora-13-x86_64-netinst.iso<br />
VBoxManage storageattach clitest --storagectl SATA\ Controller --port 1 --device 0 --type hdd --medium clitest/root.vdi<br />
{% endhighlight %}</p>
<h2>Boot it</h2>
<p>{% highlight text %}<br />
VBoxManage startvm clitest --type gui<br />
{% endhighlight %}</p>
