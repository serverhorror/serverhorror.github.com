---
comments: true
date: 2010-04-15 13:31:07
layout: post
slug: openx-has-postgresql-support-not
title: Openx has PostgreSQL support – NOT!
wordpress_id: 693
tags:
- sysadmin
---

This is what you get from [OpenX](http://www.openx.org/) if you want to use a [PostgreSQL](http://www.postgresql.org) database (which is supported!):
[sourcecode language="text"]
PEAR Error 

MDB2 Error: unknown error 

_doQuery: [Error message: Could not execute statement]
[Last executed query: SELECT m.clientid AS advertiser_id,d.campaignid AS placement_id,s.ad_id AS ad_id,SUM(s.impressions) AS sum_views,SUM(s.clicks) AS sum_clicks,SUM(s.revenue) AS sum_revenue, m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height  AS ad_id,( m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height ) AS pkey FROM "ext_market_stats" AS s INNER JOIN "banners" AS d ON (d.bannerid=s.ad_id) INNER JOIN "campaigns" AS m ON (m.campaignid=d.campaignid) INNER JOIN "clients" AS a ON (a.clientid=m.clientid) WHERE a.type = 1 AND s.zone_id <> 0 AND s.date_time>='2010-04-15 00:00:00' AND s.date_time<='2010-04-15 23:59:59' GROUP BY advertiser_id,placement_id,pkey]
[Native message: ERROR:  column "s.ad_id" must appear in the GROUP BY clause or be used in an aggregate function]

PEAR Error

MDB2 Error: unknown error

_doQuery: [Error message: Could not execute statement]
[Last executed query: SELECT m.clientid AS advertiser_id,d.campaignid AS placement_id,s.ad_id AS ad_id,SUM(s.impressions) AS sum_views,SUM(s.clicks) AS sum_clicks,SUM(s.revenue) AS sum_revenue, m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height  AS ad_id,( m.campaignid || IF( LENGTH(market_advertiser_id) > 0, ('_' || market_advertiser_id || '_'),  '_') || ad_width || ' x ' || ad_height ) AS pkey FROM "ext_market_stats" AS s INNER JOIN "banners" AS d ON (d.bannerid=s.ad_id) INNER JOIN "campaigns" AS m ON (m.campaignid=d.campaignid) INNER JOIN "clients" AS a ON (a.clientid=m.clientid) WHERE s.zone_id = 0 AND a.type = 1 AND s.date_time>='2010-04-15 00:00:00' AND s.date_time<='2010-04-15 23:59:59' AND s.zone_id = 0 GROUP BY advertiser_id,placement_id,pkey]
[Native message: ERROR:  column "s.ad_id" must appear in the GROUP BY clause or be used in an aggregate function]

Fatal error: Unsupported operand types in .../www/admin/market/stats.php on line 164
[/sourcecode]
