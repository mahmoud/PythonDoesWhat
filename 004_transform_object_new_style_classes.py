#!/bin/env python
"""
>>> a = A()
>>> type(a)   # doctest:+ELLIPSIS
<class '....A'>
>>> import json
>>> transform(a, json.JSONDecoder)
>>> type(a)
<class 'json.decoder.JSONDecoder'>
>>> a.decode('{"foo":1}')
{u'foo': 1}
"""

import json

def transform(obj, cls, *a, **kw):
    obj.__dict__.clear()
    obj.__class__ = cls
    cls.__init__(obj, *a, **kw)

class A(object): pass

title = "Transform object into different (new-style) class."
author = "Kurt"
date = (2010, 12, 4, 23, 15)
