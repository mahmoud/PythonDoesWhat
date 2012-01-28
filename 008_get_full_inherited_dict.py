#/bin/env python
"""
NOTE: You probably want to use the inspect module's getmembers() function.

>>> b = B()
>>> b.testb = "b"
>>> b_dict = get_full_dict(b)
>>> b_dict["testA"]
'A'
>>> b_dict["testB"]
'B'
>>> b_dict["testb"]
'b'
"""

class A(object):
    testA = "A"
    testB = "A"
    testb = "A"

class B(A):
    testB = "B"
    testb = "B"

"""
this is just a comment test. remove me in a second
"""

def get_full_dict(obj):
    parent_dicts = [obj.__dict__] + [cls.__dict__ for cls in obj.__class__.__mro__ if cls.__name__ != "object"]
    return reduce(lambda a,b: dict(b.items() + a.items()), parent_dicts, {})

"""
another comment test.


hehehhe
"""

title = "Get full inherited __dict__"
author = "Kurt"
date = (2010, 12, 6, 10, 57)
