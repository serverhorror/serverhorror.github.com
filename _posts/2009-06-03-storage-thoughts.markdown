---
comments: true
date: 2009-06-03 00:30:00
layout: post
slug: storage-thoughts
title: Storage Thoughts
wordpress_id: 10
tags:
- sysadmin
---

# Would the best storage please stand up?


So we do need some storage to run our projects. OK, most of the projects don't need huge amounts of storage, I think the largest one we have in a a single system is some mail store for a project that has been running for quite some time now.

Next up is a (single) [PostgreSQL](http://www.postgresql.org) database from the same project. It's size is about 120 GB and steadily growing, not really fast, but after all it's growing.

Next best thing is a project (actually a couple of projects but they all share the same codebase and thus: problems) that implement sharding with a MySQL database - at least the original developers thought they were sharding, but actually the aren't. So now we are stuck with 12 databases (for a single project!) which aren't evenly loaded at all, sizes vary from 60 GB to 5 GB (total amount of all databases per project is about 200GB but they are distributed on several machines).

Those numbers aren't actually large storage needs, but having local storage in each of those servers doesn't exactly help in solving the problem. We do however have a couple of options...


# Solutions?


First thing to use would be a storage unit from one of the large storage providers, we talked to a pre-sales consultant from [NetApp](http://en.wikipedia.org/wiki/Netapp), the feature set of those devices is impressive and for our current needs it would solve all problems, so from a practical point of view I'm all for it (To be fair there are a couple of competitors out there: [EMC](http://en.wikipedia.org/wiki/EMC_Corporation), [HP](http://en.wikipedia.org/wiki/Hewlett_Packard), [DELL](http://en.wikipedia.org/wiki/Dell), [IBM](http://en.wikipedia.org/wiki/IBM), [and so on](http://en.wikipedia.org/wiki/List_of_networked_storage_hardware_platforms)).

But I don't think that solution would last on the long term. There are a couple of problems I see with those devices - mor on that later.

Another option would be something like [GFS](http://en.wikipedia.org/wiki/Google_File_System). I recently read about RAIPCs (Redundant Array of Inexpensive PCs) which is exactly the same. It all boils down to spending some portion of the local storage in each server to a globally available storage pool. There are a couple of projects out there that try to provide exactly this. In recent press [Hadoop](http://en.wikipedia.org/wiki/Hadoop) seems to be everybodies darling. I'm not quite convinced of Hadoop yet because they still have a [Single Point of Failure (SPOF)](http://en.wikipedia.org/wiki/SPOF). The NameNode, in Hadoops current state of development there's only a single NameNode, although there are possibilities to set up [Hot Standby](http://en.wikipedia.org/wiki/Hot_standby) Servers to take over in case of failure, I'd rather like to see this option built in than having to rely on my limited knowledge about the system. Maybe Linux HA isn't fast enough for the switch, maybe the clients are somehow caching a state of the NameNode that for some reason is different on the standby server than it was on the original server. Also currently Hadoop isn't a native filesystem for Linux (I don't know if it's useable as a file system for windows at all), but rather relies on [FUSE](http://en.wikipedia.org/wiki/Filesystem_in_Userspace) to be able to mount it. I'm not a huge fan of FUSE filesystems. Other players in that direction are:



	
  * [GlusterFS](http://en.wikipedia.org/wiki/GlusterFS)

	
    * no SPOF

	
    * "quite" stable (I've read different posts that state problem)




	
  * [Lustre](http://en.wikipedia.org/wiki/Lustre_(file_system))

	
    * SPOF (metadata servers)




	
  * [Ceph](http://en.wikipedia.org/wiki/Ceph)

	
    * very alpha

	
    * feature set sounds very promising







## RAID to the Rescue


There is some help from [RAID](http://en.wikipedia.org/wiki/RAID) to meet our storage needs. We are mostly working with HP hardware, [HP DL 360](http://en.wikipedia.org/wiki/List_of_Hewlett-Packard_products#ProLiant_DL_Series) to be exact. They do have quite a nice hardware RAID controller built-in. In the newest generation up to 8 disks can be put in a 1U Server. Up until now we had be fine with 6 disks per 1U server, the largest certified disk is currently 300GB. So with a RAID 5 configuration from the controller we now have a total storage capacity of 2100 GB (2,1 TB). For a single server that is quite nice. But on some of the servers we are running into scalability problems regarding the number if [I/O operations per second (IOPS)](http://en.wikipedia.org/wiki/IOPS).

The easiest way to raise that number is to use more disks (for the record: I know RAID 10 will also speed things up, but it would lower per server storage to 1,2 TB - effectively cutting it in half).

But the point of RAID is in my opinion simply to avoid downtimes of a single node. A failing disk shouldn't bring a whole node down. It should simply generate an alert so that the System Administrator can replace it as soon as possible and wait for the RAID to rebuild. No downtime, probably somewhat slower operation but it would still work.


## Local Storage After All?


All the commercial storage units will at some point hit an expansion level, which means you have to either purchase the next option in the program (which in turn will hit it's limit too) or think about a different solution (like distributed file systems).

Not exactly the solution I'd like to see.


## Go distributed?


Going distributed certainly would get rid of all storage problems, but what other problems would come up? I can think of a couple of problems.



	
  * [Network Latency](http://en.wikipedia.org/wiki/Network_Latency)

	
  * State Consistency across the whole cluster

	
  * We loose the ability to separate projects by using [VLANs](http://en.wikipedia.org/wiki/VLAN) (Physical Network Security)

	
  * Databases anyone?

	
  * IOPS - what will happen to them

	
  * Backup?




#### Network Latency


I'm not going to do any math here, I think every SysAdmin is smart enough to calculate that. But we have to keep in mind that latency will be more of a concern than with traditional storage.


#### State Consistency


This is gonna be tough, and we will have to trust developers of distributed file systems that they do it right. Just imagine you have a farm with 10 webservers on the fronted. Your system is a [Wiki](http://en.wikipedia.org/wiki/Wiki) so everybody can edit anything. In a typical web application now you either create a simple lock file (OK with 10 frontend servers a lock probably won't do - or maybe it will?) or let the database take care of it, or you place a locking mechanism inside the application - but all webserver need to have access to the same location/resource that is being edited right now by some user. I'm not the one that is keen on handling the support calls from all the people who just edited the Roadmap for the next 3 months just to find out that only the last person who hit save still has their data (in the best case).

Maybe it should be a distributed storage system rather than a file system. Just give developers a really nice library that looks up all the resources and provides a set of useful operations (But what exactyl would useful be?)


#### Physical Network Security


Ahh Security, I wish it wouldn't be necessary :)

So, we are currently using VLANs as a base line of security. We do have quite a couple of them and use them extensively to separate stuff that really doesn't need to know about each others existence. But as soon as we start donating say 500 GB of each server to this distributed storage we are lost. Aren't we?

Personally I think making such a storage VLAN aware isn't a good solution, I'd rather see something like mountpoints and a good set of permissions in this system.

Mountpoints/Filesystems/Namespaces (whatever you call them) would be nice so that a single project can only access a certain set of namespaces. From an administrational point I'd rather not care about where exactly this namespace is stored, I just want to know it's there and only project X and project Y have access to it.

Permissions should built in right from the start, a protocol where authentication and authorization aren't a basic part of the system in these days is just shit hitting the fan.


#### Databases


I like this one. Now go have 50 Servers, each donates 500GB of storage (25 TB). Fine we have plenty of space, we now all our database needs to do is actually store stuff, it will never ever(TM) need much CPU. We are all safe. Except our distributed storage doesn't provide the locking semantics needed by the database. Shit hits the fan...

OK this is solveable, [MapReduce](http://en.wikipedia.org/wiki/Map_reduce) should be able to solve this. But on the other hand there are quite a couple of applications out there that rely on PostgreSQL, Oracle or even MySQL (I like that "rely on MySQL") to be available.

I know that a couple of the distributed file systems do try to provide POSIX semantics so that all of this would be running. But why do we need that? Why can't we just have a layer that validates the given SQL (the code is already there) that remaps the statements to something that can exist in our new shiny storage universe. And that's where Hadoop comes into play again. Not exactly Hadoop, but a sub project of Hadoop already provides an SQL-like interface that's [Hive](http://hadoop.apache.org/hive/). Personally I think that's the right direction, now we only need to have a grace time of about 8 - 10 years to get rid of all the legacy application, but by that time we will of course have some shiny new idea that seems to be the next best thing.


#### IOPS


I honestly have now idea how all of that will perform, probably IOPS won't be of interest anymore. My guess is that the network layer will be the problem at some point but not in the forseeable future, fibre is going to be standard everywhere, and it does 10Gbit/s now, SATA 3.0 just came out and has only 6Gbit/s. So not that much of a problem, we'll see what the impact [SSD Disks](http://en.wikipedia.org/wiki/Solid-state_drive) will change the market. Maybe [Moores Law](http://en.wikipedia.org/wiki/Moores_law) will become valid for storage devices too after all.


#### Backup


Do you think Google has a backup? What retention time, 30 days, 90 days? Daily incremental backups, weekly differential, and each 1st of the month a full backup? Yeah, right...

On the other hand, maybe they do. It just won't be a traditional backup that is written on tape. I'd guess they have some kind of distribution algorithm plus a snapshot function. Distribution is probably n+1 distribution, and the snapshot is what their backups are. In good old UNIX terms I'd simply use a cronjob that takes a snapshout hourly, keeps one snapshot for each of the last seven days, one snapshot for each of the last 4 weeks and discards all other snapshots automagically. Of course the papers on GFS will tell you more about that in detail - If I remember correctly data isn't even deleted from GFS in the traditional sense, it's some Copy-On-Write, so actually the snapshots are free.


# Conclusion


I'm all in for distributed storage, **if it's:**



	
  * redundant (node failure doesn't matter)

	
  * provides libs and file system like access

	
    * file-system like access is something I probably only like because I'm used to it




	
  * authentication and authorization is built in

	
  * no single point of failure

	
  * dynamic (add/remove nodes on the fly)

	
  * metrics are built in

	
    * there's just too much I don't know about it yet, I need to measure it




	
  * "legacy layer"

	
    * I'd like to still be able to run all major database servers on it, plus Oracle and MySQL (I don't run MS SQL so that leaves us with PostgreSQL :))




	
  * runs on cheap hardware

	
    * I do mean cheap, I want it to run on [this!](http://en.wikipedia.org/wiki/AMD_Geode)





