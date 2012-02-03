pdw_id   = 12
title    = "How built-in ``staticmethod`` (could be) implemented"
pub_date = (2010, 12, 9, 11, 51)
author   = "Kurt"
tags     = ('objects', 'static', 'descriptor protocol')

"""
The ``staticmethod()`` function, most commonly used as a decorator, takes a 
method defined in a class and allows it to be called in an unbound fashion.

Rest assured, the built-in ``staticmethod`` is implemented in C and is the 
superior choice for actual use, but sometimes it's fun to think of pure-Python 
ways to simulate the behavior:
"""

class static(object):
    def __init__(self, f): self.f = f
    def __get__(self, obj, type=None): return self.f

class C(object):
    @static
    def foo():  # look, Ma, no 'self' or 'cls'
        print "Yes, it works."

"""
Does it work?

>>> C.foo()
Yes, it works.

"""




