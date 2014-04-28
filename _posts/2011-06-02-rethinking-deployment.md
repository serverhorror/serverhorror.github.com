---
layout: post
title: Rethinking Deployment
categories: []
tags:
- Application programming interface
- Google AppEngine
- Hello world program
- Heroku
- Java
- Python
- Web application
- Web Server Gateway Interface
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1322875060";}
  _wpas_skip_linkedin: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_twitter: '1'
  _oembed_78f48376f847ada37fd7bbbebba9b3f2: '{{unknown}}'
author: 
---
<div class="posterous_autopost">
<h1>Rethinking <a class="zem_slink" title="Software deployment" href="http://en.wikipedia.org/wiki/Software_deployment" rel="wikipedia">Deployment</a></h1>
<p>Probably everyone knows something about one of the following environment:</p>
<ul>
<li><a href="https://appengine.google.com/">Google AppEngine</a> (runs <a href="http://www.python.org">Python</a>, <a href="http://www.java.com/">Java</a> and recently also <a href="http://golang.org">Go</a>)</li>
<li><a href="http://www.ep.io">ep.io</a> (runs <a href="http://www.python.org">Python</a>)</li>
<li><a href="http://www.engineyard.com/">Engine Yard</a> or <a href="http://www.heroku.com">Heroku</a> (runs <a href="http://www.ruby-lang.org">Ruby</a>)</li>
</ul>
<p>What you usually get from services like these is easy deployment and kind of a <em>namespace for your app</em>. By namespace I mean some kind of container that keeps your app from crashing because someone else did something bad on the server and vice versa. This is naturally what you want because you run in a hosted environment, that means you don’t actually have control about what kinds of apps run on the servers or even how many apps run on the server. Please keep in mind that hosted doesn’t necessarily mean that you pay a third party for hosting your stuff. It might as well be some service within the very own company.</p>
<p>Not a bad thing in and on itself. Just something to get used to.</p>
<p>Of course there are some things to keep in mind with that kind of automated deployment. One of the more problematic things will be how to ensure that only working apps will get deployed.</p>
<p>After all you don’t want some fancy, easy to use deployment mechanism just to take your main site down every 15 minutes. Of course you could then just easily deploy the last version again and be up and running. Still this is not a desireable solution.</p>
<p>We now know a few requirements:</p>
<ul>
<li>easy deployment (more on that later)</li>
<li>versioned deployment</li>
</ul>
<h2>Versioned Deployment</h2>
<p>Versioned deployment means that the same app must be deployable multiple times. Somehow the deployment system must be able to differentiate between the same app deployed multiple times. It’s only natural (at least to me) to use a version number. This actually brings in another requirement:</p>
<ul>
<li>semantic version numbers</li>
</ul>
<p>What does that mean? Don’t just use some random string, there needs to be a notion of comparison between versions. In simple Terms it must support the following operations:</p>
<ul>
<li>is larger than</li>
<li>is smaller than</li>
<li>is equal to</li>
</ul>
<p>There’s the nice <a href="http://semver.org">semver.org</a> site that tries to <em>standardize</em>. Personally I agree with the spec, except for the <em>special version number</em>, I just don’t see a need for it. I’m perfectly fine without it.</p>
<p>Another quite simple version number would be a unix timestamp or the date and time of the release. I suggest something like 201105261324 — but to be honest; just staying with the spec from <a href="http://semver.org">semver.org</a> is perfectly fine. <strong>It’s defined, it’s there; no need to reinvent the wheel!</strong></p>
<h2>Easy Deployment</h2>
<ul>
<li><a href="http://pivotallabs.com/talks/30-next-generation-application-deployment">http://pivotallabs.com/talks/30-next-generation-application-deployment</a></li>
</ul>
<p>Easy deployment actually means that developers have to live with quite a lot of constraints. I can’t imagine a system that allows you to do anything you can think of and still have a notion of easy deployment.</p>
<p>Contraints (or rather restrictions) have a bad side taste. Maybe I can’t write to disk. Maybe I can’t configure my logging the way I want. Maybe I don’t have the possibility of accessing the database I like best.</p>
<p>These kinds of contraints come in varying sizes and tastes. The most basic thing that won’t be available is random access to the file system. Or even the expectation that whatever you write to the file system may be there in half an hour.</p>
<p>To <a href="http://serverhorror.eu/rethinking-compliance">quote myself</a> (yeah, I know…):</p>
<blockquote class="posterous_medium_quote"><p>You want that people accept the system, hell they shouldn’t just accept it — it should be natural to them to use the whatever compliant services are provided. Because the are easy to use and because they do the job at least well.</p>
<p>If you want to have compliance and you do it in a way that users don’t like they will find ways around it.</p></blockquote>
<p>What this actually means is that for every expectation (or at least most of them) people have regarding a system, there needs to be a solution. This solution must be well thought of. I couldn’t just throw some bad API at the users and expect that people will use the deployment system.</p>
<p>The most basic requirements to deploy (web) software are:</p>
<ul>
<li>Application <em>Entry Points</em></li>
<li>Application Configuration</li>
<li>Have a <em>caching API</em></li>
<li>Have a <em>persistence API</em></li>
<li>Have a <em>data query API</em> (specifically not resctricted to SQL)</li>
<li>Have a <em>logging API</em></li>
<li>Have at <em>least very good documentation</em> for all of the above</li>
</ul>
<p>This is what needs to be available to write some app against a restricted environment. Much of this is actually just what <a href="https://appengine.google.com/">Google AppEngine</a> provides.</p>
<p>Let me construct a system that has the basic properties mentioned above. We’ll restrict to the following:</p>
<ul>
<li>Python <a class="zem_slink" title="Web application" href="http://en.wikipedia.org/wiki/Web_application" rel="wikipedia">Web Applications</a> that are accessed thru an <code>application</code> object that is a <a href="http://www.python.org/dev/peps/pep-0333/">WSGI</a> instance</li>
<li>You will run on <a href="http://www.python.org">python2.5</a></li>
<li>The application needs to be self contained
<ul>
<li>this implies that if you use <a href="http://webpy.org">web.py</a> you need to make sure that it’s importable from within you application. You cannot expect <a href="http://webpy.org">web.py</a> to be somehow magically available</li>
<li>this also means that you can only use pure python modules</li>
</ul>
</li>
</ul>
<p>I’ll ber very unspecific here. I hope nobody expects me to to use a magic hat and just pull out a solution. I hope the basic idea will still come through.</p>
<h3>Entry Points</h3>
<p>I just implicitely defined that above. Just make a WSGI application, a simple one like the <a href="http://webpy.org/cookbook/mod_wsgi-apache"><code>web.py</code> cookbook sample</a> is enough:</p>
<div class="CodeRay">
<div class="code">
{% highlight python %}
import web
urls = ( '/.*', 'hello', )

