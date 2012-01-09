"""
>>> B.a
'a'
>>> B.b = 'b'
>>> A.b
'b'
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

title = "Metaclass Abuse: Conjoined Metaclasses"
date = (2010, 12, 27, 10, 48)
author = "Kurt"
tags = ("metaclasses", "inheritance")
