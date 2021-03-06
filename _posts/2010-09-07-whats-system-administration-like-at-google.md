---
layout: post
title: What's system administration like at Google?
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_skip_twitter: '1'
  _wpas_mess: 'What''s system administration like at Google?:'
  _wpas_skip_fb: '1'
  _wp_old_slug: ''
  _wpas_skip_yup: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1301480993";}
author: 
---
<div class="document">
<div id="what-s-system-administration-like-at-google" class="section">
<blockquote cite="http://everythingsysadmin.com/2010/09/whats-system-administration-li.html" lang="en"><h1>What's system administration like at Google?</h1>
<p>by <cite><a href="http://everythingsysadmin.com/2010/09/sysadmin-at-google.html">Tom Limoncelli</a></cite></p>
<p>People often write to me for advice about submitting a resume to Google. They
always want to know what system administration is like here. I tend to write
something original each time, but I always say the same thing. Therefore, I'm
going to post it here and refer people to this post in the future.</p>
<p>What is system administration like at Google?</p>
<p>System administration at Google is quite different than at most companies.
Since we do all our computing on massive clusters we don't touch much hardware.
It is set up a rack at a time for us in data centers around the world. We don't
spend a lot of time setting up typical services like LDAP, Kerberos, and load
balancers because we have those things set up already, automated, and scaled.</p>
<p>So what /do/ we do? We keep the various web sites of google running, or keep
the systems that they rely on running. We have small teams for each product.
Members usually have 1 week of "on call" (pager) duty out of 6, and the other 5
weeks are spent making improvements to make the on call portion more optimized,
automated, and trouble-free. (Some groups are 1 out of 8, or 3.5 days out of
every 12, or whatever... some have zillions of pages per day, others 1 or two
per week).</p>
<p>When you aren't on duty, you are optimizing the system for better operational
efficiency. Suppose the last time you were oncall you noticed a certain problem
was happening a lot. You might take on a project to monitor all aspects of it,
find the problem, and either fix it or work with the developers to fix it. We
have large, complicated systems that requires deep Unix knowledge to maintain
properly.</p>
<p>A senior person takes on projects that have even larger impact. So, maybe you
notice that not only does your product have that particular problem, but other
projects do too. So you invent a new system that fixes the problem globally.
For example, rolling out software to thousands of machines is difficult. After
each upgrade the machine must be tested to make sure the software is working,
and begin rolling back the change if there are failures. We haven't done that
kind of thing manually in years, but maybe the current system can't tell the
difference between a bug that means you should roll-back all systems, or a
hardware failure that means one particular machine is down. You might refactor
the system so that the failure test is a plug-in module and now everyone can
write their own plug-ins.</p>
<p>This is why we call ourselves "Site Reliability Engineers" instead of of
Sysadmins. As a SRE, we are constantly optimizing the system. Some of us are
more focused on operational aspects (sysadmin skills) and others are focused on
writing tools (software engineering focused). However, we all do some kind of
software development, scripting, and so on. At our scale it isn't a question of
whether or not to automate, but how to automate.</p>
<p>We also have more traditional system administrators in our CorpEng group. They
are focused on internal systems (the printing system, deploying the newest Mac
OS release, etc.). This is also the group that employs our internal helpdesk.
Supporting 20k employees is a big job. Most companies don't have 10,000+ linux
desktops and 15,000+ Mac laptops, plus countless other systems.</p>
<p>A few more great things about working here:</p>
<ul class="simple">
<li>The relationship with the developers is collaborative.</li>
<li>You can stay technical while going up the career ladder without having to move into management.</li>
</ul>
<ul class="simple">
<li>My co-workers are so smart, I usually feel pretty stupid.</li>
<li>The challenges are so huge, I think we're 2-10 years ahead of the industry. Working here is like having a crystal ball that lets you see the future of our industry</li>
</ul>
</blockquote>
</div>
</div>
