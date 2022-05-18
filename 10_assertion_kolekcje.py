# -*- coding: utf-8 -*-

"""
assertListEqual    - czy 2 liczby są = 
assertTupleEqual   - czy 2 tuple są =
assertSetEqual     - czy 2 zbiory są = 
assertDictEqual    - czy 2 słowniki są = 
"""

import unittest


class SimpleTest(unittest.TestCase):
    
    def test_1(self):
        self.assertListEqual([1,2,3],[1,2,3])

    def test_1(self):
        self.assertTupleEqual((1,2),(1,2))
        
    def test_1(self):
        self.assertSetEqual({2,3},{2,3})
        
    def test_1(self):
        self.assertDictEqual({'a':2,'b':3},{'a':2,'b':3})
        
if __name__ == '__main__':
    unittest.main()