pdw_id   = 1
title    = "Class keyword assigns to a variable"
pub_date = (2010, 12, 3, 13, 5)
author   = "Kurt"
tags     = ('class', 'assignment')

"""
The ``class`` keyword in Python is exactly equivalent to a call to the ``type()``
function, even down to how it interacts with the ``global`` keyword.

>>> g = 1
>>> def f():
...    global g
...    class g(): pass
>>> g
1
>>> f()
>>> g
<class ...

"""


