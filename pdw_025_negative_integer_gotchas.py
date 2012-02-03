pdw_id   = 25
title    = "Negative Integer Gotchas (mod and div)"
pub_date = (2011, 3, 17, 10, 33)
author   = "Kurt"
tags     = ("math", "types", "int")

"""
Quick! What's ``-5/100``? Or ``-5/100``?

If you said -5 and 0, you'd be right... if this was C or Java.

>>> print -5%100, -5/100
95 -1

Some more fun with negative modulos:

>>> 3%-1
0
>>> 3%-2
-1
>>> 3%-3
0
>>> 3%-4
-1
>>> 3%-5
-2
>>> 3%-6
-3
>>> 3%-7
-4

So why does Python have a different behavior than C, Java, Fortran et al?

`Why, the decree of the Benevolent Dictator For Life, of course!`__

__ http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
"""
