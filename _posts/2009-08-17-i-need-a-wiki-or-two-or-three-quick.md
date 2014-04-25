---
layout: post
title: I need a Wiki (or two, or three) - Quick!
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1270743942";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1270743952";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
  _oembed_bdbabac7ed8ad88b9924e84017eed55a: '{{unknown}}'
author: 
---
<p>OK so you need a <a href="http://en.wikipedia.org/wiki/Wiki">Wiki</a> in your company? - Not much of a problem just grab a copy of some wiki and there you go. Now that is fine for very small companies. You may need to have a Wiki for each project or departement and have some user rights within those Wikis. What are you gonna do? Create a whole new instance all the way thru everytime? I recommend a <a href="http://en.wikipedia.org/wiki/WikiFarm">Wiki-Farm</a>!</p>
<p>Let's have some requirements:</p>
<ul>
<li>ACL or any kind of permissions for pages</li>
<li>Shared User Base (mentioned below as an exercise to the reader...)</li>
<li>Quick Setup of new Wikis</li>
</ul>
<p>Personally I like <a href="http://www.python.org">Python</a> and so I naturally prefer a Wiki implemented in Python - <a href="http://moinmo.in">MoinMoin</a> is such a Wiki. Also since <a href="http://www.modwsgi.org">modwsgi</a> came up a setup with some webserver in front of it is not only quite easy but also fast.</p>
<p>It's not that much to set up a nice little <a href="http://en.wikipedia.org/wiki/WikiFarm">Wiki-Farm</a>.</p>
<p>Get a copy of the source code and create a nice directory structure to hold your new Wiki-Farm, I'm on <a href="http://www.debian.org">Debian</a> and this is my test box, so I simply installed <a href="http://packages.debian.org/libapache2-mod-wsgi">modwsgi</a> to get a nice setup resembling at least some kind of production layout.<br />
[sourcecode langauage="text"]<br />
$ # create a nice directory structure<br />
$ sudo cd /srv<br />
$ sudo mkdir -p /srv/moin/code/<br />
$ sudo mkdir -p /srv/moin/wikis/wsgi<br />
$ sudo mkdir -p /srv/moin/wikis/data<br />
$ # grab the source from the mercurial repository<br />
$ sudo hg clone http://hg.moinmo.in/moin/1.8 /srv/moin/code/1.8<br />
$ sudo apt-get install libapache2-mod-wsgi<br />
[/sourcecode]</p>
<p>Ok now we have a nice little setup to get things started, let's configure <a href="http://http.apache.org">Apache</a> to get some error messages so that we know Python is actually handling our request...<br />
[sourcecode langauage="text"]<br />
$ # copy the configuration from upstream to a place that is maintainable<br />
$ # we'll need this later on<br />
$ sudo cp -i /srv/moin/code/1.8/wiki/server/moin.wsgi /srv/moin/wikis/wsgi/moin18.wsgi<br />
$ sudo cp -i /srv/moin/code/1.8/wiki/config/wikifarm/farmconfig.py /srv/moin/wikis/wsgi/<br />
$ sudo vim /etc/apache2/sites-enabled/000-default<br />
[/sourcecode]<br />
We actually only need 3 lines (4 actually but this is just simple Apache stuff) of additional configuration for Apache HTTP Server, I personally like a bit overview so I split the lines up to provide a better human readable format.<br />
[sourcecode langauage="text"]<br />
alias /moin_static184/ &amp;quot;/srv/moin/code/1.8/wiki/htdocs/&amp;quot;<br />
WSGIScriptAlias /wikis/moin18.wsgi /srv/moin/wikis/wsgi/moin18.wsgi<br />
WSGIDaemonProcess moin18 \<br />
   user=moin18 \<br />
   group=moin18 \<br />
   home=/srv/moin/wikis/18 \<br />
   processes=5 \<br />
   threads=15 \<br />
   maximum-requests=1000 \<br />
   umask=0007 \<br />
   display-name=moin18<br />
