pdw_id   = 23
title    = "PHP-like string concatenation (almost)"
pub_date = (2011, 2, 28, 14, 38)
author   = "Kurt"
tags     = ("string", "getattr", "cross-language")

"""
Now Pythonauts can enjoy everyone's favorite PHP feature: dot-based 
string concatenation!
"""

class PHPstr(str):
    def __getattr__(self, attr):
        return PHPstr(self+attr)

"""
>>> a = PHPstr("foo")
>>> a.bar
'foobar'

*Mahmoud sez*: "I'm gonna murder myself if anyone uses this."
"""


