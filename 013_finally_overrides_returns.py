"""
Always remember kids, when Python says finally, it means finally.

>>> print_then_return()
finally
'returns'
>>> override_return()
'finally'
"""

def print_then_return():
    try:
        return "returns"
    finally:
        print "finally"

def override_return():
    try:
        return "returns"
    finally:
        return "finally"

title = "finally block can override enclosed return statement"
date = (2010, 12, 10, 12, 45)
author = "Kurt"
tags = ("finally", "exceptions", "call order")
