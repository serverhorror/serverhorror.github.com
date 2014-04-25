---
layout: post
title: Rethinking Storage (again...)
categories: []
tags: []
status: publish
type: post
published: true
meta:
  _wpas_mess: 'Rethinking Storage (again...): http://wp.me/pxxjT-kk'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1306442938";}
  _wpas_done_yup: '1'
  _wpas_done_twitter: '1'
author: 
---
<p>Initially I started to write this down in the wordpress.com WYSIWYG editor. It was more like <em>What You See Is What You Deserve</em>. So I fired up a text editor and just wrote it down in markdown.</p>
<p>If anyone knows about a nice hosted blog where I can just throw markdown at it I'll be grateful...</p>
<pre>Today I was once again on the hunt for a storage solution. Having the naive
idea of a one size fits all and wading thru piles of old bookmarks I had a
genius moment...

* There's no one size fits all! (*Can you believe it? -- No shit, Sherlock!*)

So which sizes (categories) would you need? Of course that's just generally
speaking and kind of a no-brainer, if you really think about it, but given the
amount of bookmarks and thoughts I had filed under storage I need to write
this down so that I can reference this in the future.

Ok let's get started.

# Persistence

OK, so persistence means to me a lot of things. There's a local filesystem (as
in Maildir, mbox, local files, whatever floats your boat) all kinds of SQL
databases, all kinds of NoSQL databases.

Then there are *distributed filesystems*, *distributed fault tolerant
filesystems* and a whole stack of other categories. That would then be storage
APIs like Amazon S3, Cleversafe, Google has something too...

## So why is persistence something that's actually important?

Simple reason, power down a server (or for that matter a whole datacenter) and
boot it again. There's gotta be someway to restore state. That's the most
basic reason why I need persistence.

Of course I can go and get GlusterFS, Lustre maybe even Ceph. But all I
essentially care about is that I can somehow just throw nodes at it and there
will be more storage, available under a nice namespace.

Not a single name that when failed renders the whole persistence thing useless
(that would be NFS). By namespace I mean something like I can talk to any
endpoint in the system and it will give me essentially the same thing back --
take care I specifically do not mean Atomicity here. Just that I want to be
able to talk to any server that is in the system

Also there'll be a bunch of different projects that all want to use the
service that our *persistence thingie* provides. So what I need is some kind
of security (broadly speeking).

I want to be able to *let Project A access Namespace A (and only A)* and I want
*Project B to be able to access Namespace A and B*. So that needs to be
configurable.

Right now I don't see a need for a super secure storage. **Something where every
client needs it's own X509 certificate** and the server will verify the
chain of trust. That's just overkill. It's nice to have this as an option, but
definitely **do not make it the only option available**!

## Extracted Requirements

All of the following requirements must be doable while the "persistence thing" is online

* **Scale Up**, or Out or whatever the word of month is for that -- just throw
  more hardware at it and there will be more persistent storage
* Handle Node Failure.

  It's not a disaster if I have 10 nodes and 2 fail. It should just tell me
  about it. A perfect thing would be if it would just say something like:

  &gt; OK, I just found out that 2 of my 10 nodes are missing so I'll simply make
  &gt; sure I have enough copies of the data and tell everyone that now there's
  &gt; less overall storage available!

* A nice API for applications to use the storage. That means:
  * Authentication, Authorization
  * Reading
  * Writing

Requirements that are allowed to be available only as what I'll call offline
operations. It would still be nice if that could be done online:

* Scale Down -- I want to have a way to remove hardware as well

  What if I want to take the system out of service in a couple of years from
  now. Do I really have to set up another complete storage area. I'd think it
  would be nice if I don't have to do that but could simply unprovision parts
  of the system.

  The requirement isn't quite that hard because I guess if I buid up a new
  system then there has to be bugdet for it. And if the the average box in my
  storage system is 2 years old, each box in the new system probably has a lot
  more storage than each box in the old system.

# Caching

There's another kind of storage. Caching! This has mostly *non-requirements*
(lacking a better term; these are the things I wouldn't expect from a cache
layer - but I wouldn't get mad if it had those features)

* Persistence -- Yes, really! I don't expect data in a caching layer to
  survive reboots
* Scale Up/Down
* **Add and Remove** nodes on the fly
* **Handle unexpected failure** of nodes
* Essentially all the things scalaris provides
* A nice API for applications!

# Logging

That may be a strange requirement for storage. But, personally, I need to know
what's going on. Do log structured data. That means (honestly stolen from the
[Logstash style
guide](https://github.com/logstash/logstash/blob/master/STYLE.md))

Rather than this:

    "Some error occured in request #{request} on input #{input} from client #{ip}"

Do this:

    ["Some error occured in this request", { :request =&gt; request, :input =&gt; input, :client =&gt; ip}]

I have yet to find server software that does this in a way where I don't want
to run away and cry. Please, please anyone who writes daemon software either
use JSON or something else that is easy to parse and still somewhat
human-readable or read
[RFC5424#Section-6.3](http://tools.ietf.org/html/rfc5424#section-6.3) (at
least, better read the whole thing).

# Monitoring

Yes, apart from that I want to be able to read what's going on I want to be
able to ask the daemon (and preferrably the system as a whole) about the
things that are going on. Sure I can just ICMP ping all the servers, sure I
can test wether a port accepts TCP connections. And if that goes wrong I know:

&gt; Hey, another one of the 10 servers is down

But what I really want to know is:

&gt; Geeh! It's 3.42AM, do I really have to care about that or can I just get
&gt; back to sleep and fix that tomorrow?</pre>
