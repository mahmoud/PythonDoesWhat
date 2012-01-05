"""
While not a good idea in general, it is possible to modify lists while iterating over them. Note that this only works for lists since they have a defined ordering, and so the iterator doesn't "lose its place" if the list is modified.  For sets and dicts, this type of construct will result in "RuntimeError: changed size during iteration."

>>> iter_change()
1 [1, 2] [0]
2 [1, 2, 0] [1, 1]
0 [1, 2, 0, 1, 1] []
1 [1, 2, 0, 1, 1] [0]
1 [1, 2, 0, 1, 1, 0] [0]
0 [1, 2, 0, 1, 1, 0, 0] []
0 [1, 2, 0, 1, 1, 0, 0] []
"""

def iter_change():
    a = [1,2]
    for n in a:
        print n, a, [n-1]*n
        a += [n-1]*n

title = "Extend list while iterating"
date = (2010, 12, 13, 15, 25)
author = "Kurt"
tags = ('list','iteration')
