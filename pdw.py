#!/bin/env python

"""
Just a little __main__ script to run PDW's posts (using doctest).
"""
def main():
    import pkgutil
    import os
    import doctest

    pdw_path =  os.path.split(os.path.abspath(__file__))[0]
    pdws = pkgutil.walk_packages([pdw_path]) 

    results = {}
    
    for pdw, name, ispkg in pdws:
        if name == 'pdw':
            continue  # this is a script, not a post
        mod = pdw.find_module(name).load_module(name) # test that it loads ok
        filename = mod.__file__.rstrip('c') # all those pesky .pyc files
        src = open(filename).read()
        doctests = get_doctests(src)

        dtr = run_doctests(mod, doctests)
        results[name] = dtr.summarize()

    print len(results),'modules processed,',
    print sum(x.attempted for x in results.values()), 'tests run,',
    print sum(x.failed for x in results.values()), 'tests failed.'

def get_doctests(string):
    import ast
    from ast import Expr, Str, Assign
    from doctest import DocTestParser,Example

    ret = []
    dtp = DocTestParser()

    m_ast = ast.parse(string)
    for node in m_ast.body:
        if isinstance(node, Expr) and isinstance(node.value, Str):
            for s in dtp.parse(node.value.s):
                if isinstance(s, Example):
                    ret.append(s)

    return ret
        
def run_doctests(module, examples):
    from doctest import DocTest, DocTestRunner, ELLIPSIS

    dt = DocTest(examples, module.__dict__, module.__file__, None, None, None)
    dtr = DocTestRunner(optionflags=ELLIPSIS)
    
    dtr.run(dt, clear_globs=False)

    return dtr

if __name__ == "__main__":
    main()
