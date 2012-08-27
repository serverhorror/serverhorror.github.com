---
comments: true
date: 2011-01-27 15:20:27
layout: post
slug: migrating-raid-levels-in-linux-with-mdadm
title: Migrating RAID Levels in Linux with mdadm
wordpress_id: 1003
tags:
- sysadmin
---

This is a quick note. If you try the stuff here I suggest you do it in a virtualised guest machine. This does not resemble the whole truth you can use --backup-file to minimize the number of hot spares required...

Clear out any RAID information on the disks involved

[sourcecode]
$ sudo mdadm --zero-superblock /dev/sd[bcdefghijk]
{% endhighlight %}

Keep Status overview running while we work on this:

[sourcecode]
$ while true;
    do
        clear
        cat /proc/mdstat
        /bin/echo -e '\nmdadm --detail'
        sudo mdadm --detail /dev/md/md0
        sleep 2
    done
{% endhighlight %}

Create a RAID1 with a missing disk:

[sourcecode]
$ sudo mdadm --create md0 --raid-devices 2 --level 1 /dev/sdb missing
{% endhighlight %}

Add a hot spare(s), mdadm will start a recovery process so that the degraded
array will gain a clean state:

[sourcecode]
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdc
{% endhighlight %}

Add a hot spare(s):

[sourcecode]
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdd
{% endhighlight %}

Check the hot spare is working and make sdc available again:

[sourcecode]
$ sudo mdadm --manage /dev/md/md0 --fail /dev/sdc --remove /dev/sdc --add /dev/sdc
{% endhighlight %}

Convert into a RAID5 array:

[sourcecode]
$ sudo mdadm --grow /dev/md/md0 --level 5
{% endhighlight %}

Add a disk to the array, to get a clean state for the array:

[sourcecode]
$ sudo mdadm --grow /dev/md/md0 --raid-devices 3
{% endhighlight %}

Add a hot spare(s):

[sourcecode]
$ sudo mdadm --manage /dev/md/md0 --add /dev/sd[ef]
{% endhighlight %}

Grow the RAID5 to have more space available:

[sourcecode]
$ sudo mdadm --grow /dev/md/md0 --raid-devices 4
{% endhighlight %}

Add a second hot spare so that we can migrate from RAID5 to RAID6 (RAID5 to RAID6 needs to spares available):

[sourcecode]
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdg
{% endhighlight %}

Convert into a RAID6 array and make it rebuild to a clean state:

[sourcecode]
$ sudo mdadm --grow /dev/md/md0 --raid-devices 6 --level 6
{% endhighlight %}

Add another hot-spare to be able to migrate from RAID6 to RAID5 (RAID6 to RAID5 needs one spare available):

[sourcecode]
$ sudo mdadm --manage /dev/md/md0 --add /dev/sdh
{% endhighlight %}

Convert from RAID6 to RAID5:

[sourcecode]
$ sudo mdadm --grow /dev/md/md0 --level 5 --raid-devices 7
{% endhighlight %}

Add 3 more spares (just in case):

[sourcecode]
sudo mdadm --manage /dev/md/md0 --add /dev/sd[ijk]
{% endhighlight %}

Exercise left to the reader (in that order):



	
  1. Convert from RAID5 to RAID6

	
  2. Convert from RAID 6 to RAID5


