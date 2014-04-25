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
<p>Simply use "format" :)<br />
[sourcecode langauage="text"]<br />
$ pfexec format<br />
Searching for disks...done</p>
<p>AVAILABLE DISK SELECTIONS:<br />
 0. c8t0d0 &lt;DEFAULT cyl 30398 alt 2 hd 255 sec 63&gt;<br />
 /pci@0,0/pci103c,3035@1f,2/disk@0,0<br />
 1. c8t2d0 &lt;ATA-ST3250310AS-C cyl 30398 alt 2 hd 255 sec 63&gt;<br />
 /pci@0,0/pci103c,3035@1f,2/disk@2,0<br />
Specify disk (enter its number): 1<br />
selecting c8t2d0<br />
[disk formatted]</p>
<p>FORMAT MENU:<br />
 disk       - select a disk<br />
 type       - select (define) a disk type<br />
 partition  - select (define) a partition table<br />
 current    - describe the current disk<br />
 format     - format and analyze the disk<br />
 fdisk      - run the fdisk program<br />
 repair     - repair a defective sector<br />
 label      - write label to the disk<br />
 analyze    - surface analysis<br />
 defect     - defect list management<br />
 backup     - search for backup labels<br />
 verify     - read and display labels<br />
 save       - save new disk/partition definitions<br />
 inquiry    - show vendor, product and revision<br />
 volname    - set 8-character volume name<br />
 !&lt;cmd&gt;     - execute &lt;cmd&gt;, then return<br />
 quit<br />
[/sourcecode]<br />
No go "fdisk" it and delete all the partitions on the disk. Then create a new partition, make it a Solaris partition and be done with that part.<br />
[sourcecode langauage="text"]<br />
format&gt; fdisk<br />
Total disk size is 30401 cylinders<br />
 Cylinder size is 16065 (512 byte) blocks</p>
<p> Cylinders<br />
 Partition   Status    Type          Start   End   Length    %<br />
 =========   ======    ============  =====   ===   ======   ===<br />
 1       Active    Solaris2          1  30400    30400    100</p>
<p>SELECT ONE OF THE FOLLOWING:<br />
 1. Create a partition<br />
 2. Specify the active partition<br />
 3. Delete a partition<br />
 4. Change between Solaris and Solaris2 Partition IDs<br />
 5. Exit (update disk configuration and exit)<br />
 6. Cancel (exit without updating disk configuration)<br />
Enter Selection: 3<br />
Specify the partition number to delete (or enter 0 to exit): 1<br />
Are you sure you want to delete partition 1? This will make all files and<br />
programs in this partition inaccessible (type &quot;y&quot; or &quot;n&quot;).<br />
y<br />
Partition 1 has been deleted. This was the active partition.<br />
Enter Selection: 1<br />
Select the partition type to create:<br />
 1=SOLARIS2  2=UNIX        3=PCIXOS     4=Other<br />
 5=DOS12     6=DOS16       7=DOSEXT     8=DOSBIG<br />
 9=DOS16LBA  A=x86 Boot    B=Diagnostic C=FAT32<br />
 D=FAT32LBA  E=DOSEXTLBA   F=EFI        0=Exit? 1<br />
Specify the percentage of disk to use for this partition<br />
(or type &quot;c&quot; to specify the size in cylinders). 100<br />
Should this become the active partition? If yes, it  will be activated<br />
each time the computer is reset or turned on.<br />
Please type &quot;y&quot; or &quot;n&quot;. y<br />
Partition 1 is now the active partition.<br />
Enter Selection: 5<br />
[/sourcecode]</p>
<h1>Duplicate the disk layout on both disks</h1>
<p>Now OpenSolaris provides us with 2 nice tools to make one disk have exactly the same layout as another disk. Use them like below:<br />
[sourcecode langauage="text"]<br />
$ pfexec prtvtoc /dev/rdsk/c8t0d0s2 # first disk<br />
$ pfexec prtvtoc /dev/rdsk/c8t2d0s2 # second disk<br />
$ pfexec prtvtoc /dev/rdsk/c8t0d0s2 | pfexec fmthard -s - /dev/rdsk/c8t2d0s2 # make the 1st disk the same as the 2nd<br />
[/sourcecode]</p>
<h1>Attach it to the pool in question</h1>
<p>Let's have a quick look at the existing pool:<br />
[sourcecode langauage="text"]<br />
$ zpool status<br />
 pool: rpool<br />
 state: ONLINE<br />
 scrub: scrub completed after 0h26m with 0 errors on Wed Nov 25 10:52:26 2009<br />
