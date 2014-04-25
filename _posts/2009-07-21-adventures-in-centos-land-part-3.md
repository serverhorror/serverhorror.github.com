---
layout: post
title: Adventures in CentOS-Land (Part 3)
categories: []
tags:
- sysadmin
status: publish
type: post
published: true
meta:
  delicious: a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1259053358";}
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1259053358";}
  _wpas_skip_twitter: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_yup: '1'
author: 
---
<p>Let's get to work with CentOS5 now that we have set up the yum repositories and are able to install all the software we need. As a short reminder our requirements listing again. So let's <a href="http://serverhorror.wordpress.com/2009/07/20/adventures-in-centos-land-part-2/">continue from last time...</a></p>
<p>Our requirements are the following:</p>
<ul>
<li>nagios for monitoring of
<ul>
<li>disk space</li>
<li>system load</li>
<li>service availability</li>
<li>...</li>
</ul>
</li>
<li>openLDAP (v3 only and TLS only)</li>
<li>SMTP with Sender Authentication over TLS only</li>
<li>IMAPs (only, and only over TLS)</li>
<li>a webmail interface for easy access from anywhere - also TLS only</li>
</ul>
<p>Since I know <a href="http://www.postfix.org/">Postfix</a> best I decided to go with it, also <a href="http://www.dovecot.org/">Dovecot</a> is a nice (and fast) IMAP server (as I learned on the way). User Information for the mail users should come from <a href="http://www.openldap.org">LDAP</a> - that also makes it easy to set up some password changing webform (did I mention: TLS only).</p>
<p>But first the basic setup. This is where the problems started:</p>
<ul>
<li>no nagios in the official repositories - rpmforge has them
<ul>
<li>it seems Dag Wieers is an official package maintainer taking part in this repo so it seems trustworthy according to some Google research</li>
</ul>
</li>
<li>postfix seems to be in the CentOsPlus repository</li>
</ul>
<p>Let's see, yum is the package manager and seems to work quite well, no sign of RPM-dependency hell any more.</p>
<p>O.K. - so much for a basic running service. Of course that doesn't do that much that is useful for us. Let's first configure slapd and a basic LDAP tree. The config of slapd is rather simple, we don't really have any users except one so we don't exactly need any groups. Why bother with LDAP then? Well, once you get used to having LDAP and a nice GUI tool is actually a lot <del>easier</del> more convenient to deal with than with the good unix passwords. <strong>Note: I recommend to NEVER EVER put system users required to start daemons/applications in LDAP, don't even think about it!</strong></p>
<p>Now here comes the slapd.conf:

{% highlight text %}
# egrep -v '^ *#|^$' /etc/openldap/slapd.conf
include        /etc/openldap/schema/core.schema
include        /etc/openldap/schema/cosine.schema
include        /etc/openldap/schema/inetorgperson.schema
include        /etc/openldap/schema/nis.schema
include        /etc/openldap/schema/misc.schema
pidfile        /var/run/openldap/slapd.pid
argsfile    /var/run/openldap/slapd.args
TLSCACertificateFile /etc/pki/tls/certs/ca-bundle.crt
TLSCertificateFile /etc/pki/tls/certs/slapd.pem
TLSCertificateKeyFile /etc/pki/tls/certs/slapd.pem
access to dn.base=&quot;&quot; by * read
access to dn.base=&quot;cn=Subschema&quot; by * read
access to *
 by self write
 by users read
 by anonymous auth
database    bdb
suffix &quot;dc=example,dc=org&quot;
rootdn &quot;cn=System Maintenance Account,ou=System,dc=example,dc=org&quot;
rootpw changeme
directory    /var/lib/ldap
index objectClass                       eq,pres
index ou,cn,mail,surname,givenname      eq,pres,sub
index uidNumber,gidNumber,loginShell    eq,pres
index uid,memberUid                     eq,pres,sub
index nisMapName,nisMapEntry            eq,pres,sub
{% endhighlight text %}

And this is our LDIF (already with the user we want to use for mailing):

{% highlight text %}
dn: dc=example,dc=org
objectClass: dcObject
objectClass: top
objectClass: organization
dc: dc=example,dc=org
o: Example Corp.

dn: ou=People,dc=example,dc=org
objectClass: organizationalUnit
objectClass: top
ou: People

dn: cn=Alice  Squarepants,ou=People,dc=example,dc=org
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: person
objectClass: top
objectClass: inetLocalMailRecipient
cn: Alice  Squarepants
mail: asquarepants@example.org
mailLocalAddress: alice@example.org
sn: Doe
userPassword: changeme

dn: ou=System,dc=example,dc=org
objectClass: organizationalUnit
objectClass: top
ou: System

dn: cn=System Maintenance Account,ou=System,dc=example,dc=org
objectClass: organizationalRole
objectClass: top
objectClass: simpleSecurityObject
cn: System Maintenance Account
userPassword: changeme

dn: cn=postfix,ou=System,dc=example,dc=org
objectClass: organizationalRole
objectClass: top
objectClass: simpleSecurityObject
cn: postfix
userPassword: changeme

dn: cn=dovecot,ou=System,dc=example,dc=org
objectClass: organizationalRole
objectClass: top
objectClass: simpleSecurityObject
cn: dovecot
userPassword: changeme

dn: cn=Bob,ou=People,dc=example,dc=org
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: person
objectClass: top
objectClass: inetLocalMailRecipient
cn: Bob  Squarepants
mail: bob@example.org
sn: Bob Squarepants
userPassword: changeme

dn: cn=Postmaster,ou=People,dc=example,dc=org
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: person
objectClass: top
objectClass: inetLocalMailRecipient
cn: Postmaster
mail: postmaster@example.org
mailLocalAddress: hostmaster@example.org
mailLocalAddress: abuse@example.org
sn: Postmaster
userPassword: changeme
{% endhighlight text %}

Let's see now what we have.</p>
<ul>
<li>Non-System users ready to use in LDAP - <span style="color:#ff0000;">check</span></li>
<li>Aliases that can be used easily - <span style="color:#ff0000;">check</span></li>
<li>a container for "real people" vs. a container for "role objects" - <span style="color:#ff0000;">check</span></li>
<li><span style="color:#ff0000;"><span style="color:#000000;">Hopefully no typos since I made some modifications like changing the passwors (of course) the Root DSE and some DNs</span></span></li>
</ul>
<p>Next time we'll see how to configure Dovecot to use this information and automagically create the correct mailbox with the information provided from our LDAP tree.</p>
