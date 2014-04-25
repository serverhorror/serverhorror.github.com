---
layout: post
title: Openx has PostgreSQL support – NOT!
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  _wpas_done_fb: '1'
  _wpas_done_twitter: '1'
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275723775";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1295290316";}
author: 
---
<p>This is what you get from <a href="http://www.openx.org/">OpenX</a> if you want to use a <a href="http://www.postgresql.org">PostgreSQL</a> database (which is supported!):
{% highlight text %}
PEAR Error </p>
<p>MDB2 Error: unknown error </p>
<p>_doQuery: [Error message: Could not execute statement]
[Last executed query: SELECT m.clientid AS advertiser_id,d.campaignid AS placement_id,s.ad_id AS ad_id,SUM(s.impressions) AS sum_views,SUM(s.clicks) AS sum_clicks,SUM(s.revenue) AS sum_revenue, m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height  AS ad_id,( m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height ) AS pkey FROM &quot;ext_market_stats&quot; AS s INNER JOIN &quot;banners&quot; AS d ON (d.bannerid=s.ad_id) INNER JOIN &quot;campaigns&quot; AS m ON (m.campaignid=d.campaignid) INNER JOIN &quot;clients&quot; AS a ON (a.clientid=m.clientid) WHERE a.type = 1 AND s.zone_id <> 0 AND s.date_time>='2010-04-15 00:00:00' AND s.date_time<='2010-04-15 23:59:59' GROUP BY advertiser_id,placement_id,pkey]
[Native message: ERROR:  column &quot;s.ad_id&quot; must appear in the GROUP BY clause or be used in an aggregate function]</p>
<p>PEAR Error</p>
<p>MDB2 Error: unknown error</p>
<p>_doQuery: [Error message: Could not execute statement]
[Last executed query: SELECT m.clientid AS advertiser_id,d.campaignid AS placement_id,s.ad_id AS ad_id,SUM(s.impressions) AS sum_views,SUM(s.clicks) AS sum_clicks,SUM(s.revenue) AS sum_revenue, m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height  AS ad_id,( m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height ) AS pkey FROM &quot;ext_market_stats&quot; AS s INNER JOIN &quot;banners&quot; AS d ON (d.bannerid=s.ad_id) INNER JOIN &quot;campaigns&quot; AS m ON (m.campaignid=d.campaignid) INNER JOIN &quot;clients&quot; AS a ON (a.clientid=m.clientid) WHERE s.zone_id = 0 AND a.type = 1 AND s.date_time>='2010-04-15 00:00:00' AND s.date_time<='2010-04-15 23:59:59' AND s.zone_id = 0 GROUP BY advertiser_id,placement_id,pkey]
[Native message: ERROR:  column &quot;s.ad_id&quot; must appear in the GROUP BY clause or be used in an aggregate function]</p>
<p>Fatal error: Unsupported operand types in .../www/admin/market/stats.php on line 164
{% endhighlight %}</p>
