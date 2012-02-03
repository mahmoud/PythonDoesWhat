pdw_id   = 4
title    = "Transform object into different (new-style) class."
author   = "Kurt"
pub_date = (2010, 12, 4, 23, 15)
tags     = ('inheritance',)

"""
Have you ever felt lonely, left-out, and wishing you could be someone else? 
*(looking at you, Ruby guy, reading this post)*

Well, too bad. You're an individual and it's important to stay true to your
roots. If you had been a Python object, though...
"""

def transform(obj, cls, *a, **kw):
    obj.__dict__.clear()
    obj.__class__ = cls
    cls.__init__(obj, *a, **kw)


class A(object): pass

"""
We're gonna give boring ``A`` instance a ``mako``-ver [*]_.

>>> a = A()
>>> type(a)   # doctest:+ELLIPSIS
<class '....A'>

JSON's got a particular utilitarian attractiveness about her:

>>> import json
>>> transform(a, json.JSONDecoder)
>>> type(a)
<class 'json.decoder.JSONDecoder'>
>>> a.decode('{"foo":1}')
{u'foo': 1}

So hawt. Never look back, ``a``.


.. [*] Shoutouts to Mako_, the templating powerhouse behind this very 
   site. Also, apologies for the irrelevant puns. They happun.

.. _Mako: http://www.makotemplates.org/

"""







