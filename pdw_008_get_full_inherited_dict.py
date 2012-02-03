pdw_id   = 8
title    = "Get full inherited __dict__"
author   = "Kurt"
pub_date = (2010, 12, 6, 10, 57)
tags     = ('dict', 'inheritance')

"""
``__dict__`` (or ``vars()``) is great, but sometimes you want to get more 
than just a given instance's members. For instance, in:
"""
class A(object):
    testA = "A"
    testB = "A"
    testb = "A"

class B(A):
    testB = "B"
    testb = "B"

"""
it might be nice to get dictionary access to the ``testA`` class member. 
Here's a function that could do that:
"""

def get_full_dict(obj):
    parent_dicts = [obj.__dict__] + \
        [cls.__dict__ for cls in obj.__class__.__mro__ if cls.__name__ != "object"]
    return reduce(lambda a,b: dict(b.items() + a.items()), parent_dicts, {})

"""
Let's test it out:

>>> b = B()
>>> b.testb = "b"
>>> b_dict = get_full_dict(b)
>>> b_dict["testA"]
'A'
>>> b_dict["testB"]
'B'
>>> b_dict["testb"]
'b'

For real use, you probably want to use the ``inspect`` module's ``getmembers()`` function.
"""
