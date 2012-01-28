pdw_id   = 13
title    = "finally block can override enclosed return statement"
author   = "Kurt"
pub_date = (2010, 12, 10, 12, 45)
tags     = ("finally", "exceptions", "call order")

"""
Always remember kids, when Python says finally, it means finally.
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

"""
>>> print_then_return()
finally
'returns'
>>> override_return()
'finally'
"""


