pdw_id   = 26
title    = "Every string is an iterable of strings"
author   = "Kurt"
pub_date = (2011, 3, 31, 10, 49)
tags     = ('string', 'iterables')

"""
In case you hadn't noticed, strings aren't your average iterable.

>>> 'a'[0][0][0][0][0]
'a'

Good news is, Python doesn't actually create a bunch of string 
objects when you do this.

>>> a = 'a'
>>> id(a) == id(a[0][0][0][0])
True

Phew! Dodged a bullet there.
"""
