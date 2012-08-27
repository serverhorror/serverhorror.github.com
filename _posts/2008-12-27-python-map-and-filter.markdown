---
comments: true
date: 2008-12-27 01:30:00
layout: post
slug: python-map-and-filter
title: Python, map and filter.
wordpress_id: 240
---

Just another note to myself for some useful python stuff:

    
    Python 2.4.4 (#2, Oct 22 2008, 20:20:22)
    [GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> def multby3(elem):
    ...     return elem * 3
    ...
    >>> map(multby3, (1, 2, 3, ))
    [3, 6, 9]
    >>> def even(elem):
    ...     return not elem % 2
    ...
    >>> filter(even, (1, 2, 3, ))
    (2,)
    >>> map(multby3, filter(even, (1, 2, 3, )))
    [6]
    >>>
