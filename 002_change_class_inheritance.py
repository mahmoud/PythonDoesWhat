#!/bin/env python
"""
>>> b = B()
>>> isinstance(b, A)
True
>>> B.__bases__
(<class ...
>>> B.__bases__ = ()
>>> isinstance(b, A)
False

The super-classes of a class are available under the __bases__ attribute.  These can be modified to dynamically change the class inheritance tree.
"""

class A(): pass
class B(A): pass

title = "Change class inheritance"
date = (2010, 12, 3, 1, 12)
author = "Kurt"
