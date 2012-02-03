pdw_id   = 6
title    = "Call a function with all possible inputs"
author   = "Kurt"
pub_date = (2010, 12, 5, 13, 03)
tags     = ('itertools', 'testing', 'functions')

"""
Want a quick way to increase your code coverage? Try calling a function with all
possible combinatons of several inputs!

``itertools`` makes it easy:
"""

import itertools
def try_all(f, *possible_inputs):
    inputs = itertools.product(*possible_inputs)
    while True: yield f(*(inputs.next()))

"""
The output is kept in generator form rather than being returned as a list since
it could be prohibitively slow and memory-intensive otherwise.

Given an example function, ``ftp()``:
"""

def ftp(a,b,c): return a,b,c

"""
We can try it out:

>>> [a for a in try_all(ftp, [1], ["a","b"], [2.75, 3.5, 1.375])]
[(1, 'a', 2.75), (1, 'a', 3.5), (1, 'a', 1.375), (1, 'b', 2.75), (1, 'b', 3.5), (1, 'b', 1.375)]
"""
