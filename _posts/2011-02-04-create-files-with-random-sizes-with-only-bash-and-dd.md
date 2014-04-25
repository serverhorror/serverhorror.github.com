---
layout: post
title: Create files with random sizes with only bash and dd
categories: []
tags:
- bash
- linux
- Randomness
- Shell
- sysadmin
- Unix
- useless math
status: publish
type: post
published: true
meta:
  _wpas_done_yup: '1'
  reddit: a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1319574128";}
  _wpas_mess: 'Create files with random sizes with only bash and dd: http://wp.me/pxxjT-hK'
  _wpas_done_twitter: '1'
  _wpas_done_fb: '1'
author: 
---
<h2>The Rules</h2>
<p>So you need a bunch of files of random size. Say something between 1 MiB and 10 MiB. And you need 3 of them. <code>bash</code> to the rescue.</p>
<ul>
<li>The variable <code>$RANDOM</code> will return an integer between 0 a nd 32,767.</li>
<li><code>$((...))</code> will do arithmetic expansion for the expression contained within</li>
<li>The <code>%</code>-operator will do a modulo operation</li>
</ul>
<p>Let me use those 3 simple rules to create</p>
<ol>
<li>3 files between 1 MiB and 10 MiB</li>
<li>3 files between 15 MiB and 25 MiB</li>
</ol>
<p><strong>As a side note: I will be creating sparse files here. Look up <code>dd(1)</code> for the details. Your use case might be different anyway.</strong></p>
<h2>1 MiB -- 10 MiB files</h2>
<p>[sourcecode language="bash"]$(( ($RANDOM % 10) + 1))[/sourcecode]</p>
<h2>15 MiB -- 25 MiB files</h2>
<p>[sourcecode language="bash"]$(( ($RANDOM % 10) + 15))[/sourcecode]</p>
<h2>General Solution</h2>
<p>[sourcecode language="bash"]<br />
MINSIZE=&lt;number&gt;<br />
MAXSIZE=&lt;number&gt;<br />
$(( ($RANDOM % ($MAXSIZE-$MINSIZE)) + $MINSIZE))<br />
[/sourcecode]</p>
<p>[sourcecode language="bash"]<br />
MINSIZE=30<br />
MAXSIZE=60<br />
for i in {1..3}<br />
do<br />
    dd if=/dev/zero of=testdata.01-15.${i}.data bs=1m count=0 seek=$(( ($RANDOM % 10) + 1))<br />
    dd if=/dev/zero of=testdata.15-25.${i}.data bs=1m count=0 seek=$(( ($RANDOM % 10) + 15))<br />
    dd if=/dev/zero of=testdata.${MINSIZE}-${MAXSIZE}.${i}.data bs=1m count=0 seek=$(( ($RANDOM % ($MAXSIZE-$MINSIZE)) + $MINSIZE))</p>
<p>done 2&gt;/dev/null \<br />
&amp;&amp; echo 'SUCCESS: Creating data files' \<br />
|| echo 'FAILURE: Creating data files'<br />
[/sourcecode]</p>
<p>The result looks quite good.</p>
<p>[sourcecode lang="bash"]<br />
du -sm testdata.*<br />
10	testdata.01-15.1.data<br />
5	testdata.01-15.2.data<br />
3	testdata.01-15.3.data<br />
17	testdata.15-25.1.data<br />
21	testdata.15-25.2.data<br />
20	testdata.15-25.3.data<br />
31	testdata.30-60.1.data<br />
38	testdata.30-60.2.data<br />
55	testdata.30-60.3.data<br />
[/sourcecode]</p>
<p>Yes I know this is minor math at best. But still I tend to forget that problems like this are easily solveable, so I'll not it down here. And yes, there's probably a bunch of cases where bash isn't what you want to use. I needed lots of files to test mdadm behaviour so that I can use them as disks and create RAID arrays.</p>
