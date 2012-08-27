---
comments: true
date: 2011-06-02 13:25:07
layout: post
slug: rethinking-compliance
title: Rethinking Compliance
wordpress_id: 1281
---

**BIG FAT WARNING**  
This is not about legal compliance; it's about basic compliance and actually it's even more about talking to each other before doing something like this. You do not want to end up with some ueber-cool system that nobody wants to use. You want that people accept the system, hell they shouldn't just accept it -- it should be natural to them to use the whatever **compliant services** are provided. Because the are easy to use and because they do the job _at least well_.  
If you want to have compliance and you do it in a way that users don't like they will find ways around it.

 

I've had some thoughts about what compliance actually is. Basically compliance is nothing more than trying to save money by agreeing to a standard. Therefore everyone just can work with the same set of tools.

 

What this means: Say I want to serve static content, common sense tells me that I'd like to agree to some software and probably some kind of directory structure where everyone just puts files and they will be publicly available.

 

Let's take another step. Why do I need to create directories myself? Probably the only reason is because there's no API that just let's me upload stuff and and then tells me a URL where it's available. So there's some automation missing.

 

Let's take a company that earns money by providing _something_ thru http. What could be the basic things I want?

 

I'd like to be able to make static content available.

 

  * I need a content farm
  * I need a way to make the content available _automagically_
  

Also I'd probably like to tell my content farm something like:

 

> _Hey, look I have this file here. I want to make it available. I want the domain under which it is reachable to be `example.invalid`_

 

So I want a way to specify that as well. Now let's define **something we don't expect**:

 

  * _automagically_ Versioned content
  

If I upload some file `new_cool_aid.png` and then somebody else comes and uploads the same file again it'll be overwritten. No way to restore the old version from our system, no magic _Trash Bin_ that will version all of that somehow. It's simply overwritten.

 

But then again something we do expect, given I have to files `new_cool_aid.png` with different content. I want both files to be available.

 

  * [Content-addressable Storage](http://en.wikipedia.org/wiki/Content-addressable_storage).

 

I belive the [Git Version Control System](http://git-scm.org) is the most commonly known one of those.

  

OK, I was just talking about some requirements and some ideas. Now that's all nice and shiny. It's not up to me to implement that here. Maybe I'll just put something on [my github account](http://github.com/serverhorror/) and see if anybody uses it.

 

On the other hand; I'll probably implement this at my current employer so I have no idea wether or not I'll get clearance about making that publicly available. In my mind I have the system ready, actually it should just be a matter of a few days to get the basic version up and running. It may not be as scalable as I'd like it to be initially; scaling is actually the hard part about it :)
