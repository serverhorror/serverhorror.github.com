---
layout: post
title: PostgreSQL Migrating from Single Server to DRBD-HA Setup
date: 2014-05-05 12:01
tags: postgres, postgresql, ha, drbd, migration
author: Martin Marcher
---
# Overal Plan

1. *Single PostgreSQL Server* without redundancy
1. *Single PostgreSQL Server* (now a master) without redundancy **plus**
 1. DRBD Server with only one side
 1. DRBD PostgreSQL Slave with only one side (*DRBD-A Side*)
1. Configure VIP on *Single PostgreSQL Server* (now a master)
1. Wait for synchronization and Test Slave
1. Kill master and wait for failover to finish
1. Set up the old master be the *DRBD-B Side*
1. Wait for DRBD synchronization to finish
1. Fail over between *DRBD-A* and *DRBD-B* side
