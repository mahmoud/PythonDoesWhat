"""
A normal class repr:
>>> object          # doctest:+ELLIPSIS
<type 'object'>

An instance repr:
>>> A()             # doctest:+ELLIPSIS
<....A object at 0x...>

A custom repr for your class:
>>> A
Hello, world!
"""

class PrintMeta(type):
    def __repr__(cls):
        return "Hello, world!"

class A(object):
    __metaclass__ = PrintMeta

title  = "Change class (not instance) __repr__ with metaclass"
date   = (2010, 12, 27, 10, 52)
author = "Kurt"
tags   = ("metaclasses", "repr")
