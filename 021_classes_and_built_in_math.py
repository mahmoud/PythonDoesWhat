pdw_id   = 21
title    = 'Making your class work with built-in math functions'
pub_date = (2011, 1, 5, 12, 20)
author   = 'Kurt'
tags     = ('math',)

"""
You can make your class work with built-in math module's functions simply by 
adding __float__ and/or __int__. Then, built-in math functions or anything 
that sanitizes its input via int() or float(), will see your objects as a 
numeric type.
"""
class B(object):
    def __float__(self):
        return 0.5
"""
>>> import math
>>> round(math.sin(B()), 6) # different platformas have different precisions
0.479426

If you want your class to work with arithmetic operators (like +, -, etc.), 
you should look into further operator overloading (e.g., implementing 
``__add__()``/``__iadd__()``).
"""