WSGIProcessGroup moin18<br />
[/sourcecode]<br />
Let's see what we did wrong:<br />
[sourcecode langauage="text"]<br />
$ sudo apache2ctl -t<br />
apache2: bad user name moin18<br />
[/sourcecode]<br />
Uh oh! Let's now add the user (and group)<br />
[sourcecode langauage="text"]<br />
$ sudo adduser --no-create-home --disabled-login --shell /bin/false moin18<br />
[/sourcecode]<br />
Debian will ask a few questions and create a user and group appropriate for our requirements. Another time checking the Apache config tells us everyting is fine.<br />
[sourcecode langauage="text"]<br />
$ sudo apache2ctl -t<br />
Syntax OK<br />
$ sudo /etc/init.d/apache2 restart<br />
Restarting web server: apache2 ... waiting .<br />
[/sourcecode]<br />
Ok so let's try the configured URL - <a href="http://localhost/wikis/moin18.wsgi">http://localhost/wikis/moin18.wsgi</a>. Gives us an internal server error and that is <em>a good thing(TM)</em> because we know Apache HTTP is trying to serve something that is configured the wrong way.</p>
<p>So let's fix our <a href="http://en.wikipedia.org/wiki/Wsgi">WSGI</a> Script. At the top level add the path to the <a href="http://moinmo.in">MoinMoin</a> package and then add the path to where your WSGI script is located:<br />
[sourcecode langauage="python"]<br />
sys.path.insert(0, '/srv/moin/code/1.8/')<br />
sys.path.insert(0, '/srv/moin/wikis/wsgi/')<br />
[/sourcecode]<br />
Calling <a href="http://localhost/wikis/moin18.wsgi">http://localhost/wikis/moin18.wsgi</a> again should now show you a nice little error message that looks a bit more like python.</p>
<p>Let's edit the aforementiond <em>farmconfig.py</em> file, we don't need to do that much,  actually I changed only 3 settings:<br />
[sourcecode langauage="python"]<br />
# data_dir = &amp;quot;./data&amp;quot; # comment this out to explicitely set the data dir for a single Wiki<br />
data_underlay_dir = '/srv/moin/code/1.8/wiki/underlay/'<br />
superuser = [u&amp;quot;MartinMarcher&amp;quot;, ]<br />
acl_rights_before = u&amp;quot;MartinMarcher:read,write,delete,revert,admin&amp;quot;<br />
[/sourcecode]<br />
We'll configure the underlay dir, and make sure that there is a user that can do everyting (myself in that case). Now there's the wiki variable at the top of the <em>farmconfig.py</em> file, it has a wiki preconfigured "mywiki". Now the interesting part is to create a simple config that uses everything that<br />
[sourcecode langauage="python"]<br />
import farmconfig<br />
class Config(farmconfig.FarmConfig):<br />
    sitename = u&amp;quot;MyWiki&amp;quot;<br />
    data_dir = '/srv/moin/wikis/data/mywiki/'<br />
    page_front_page = u&amp;quot;FrontPage&amp;quot;<br />
[/sourcecode]<br />
All you need to do is actually tell MoinMoin where it should place the data and what the start page of your Wiki is (the last one is actually a lie but I like the implicit mentioning of the configuration parameter more that having it in the <em>farmconfig.py</em>).</p>
<p>Nearly finished, let's set up the underlay_dir which holds the help pages provided by MoinMoin upstream and also fix the permissions:<br />
[sourcecode langauage="text"]<br />
$ sudo tar -C /srv/moin/code/1.8/wiki -tf /srv/moin/code/1.8/wiki/underlay.tar<br />
$ sudo chown -R moin18:moin18 /srv/moin/code/1.8/wiki/underlay<br />
[/sourcecode]<br />
Also we need the data_dir set up correctly for our shiny new wiki:<br />
[sourcecode langauage="text"]<br />
$ sudo cp -a /srv/moin/code/1.8/wiki/data/ /srv/moin/wikis/data/mywiki/<br />
$ sudo chown -R moin18:moin18 /srv/moin/wikis/data/mywiki/<br />
[/sourcecode]<br />
That's about it. You now have a nice Wiki in place you can send as a gift to your customers. Actually that was not quite as short as one might think but the effort pays of with a second wiki.</p>
<p>Wiki-Farms in MoinMoin work by matching the request URI. go to your <em>farmconfig.py</em> (<em>/srv/moin/wikis/wsgi/farmconfig.py</em>) and edit the list variable called wikis. By default it looks like this:<br />
[sourcecode langauage="python"]<br />
wikis = [<br />
    # Standalone server needs the port e.g. localhost:8000<br />
    # Twisted server can now use the port, too.                         </p>
<p>    # wikiname,     url regular expression (no protocol)<br />
    # ---------------------------------------------------------------<br />
    (&amp;quot;mywiki&amp;quot;, r&amp;quot;.*&amp;quot;),   # this is ok for a single wiki</p>
<p>    # for multiple wikis, do something like this:<br />
    #(&amp;quot;moinmoin&amp;quot;,    r&amp;quot;^moinmo.in/.*$&amp;quot;),<br />
    #(&amp;quot;moinmaster&amp;quot;,  r&amp;quot;^master.moinmo.in/.*$&amp;quot;),<br />
]<br />
[/sourcecode]<br />
Now make it look like this and there's just one more step to do for a second wiki:<br />
[sourcecode langauage="python"]<br />
wikis = [<br />
    # wikiname,     url regular expression (no protocol)<br />
    # ---------------------------------------------------------------<br />
    (&amp;quot;mywiki&amp;quot;, r&amp;quot;^localhost/wikis/moin18.wsgi/mywiki/.*&amp;quot;),<br />
    (&amp;quot;anotherwiki&amp;quot;, r&amp;quot;^localhost/wikis/moin18.wsgi/anotherwiki/.*&amp;quot;),<br />
]<br />
[/sourcecode]<br />
Now create a new python module in /srv/moin/wikis/wsgi/ and edit the sitename variable accordingly.<br />
[sourcecode langauage="python"]<br />
class Config(farmconfig.FarmConfig):<br />
    siteid = u&amp;quot;AnotherWiki&amp;quot;<br />
    sitename = u&amp;quot;AnotherWiki&amp;quot;<br />
    data_dir = '/srv/moin/wikis/data/anotherwiki/'<br />
    page_front_page = u&amp;quot;FrontPage&amp;quot;<br />
