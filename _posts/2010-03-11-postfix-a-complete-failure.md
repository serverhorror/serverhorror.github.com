---
layout: post
title: Postfix – A Complete Failure!
categories: []
tags: []
status: publish
type: post
published: true
meta:
  _wpas_done_twitter: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275723777";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1275723778";}
author: 
---
<p>Yes this is a rant.</p>
<ul>
<li>I used to like postfix</li>
<li>Until now I never had the need to do deeper analysis of the postfix logs</li>
<li>I always thought exim was way too complicated</li>
</ul>
<p>2 of the 3 points above changed right now at this very moment. I still think exim is way to complicated but that's probably because I never had to care about configuring it. However we need to analyze the log data of email deliveries, receptions, failures and whatnot.</p>
<p>"<em>How hard can it be?</em>" - at least that was my first thought. <strong>It can be very hard.</strong></p>
<p>Just compare:</p>
<ul>
<li>the <strong>documentation of postfix' log format</strong>: <a title="Re: Postfix log format: formal syntax defined?" href="http://readlist.com/lists/postfix.org/postfix-users/2/12192.html">here</a> and <a title="Re: Format of smtpd reject: log line" href="http://archives.neohapsis.com/archives/postfix/2004-05/1196.html">here</a></li>
<li>the <strong>documentation of exim's log format</strong>: <a title="49. Log files" href="http://exim.org/exim-html-current/doc/html/spec_html/ch49.html">here</a></li>
</ul>
<p>Postfix just died for me from this very moment....</p>
