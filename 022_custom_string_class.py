"""
Here is how to make a sublcass of a string that has the same operations, but which return instances of that subclass.

>>> MyStr('cat')
MyStr'cat'
>>> MyStr('cat')+'dog'
MyStr'catdog'
>>> MyStr('cat')[1:]
MyStr'at'

If you're doing this, it's probably a bad code smell. 
"""

import inspect
import functools

class MyStr(str):
    def __radd__(self, other):
        return MyStr(str.__add__(other, self))
    def __repr__(self):
        return self.__class__.__name__ + str.__repr__(self)

def _mystr_wrap(f):
    @functools.wraps(f, ('__name__', '__doc__'))
    def g(*a, **kw):
        res = f(*a, **kw)
        if res.__class__ == str:
            return MyStr(res)
        return res
    return g

for name, f in inspect.getmembers(str, callable):
    # skip some special cases
    if name not in ('__class__', '__new__', '__str__', '__init__', '__repr__'):
        setattr(MyStr, name, _mystr_wrap(f))

title  = "Custom string class"
date   = (2011, 1, 21, 10, 03)
author = "Kurt"
tags   = ("inheritance", "inspect", "functools", "classes")
