#!/bin/env python
"""
The output is kept in generator form rather than being returned as a list since it is likely to be extremely large.

>>> [a for a in try_all(ftp, [1], ["a","b"], [2.75, 3.5, 1.375])]
[(1, 'a', 2.75), (1, 'a', 3.5), (1, 'a', 1.375), (1, 'b', 2.75), (1, 'b', 3.5), (1, 'b', 1.375)]
"""

import itertools
def try_all(f, *possible_inputs):
    inputs = itertools.product(*possible_inputs)
    while True: yield f(*(inputs.next()))

def ftp(a,b,c): return a,b,c

title = "Call a function with all possible inputs"
author = "Kurt"
date = (2010, 12, 5, 13, 03)
