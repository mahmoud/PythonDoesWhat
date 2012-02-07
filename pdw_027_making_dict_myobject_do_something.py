pdw_id   = 27
title    = "Making ``dict(myobject)`` do something useful"
author   = "Kurt"
pub_date = (2011, 4, 20, 11, 25)
tags     = ('dict', 'iterables')

"""
Normally if you pass your run-of-the-mill object to the ``dict()`` 
constructor, you'll see an error. If only there were a sane and
succinct default...
"""

class A(object):
    def __iter__(self):
        return self.__dict__.items().__iter__()

"""
This example class is now iterable and returns an iterator over
its instance members/values.

>>> a = A()
>>> a.knight = "ni"
>>> a.peon   = "newt"
>>> dict(a)
{'knight': 'ni', 'peon': 'newt'}

Note again that this only covers instance-level members and doesn't
include anything from the class or inheritance structure. See PDW 8
for a note on that sort of thing.
"""
