---
comments: true
date: 2010-03-31 19:35:10
layout: post
slug: microsoft-did-it-right-making-a-case-for-dns-srv-records
title: Microsoft did it right! (Making a case for DNS SRV records)
wordpress_id: 581
tags:
- sysadmin
---

Yes the people over at Microsoft do (quite?) some stuff [the correct way](http://technet.microsoft.com/en-us/library/cc961719.aspx). Among those things is the excessive usage of [DNS SRV records](http://en.wikipedia.org/wiki/SRV_record).

I'm saying this because I think  a some tools will benefit from the usage, namely:



	
  * Firefox (that even benefits end users not only IT people) and

	
  * Configuration Management Tools


Consider the following use cases:

	
  * Mass hosting SSL enabled websites

	
  * Discovering where get information or where to put it for automated tools

	
  * Automagically discover where a login service is

	
  * ...


The tool that comes to my mind first is [puppet](http://puppet.reductivelabs.com). We use the tool quite extensively in our infrastructure and now deploying a new host is actually just the work of a few minutes. Thanks to my colleagues who invested vast amounts of time into setting up all the modules we need puppet will nearly automatically configure a host and even set up tests in Nagios to make sure service availability.

However the main "_problem_" remaining (although solved by using a packages tailored to our needs) is the conventions a default puppet installation makes. Namely it expects the master host to be reachable by DNS on a host named "_puppet_". That isn't consistent with the [naming scheme we made up for our hosts](http://serverhorror.wordpress.com/2009/06/15/naming-schemas-that-work-or-not/). So why not use a perfectly available standard to discover where the correct endpoint is (yes Microsoft keeps to a standard - at least in some way)?

Staying with the example of puppet I'd like to see that puppet tries to find the master node by doing a DNS query that asks for the _x-puppet._tcp.example.com SRV record. So in accordance to our naming schema we could simply answer with its-devl-puppet01.example.com or any other suitable host.

So what about the rest of the above examples?

Consider SSL mass hosting with a single IP and say you give each VHost another port starting at 8441.

{% highlight text %}
_https._tcp.example.com. 3600 IN SRV 0 10 8441 www.example.com.
_https._tcp.example.net. 3600 IN SRV 0 10 8442 www.example.net.
_https._tcp.example.org. 3600 IN SRV 0 10 8443 www.example.org.
{% endhighlight %}


Granted with [Server Name Indication](http://en.wikipedia.org/wiki/Server_Name_Indication) that problem is already solved, but I know  a few setups that for certain reasons won't be able to upgrade to packages that are able to use that technique. And personally I think that this approach is nicer especially since it solves this problem for every service. Take Thunderbird 3, it _tries autodiscovery_ but quite often fails. If there was a _pop3._tcp.example.com SRV entry it would just work.

Also granted, there are quite a few protocols that already benefit from this, Kerberos clients, should do, (or rather "[RFC4120](http://www.rfc-editor.org/rfc/rfc4120.txt) compliant clients" should do) autodiscovery in the way I described it.

So actually this is a plea to the developers out there. If you create services that expect some endpoint reachable over TCP or UDP don't just juse a "This is the default hostname convention". Nothing wrong with that as a fallback, but please (please, please) also allow us SysAdmins who have to deal with compliance rules to use existing ways to specify where to connect to that automagically work, and don't have to edit a file on every box or instance we have to take care of.

Especially for cases like configuration management, once tested we like to roll stuff out on quite a few boxes, and to keep maintenance low we also love it if we can use the default upstream sources (be it from the favorite distribution or the original upstream). And that is the case I'm making here. We have to be compliant with some rules and probably have (or have to) access more boxes than a single developer, so we may encounter cases you haven't thought of.

We are happy to send you accurate bug reports but please listen to us sometimes.

Enough begging for today...
