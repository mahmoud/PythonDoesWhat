"""
Very similar to PDW 13, but here it is anyway.

>>> foo()
returning
after return
"""

def foo():
    try:
        print "returning"
        return
    finally:
        print "after return"

title  = "Using finally to do something after return"
date   = (2010, 12, 28, 11, 33)
author = "Kurt"
tags   = ("finally",)
