---
layout: post
title: 'Re: [sqlalchemy] How to filter by date with SA 0.6?'
categories: []
tags: []
status: draft
type: post
published: false
meta: {}
author: 
---
<p>try this:</p>
<p>from sqlalchemy import func</p>
<p>session.query(MyObj).fitler(func.strftime('%Y',MyObj.date_field)=='2004').all()</p>
<p>On 08/16/2010 01:03 PM, Italo Maia wrote:</p>
<p>By the way, sqlite here!</p>
<p>2010/8/16 Italo Maia <italo.m...@gmail.com ></p>
<p>    How's the best way to filter a date field by year?</p>
<p>via <a href='http://www.mail-archive.com/sqlalchemy@googlegroups.com/msg20736.html'>Re: [sqlalchemy] How to filter by date with SA 0.6?</a>.</p>
