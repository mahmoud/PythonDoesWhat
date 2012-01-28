pdw_id   = 24
title    = 'Local variable performance and dis'
pub_date = (2011, 3, 14, 12, 13)
author   = 'Kurt'
tags     = ('local variables', 'performance', 'dis')

"""
Local variables are significantly faster in Python. They are accessed as offsets from a stack, rather than looked up in a hashmap/dict.

Using the dis module, we can investigate this sort of backend behavior. There are 8 distinct variable load routines that are used by the Python interpreter:

>>> import dis
>>> sorted(x for x in dis.opname if 'LOAD' in x)
['LOAD_ATTR', 'LOAD_CLOSURE', 'LOAD_CONST', 'LOAD_DEREF', 'LOAD_FAST', 'LOAD_GLOBAL', 'LOAD_LOCALS', 'LOAD_NAME']
"""

# dis setup
a = 1
def global_var():
    return a

def nonlocal_var():
    b = 2
    def ret():
        return b
    return ret

def local_var():
    c = 3
    return c

def argument(v):
    return v

"""
We'll get around to all of them someday, but for now we'll focus on LOAD_FAST, LOAD_DEREF, and LOAD_GLOBAL. LOAD_FAST is used to load variables in the local scope and function arguments (because they're just local variables). LOAD_DEREF is used to load variables in the enclosing scope. LOAD_GLOBAL is used for, you guessed it, globals (module-level scope).

>>> dis.dis(global_var)     # doctest:+SKIP
2           0 LOAD_GLOBAL              0 (a)
            3 RETURN_VALUE        

>>> dis.dis(nonlocal_var()) # doctest:+SKIP
7           0 LOAD_DEREF               0 (b)
            3 RETURN_VALUE        

>>> dis.dis(local_var)      # doctest:+SKIP
11          0 LOAD_CONST               1 (3)
            3 STORE_FAST               0 (c)
<BLANKLINE>
12          6 LOAD_FAST                0 (c)
            9 RETURN_VALUE        

>>> dis.dis(argument)       # doctest:+SKIP
12          6 LOAD_FAST                0 (v)
            9 RETURN_VALUE        

Here is an example showing the use of local variables as a performance optimization:
   http://wiki.python.org/moin/PythonSpeed/PerformanceTips#Local_Variables
"""


