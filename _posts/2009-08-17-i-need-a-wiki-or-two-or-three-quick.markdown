---
comments: true
date: 2009-08-17 15:00:04
layout: post
slug: i-need-a-wiki-or-two-or-three-quick
title: I need a Wiki (or two, or three) - Quick!
wordpress_id: 445
tags:
- sysadmin
---

OK so you need a [Wiki](http://en.wikipedia.org/wiki/Wiki) in your company? - Not much of a problem just grab a copy of some wiki and there you go. Now that is fine for very small companies. You may need to have a Wiki for each project or departement and have some user rights within those Wikis. What are you gonna do? Create a whole new instance all the way thru everytime? I recommend a [Wiki-Farm](http://en.wikipedia.org/wiki/WikiFarm)!

Let's have some requirements:



	
  * ACL or any kind of permissions for pages

	
  * Shared User Base (mentioned below as an exercise to the reader...)

	
  * Quick Setup of new Wikis


Personally I like [Python](http://www.python.org) and so I naturally prefer a Wiki implemented in Python - [MoinMoin](http://moinmo.in) is such a Wiki. Also since [modwsgi](http://www.modwsgi.org) came up a setup with some webserver in front of it is not only quite easy but also fast.

It's not that much to set up a nice little [Wiki-Farm](http://en.wikipedia.org/wiki/WikiFarm).

Get a copy of the source code and create a nice directory structure to hold your new Wiki-Farm, I'm on [Debian](http://www.debian.org) and this is my test box, so I simply installed [modwsgi](http://packages.debian.org/libapache2-mod-wsgi) to get a nice setup resembling at least some kind of production layout.
{% highlight text %}]
$ # create a nice directory structure
$ sudo cd /srv
$ sudo mkdir -p /srv/moin/code/
$ sudo mkdir -p /srv/moin/wikis/wsgi
$ sudo mkdir -p /srv/moin/wikis/data
$ # grab the source from the mercurial repository
$ sudo hg clone http://hg.moinmo.in/moin/1.8 /srv/moin/code/1.8
$ sudo apt-get install libapache2-mod-wsgi
{% endhighlight %}

Ok now we have a nice little setup to get things started, let's configure [Apache](http://http.apache.org) to get some error messages so that we know Python is actually handling our request...
{% highlight text %}]
$ # copy the configuration from upstream to a place that is maintainable
$ # we'll need this later on
$ sudo cp -i /srv/moin/code/1.8/wiki/server/moin.wsgi /srv/moin/wikis/wsgi/moin18.wsgi
$ sudo cp -i /srv/moin/code/1.8/wiki/config/wikifarm/farmconfig.py /srv/moin/wikis/wsgi/
$ sudo vim /etc/apache2/sites-enabled/000-default
{% endhighlight %}
We actually only need 3 lines (4 actually but this is just simple Apache stuff) of additional configuration for Apache HTTP Server, I personally like a bit overview so I split the lines up to provide a better human readable format.
{% highlight text %}]
alias /moin_static184/ &quot;/srv/moin/code/1.8/wiki/htdocs/&quot;
WSGIScriptAlias /wikis/moin18.wsgi /srv/moin/wikis/wsgi/moin18.wsgi
WSGIDaemonProcess moin18 \
   user=moin18 \
   group=moin18 \
   home=/srv/moin/wikis/18 \
   processes=5 \
   threads=15 \
   maximum-requests=1000 \
   umask=0007 \
   display-name=moin18
WSGIProcessGroup moin18
{% endhighlight %}
Let's see what we did wrong:
{% highlight text %}]
$ sudo apache2ctl -t
apache2: bad user name moin18
{% endhighlight %}
Uh oh! Let's now add the user (and group)
{% highlight text %}]
$ sudo adduser --no-create-home --disabled-login --shell /bin/false moin18
{% endhighlight %}
Debian will ask a few questions and create a user and group appropriate for our requirements. Another time checking the Apache config tells us everyting is fine.
{% highlight text %}]
$ sudo apache2ctl -t
Syntax OK
$ sudo /etc/init.d/apache2 restart
Restarting web server: apache2 ... waiting .
{% endhighlight %}
Ok so let's try the configured URL - [http://localhost/wikis/moin18.wsgi](http://localhost/wikis/moin18.wsgi). Gives us an internal server error and that is _a good thing(TM)_ because we know Apache HTTP is trying to serve something that is configured the wrong way.

So let's fix our [WSGI](http://en.wikipedia.org/wiki/Wsgi) Script. At the top level add the path to the [MoinMoin](http://moinmo.in) package and then add the path to where your WSGI script is located:
{% highlight python %}]
sys.path.insert(0, '/srv/moin/code/1.8/')
sys.path.insert(0, '/srv/moin/wikis/wsgi/')
{% endhighlight %}
Calling [http://localhost/wikis/moin18.wsgi](http://localhost/wikis/moin18.wsgi) again should now show you a nice little error message that looks a bit more like python.

Let's edit the aforementiond _farmconfig.py_ file, we don't need to do that much,  actually I changed only 3 settings:
{% highlight python %}]
# data_dir = &quot;./data&quot; # comment this out to explicitely set the data dir for a single Wiki
data_underlay_dir = '/srv/moin/code/1.8/wiki/underlay/'
superuser = [u&quot;MartinMarcher&quot;, ]
acl_rights_before = u&quot;MartinMarcher:read,write,delete,revert,admin&quot;
{% endhighlight %}
We'll configure the underlay dir, and make sure that there is a user that can do everyting (myself in that case). Now there's the wiki variable at the top of the _farmconfig.py_ file, it has a wiki preconfigured "mywiki". Now the interesting part is to create a simple config that uses everything that
{% highlight python %}]
import farmconfig
class Config(farmconfig.FarmConfig):
    sitename = u&quot;MyWiki&quot;
    data_dir = '/srv/moin/wikis/data/mywiki/'
    page_front_page = u&quot;FrontPage&quot;
{% endhighlight %}
All you need to do is actually tell MoinMoin where it should place the data and what the start page of your Wiki is (the last one is actually a lie but I like the implicit mentioning of the configuration parameter more that having it in the _farmconfig.py_).

