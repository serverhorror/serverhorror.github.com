---
layout: post
title: Python and "Interfaces" (Abstract Base Classes)
categories: []
tags: []
status: publish
type: post
published: true
meta:
  _wp_old_slug: ''
  _wpas_done_fb: '1'
  _wpas_done_twitter: '1'
  _wpas_skip_yup: '1'
author: 
---
<p>{% highlight text %}
import sys
import os</p>
<p>from abc import ABCMeta
from abc import abstractmethod</p>
<p>class MetaClass:
    __metaclass__ = ABCMeta</p>
<p>    @abstractmethod
    def needs_implementation(self):
        pass</p>
<p>class ImplementationClassOK(MetaClass):
    def random_method(self):
        pass
    def needs_implementation(self):
        pass</p>
<p>class ImplementationClassFail(MetaClass):
    def random_method(self):
        pass</p>
<p>if __name__ == u'__main__':</p>
<p>    print u'Type OK: ', type(ImplementationClassOK)
    ok = ImplementationClassOK()
    print u'Type Instance OK: ', type(ok)
    print ok</p>
<p>    print type(ImplementationClassFail)</p>
<p>    try:
        print u'Type FAIL: ', type(ImplementationClassFail)
        fail = ImplementationClassFail()
        print u'Type Instance FAIL: ', type(fail)
        print fail
    except (TypeError, ) as error:
        print error
        raise
{% endhighlight %}</p>
