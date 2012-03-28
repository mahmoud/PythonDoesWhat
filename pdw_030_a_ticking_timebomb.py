pdw_id   = 30
title    = "A Ticking TimeBomb"
author   = "Kurt"
pub_date = (2012, 3, 28, 16, 13)
tags     = ('dict', 'iterables')

"""
Generally speaking, you can only raise exceptions when your code is
being called.  Wouldn't it be nice if instead you could leave a
time bomb that would go off later?
"""

class TimeBomb(object):
    def __del__(self):
        raise Exeption("BOOM!")

"""

>>> t = TimeBomb()
>>> #...
>>> t = 3
Exception Exception: Exception('BOMOM!',) in <bound method TimeBomb.__del__ of <
__main__.TimeBomb object at 0x0122E090>> ignored

"""
