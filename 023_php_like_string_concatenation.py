"""
Everyone's favorite PHP feature: dot-based string concatenation!

>>> a = PHPstr("foo")
>>> a.bar
'foobar'
"""

class PHPstr(str):
    def __getattr__(self, attr):
        return PHPstr(self+attr)

title  = "PHP-like string concatenation (almost)"
date   = (2011, 2, 28, 14, 38)
author = "Kurt"
tags   = ("string", "getattr")
