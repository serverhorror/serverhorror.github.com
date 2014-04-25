---
layout: post
title: 'HowTo: Mirror the ZFS rpool'
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1270743928";}
  _wpas_done_twitter: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1270743938";}
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
<p>[digg=http://digg.com/linux_unix/HowTo_Mirror_the_ZFS_rpool_ServerHorror]</p>
<p>Let's use the shiny ZFS to have a mirrored pool which we can use to boot in case one of the hard disks fails. This involves several steps :</p>
<ol>
<li>Install a second disk in your box :)</li>
<li>format the disk so that we can actually use it</li>
<li>make it the same layout as the disk we already run on</li>
<li>attach it to the pool in question</li>
</ol>
<p>Now point (3) and (4) need some explanation since I'm experimenting with the root pool (nothing better than a little thrill not being able to boot if things go wrong) and my computer uses the good old <a href="http://en.wikipedia.org/wiki/BIOS">BIOS</a> it cannot boot <a href="http://en.wikipedia.org/wiki/Extensible_Firmware_Interface">EFI</a> labeled disks. For this reason I have to use slices, I'll probably rip out some old storage box in the next weeks and see how much of this process is left when using whole disks.</p>
<p>I assume you are indeed capable of physically installing a second, third or n<sup>th</sup> disk in your computer so let's jump to point (2).</p>
<h1>Formatting the disk(s)</h1>
<p>Simply use "format" :)
{% highlight text %}
$ pfexec format
Searching for disks...done</p>
<p>AVAILABLE DISK SELECTIONS:
 0. c8t0d0 &lt;DEFAULT cyl 30398 alt 2 hd 255 sec 63&gt;
 /pci@0,0/pci103c,3035@1f,2/disk@0,0
 1. c8t2d0 &lt;ATA-ST3250310AS-C cyl 30398 alt 2 hd 255 sec 63&gt;
 /pci@0,0/pci103c,3035@1f,2/disk@2,0
Specify disk (enter its number): 1
selecting c8t2d0
[disk formatted]</p>
<p>FORMAT MENU:
 disk       - select a disk
 type       - select (define) a disk type
 partition  - select (define) a partition table
 current    - describe the current disk
 format     - format and analyze the disk
 fdisk      - run the fdisk program
 repair     - repair a defective sector
 label      - write label to the disk
 analyze    - surface analysis
 defect     - defect list management
 backup     - search for backup labels
 verify     - read and display labels
 save       - save new disk/partition definitions
 inquiry    - show vendor, product and revision
 volname    - set 8-character volume name
 !&lt;cmd&gt;     - execute &lt;cmd&gt;, then return
 quit
{% endhighlight %}
No go "fdisk" it and delete all the partitions on the disk. Then create a new partition, make it a Solaris partition and be done with that part.
{% highlight text %}
format&gt; fdisk
Total disk size is 30401 cylinders
 Cylinder size is 16065 (512 byte) blocks</p>
<p> Cylinders
 Partition   Status    Type          Start   End   Length    %
 =========   ======    ============  =====   ===   ======   ===
 1       Active    Solaris2          1  30400    30400    100</p>
<p>SELECT ONE OF THE FOLLOWING:
 1. Create a partition
 2. Specify the active partition
 3. Delete a partition
 4. Change between Solaris and Solaris2 Partition IDs
 5. Exit (update disk configuration and exit)
 6. Cancel (exit without updating disk configuration)
Enter Selection: 3
Specify the partition number to delete (or enter 0 to exit): 1
Are you sure you want to delete partition 1? This will make all files and
programs in this partition inaccessible (type &quot;y&quot; or &quot;n&quot;).
y
Partition 1 has been deleted. This was the active partition.
Enter Selection: 1
Select the partition type to create:
 1=SOLARIS2  2=UNIX        3=PCIXOS     4=Other
 5=DOS12     6=DOS16       7=DOSEXT     8=DOSBIG
 9=DOS16LBA  A=x86 Boot    B=Diagnostic C=FAT32
 D=FAT32LBA  E=DOSEXTLBA   F=EFI        0=Exit? 1
