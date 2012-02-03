pdw_id   = 5
title    = "``zip(*a)`` is its own inverse"
author   = "Kurt"
pub_date = (2010, 12, 5, 12, 14)
tags     = ('zip', 'iterables')

"""
Like a regular zipper, ``zip()`` goes one way about as easily as the other.

>>> zip( *[(1, 2, 3), ('a', 'b', 'c')] )
[(1, 'a'), (2, 'b'), (3, 'c')]

>>> zip( *[(1, 'a'), (2, 'b'), (3, 'c')] )
[(1, 2, 3), ('a', 'b', 'c')]

Just don't try to do it as fast as Python. You might hurt yourself.
"""


