pdw_id   = 2
title    = "Change class inheritance"
pub_date = (2010, 12, 3, 13, 12)
author   = "Kurt"
tags     = ('inheritance',)

"""
The super-classes of a class are available under the __bases__ attribute.  These
 can be modified to dynamically change the class inheritance tree.

A couple of volunteers from the audience, please.
"""

class A(): pass
class B(A): pass

"""
Let's see how this works:

>>> b = B()
>>> isinstance(b, A)
True
>>> B.__bases__
(<class ...
>>> B.__bases__ = ()
>>> isinstance(b, A)
False

Now go write yourself into some royal family tree and live happily ever after.
"""