[/sourcecode]<br />
All there's left to do is to create another data dir for your shiny new (second) Wiki and apply the correct permissions:<br />
[sourcecode langauage="text"]<br />
$ sudo cp -a /srv/moin/code/1.8/wiki/data/ /srv/moin/wikis/data/anotherwiki/<br />
$ sudo chown -R moin18:moin18 /srv/moin/wikis/data/anotherwiki/<br />
[/sourcecode]<br />
What we did, in this las step, was:</p>
<ul>
<li>create another "data" directory for our new wiki</li>
<li>give it to the moin18 user and group so that modwsgi can write to it</li>
<li>tell the <em>farmconfig.py</em> file that we have a second Wiki. This is done by URI matching</li>
</ul>
<p>The URI matching probably needs a bit of explanation it matches everything except the protocoll part (http:// or https://). Construct it this way:</p>
<ul>
<li>&lt;servername&gt; + "/"</li>
<li>&lt;path to wsgi file + "/"</li>
<li>&lt;wikiname&gt; + "/"</li>
<li>".*$"</li>
</ul>
<p>To read it in a single line:</p>
<ul>
<li>&lt;servername&gt;/&lt;path to wsgi file&gt;/&lt;wikiname&gt;/.*$</li>
</ul>
<p>Personally there's only one thing that bugs me, the servername, luckily this is Python code and you can easily write some nice code that spits out the right string you need to match the URI in question.</p>
<p>Because it's so much fun, let's create another wiki. Add a third line to the wikis-Variable:<br />
[sourcecode langauage="python"]<br />
(&amp;quot;yetanotherwiki&amp;quot;, r&amp;quot;^localhost/wikis/moin18.wsgi/yetanotherwiki/.*&amp;quot;),<br />
[/sourcecode]<br />
Create the data directory and give it correct permissions:<br />
[sourcecode langauage="text"]<br />
$ sudo cp -a /srv/moin/code/1.8/wiki/data/ /srv/moin/wikis/data/yetanotherwiki/<br />
$ sudo chown -R moin18:moin18 /srv/moin/wikis/data/yetanotherwiki/<br />
[/sourcecode]<br />
One last step left. Copy /srv/moin/wikis/wsgi/mywiki.py to /srv/moin/wikis/wsgi/yetanotherwiki.py and edit the sitename variable. There you go, 3 shiny new wikis.</p>
<p>While the initial setup may seem a bit complicated, once the Wiki-Farm is set up you'll have just as many Wikis as you like in no time afterwards - and they are manageable also.</p>
<p>I recommend you have a look at <a href="http://moinmo.in/HelpOnConfiguration#paths">HelpOnConfiguration#Paths</a> especially the user_dir variable so that you can have a single userbase for all your Wikis. This is very convenient for multiple Wikis inside a company where everybody "needs" to have the same name thruout all Wiki instances.</p>
