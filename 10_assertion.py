# -*- coding: utf-8 -*-

"""
assertEqual      - czy 2 elementy sa = 
assertNotEqual   - czy 2 elementy <>
assertTrue       - czy prawda 
AssertFalse      - czy fałsz
assertIn         - czy należy 
assertNotIn      - czy nie należy 
"""

import unittest


class Simpletest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(3 + 7, 10)
        
    def test_sub(self):
        self.assertNotEqual(8 - 3, 7)

    def test_true(self):
        self.assertTrue(8 - 3 == 5)
        
    def test_false(self):
        self.assertFalse(8 - 3 == 8)
    
    def test_in(self):
        self.assertIn(3, [1, 2, 3, 4])
        
    def test_not_in(self):
        self.assertNotIn(20, range(15))
        
if __name__ == '__main__':
    unittest.main()
          