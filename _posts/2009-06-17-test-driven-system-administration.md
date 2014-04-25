---
layout: post
title: Test driven system administration
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1245787898";}
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1245787899";}
  _wpas_skip_yup: '1'
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
author: 
---
<h1>Where are the general (best) practices for System Administration?</h1>
<p>Software development has various aspects on how to do it right, there is so much choice that you could let a holy war break loose about it, to people (like me) not doing too much with actual development the one that is probably the best known method is probably <a href="http://en.wikipedia.org/wiki/Test-driven_development">Test Driven Software Development (TDD)</a>, there are <a href="http://en.wikipedia.org/wiki/List_of_software_development_philosophies">some other methods availabe</a> - at least half of which I haven't heard about by now.</p>
<p>I'll focus on how TDD could be applied to System Administration and what the benefits are. For the sake of convenience I'll refer to Test Driven Administration (TDA) from now on.</p>
<h2>Documentation</h2>
<p>In System Administration we need to document how things are set up and how they work, I think that for SysAdmins that is even more true than for Developers. You might throw some piece of code at a developer with no comments or documentation at all and he or she can simply debug it locally. That is not always possible in larger systems, one might need to debug why all of a sudden in a certain time only 50 % percent of the emails go out thru the pipe with no obvious change to the setup. We can't simply take the stuff offline and look at it. Of course there are systems where the same is true for developers but from my impression it's more often that SysAdmins have to deal with such situations than developers.</p>
<p>People need to know about all the dependencies that might affect another system and with that being written down it's often still not obvious if the list is accurate or if it is just some list that was valid half a year ago.</p>
<p>TDA is a great help here. A lot of people use check lists to document their systems, these checklists coul look like below:</p>
<ul>
<li>Apache listening on port 8000
<ul>
<li>Port 8000 returns the extended server status</li>
</ul>
</li>
<li>Each project is listening on on it's own port starting at 8001
<ul>
<li>possibly using multiple VHosts</li>
</ul>
</li>
<li>Make sure all security updates are applied</li>
<li>Make sure that at least 20 IDLE processes are ready to serve requests</li>
<li>Apache must not use more than 80% of RAM</li>
<li>...</li>
</ul>
<p>You get the idea. This can easily be converted into automated checks. <a href="http://www.nagios.org/">Nagios</a> (soon to be <a href="http://www.icinga.org/">Icinga</a> at our site) or <a href="http://en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems">other tools</a> are of great help here. Wouldn't it be nice if somebody told you immediately if one of those points on the list isn't working as "documented"? Maybe even text message you about it?</p>
<p>No problem just define the checks you need and you'll have at least an overview on the web. You just added more documentation as well as made your checklist easily expandable (Right now I'm speaking in terms of Nagios/Icinga since that is what I know best). In case you need to add another webserver just add it to the service group, right out of nowhere you'll probably have a bunch of items on you checklist either totally failing of everything is OK, either of those is actually good. You won't need to print out the checklist 3 times just to not get confused with your markers what you already did and what is still on the todo list. It will update automatically as soon as a state change is found. This brings us to the next point, reproducible results</p>
<h2>Reproducible Results</h2>
<p>As nice as checklists are the checking of the items is still not done the same everytime you do it. You could forget to check this one itzi-bitzi small item, you could just assume that everything works by implication that another check on the list worked, or you simply have a lazy day and don't do it.</p>
<p>Testing the list as often as possible in an automated manner will give you reproducible results and also ensure (to some point) that you have somewhat the same configuration all over the place. Actually ensuring that you have your systems set up in the same way is a different topic, but having those tests will provide a good basis to get started with a more streamlined infrastructure.</p>
<p>You (as a person) could for example always check with `netstat -tulpen|grep -c apache 2` and then know that at least some process that is named apache2 is listening, now your junior SysAdmin gets the checklist and has to go thru all of it, he does a `netstat -tuln` and looks for something that is listening on port 80. Well most of the time it will be apache, but what if it's not Apache, some 3rd admin with access to the system could have killed it and replaced it with lighttpd which is now serving it's wonderful default page instead of your company's homepage. Not quite that nice.</p>
<p>Now instead of having that item on the checklist just make up the following tests:</p>
<ul>
<li>something is listening on port 80</li>
<li>the answer has to contain some string (preferably one that is rather unique to your site)</li>
<li>something is listening on port 8100</li>
<li>the answer on port 8100 contains "Apache Server Status for"</li>
</ul>
<p>There you go you just created 2 reproducible results for your tests, those are not actually the first to listed but rather the last to. How does that help you? It will ensure that</p>
<ul>
<li>you are indeed serving your company's website</li>
<li>you are indeed using Apache to do that</li>
</ul>
<p>The server-status page enables a few more nice things but what information you need from that page is up to you to figure out.</p>
<h2>Service Migration</h2>
<p>This is another interesting topic where checklists have failed on me not only once. The situation of migrating services. A written checklist (be it in paper, wiki or some other system) can really let you down.</p>
<p>Every time a service has to be migrated it's not the problem of migration actually it's a benchmark of your documentation, there can be different situations:</p>
<ul>
<li>migration to a new location with new hardware</li>
<li>migration to another server in the same location
<ul>
<li>the difference being quite notable in the speed of data transfer</li>
</ul>
</li>
<li>migration of several services to a single server (down scaling, consolidation, re planning)</li>
<li>migration of several services from a single server to a multitude of server (up scaling, growth)</li>
</ul>
<p>the most critical one being when you have to completely (geographically) relocate an installation with no redundant hardware on the target site. How are your checklists working then, you'd need to bring up your storage, database server and Wiki before you can access that one single document you forgot to print out that lists how to bring up the database correctly - catch22 anyone?</p>
<p>If you have monitoring in place (preferably on a single system of course) you will be able to fire up your monitoring server and see hell break loose, red items all over the place nothing is working! Quick, everybody, panic! Of course everything is red, because none of the servers is running. As you start deploying your services you will see light at the end of the tunnel because your items will become green.</p>
<p>Now how is that better than checklists when you could just have a look at the list and see that all the items are checked? There are quite a couple of points you can make here but some are really more useful than others.</p>
<p><strong>Communication</strong>. You won't have to run in circles just to find everybody and check on his or her status. You will be able to see what has already been done from one single point. If you have an out of bands channel, like text messages (and you should) the need to make phone calls whether or not a service works will be minimized. Of course people will have to wait for the test cycle to complete from your monitoring solution but on the other hand as long as it isn't verifiably good you have to consider it's in a bad state. As soon as you get a green item everybody in your team will be text messaged and knows that there's another working service. That's actually a good transition to the next point.</p>
<p><strong>Motivation</strong> (even if you are on your own). You will be able to see progress. You don't have to check all around who finished what, you see progress as it happens. Of course that also adds a little pressure to everyone but as you start realizing someone may have a problem because some service is 30 minutes late, in a good team someone will probably be already on his or her way to give a helping hand. Might be some screws are missing to mount a switch, might be someone screwed (sic) up big-time and totally destroyed a switch. In a stressful situation a helping hand is always welcome. But how does it help you if you are on your own? Consider doing all the physical installation of the servers in a rack and finally switching on the power, now while you wait for you cell phone to go crazy you can mount the next rack full of servers without wasting time by going thru the checklist. There another 30 minutes saved. Finally there's another point which your boss will definitely like.</p>
<p><strong>Traceability</strong>. You don't need to take care of carefully writing down the time of when things happend, any decent monitoring solution will let you do that after you got up and running again by simply looking at the logs. Of course you can write everything, but in the heat of the moment you may be scribbling something on you checklist you might even be able to read later on. Nobody will be happy if you have to start guessing about when things happened, after all a complete migration is the ultimate test for the administration team, because you will be taking down everything - just like a complete power outage with UPS installed maybe even worse you may have to reconfigure a couple of IPs or the whole network. Some may say now that reconfiguring the whole network will make the monitoring useless anyway - I don't think so. Just clone the configuration of your monitoring server either to a virtual OS installation or if the system allows it let it run in parallel with all the tests going to the new IPs. Parallelism is actually the next point.</p>
<p><strong>Parallelism</strong>. As noted before you don't have to waste time double checking (or checking even once) what your documentation says you'll get the notices anyway, or at least see them on the overview screen of your monitoring software. Also some DBA might work on the local console of a server, not even being able to reach the outside world, while your networking people set up the core switch. Now as soon as the core switch is up half the databases will be instantly reachable (verifiably reachable) and people can go on to the next task. Manually going thru documentation might keep you from this as the DBA might be able to do his work on a console but has to go thru the checklist twice or more often.</p>
<h1>Conclusion</h1>
<p>TDA is a nice complement to simply writing everything down. Why do I say complement if TDA is so great and you will have all the bells ringing when something doesn't work? Well you will instantly know what works, but there are always parts of the system that you don't work with daily, things you might have forgotten or something that you simply don't know but need to fix.</p>
<p>Written documentation is not something you should drop but it's something that should only be used as a complementary point of information, all admins in the team should be able to (basically) fix everything. Even if fixing just means to know who to call, that is not something your monitoring will or can tell you (well actually it can if you give it the information to message you some short URI where to go in case of emergency). Properly set up it will however tell you that 1 switch just broke and now 25 webservers are down. So instead of of panicing because a multitude of websites are down you can be relaxed and call your vendor (for which you hopefully have a good support contract in such a case) and demand replacement hardware - or better yet just restore the configuration backup to a replacement hardware on-site throw it in your trunk (probably handle it more carefully, do not "throw" it) and drive to the datacenter to replace everything. Time save by knowing what was broken without even looking at it.</p>
<p>You might want to check out some articles that refer to other "new" ways of system administration i found on the web, there's even one article from Microsoft. These article may not apply fully to TDA but they show the point of having more options than the traditional setup - document cycle:</p>
<ul>
<li><a href="http://delducagroup.com/ddg-blog/2009/04/22/test-driven-system-administration/">http://delducagroup.com/ddg-blog/2009/04/22/test-driven-system-administration/</a></li>
<li><a href="http://www.onlamp.com/pub/a/onlamp/2005/03/31/extreme_admin.html">http://www.onlamp.com/pub/a/onlamp/2005/03/31/extreme_admin.html</a></li>
<li><a href="http://lwn.net/Articles/266520/">http://lwn.net/Articles/266520/</a></li>
<li><a href="http://msdn.microsoft.com/en-us/library/bb491123.aspx">http://msdn.microsoft.com/en-us/library/bb491123.aspx</a></li>
</ul>
