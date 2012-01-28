#!/bin/env python
"""
>>> zip( *[(1, 2, 3), ('a', 'b', 'c')] )
[(1, 'a'), (2, 'b'), (3, 'c')]

>>> zip( *[(1, 'a'), (2, 'b'), (3, 'c')] )
[(1, 2, 3), ('a', 'b', 'c')]
"""

title = "``zip(*a)`` is its own inverse"
author = "Kurt"
date = (2010, 12, 5, 12, 14)