Specify the percentage of disk to use for this partition
(or type &quot;c&quot; to specify the size in cylinders). 100
Should this become the active partition? If yes, it  will be activated
each time the computer is reset or turned on.
Please type &quot;y&quot; or &quot;n&quot;. y
Partition 1 is now the active partition.
Enter Selection: 5
{% endhighlight %}</p>
<h1>Duplicate the disk layout on both disks</h1>
<p>Now OpenSolaris provides us with 2 nice tools to make one disk have exactly the same layout as another disk. Use them like below:
{% highlight text %}
$ pfexec prtvtoc /dev/rdsk/c8t0d0s2 # first disk
$ pfexec prtvtoc /dev/rdsk/c8t2d0s2 # second disk
$ pfexec prtvtoc /dev/rdsk/c8t0d0s2 | pfexec fmthard -s - /dev/rdsk/c8t2d0s2 # make the 1st disk the same as the 2nd
{% endhighlight %}</p>
<h1>Attach it to the pool in question</h1>
<p>Let's have a quick look at the existing pool:
{% highlight text %}
$ zpool status
 pool: rpool
 state: ONLINE
 scrub: scrub completed after 0h26m with 0 errors on Wed Nov 25 10:52:26 2009
config:</p>
<p> NAME        STATE     READ WRITE CKSUM
 rpool       ONLINE       0     0     0
 c8t0d0s0    ONLINE       0     0     0</p>
<p>errors: No known data errors
{% endhighlight %}
Nice we now see what our original device name is and what our pool name is, we need both for the next command. Remember in my example the new disk slice (the BIOS vs. EFI thing) is  <em>c8t2d0s0</em>. We should be all fine to attach the slice to the pool and see it start recovering.<em></em>
{% highlight text %}
$ pfexec zpool attach rpool c8t0d0s0 c8t2d0s0
invalid vdev specification
use '-f' to override the following errors:
/dev/dsk/c8t2d0s0 overlaps with /dev/dsk/c8t2d0s2
{% endhighlight %}
Ouch, didn't quite work, so let's do as instructed, and right thereafter let's investigate the staus of the pool:
{% highlight text %}
$ pfexec zpool attach -f rpool c8t0d0s0 c8t2d0s0
Please be sure to invoke installgrub(1M) to make 'c8t2d0s0' bootable.
$ zpool status
 pool: rpool
 state: ONLINE
status: One or more devices is currently being resilvered.  The pool will
 continue to function, possibly in a degraded state.
action: Wait for the resilver to complete.
 scrub: resilver in progress for 0h0m, 0.18% done, 3h28m to go
config:</p>
<p> NAME          STATE     READ WRITE CKSUM
 rpool         ONLINE       0     0     0
 mirror        ONLINE       0     0     0
 c8t0d0s0      ONLINE       0     0     0
 c8t2d0s0      ONLINE       0     0     0  113M resilvered</p>
<p>errors: No known data errors
{% endhighlight %}
Looks all nice, now let's do the grub stuff so that we can boot from both disks:
{% highlight text %}
$ pfexec installgrub /boot/grub/stage1 /boot/grub/stage2 /dev/rdsk/c8t2d0s0
stage1 written to partition 0 sector 0 (abs 16065)
stage2 written to partition 0, 271 sectors starting at 50 (abs 16115)
{% endhighlight %}
A last check on the status of our pool:
{% highlight text %}
$ zpool status
 pool: rpool
 state: ONLINE
status: One or more devices is currently being resilvered.  The pool will
 continue to function, possibly in a degraded state.
action: Wait for the resilver to complete.
 scrub: resilver in progress for 0h2m, 4.89% done, 0h53m to go
config:</p>
<p> NAME          STATE     READ WRITE CKSUM
 rpool         ONLINE       0     0     0
 mirror        ONLINE       0     0     0
 c8t0d0s0      ONLINE       0     0     0
 c8t2d0s0      ONLINE       0     0     0  2.95G resilvered</p>
<p>errors: No known data errors
{% endhighlight %}
To my untrained OpenSolaris eye this looks all nice and shiny now.</p>
