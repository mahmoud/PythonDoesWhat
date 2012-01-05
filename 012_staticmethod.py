"""
MH:

The built-in staticmethod() function, most commonly used as a decorator, takes a method defined in a class and allows it to be called in an unbound fashion.

This is an example of a pure-Python way you can simulate the behavior. Rest assured staticmethod is implemented in C and is the superior choice for actual use.

>>> C.foo()
Hello, world!
"""

class static(object):
    def __init__(self, f): self.f = f
    def __get__(self, obj, type=None): return self.f

class C(object):
    @static
    def foo():  # look, Ma, no 'self' or 'cls'
        print "Hello, world!"

title = "How built-in staticmethod (could be) implemented"
date = (2010, 12, 9, 11, 51)
author = "Kurt"
tags = ('objects', 'static', 'descriptor protocol')
