"""
>>> foo(1,(2,3))
1 2 3
>>> foo(1,())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in foo
ValueError: need more than 0 values to unpack
"""

def foo(a, (b,c)):
    print a,b,c

"""
This feature has probably really confused you if you ever mistakenly put parenthesis around the parameters to a lambda.  In that case the lambda expression will take only one argument, and that argument will be a tuple.

>>> a = lambda (a,b): a+b
>>> a(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes exactly 1 argument (2 given)
>>> a((1,2))
3
"""

title  = "Sequence unpacking in argument list"
date   = (2010, 12, 28, 11, 29)
author = "Kurt"
tags   = ("tuples", "unpacking", "functions")
