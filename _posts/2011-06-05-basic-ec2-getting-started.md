---
layout: post
title: Basic EC2 Getting Started
categories: []
tags:
- Amazon
- Amazon EC2
- Amazon Elastic Compute Cloud
- Amazon Web Services
- Application programming interface
- Public-key cryptography
- Secure Shell
- SSH
status: publish
type: post
published: true
meta:
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1322875045";}
  _wpas_skip_linkedin: '1'
  _wpas_skip_fb: '1'
  _wpas_skip_twitter: '1'
  _oembed_c683b4c1886b152a38ab17a3e0933b83: '{{unknown}}'
  _oembed_2d34632b5fd616586afc8564f97790d7: '{{unknown}}'
  _oembed_16aaf341365d8a75cc988c16825bd9dc: '{{unknown}}'
  _oembed_70f6d28765567b02b9b55d9ea09b96a2: '{{unknown}}'
author: 
---
<div class="posterous_autopost">
<h1>Basic EC2 Getting Started</h1>
<ol>
<li>Set up the amazon <a href="http://aws.amazon.com/developertools/351">EC2 API tools</a></li>
<li>Create an X.509 Keypair from the Amazon website</li>
<li>Set up the environment accordingly
<div class="CodeRay">
<div class="code">
<pre># required environment for EC2 tools EC2_HOME EC2_PRIVATE_KEY EC2_CERT JAVA_HOME # add ec2 tools to default path!</pre>
</div>
</div>
</li>
<li>Create an SSH keypair
<p>Logins on EC2 only allow public key authentication — and that is a good thing!</p>
<div class="CodeRay">
<div class="code">
<pre># only one time (per host that is authorized for this image) ec2-add-keypair my-keypair cat < ~/.ec2/id_rsa-my-keypair &gt; -----BEGIN RSA PRIVATE KEY----- &gt;... &gt; -----END RSA PRIVATE KEY----- &gt; EOF chmod 0600 ~/.ec2/id_rsa-my-keypair</pre>
</div>
</div>
</li>
<li>Find an instance to run
<div class="CodeRay">
<div class="code">
<pre>ec2-describe-images -a</pre>
</div>
</div>
</li>
<li>Run an instance
<p>Instances of type <code>m1.small</code> must be 32-bit images!</p>
<div class="CodeRay">
<div class="code">
<pre>ec2-run-instances -k my-keypair  -t m1.small</pre>
</div>
</div>
</li>
<li>Find out what’s running on EC2
<div class="CodeRay">
<div class="code">
<pre>ec2-describe-instances</pre>
</div>
</div>
</li>
<li>Grant access to the instances
<div class="CodeRay">
<div class="code">
<pre># only one time -- allows SSH access from anywhere for all instances ec2-authorize default -p 22</pre>
</div>
</div>
</li>
<li>Shut everything down again
<p>Keeps the bill low :)</p>
<div class="CodeRay">
<div class="code">
<pre>ec2-terminate-instances</pre>
</div>
</div>
</li>
</ol>
<hr />
<p>I'm switching blogs. Just look at <a href="http://serverhorror.eu">http://serverhorror.eu</a> during the time of transition.</p>
<p><strong>Original Post at: <a href="http://serverhorror.eu/basic-ec2-getting-started">http://serverhorror.eu/basic-ec2-getting-started</a></strong></p>
</div>
