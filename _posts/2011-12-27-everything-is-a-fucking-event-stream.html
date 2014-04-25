---
layout: post
title: Everything is a fucking event stream!
categories: []
tags:
- Cron
- Data logger
- GlusterFS
- Java
- Loggly
- Metadata
- Nagios
- Zabbix
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1324973847";}
author: 
---
<p>I got quite fed up with monitoring systems lately. <strong>I do not see a need for such systems any more</strong>, and I hate to introduce yet another component that does not actually add any value!</p>
<p>No go away and turn around and read something else if you think this is utter bullshit, but recently I took some time to think about what a monitoring system actually does.</p>
<p>In my opinion a monitoring system is nothing more that a logging system. You generate some log message (which actually isn’t a log message) and send it off to a central host (possibly with several level of intermediate hosts) just to fire off a notification your log message.</p>
<p>So what do we have we have a log stream. But since I don’t actually really care about <a class="zem_slink" title="Data logger" href="http://en.wikipedia.org/wiki/Data_logger" rel="wikipedia">log messages</a> let’s generalize a bit and call everything an event!</p>
<h2>Everything is a fucking event stream!</h2>
<blockquote><p>I do mean everything!</p></blockquote>
<p>Let’s begin with syslog (yup classic syslog, no bells and whistles). Have you ever thought about what the separation marker for a syslog event is? I don’t know for sure what it is. For a long time I thought that the only true answer would be a newline.</p>
<p>Hey, <em>who the hell wants to read Java stack traces in a log file or Python or any “multi line message”</em>.</p>
<blockquote><p>I do!</p></blockquote>
<p>Of course I don’t want to use grep or less or anything to work throu those files. I want a tool that understands those messages. Better yet I want a tool that is usable and that let’s me define reusable rules to <em>tag</em> <del>log messages</del> events.</p>
<p>Think of <a class="zem_slink" title="Nagios" href="http://www.nagios.org/" rel="homepage">Nagios</a>:</p>
<p style="padding-left:30px;">You write some plug-in, the plug-in has a log, the plug-in reports to stdout for Nagios messages, the plug-in writes to stderr to tell about errors, there are different levels of verbosity to debug, it has at least 2 different return values</p>
<p>Why on earth is there:</p>
<p style="padding-left:30px;" dir="ltr">A stream of plugin results (usually exit codes), a stream of messages on stdout (meta results?), a stream of log messages (meta2 results?), a stream of messages for stderr (is that logging, monitoring, meta3 results, ignorable?)</p>
<p>On top of that all those kinds of messages are incompatible. <strong>There’s no such thing as structured logging!</strong><br />
Please, please just let me send everything to some remote place where it will be persisted and I have a central view on all my events.</p>
<p>Add as much <a class="zem_slink" title="Metadata" href="http://en.wikipedia.org/wiki/Metadata" rel="wikipedia">meta data</a> as possible.</p>
<p style="padding-left:30px;">source host, receiving host (or hosts if there were several in between), reception times, timestamps -- <strong>and please: do add fractions of a second, host names and ip addresses</strong>, a possibility to extend the amount of meta data</p>
<p>Now when I have a place where I can look at all my events, then and only then I want to make decisions about what I’m interested in. I’m nowhere near deciding on whether this any of this is an alert.</p>
<h2>After the fact tagging</h2>
<p>Nagios, Icinga, <a class="zem_slink" title="Zabbix" href="http://www.zabbix.com/" rel="homepage">Zabbix</a> all force me to make something up. Some test, a probe or whatnot where I have to write some script (Don’t get me wrong: I like scripting -- scripting takes away those repetitive tasks I hate!) and make up arbitrary values that represent a certain level of goodness or badness. OK, CRITICAL, WARNING?</p>
<blockquote><p>WTF? Who said I need three of them?</p></blockquote>
<p>Just let me define some criteria that will match events. Please note that I am not restricting the criteria to regular expressions. Something like “Has the meta data field X”, “Does not have meta data field Y”, “After January 1st 1992 but not before May 3rd 1982”, “Only between 13:00h and and 13:15h when the load was higher than 3 on systems with with only 2 cores” and so on. Those are equally important.</p>
<blockquote><p>Uh, oh! I just defined some <a class="zem_slink" title="Plug-in (computing)" href="http://en.wikipedia.org/wiki/Plug-in_%28computing%29" rel="wikipedia">plug-ins</a>, now I’m back at monitoring! No I’m not!</p></blockquote>
<p>I ran a <a class="zem_slink" title="Cron" href="http://en.wikipedia.org/wiki/Cron" rel="wikipedia">cron job</a> (in the simplest case) that generated an event which told me the load, and another cron job that told me the number of cores in the system. This event was sent to my <a class="zem_slink" title="Sink (computing)" href="http://en.wikipedia.org/wiki/Sink_%28computing%29" rel="wikipedia">event sink</a> for later processing!</p>
<p>I need to be able to save those criteria collections as filters/view or whatever you want to call them and I need to be able to name those things so that I can find them later on. I simply want to label my events.</p>
<p>I need to be able to attach as many labels to events as I see fit. Also I need the ability to find unlabeled events.</p>
<h2>Which brings us to alerts!</h2>
<p>So now that I know what’s interesting and gives me the ability to make educated decisions about what’s actually interesting I can decide on when it’s worth to raise something that will wake me up in the middle of the night.</p>
<p>I do want to be able to generate alerts and send them of to some other system...</p>
<blockquote><p>Hey look! Another event stream!</p></blockquote>
<p>...and then I’d rather not want to specify when things go bad. I’d rather would like to specify when things are good. Everything else is just <strong>badness enumeration</strong>.</p>
<p>I’d rather triple the amount of time I invest in such a system than to create yet another monitoring system that doesn’t use what’s already there.</p>
<h2>But today's alerts aren’t worth anything tomorrow!</h2>
<p>Any system that silently throws away data is useless (I’m looking at you Munin and friends). I’m not saying <a class="zem_slink" title="RRDtool" href="http://oss.oetiker.ch/rrdtool/" rel="homepage">RRDtool</a> is a bad thing. I love it, the problem is how people use it.</p>
<p>Throw away data? Come on, who wants this? I do want to the finest possible resolution, we have Hadoop, <a class="zem_slink" title="GlusterFS" href="http://www.gluster.org" rel="homepage">GlusterFS</a>, Ceph. Storage is something that shouldn’t be in the way. I’d rather have only 7 days of data than a year of useless junk.</p>
<p>Of course there’s trends over long periods of time but those shouldn’t be the default, those should be something that are added on top of existing data!</p>
<p>How are today’s alerts helpful if I can’t possibly tell what happened yesterday between 15:03h and 15:07h?</p>
<h2>Yes this actually is basic stuff</h2>
<blockquote><p>But it’s just a syslog server and some scripts!</p></blockquote>
<p>Yup you are absolutely right, and that’s the reason why companies like Splunk and <a class="zem_slink" title="Loggly" href="http://www.loggly.com/" rel="homepage">Loggly</a> make money right? Because anyone just has stuff like that. It’s a default, no more to-dos, nothing to see just go along!</p>
<p>Ah so you don’t actually have it? Neither do I. But I’d love to! Please someone skilled create such a system and make it open source!</p>
<blockquote><p>On top of that: make it near real time!</p></blockquote>
<p style="text-align:right;"><em>/serverhorror</em></p>
