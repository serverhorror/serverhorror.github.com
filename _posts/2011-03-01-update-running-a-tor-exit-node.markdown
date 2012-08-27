---
comments: true
date: 2011-03-01 12:05:08
layout: post
slug: update-running-a-tor-exit-node
title: 'Update: Running a TOR Exit Node'
wordpress_id: 1187
tags:
- privacy
- Tor
---

As said before: [I run a TOR exit node](http://blog.serverhorror.com/2011/02/28/running-a-tor-exit-node/).

What's nice is that this gives me a box to play (privately) that has quite some traffic. Since I didn't use it before anyway and cancelled the server already - don't worry I intend to run it for the next couple of months so that I'll get a feeling for that - I figured it might be a nice thing to do for other people.

Anyway I started "monitoring" the traffic with vnstat. Here's the first day:

    
    <code># vnstat -i eth0
    Database updated: Tue Mar  1 10:56:31 2011
    
       eth0 since 02/28/11
    
              rx:  191.93 GiB      tx:  205.07 GiB      total:  397.00 GiB
    
       monthly
                         rx      |     tx      |    total    |   avg. rate
         ------------------------+-------------+-------------+---------------
           Feb '11     37.29 GiB |   39.92 GiB |   77.21 GiB |  267.73 kbit/s
           Mar '11    154.64 GiB |  165.15 GiB |  319.79 GiB |   68.10 Mbit/s
         ------------------------+-------------+-------------+---------------
         estimated     10.27 TiB |   10.97 TiB |   21.23 TiB |   daily
                         rx      |     tx      |    total    |   avg. rate
         ------------------------+-------------+-------------+---------------
         yesterday     37.29 GiB |   39.92 GiB |   77.21 GiB |    7.50 Mbit/s
             today    154.64 GiB |  165.15 GiB |  319.79 GiB |   68.10 Mbit/s
         ------------------------+-------------+-------------+---------------
         estimated    339.45 GiB |  362.53 GiB |  701.98 GiB |
    </code>


Times are in UTC and I started on 02/28/11 ~11:30 with the monitoring. That was at a point where virtually no TOR traffic was coming in due to the low uptime of the TOR daemon.

My colocation says I used 30GB of outgoing traffic so that might be in line - with a little bit of fantasy applied :)
