---
comments: true
date: 2011-06-05 14:07:30
layout: post
slug: basic-ec2-getting-started
title: Basic EC2 Getting Started
wordpress_id: 1302
tags:
- Amazon
- Amazon EC2
- Amazon Elastic Compute Cloud
- Amazon Web Services
- Application programming interface
- Public-key cryptography
- Secure Shell
- SSH
---




# Basic EC2 Getting Started





	
  1. Set up the amazon [EC2 API tools](http://aws.amazon.com/developertools/351)

	
  2. Create an X.509 Keypair from the Amazon website

	
  3. Set up the environment accordingly







    
    # required environment for EC2 tools EC2_HOME EC2_PRIVATE_KEY EC2_CERT JAVA_HOME # add ec2 tools to default path!








	
  4. Create an SSH keypair

Logins on EC2 only allow public key authentication — and that is a good thing!







    
    # only one time (per host that is authorized for this image) ec2-add-keypair my-keypair cat < ~/.ec2/id_rsa-my-keypair > -----BEGIN RSA PRIVATE KEY----- >... > -----END RSA PRIVATE KEY----- > EOF chmod 0600 ~/.ec2/id_rsa-my-keypair








	
  5. Find an instance to run







    
    ec2-describe-images -a








	
  6. Run an instance

Instances of type `m1.small` must be 32-bit images!







    
    ec2-run-instances -k my-keypair  -t m1.small








	
  7. Find out what’s running on EC2







    
    ec2-describe-instances








	
  8. Grant access to the instances







    
    # only one time -- allows SSH access from anywhere for all instances ec2-authorize default -p 22








	
  9. Shut everything down again

Keeps the bill low :)







    
    ec2-terminate-instances












* * *



I'm switching blogs. Just look at [http://serverhorror.eu](http://serverhorror.eu) during the time of transition.

**Original Post at: [http://serverhorror.eu/basic-ec2-getting-started](http://serverhorror.eu/basic-ec2-getting-started)**


