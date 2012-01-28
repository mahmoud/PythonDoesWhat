"""
You can make your class work with built-in math module's functions simply by adding __float__ and/or __int__.
Then, built-in math functions or anything that sanitizes its input via int() or float(), will see your objects as a numeric type.

>>> import math
>>> round(math.sin(B()), 6) # different platformas have different precisions
0.479426

If you want your class to work with arithmetic operators (like +, -, etc.), look into operator overloading (e.g., implementing __add__()/__iadd__()).
"""

class B(object):
    def __float__(self):
        return 0.5

title  = 'Making your class work with built-in math functions'
date   = (2011, 1, 5, 12, 20)
author = 'Kurt'
tags   = ('math',)
