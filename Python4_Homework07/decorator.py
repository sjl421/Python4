#!/bin/env python
# -*- coding: utf-8 -*-

import unittest

def addarg(arg):
    "Takes an argument and adds that argument as the first argument to all calls to decorated functions"
    def decorator(f):
        def wrapper(*args, **kw):
            new_args = (arg, ) + args
            return f(*new_args, **kw)
        return wrapper
    return decorator
    
if __name__ == '__main__':
    @addarg(1)
    def prargs(*args):
        return args
             
    class TestDecorator(unittest.TestCase):
        
        def test_prargs(self):
            self.assertTrue(prargs(2, 3), "(1, 2, 3")
            self.assertTrue(prargs("child"), "(1, 'child')")

    unittest.main()