config:</p>
<p> NAME        STATE     READ WRITE CKSUM<br />
 rpool       ONLINE       0     0     0<br />
 c8t0d0s0    ONLINE       0     0     0</p>
<p>errors: No known data errors<br />
[/sourcecode]<br />
Nice we now see what our original device name is and what our pool name is, we need both for the next command. Remember in my example the new disk slice (the BIOS vs. EFI thing) is  <em>c8t2d0s0</em>. We should be all fine to attach the slice to the pool and see it start recovering.<em></em><br />
[sourcecode langauage="text"]<br />
$ pfexec zpool attach rpool c8t0d0s0 c8t2d0s0<br />
invalid vdev specification<br />
use '-f' to override the following errors:<br />
/dev/dsk/c8t2d0s0 overlaps with /dev/dsk/c8t2d0s2<br />
[/sourcecode]<br />
Ouch, didn't quite work, so let's do as instructed, and right thereafter let's investigate the staus of the pool:<br />
[sourcecode langauage="text"]<br />
$ pfexec zpool attach -f rpool c8t0d0s0 c8t2d0s0<br />
Please be sure to invoke installgrub(1M) to make 'c8t2d0s0' bootable.<br />
$ zpool status<br />
 pool: rpool<br />
 state: ONLINE<br />
status: One or more devices is currently being resilvered.  The pool will<br />
 continue to function, possibly in a degraded state.<br />
action: Wait for the resilver to complete.<br />
 scrub: resilver in progress for 0h0m, 0.18% done, 3h28m to go<br />
config:</p>
<p> NAME          STATE     READ WRITE CKSUM<br />
 rpool         ONLINE       0     0     0<br />
 mirror        ONLINE       0     0     0<br />
 c8t0d0s0      ONLINE       0     0     0<br />
 c8t2d0s0      ONLINE       0     0     0  113M resilvered</p>
<p>errors: No known data errors<br />
[/sourcecode]<br />
Looks all nice, now let's do the grub stuff so that we can boot from both disks:<br />
[sourcecode langauage="text"]<br />
$ pfexec installgrub /boot/grub/stage1 /boot/grub/stage2 /dev/rdsk/c8t2d0s0<br />
stage1 written to partition 0 sector 0 (abs 16065)<br />
stage2 written to partition 0, 271 sectors starting at 50 (abs 16115)<br />
[/sourcecode]<br />
A last check on the status of our pool:<br />
[sourcecode langauage="text"]<br />
$ zpool status<br />
 pool: rpool<br />
 state: ONLINE<br />
status: One or more devices is currently being resilvered.  The pool will<br />
 continue to function, possibly in a degraded state.<br />
action: Wait for the resilver to complete.<br />
 scrub: resilver in progress for 0h2m, 4.89% done, 0h53m to go<br />
config:</p>
<p> NAME          STATE     READ WRITE CKSUM<br />
 rpool         ONLINE       0     0     0<br />
 mirror        ONLINE       0     0     0<br />
 c8t0d0s0      ONLINE       0     0     0<br />
 c8t2d0s0      ONLINE       0     0     0  2.95G resilvered</p>
<p>errors: No known data errors<br />
[/sourcecode]<br />
To my untrained OpenSolaris eye this looks all nice and shiny now.</p>
