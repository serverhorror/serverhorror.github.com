---
layout: post
title: About the FHS not being right...
categories: []
tags:
- fhs
- filesystem
- linux
- srv
- standard
- sysadmin
- var
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1319733773";}
  _wpas_done_yup: '1'
  _wpas_done_twitter: '1'
  _wpas_done_fb: '1'
author: 
---
<p><a href="http://utcc.utoronto.ca/~cks/">Chris Siebenmann</a> wrote about the <a href="http://utcc.utoronto.ca/~cks/space/blog/linux/FHSNotAlwaysRight">FHS not being right</a>. Well I can't say I disagree completely but the points he makes aren't quite the points I dislike about the FHS.</p>
<blockquote><p>Dear Chris,</p>
<p>Err...have you read about <tt>/srv</tt> (<a title="/srv : Data for services provided by this system" href="http://www.pathname.com/fhs/pub/fhs-2.3.html#SRVDATAFORSERVICESPROVIDEDBYSYSTEM">http://www.pathname.com/fhs/pub/fhs-2.3.html#SRVDATAFORSERVICESPROVIDEDBYSYSTEM</a>)?
Seems to me that it's not <tt>/var</tt> you should target with your comments but rather <tt>/srv</tt>. Then again I haven't seen any package management that does soemthing to <tt>/srv</tt> - which in my opinion whould make the critic pointless (correct me if I'm wrong). Actually <em>I never even considered putting site-local data into the <tt>/var</tt> hierarchy</em> exactly because I consider it to be the space where my distribution does it's things.</p>
<p>On a side note I just wish that there was a site alternative for <tt>/etc</tt>.</p></blockquote>
