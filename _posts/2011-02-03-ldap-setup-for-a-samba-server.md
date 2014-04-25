---
layout: post
title: LDAP Setup for a SAMBA-Server
categories: []
tags:
- sysadmin
status: draft
type: post
published: false
meta: {}
author: 
---
<p>ahhh....the wonderful world of CIFS (Samba and Windows).</p>
<p>Until recently we had an old legacy Samba server providing CIFS shares to our users. We decided it was time to provide real service to our users with good shares(TM). After some requirement thinking we came up with a list of what we need to do.<!--more--></p>
<p>I'll adapt the requirements mentioned here to what I think is better than what we can currently do (like LDAPv3 only and other minor stuff but the overall requirements are still the same.</p>
<p>Also this is only about the (re)design of the LDAP tree so that we are in a useable state, and hopefully have some good stuff in it that will ease up working with it in the future.</p>
<h2>LDAP with V3 and TLS only</h2>
<h2>rfc2307bis</h2>
<p>Makes objectClass: posixGroup an auxilliary objectClass. Let's us use objectClass: groupOfNames as a grouping mechanism.</p>
<h2>Lock down via ACL</h2>
<ul>
<li>Do not let anonymous users access the directory</li>
<li>allow access to password attributes by anonymous auth</li>
<li>allow access to password attributes by self write, by operator write, by * none</li>
</ul>
<h2>LDAP Auth via PAM</h2>
<ul>
<li>libnss-ldap</li>
<li>libpam-ldap</li>
</ul>
<h2>Nested Groups via PAM</h2>
<ul>
<li>for free with rfc2307bis</li>
</ul>
<h2>LDAP Overlays</h2>
<h3>dynlist</h3>
<ul>
<li>activate the overlay for dynamic Groups</li>
<li>configure the overlay to (optionally) remap roleOccupant to member when retrieving roleMembers/Occupants</li>
</ul>
<h3>unique</h3>
<ul>
<li>uidNumber in ou=People</li>
<li>uid in ou=People</li>
<li>cn in ou=People</li>
<li>sambaSID in ou=People</li>
<li>gidNumber in ou=Groups</li>
<li>cn in ou=Groups</li>
</ul>
<h3>memberOf Attribute Overlay</h3>
<ul>
<li>convienence to quickly see the memberships of an object directly at the object
<ul>
<li>fix the issue with recursive memberOf attributes not working</li>
</ul>
</li>
</ul>
<h2>Using Roles instead of Groups</h2>
<ul>
<li>objectClass: organizationalRole</li>
<li>fix the libnss-ldap issue that somehow pop's up when using this</li>
</ul>
<p>Needs some special config in the dynlist overlay</p>
