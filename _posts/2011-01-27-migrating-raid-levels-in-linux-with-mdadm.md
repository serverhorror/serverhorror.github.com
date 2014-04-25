---
layout: post
title: Migrating RAID Levels in Linux with mdadm
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1320179141";}
  _wpas_done_yup: '1'
  _wpas_done_fb: '1'
author: 
---
<p>This is a quick note. If you try the stuff here I suggest you do it in a virtualised guest machine. This does not resemble the whole truth you can use <tt>--backup-file</tt> to minimize the number of hot spares required...</p>
<p>Clear out any RAID information on the disks involved</p>
<p>[sourcecode]<br />
$ sudo mdadm --zero-superblock /dev/sd[bcdefghijk]<br />
[/sourcecode]</p>
<p>Keep Status overview running while we work on this:</p>
<p>[sourcecode]<br />
$ while true;<br />
    do<br />
        clear<br />
        cat /proc/mdstat<br />
        /bin/echo -e '\nmdadm --detail'<br />
        sudo mdadm --detail /dev/md/md0<br />
        sleep 2<br />
    done<br />
[/sourcecode]</p>
<p>Create a RAID1 with a missing disk:</p>
<p>[sourcecode]<br />
$ sudo mdadm --create md0 --raid-devices 2 --level 1 /dev/sdb missing<br />
[/sourcecode]</p>
<p>Add a hot spare(s), mdadm will start a recovery process so that the degraded<br />
array will gain a clean state:</p>
<p>[sourcecode]<br />
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdc<br />
[/sourcecode]</p>
<p>Add a hot spare(s):</p>
<p>[sourcecode]<br />
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdd<br />
[/sourcecode]</p>
<p>Check the hot spare is working and make sdc available again:</p>
<p>[sourcecode]<br />
$ sudo mdadm --manage /dev/md/md0 --fail /dev/sdc --remove /dev/sdc --add /dev/sdc<br />
[/sourcecode]</p>
<p>Convert into a RAID5 array:</p>
<p>[sourcecode]<br />
$ sudo mdadm --grow /dev/md/md0 --level 5<br />
[/sourcecode]</p>
<p>Add a disk to the array, to get a clean state for the array:</p>
<p>[sourcecode]<br />
$ sudo mdadm --grow /dev/md/md0 --raid-devices 3<br />
[/sourcecode]</p>
<p>Add a hot spare(s):</p>
<p>[sourcecode]<br />
$ sudo mdadm --manage /dev/md/md0 --add /dev/sd[ef]<br />
[/sourcecode]</p>
<p>Grow the RAID5 to have more space available:</p>
<p>[sourcecode]<br />
$ sudo mdadm --grow /dev/md/md0 --raid-devices 4<br />
[/sourcecode]</p>
<p>Add a second hot spare so that we can migrate from RAID5 to RAID6 (RAID5 to RAID6 needs to spares available):</p>
<p>[sourcecode]<br />
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdg<br />
[/sourcecode]</p>
<p>Convert into a RAID6 array and make it rebuild to a clean state:</p>
<p>[sourcecode]<br />
$ sudo mdadm --grow /dev/md/md0 --raid-devices 6 --level 6<br />
[/sourcecode]</p>
<p>Add another hot-spare to be able to migrate from RAID6 to RAID5 (RAID6 to RAID5 needs one spare available):</p>
<p>[sourcecode]<br />
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdh<br />
[/sourcecode]</p>
<p>Convert from RAID6 to RAID5:</p>
<p>[sourcecode]<br />
$ sudo mdadm --grow /dev/md/md0 --level 5 --raid-devices 7<br />
[/sourcecode]</p>
<p>Add 3 more spares (just in case):</p>
<p>[sourcecode]<br />
sudo mdadm --manage /dev/md/md0 --add /dev/sd[ijk]<br />
[/sourcecode]</p>
<p>Exercise left to the reader (in that order):</p>
<ol>
<li>Convert from RAID5 to RAID6</li>
<li>Convert from RAID 6 to RAID5</li>
</ol>
