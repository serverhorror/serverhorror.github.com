---
comments: true
date: 2010-08-18 08:09:06
layout: post
slug: python-and-interfaces-abstract-base-classes
title: Python and "Interfaces" (Abstract Base Classes)
wordpress_id: 799
---

{% highlight python %}
import sys
import os

from abc import ABCMeta
from abc import abstractmethod

class MetaClass:
    __metaclass__ = ABCMeta

    @abstractmethod
    def needs_implementation(self):
        pass

class ImplementationClassOK(MetaClass):
    def random_method(self):
        pass
    def needs_implementation(self):
        pass

class ImplementationClassFail(MetaClass):
    def random_method(self):
        pass

if __name__ == u'__main__':

    print u'Type OK: ', type(ImplementationClassOK)
    ok = ImplementationClassOK()
    print u'Type Instance OK: ', type(ok)
    print ok

    print type(ImplementationClassFail)

    try:
        print u'Type FAIL: ', type(ImplementationClassFail)
        fail = ImplementationClassFail()
        print u'Type Instance FAIL: ', type(fail)
        print fail
    except (TypeError, ) as error:
        print error
        raise
{% endhighlight %}
