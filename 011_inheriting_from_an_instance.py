"""
In Python you can inherit from any object, be it a class object or an instance.

>>> class A(object):
...    def __init__(*args): print args
>>> class B(A()): pass   # doctest:+ELLIPSIS
(<...A object at ...>,)
(<...A object at ...>, 'B', (<...A object at ...>,), {'__module__': '...'})
>>> B   # doctest:+ELLIPSIS
<...A object at ...>
>>> B()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'A' object is not callable
>>> dir(B)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> B.__dict__
{}

"""

title  = "Inheriting from an instance"
date   = (2010, 12, 9, 11, 33)
author = "Kurt"
tags   = ("inheritance",)
