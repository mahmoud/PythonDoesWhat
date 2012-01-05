"""
MH:

It's possible for a module to remove itself from sys.modules. If you're thinking about doing this, you might want to look into Import Hooks instead.

This is hard to test in this format, so I'll just leave this here:

# >>> import self_destruct
# >>> reload(self_destruct)
# <module 'self_destruct' from 'self_destruct.pyc'>
# >>> self_destruct.self_destruct()
# removing self from sys.modules: 'self_destruct'
# >>> reload(self_destruct)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: reload(): module self_destruct not in sys.modules

"""

def self_destruct():
    import sys
    for k,m in sys.modules.items():
        if getattr(m, "__file__", None) is __file__:
            print "removing self from sys.modules:", repr(k)
            del sys.modules[k]

title = "Self-destructing module"
date = (2010, 12, 8, 17, 10)
author = "Kurt"
tags = ('modules', 'import')
