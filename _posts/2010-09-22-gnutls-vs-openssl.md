---
layout: post
title: GnuTLS vs. OpenSSL
categories: []
tags: []
status: draft
type: post
published: false
meta: {}
author: 
---
<p>#!/bin/sh
/usr/bin/openssl pkcs12 -in ./xid-scm01.in.inqnet.at.p12 -cacerts -nodes ## extract Trust Chain
/usr/bin/openssl pkcs12 -in ./xid-scm01.in.inqnet.at.p12 -nodes -nocerts ## extract Private Key
/usr/bin/openssl pkcs12 -in ./xid-scm01.in.inqnet.at.p12 -clcerts -nokeys ## extract Cert
/usr/bin/openssl rsa -in xid-scm01.in.iqnet.at.key ## extract Key usable for Daemon
/usr/bin/openssl x509 -in xid-scm01.in.iqnet.at.pem ## extract Cert usable for Daemon
extract key from pkcs12
exctract ca from pkcs12
configure apache for ssl
configure postgresql for ssl (f'up post)
http://technicalhitch.wordpress.com/2008/01/02/why-a-rsa-private-key-can-be-encrypted-with-a-password/
http://kahdev.wordpress.com/2008/06/21/an-intro-to-openssl/
http://sycure.wordpress.com/2008/03/31/psk-tls-and-tls-comparision-when-to-use-what/
http://sycure.wordpress.com/2008/05/15/tips-using-openssl-to-extract-private-key-pem-file-from-pfx-personal-information-exchange/</p>
