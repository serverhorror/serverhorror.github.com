---
layout: post
title: Rethinking Compliance
categories: []
tags: []
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1307092072";}
author: 
---
<div class='posterous_autopost'>
<p><strong>BIG FAT WARNING</strong><br /> This is not about legal compliance; it&rsquo;s about basic compliance and actually it&rsquo;s even more about talking to each other before doing something like this. You do not want to end up with some ueber-cool system that nobody wants to use. You want that people accept the system, hell they shouldn&rsquo;t just accept it &mdash; it should be natural to them to use the whatever <strong>compliant services</strong> are provided. Because the are easy to use and because they do the job <em>at least well</em>.<br /> If you want to have compliance and you do it in a way that users don&rsquo;t like they will find ways around it.</p>
<p>I&rsquo;ve had some thoughts about what compliance actually is. Basically compliance is nothing more than trying to save money by agreeing to a standard. Therefore everyone just can work with the same set of tools.</p>
<p>What this means: Say I want to serve static content, common sense tells me that I&rsquo;d like to agree to some software and probably some kind of directory structure where everyone just puts files and they will be publicly available.</p>
<p>Let&rsquo;s take another step. Why do I need to create directories myself? Probably the only reason is because there&rsquo;s no API that just let&rsquo;s me upload stuff and and then tells me a URL where it&rsquo;s available. So there&rsquo;s some automation missing.</p>
<p>Let&rsquo;s take a company that earns money by providing <em>something</em> thru http. What could be the basic things I want?</p>
<p>I&rsquo;d like to be able to make static content available.</p>
<ul>
<li>I need a content farm</li>
<li>I need a way to make the content available <em>automagically</em></li>
</ul>
<p>Also I&rsquo;d probably like to tell my content farm something like:</p>
<blockquote class="posterous_short_quote"><p><em>Hey, look I have this file here. I want to make it available. I want the domain under which it is reachable to be <code>example.invalid</code></em></p>
</blockquote>
<p>So I want a way to specify that as well. Now let&rsquo;s define <strong>something we don&rsquo;t expect</strong>:</p>
<ul>
<li><em>automagically</em> Versioned content</li>
</ul>
<p>If I upload some file <code>new_cool_aid.png</code> and then somebody else comes and uploads the same file again it&rsquo;ll be overwritten. No way to restore the old version from our system, no magic <em>Trash Bin</em> that will version all of that somehow. It&rsquo;s simply overwritten.</p>
<p>But then again something we do expect, given I have to files <code>new_cool_aid.png</code> with different content. I want both files to be available.</p>
<ul>
<li>
<p><a href="http://en.wikipedia.org/wiki/Content-addressable_storage">Content-addressable Storage</a>.</p>
<p>I belive the <a href="http://git-scm.org">Git Version Control System</a> is the most commonly known one of those.</p>
</li>
</ul>
<p>OK, I was just talking about some requirements and some ideas. Now that&rsquo;s all nice and shiny. It&rsquo;s not up to me to implement that here. Maybe I&rsquo;ll just put something on <a href="http://github.com/serverhorror/">my github account</a> and see if anybody uses it.</p>
<p>On the other hand; I&rsquo;ll probably implement this at my current employer so I have no idea wether or not I&rsquo;ll get clearance about making that publicly available. In my mind I have the system ready, actually it should just be a matter of a few days to get the basic version up and running. It may not be as scalable as I&rsquo;d like it to be initially; scaling is actually the hard part about it :)</p>
</div>
