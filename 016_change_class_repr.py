pdw_id   = 16
title    = "Change class (not instance) __repr__ with metaclass"
pub_date = (2010, 12, 27, 10, 52)
author   = "Kurt"
tags     = ("metaclasses", "repr")

"""
First let's understand what a normal *class* repr looks like:
>>> object          # doctest:+ELLIPSIS
<type 'object'>

Versus the much more common default instance repr:
>>> A()             # doctest:+ELLIPSIS
<....A object at 0x...>

If you want to change the instance's repr, you usually just ``def __repr__(self)`` in your class definition. If you want to change the class's repr, you need to do something different:
"""

class PrintMeta(type):
    def __repr__(cls):
        return "Hello, world!"

class A(object):
    __metaclass__ = PrintMeta

"""
Here's the custom repr in action:
>>> A
Hello, world!

"""