class hello:
	def GET(self):
		return


application = web.application(urls, globals()).wsgifunc()
{% endhighlight %}
</div>
</div>
<h3>Application Configuration</h3>
<p>This mostly about data that shouldn’t be the default. For web application this means:</p>
<ul>
<li>cookie/session secret</li>
<li>API credentials (which may be different for different <a class="zem_slink" title="Application programming interface" href="http://en.wikipedia.org/wiki/Application_programming_interface" rel="wikipedia">APIs</a>)</li>
<li>other data that is not under the direct control of a user</li>
</ul>
<h3>Caching API</h3>
<p><strong>Note</strong>: Stealing from <a href="http://memcached.org/"><code>memcached</code></a> here. You might want to read up on <a href="http://code.sixapart.com/svn/memcached/trunk/server/doc/protocol.txt">the memcached protocol</a></p>
<p>Some assumptions that need to be dealt with:</p>
<ul>
<li>Cached items may expire at any time</li>
<li><code>set</code>ing something doesn’t mean that the next time I want to retrieve it it’s still there (yes this is actually <strong>very, very, very bad</strong> – just trying to simplify)</li>
</ul>
<p>Basic idea:</p>
<div class="CodeRay">
<div class="code">
<pre>[bytes]  set   get</pre>
</div>
</div>
<h3>Persistence API</h3>
<p>This should be nothing special. Just <code>write(bytes)</code> and <code>read(identifier)</code>. I like the notion of content-addressed storage for that part so I’m biased. But the <code>identifier</code> could be anything. A path a sha1-sum, really anything.</p>
<p>Again stealing from above (and yes, this works in the real world – just look at <a href="http://www.basho.com">riak</a>).</p>
<p>There’s something go keep in mind here: I want to make sure nobody writes vast amounts of data, either in a single object or by issuing a multitude of <code>write</code>s that’ll take down the system. I want some kind of quote. Say 100 GiB per application.</p>
<p>Basic idea:</p>
<div class="CodeRay">
<div class="code">
<pre>[bytes]  write   read</pre>
</div>
</div>
<h3>Data Query API</h3>
<p>This get’s a bit more tricky. Usually as soon as I take away SQL from some kind of data query I hear screams. I’m not saying SQl is bad or wrong in any way. But as soon as there aren’t dedicated DBAs involved that will take care of largish databases most servers run into a problem.</p>
<p>For the sake of simplicity let’s stay with a nice simple (for certain definitions of simple) SQL database. I’d allow people to:</p>
<ul>
<li><code>CREATE TABLE</code>,</li>
<li><code>DROP TABLE</code>,</li>
<li><code>CREATE VIEW</code>,</li>
<li><code>SELECT</code>,</li>
<li><code>INSERT</code>,</li>
<li><code>DELETE</code></li>
</ul>
<p>Maybe even:</p>
<ul>
<li><code>CREATE INDEX</code>,</li>
<li><code>DROP INDEX</code>.</li>
</ul>
<p>Things I specifically wouldn’t allow (speaking in MySQL permissions here):</p>
<ul>
<li><code>CREATE TEMPORARY TABLES</code></li>
<li><code>SELECT INTO OUTFILE</code></li>
<li><code>COPY FROM FILE</code></li>
</ul>
<p>Basically I’d let everyone talk to his/her own database with basic usage rights. But especially deny everything that would need access to the filesystem or something near that.</p>
<h3>Logging API</h3>
<p>This is a special case. All of the above were external things. External in the sense that there’s no problem by only allowing communication to run thru some sort of tcp connection. Logging however would should be available as a “<em>local</em>” API call. I’d just stay with the standard python logging library.</p>
<p>The important point would be that users must not set up their own Handlers. Basically people are allowed to either use a <code>StreamHandler</code> or a <code>NullHandler</code>.</p>
<p>A <code>StreamHandler</code> would be exactly what any other log system does. Provide a stream of events. An event isn’t necessarily something that ends with a newline. But the point is that writing something to the filesystem through the logging API sets up expectatiions that these log events will later be available. This assumption is wrong. The only events that will be available will be the ones that have been emitted through the <code>StreamHandler</code>s provided by the system.</p>
<p>What’s the point in providing a NullHandler? To be honest I can’t think of one. But hey! There’s gotta be some choice :)</p>
<h3>Documentation</h3>
<p>I’m a believer of learning by example. This has 2 advantages:</p>
<ul>
<li>diving in is easy</li>
<li>by writing examples I will be a user</li>
</ul>
<p>The last point is a “<em>eat your own dogfood</em>” argument. But it will inflict the same pain on me that the users of the system have. Thus it will get better “<em>real soon now</em>”™.</p>
<p>Jokes aside. There’s a third point to it. Libraries will pop up for free. By writing code against the carefully designed APIs I will automagically create libraries to make my life easier, I will then either publish these libraries or incorporate the libraries in the existing API thus making everyone elses life easier.</p>
<p>The valid point of “If you need to create a library it’s not good enough” has a shortcoming here. If the API is just some HTTP-Restful API this API could be very good. But why not just create a library that will do directly in Python (or Ruby, Java, <a href="http://golang.org">Go</a>), after all nearly everyone will be using these libraries and by providing them I have the potential to take serverload away by optimizing a single library and updating it on the server.</p>
<p>Original Post: http://serverhorror.eu/rethinking-deployment New Blog Location: http://serverhorror.eu</p>
</div>
