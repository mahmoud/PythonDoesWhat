pdw_id   = 7
title    = "Reverse a list with slicing"
author   = "Kurt"
pub_date = (2010, 12, 5, 13, 14)
tags     = ('list', 'slice', 'iterables')

"""
Savvy readers[*]_ may be familiar with this syntax for copying a list:
>>> [1,2,3][:]
[1, 2, 3]

The funny little bracket-colon-bracket is an empty 
`slice <http://docs.python.org/glossary.html#term-slice>`_ operator. The even-savvier 
know that you can pass it a third parameter, which acts as a 'step', which we can use
to reverse a list:

>>> [1,2,3][::-1]
[3, 2, 1]

You've probably correctly guessed that this actually copies *and* reverses the list, as
opposed to ``list.reverse()``, which works in place. For those seeking more clarity, you
will probably enjoy the ``reversed()`` built-in, which does almost the same thing as the 
second example, but returns an iterator/generator, making it somewhat more efficient.

.. [*] This is a trick statement; all readers of PDW are obviously savvy beyond their
   years.
"""


