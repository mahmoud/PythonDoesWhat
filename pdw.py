#!/bin/env python

"""
Just a little __main__ script to run PDW's posts (using doctest).
"""
if __name__ == "__main__":
    import pkgutil
    import os
    import doctest

    pdw_path =  os.path.split(os.path.abspath(__file__))[0]
    pdws = pkgutil.walk_packages([pdw_path]) 
    
    for pdw, name, ispkg in pdws:
        mod = pdw.find_module(name).load_module(name)
        print name, doctest.testmod(mod, report=True)

