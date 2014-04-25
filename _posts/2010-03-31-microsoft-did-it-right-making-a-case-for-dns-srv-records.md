---
layout: post
title: Microsoft did it right! (Making a case for DNS SRV records)
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275723776";}
  _wpas_done_fb: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1295290317";}
  _wpas_mess: 'Microsoft did it right! (Making a case for DNS SRV records): http://wp.me/pxxjT-9n'
  _wpas_done_yup: '1'
author: 
---
<p>Yes the people over at Microsoft do (quite?) some stuff <a href="http://technet.microsoft.com/en-us/library/cc961719.aspx">the correct way</a>. Among those things is the excessive usage of <a href="http://en.wikipedia.org/wiki/SRV_record">DNS SRV records</a>.</p>
<p>I'm saying this because I think  a some tools will benefit from the usage, namely:</p>
<ul>
<li>Firefox (that even benefits end users not only IT people) and</li>
<li>Configuration Management Tools</li>
</ul>
<p>Consider the following use cases:</p>
<ul>
<li>Mass hosting SSL enabled websites</li>
<li>Discovering where get information or where to put it for automated tools</li>
<li>Automagically discover where a login service is</li>
<li>...</li>
</ul>
<p>The tool that comes to my mind first is <a href="http://puppet.reductivelabs.com">puppet</a>. We use the tool quite extensively in our infrastructure and now deploying a new host is actually just the work of a few minutes. Thanks to my colleagues who invested vast amounts of time into setting up all the modules we need puppet will nearly automatically configure a host and even set up tests in Nagios to make sure service availability.</p>
<p>However the main "<em>problem</em>" remaining (although solved by using a packages tailored to our needs) is the conventions a default puppet installation makes. Namely it expects the master host to be reachable by DNS on a host named "<em>puppet</em>". That isn't consistent with the <a href="http://serverhorror.wordpress.com/2009/06/15/naming-schemas-that-work-or-not/">naming scheme we made up for our hosts</a>. So why not use a perfectly available standard to discover where the correct endpoint is (yes Microsoft keeps to a standard - at least in some way)?</p>
<p>Staying with the example of puppet I'd like to see that puppet tries to find the master node by doing a DNS query that asks for the <tt>_x-puppet._tcp.example.com</tt> SRV record. So in accordance to our naming schema we could simply answer with <tt>its-devl-puppet01.example.com</tt> or any other suitable host.</p>
<p>So what about the rest of the above examples?</p>
<p>Consider SSL mass hosting with a single IP and say you give each VHost another port starting at 8441.</p>
<p>{% highlight text %}<br />
_https._tcp.example.com. 3600 IN SRV 0 10 8441 www.example.com.<br />
_https._tcp.example.net. 3600 IN SRV 0 10 8442 www.example.net.<br />
_https._tcp.example.org. 3600 IN SRV 0 10 8443 www.example.org.<br />
{% endhighlight %}</p>
<p>Granted with <a href="http://en.wikipedia.org/wiki/Server_Name_Indication">Server Name Indication</a> that problem is already solved, but I know  a few setups that for certain reasons won't be able to upgrade to packages that are able to use that technique. And personally I think that this approach is nicer especially since it solves this problem for every service. Take Thunderbird 3, it <em>tries autodiscovery</em> but quite often fails. If there was a <tt>_pop3._tcp.example.com</tt> SRV entry it would just work.</p>
<p>Also granted, there are quite a few protocols that already benefit from this, Kerberos clients, should do, (or rather "<a href="http://www.rfc-editor.org/rfc/rfc4120.txt">RFC4120</a> compliant clients" should do) autodiscovery in the way I described it.</p>
<p>So actually this is a plea to the developers out there. If you create services that expect some endpoint reachable over TCP or UDP don't just juse a "This is the default hostname convention". Nothing wrong with that as a fallback, but please (please, please) also allow us SysAdmins who have to deal with compliance rules to use existing ways to specify where to connect to that automagically work, and don't have to edit a file on every box or instance we have to take care of.</p>
<p>Especially for cases like configuration management, once tested we like to roll stuff out on quite a few boxes, and to keep maintenance low we also love it if we can use the default upstream sources (be it from the favorite distribution or the original upstream). And that is the case I'm making here. We have to be compliant with some rules and probably have (or have to) access more boxes than a single developer, so we may encounter cases you haven't thought of.</p>
<p>We are happy to send you accurate bug reports but please listen to us sometimes.</p>
<p>Enough begging for today...</p>
