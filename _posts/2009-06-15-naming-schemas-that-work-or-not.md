---
layout: post
title: Naming Schemas that work - or not
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1245787882";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1245787882";}
  _wpas_skip_twitter: '1'
  _wpas_skip_yup: '1'
  _wpas_skip_fb: '1'
author: 
---
<p>I've recently been thinking about our naming scheme in the company, up until now it has worked quite well and still does so. With about 300 devices (and growing) I thought I might share this to eventually get some input (if anyone ever reads this, if not I do have some reference at least).</p>
<h1>Domains</h1>
<p>We are actively distinguishing between internally and externally available services, one of the easiest ways to remember is to use another domain for internal services than the one you use for external services. There's however the drawback of typing, you can of course configure completely different domains but that is something I consider bad use, you either have to</p>
<ul>
<li>buy yet another domain (and never ever use it in public) or</li>
<li>use an invalid domain - <a href="http://www.faqs.org/rfcs/rfc2606.html">check the corresponding RFC on the proper names</a></li>
<li>use some random domain and hope you never want to go there or do business with them because it probably would require reconfigurinig all of your machines</li>
</ul>
<p>The option I prefer is to use a dedicated subdomain. Yes that involves some more typing but you can always choose a really short name, <strong>good options I'd consider are</strong>:</p>
<ul>
<li>in.example.com</li>
<li>int.example.com</li>
<li>local.example.com (already quite a bit long)</li>
</ul>
<p>bad options would be:</p>
<ul>
<li>internal.example.com</li>
<li>not-public.example.com</li>
</ul>
<p>Going the other way around and having a dedicated domain for external services while defaulting to internal services isn't quite working because all your customers would have some additional typing consider this:</p>
<ul>
<li>blog.public.example.com</li>
<li>www.public.example.com</li>
</ul>
<p>Not quite what you want</p>
<h2>Split Horizon DNS</h2>
<p>Deserves some paragraph on it's own :)</p>
<p>Split horizon is a technique that is able to give you different answers for the same hostname depending on the source of the request. It may be of use but I don't think it's that good to seperate services with it. How so? Consider the following situation:</p>
<p>You are at your company and visit blog.example.org to publish which is an internal only service, now you go home and remember that you forgot to add some important information, you go to blog.example.org and it just won't work. Heck why? You know the DNS works because just about an hour earlier you were happily typing, you start investigating search stuff and after all you just created unnecessary work for you.</p>
<p>I still consider a simple int.example.org to be better because not only you will know instantly about internal vs. external services but also all your users. And your job is all about giving good services to your users isn't it?</p>
<h1>Hostnames</h1>
<p>This is actually more interesting that domains because you and your customers (users and paying customers) will be typing them all day long. There are a few documents that may be helpful:</p>
<ul>
<li><a href="http://tools.ietf.org/html/rfc1178">http://tools.ietf.org/html/rfc1178</a></li>
<li><a href="http://tools.ietf.org/html/rfc2100">http://tools.ietf.org/html/rfc2100</a></li>
<li><a href="http://www.namingschemes.com/Main_Page">http://www.namingschemes.com/Main_Page</a></li>
</ul>
<p>Those naming schemes mostly refer to mythology, movies or tv series. All of them are quite well known and try to create a mental link between the meaning of a character, god or creature and the use of the server. Personally however I don't quite like this. It implies knowledge about cultural things that may not quite apply depending on where you are located.</p>
<p>We have a couple of rules that apply to our naming scheme:</p>
<ul>
<li>all devices adhere to the same schema (printers, switches, routers, servers, workstations, ...)</li>
<li>hostnames are set up from either 2 to 4 parts these are</li>
<li>company abbreviation - max. 3 letters</li>
<li>optional environment abbreviation - a fixed list</li>
<li>usage abbreviation (abbreviated only if too long or if usage is still clear)</li>
<li>if it is a service that end users should use it will have an internal name with the abbreviation "<em>vip</em>" after the environment abbreviation</li>
<li>name parts are separated by dashes</li>
</ul>
<h2>Examples</h2>
<h3>Company Abbreviations</h3>
<ul>
<li>Snake Oil Lt. would become <em>sno</em></li>
<li>Bogus Inventory would become <em>boi</em></li>
</ul>
<h3>Environment Abbreviations</h3>
<p>This is fixed in our case we use the following:</p>
<ul>
<li><em>devl</em> for development environments - Developers playground, we don't care about what happens on those boxes, we only provide daily backups</li>
<li><em>stag</em> for staging - Our playground, where we - SysAdmins - try to get the config right for a production deployment</li>
<li><em>prod</em> for production - In a perfect world <em>prod</em> matches <em>stag</em> at all times</li>
</ul>
<h4>Usage Abbreviations</h4>
<p>This is a bit tougher. There's no hard rule but rather something that makes it clear what the box actually does:</p>
<ul>
<li>mail - a mail server with services like imap, smtp or whatever is needed for a mail structure that end users see</li>
<li>mailout - guess what</li>
<li>openxdb - any ideas? <a href="http://www.openx.org">OpenX</a> is an ad-server, you can probably imagine what DB stands for. Note that we do not include the type of DB here, that kind of information is something you can figure out as soon as you are on the host or by reading internal documentation</li>
</ul>
<h1>Putting it all together</h1>
<p>Ok, so now we have a couple of rules to apply to our hostnames. Let's say we are going to put up a new project and it requires</p>
<ul>
<li>a source code repository (deployed on it's own virtualized server)</li>
<li>mailing infrastructure - fitted to the environment in question, after all we don't want to send out 200.000 test mails to real customers but rather to a certain mailbox the devs can check</li>
<li>shared storage to place images</li>
<li>a static webhost</li>
<li>a database server</li>
<li>a webhost with the application itself</li>
<li>the company responsible is Snake Oil Ltd.</li>
</ul>
<p>Let's create the hostnames we are going to use:</p>
<ul>
<li>sno-scm.in.snakeoil.example - note I'm using .invalid for documentation purposes as per <a href="http://www.faqs.org/rfcs/rfc2606.html">RFC 2606</a>, also I won't repeat the domain in all the other hostnames<a href="http://www.faqs.org/rfcs/rfc2606.html">
</a></li>
<li>sno-devl-mail, sno-devl-mailout, sno-stag-mail, sno-stag-mailout, sno-prod-mail, sno-prod-mailout - I'll also leave out the hostnames for staging and production environments now. I'm pretty sure you are able to construct them yourself</li>
<li>sno-devl-storage</li>
<li>sno-devl-db</li>
<li>sno-devl-staticweb</li>
<li>sno-devl-appweb</li>
</ul>
<p>A few points might need explanation.</p>
<p><strong>Why isn't the source code reposity a production service?</strong></p>
<p style="padding-left:30px;">Well it is, but since there's only one (and only one) we dump the environment. This is our convention for all SCM instances, it is well known so it's not a problem</p>
<p><strong>Why the "<em>appweb</em>" and "<em>staticweb</em>"?</strong></p>
<p style="padding-left:30px;">Those might sound:</p>
<ul style="padding-left:40px;">
<li>too complicated and</li>
<li>too generic</li>
</ul>
<p style="padding-left:30px;">I think neither is true, we are sysadmins and don't really care wether it's a java application, PHP, Python, Rails or plain Assembler. What I need to now is where the application is so that I can directly go to a host that needs some reconfiguration in case it's necessary. The web part of the name is a hint that it's...well a web application. Yes in this day and age there are still some applications running on a server that don't provide a GUI on port 80!</p>
<p>There are few other things we try to adhere too, while it may seem like quite a rule set that people need to keep in mind it's actually not that bad. People - that is system administrators, developers <em>and end users</em> - know about this scheme and can easily construct hostnames with little guessing. It's not too hard to write. I thought about moving from "<em>devl</em>" to "<em>devel</em>" but it's</p>
<ul>
<li>not worth the effort</li>
<li>everybody's already used to it</li>
<li>one more character to type</li>
</ul>
<p>so I have enough excuses to purposely have a typo in there. But since we are dealing with artifical names anyway we don't have much of a problem here. We get very few questions about where a service actually is, and most questions are only asked once. Those come up when we obviously did something wrong abbreviating the usage but that is something we live with for the sake of not generating sources of error. Renaming a host is quite a risky thing to do, there are references all over the place you might forget and tests don't always cover all cases. We are hit early enough with missing test cases everytime we have to migrate some server or service due to scaling issues.</p>
