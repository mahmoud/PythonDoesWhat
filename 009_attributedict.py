pdw_id   = 9
title    = "Attributedict: dictionary whose keys are also attributes"
author   = "Kurt"
pub_date = (2010, 12, 7, 16, 29)
tags     = ('dict','attributes')

"""
No doubt Javascripters out there will find this construct pretty familiar.
"""
class attributedict(dict):
    def __init__(self, *a, **kw):
        self.__dict__ = self
        dict.__init__(self, *a, **kw)

"""
attributedict is a dictionary whose keys are also accessible as object attributes. 
This incredibly simple recipe is probably one of my favorites. For most intents 
and purposes, it supplants the whole `bunch Python package <http://pypi.python.org/pypi/bunch>`_ 
in four lines.

Let's see it in action:

>>> ad = attributedict()
>>> ad["one"] = 1
>>> ad.one
1
>>> ad.two = 2
>>> ad["two"]
2
>>> attributedict(three=3).three
3

*Update*: we found `a similar recipe on ActiveState code`__. From 2005!

.. _ActiveStateRecipe: http://code.activestate.com/recipes/361668/
__ ActiveStateRecipe
"""
