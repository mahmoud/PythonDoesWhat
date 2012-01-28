#!/bin/env python
"""
attributedict is a dictionary whose keys are also accessible as object attributes. No doubt Javascripters out there will find it pretty familiar.

MH: This incredibly simple recipe is probably one of my favorites. For most intents and purposes, it supplants the whole `bunch Python package <http://pypi.python.org/pypi/bunch>`_ in four lines.

>>> ad = attributedict()
>>> ad["one"] = 1
>>> ad.one
1
>>> ad.two = 2
>>> ad["two"]
2
>>> attributedict(three=3).three
3

Also, we found `a similar recipe on ActiveState code <http://code.activestate.com/recipes/361668/>`_. From 2005!
"""

class attributedict(dict):
    def __init__(self, *a, **kw):
        self.__dict__ = self
        dict.__init__(self, *a, **kw)

title = "Attributedict: dictionary whose keys are also attributes"
author = "Kurt"
date = (2010, 12, 7, 16, 29)
