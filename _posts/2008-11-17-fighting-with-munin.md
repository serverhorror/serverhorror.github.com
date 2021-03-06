---
layout: post
title: Fighting with munin
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  blogger_blog: ctrl.alt.delete.co.at
  blogger_author: MartinMarchernoreply@blogger.com
  blogger_permalink: /2008/11/fighting-with-munin.html
author: 
---
I had a nice fight with a [Munin](http://munin.projects.linpro.no/)
plugin yesterday evening. The problem was that according [to the
docs](http://munin.projects.linpro.no/wiki/HowToWritePlugins) a munin plugin is
called with an argument count of 2 (the name of the plugin itself and the
`config` parameter).

This is all nice and well but from my experience isn't quite true. I had the problem that the graphs from munin were created configured fine. However no values were drawn.
{% highlight python %}
import sys
if (len(sys.argv)) == 2:
    if sys.argv[1] == "config":
        print "I need to ouptut the configuration directives"
    if sys.argv[1] == "autoconf":
        """This plugin doesn't have 'autoconf' capabilities."""
        print "no"
        sys.exit(1)
else:
    print "I need to output the values"
{% endhighlight %}

Do you see the error? Well I didn't for about 90 minutes. The problem is the
`else` tree. The else tree is executed fine and all correct in the shell and
even when running under the munin user, but I just couldn't get it to print out
the values when called thru the munin network interface (`telnet localhost
4949`)

To get around this I'd suggest the following with python:
{% highlight python %}
import sys
if "config" in sys.argv:
    print "I need to ouptut the configuration directives"
elif "autoconf" in sys.argv:
    """This plugin doesn't have 'autoconf' capabilities."""
    print "no"
    sys.exit(1)
else:
    print "I need to output the values"
{% endhighlight %}

With this it's not only nearly impossible to output the wrong values but also much nicer to read...
