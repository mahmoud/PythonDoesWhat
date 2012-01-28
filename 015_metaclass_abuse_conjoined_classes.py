pdw_id   = 15
title    = "Metaclass Abuse: Conjoined Metaclasses"
pub_date = (2010, 12, 27, 10, 48)
author   = "Kurt"
tags     = ("metaclasses", "inheritance")

__all__ = ['ConjoinedMeta', 'A', 'B']

"""
Metaclasses can be used to create all manner of mutant constructs. With 
great power comes great responsibility, I suppose.

Here we have a very basic use, in which ``A`` and ``B`` are conjoined
at the ``__metaclass__``.
"""

class ConjoinedMeta(type):
    def __new__(cls, name, bases, attrs):
        for k,v in attrs.items():
            setattr(ConjoinedMeta, k, v)
        return ConjoinedMeta

class A(object):
    __metaclass__ = ConjoinedMeta
    a = "a"

class B(object):
    __metaclass__ = ConjoinedMeta

"""
>>> B.a
'a'
>>> B.b = 'b'
>>> A.b
'b'

Note that we're using the classes, and not instances thereof. In fact, these
classes aren't even instantiatable right now. We'll just have to cover that 
at later date.
"""
