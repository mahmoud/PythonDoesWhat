pdw_id   = 18
title    = "Using finally to do something after return"
pub_date = (2010, 12, 28, 11, 33)
author   = "Kurt"
tags     = ("finally",)

"""
Very similar to PDW 13, but here it is anyway.
"""
def foo():
    try:
        print "returning"
        return
    finally:
        print "after return"
"""
>>> foo()
returning
after return
"""
