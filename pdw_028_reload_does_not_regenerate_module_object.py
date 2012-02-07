pdw_id   = 28
title    = "reload() does not regenerate existing module objects"
author   = "Kurt"
pub_date = (2011, 5, 5, 12, 34)
tags     = ('module', 'reload')

"""
The |reload|_ function is one of the most legitimately unintuitive built-in
functions in Python. On the surface it fulfills a simple and fundamental
role: reloading a module as though it was being imported for the first time,
presumably because it has changed or needs some state reset.

Unfortunately, doing this in a comprehensive fashion is actually very involved,
and the |reload|_ function understandably doesn't even really try. Here's an 
basic example of how it might violate one's expectations:

>>> import json  # arbitrary example module
>>> oldjson = json
>>> reload(json)
<module 'json' from ...>
>>> json is oldjson
True

As you can see, the ``json`` module is successfully reloaded, but
the original object remains in memory. Furthermore, any attributes
added to that namespace also stick around:

>>> json.a = 'A persistent attribute.'
>>> reload(json)
<module 'json' from ...>
>>> json.a
'A persistent attribute.'

As mentioned before, `cleaning up modules in memory is a tricky
process <http://pyunit.sourceforge.net/notes/reloading.html>`_. If
someone wants to submit a patch, we'd be much obliged for the life
sacrifice. :)

.. |reload| replace:: ``reload()``
.. _reload: http://docs.python.org/library/functions.html#reload
"""
