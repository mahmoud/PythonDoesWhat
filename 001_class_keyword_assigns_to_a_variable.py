#!/bin/env python
"""
A thing.

>>> g = 1
>>> def f():
...    global g
...    class g(): pass
>>> g
1
>>> f()
>>> g
<class ...

The class keyword in python is exactly equivalent to a call to the type function, even down to how it interacts with the global keyword.
"""

title = "Class keyword assigns to a variable"
date = (2010, 12, 3, 13, 5)
author = "Kurt"
