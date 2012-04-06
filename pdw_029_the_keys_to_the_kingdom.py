pdw_id   = 29
title    = "ctypes: The keys to the kingdom"
author   = "Mahmoud"
pub_date = (2011, 5, 16, 17, 48)
tags     = ('c', 'ctypes', 'ffi')

"""
Like it or not, most of the code in the world is not written in Python. 

It's probably for the best, because one can only imagine how much maintaining 
some mid-90s, Python 1.4 library would suck today. But seriously, there are a
lot of languages and libraries out there, and Python's OK with that.

Take `the ssl module <http://docs.python.org/library/ssl.html>`_.
`OpenSSL <http://www.openssl.org/>`_ is a powerful, open-source standard when it
comes to libraries, but the ``ssl`` module only became a first-class core library
in Python 2.6. And even then, OpenSSL has a lot of power to offer beyond what's
exposed in the module. How do we get at that one obscure function? [#]_

Enter |ctypes|_, Python's convenient and powerful portal to the C FFI_. Given the
prevalence and power of C, ``ctypes`` gives you access to everything from 
scientific libraries to the low-level guts of your OS. In our OpenSSL example, that
might look like this:

>>> import ctypes
>>> libssl = ctypes.cdll.LoadLibrary('libssl.so')
>>> libssl.PEM_read_bio_PrivateKey
<_FuncPtr object at ...>

Now you have `an SSL function <http://www.openssl.org/docs/crypto/pem.html>`_, not
provided by the standard ``ssl`` module, but still ready to be called from Python.

In a simplistic way, Python is to C as C is to assembly, both in concept and
implementation. C lets you embed assembly, and Python gives you an interface to
C. Of course, just as too much assembly in C is probably a bad code smell, for 
involved use cases, you'll probably want to look at Cython_ and Weave_.

.. |ctypes| replace:: ``ctypes``
.. _ctypes: http://docs.python.org/library/ctypes.html

.. _FFI: http://en.wikipedia.org/wiki/Foreign_function_interface
.. _Cython: http://cython.org
.. _Weave: http://www.scipy.org/Weave

.. [#] Historical note: before ``ctypes``, one could wrap the library as a Python 
   module, but this meant building against a specific version of Python, among
   other headaches. That said, the practice still has its place.

"""
