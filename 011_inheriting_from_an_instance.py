pdw_id   = 11
title    = "Inheriting from an instance"
pub_date = (2010, 12, 9, 11, 33)
author   = "Kurt"
tags     = ("inheritance",)

"""
In Python you can inherit from any object, be it a class object or an instance.

Our familiar volunteers from the audience, ``A`` and ``B``:
"""
arg_holder = None
class A(object):
    def __init__(*args):
        global arg_holder
        arg_holder = args

class B(A()): pass
"""
Notice how ``B`` inherits from an *instance* of ``A``.

>>> A   # doctest:+ELLIPSIS
<class '...A'>

And it's already been called once, when the ``B`` class was defined. Let's look
at the arguments passed to ``__init__``:

>>> arg_holder   # doctest:+ELLIPSIS
(<...A object at ...>, 'B', (<...A object at ...>,), {'__module__': '...'})

``B`` is now a weird ``A`` object thing.

>>> B   # doctest:+ELLIPSIS
<...A object at ...>

And if you try to instantiate it, well, there's a reason you don't want to do this:

>>> B()   # doctest:+ELLIPSIS
Traceback (most recent call last):
 ...
TypeError: 'A' object is not callable
>>> dir(B)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> B.__dict__
{}

You could make ``A`` callable and have it return a type and so forth, and in a feat
of duck-typing everything would work great. The only case I've seen of instantiating
and inheriting in one go like this is with ``namedtuple``, found in the ``collections``
module. It's a type factory, and it's great for many reasons not to be tarnished by
the sort of silliness in this post.
"""

