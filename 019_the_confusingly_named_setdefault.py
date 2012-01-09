"""
dict.setdefault(key[, default]) returns the key's value if the key is in the dict.
If it's not, it inserts the default and returns that value. An equivalent function is described below.

>>> d = {}
>>> setdefault_py(d, "a", "b")
'b'
>>> d.setdefault(1, 2)
2
>>> setdefault_py(d, "a", "c")
'b'
>>> d.setdefault(1, 3)
2
>>> d
{'a': 'b', 1: 2}

This function is useful in similar cases to a collections.defaultdict.  The difference being, with this function you can choose what you want the default to be each time you fetch a key from the dictionary.  With a defaultdict, the default value for a missing key must be set at construction time.
"""
def setdefault_py(my_dict, key, default):
    my_dict[key] = my_dict.get(key, default)
    return my_dict[key]

title  = "The confusingly named setdefault"
date   = (2010, 12, 28, 11, 42)
author = "Kurt"
tags   = ("dict", "setdefault", "collections", "defaultdict")