Nearly finished, let's set up the underlay_dir which holds the help pages provided by MoinMoin upstream and also fix the permissions:
{% highlight text %}]
$ sudo tar -C /srv/moin/code/1.8/wiki -tf /srv/moin/code/1.8/wiki/underlay.tar
$ sudo chown -R moin18:moin18 /srv/moin/code/1.8/wiki/underlay
{% endhighlight %}
Also we need the data_dir set up correctly for our shiny new wiki:
{% highlight text %}]
$ sudo cp -a /srv/moin/code/1.8/wiki/data/ /srv/moin/wikis/data/mywiki/
$ sudo chown -R moin18:moin18 /srv/moin/wikis/data/mywiki/
{% endhighlight %}
That's about it. You now have a nice Wiki in place you can send as a gift to your customers. Actually that was not quite as short as one might think but the effort pays of with a second wiki.

Wiki-Farms in MoinMoin work by matching the request URI. go to your _farmconfig.py_ (_/srv/moin/wikis/wsgi/farmconfig.py_) and edit the list variable called wikis. By default it looks like this:
{% highlight python %}]
wikis = [
    # Standalone server needs the port e.g. localhost:8000
    # Twisted server can now use the port, too.                         

    # wikiname,     url regular expression (no protocol)
    # ---------------------------------------------------------------
    (&quot;mywiki&quot;, r&quot;.*&quot;),   # this is ok for a single wiki

    # for multiple wikis, do something like this:
    #(&quot;moinmoin&quot;,    r&quot;^moinmo.in/.*$&quot;),
    #(&quot;moinmaster&quot;,  r&quot;^master.moinmo.in/.*$&quot;),
]
{% endhighlight %}
Now make it look like this and there's just one more step to do for a second wiki:
{% highlight python %}]
wikis = [
    # wikiname,     url regular expression (no protocol)
    # ---------------------------------------------------------------
    (&quot;mywiki&quot;, r&quot;^localhost/wikis/moin18.wsgi/mywiki/.*&quot;),
    (&quot;anotherwiki&quot;, r&quot;^localhost/wikis/moin18.wsgi/anotherwiki/.*&quot;),
]
{% endhighlight %}
Now create a new python module in /srv/moin/wikis/wsgi/ and edit the sitename variable accordingly.
{% highlight python %}]
class Config(farmconfig.FarmConfig):
    siteid = u&quot;AnotherWiki&quot;
    sitename = u&quot;AnotherWiki&quot;
    data_dir = '/srv/moin/wikis/data/anotherwiki/'
    page_front_page = u&quot;FrontPage&quot;
{% endhighlight %}
All there's left to do is to create another data dir for your shiny new (second) Wiki and apply the correct permissions:
{% highlight text %}]
$ sudo cp -a /srv/moin/code/1.8/wiki/data/ /srv/moin/wikis/data/anotherwiki/
$ sudo chown -R moin18:moin18 /srv/moin/wikis/data/anotherwiki/
{% endhighlight %}
What we did, in this las step, was:



	
  * create another "data" directory for our new wiki

	
  * give it to the moin18 user and group so that modwsgi can write to it

	
  * tell the _farmconfig.py_ file that we have a second Wiki. This is done by URI matching


The URI matching probably needs a bit of explanation it matches everything except the protocoll part (http:// or https://). Construct it this way:

	
  * <servername> + "/"

	
  * <path to wsgi file + "/"

	
  * <wikiname> + "/"

	
  * ".*$"


To read it in a single line:

	
  * <servername>/<path to wsgi file>/<wikiname>/.*$


Personally there's only one thing that bugs me, the servername, luckily this is Python code and you can easily write some nice code that spits out the right string you need to match the URI in question.

Because it's so much fun, let's create another wiki. Add a third line to the wikis-Variable:
{% highlight python %}]
(&quot;yetanotherwiki&quot;, r&quot;^localhost/wikis/moin18.wsgi/yetanotherwiki/.*&quot;),
{% endhighlight %}
Create the data directory and give it correct permissions:
{% highlight text %}]
$ sudo cp -a /srv/moin/code/1.8/wiki/data/ /srv/moin/wikis/data/yetanotherwiki/
$ sudo chown -R moin18:moin18 /srv/moin/wikis/data/yetanotherwiki/
{% endhighlight %}
One last step left. Copy /srv/moin/wikis/wsgi/mywiki.py to /srv/moin/wikis/wsgi/yetanotherwiki.py and edit the sitename variable. There you go, 3 shiny new wikis.

While the initial setup may seem a bit complicated, once the Wiki-Farm is set up you'll have just as many Wikis as you like in no time afterwards - and they are manageable also.

I recommend you have a look at [HelpOnConfiguration#Paths](http://moinmo.in/HelpOnConfiguration#paths) especially the user_dir variable so that you can have a single userbase for all your Wikis. This is very convenient for multiple Wikis inside a company where everybody "needs" to have the same name thruout all Wiki instances.
