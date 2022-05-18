# -*- coding: utf-8 -*-

"""
assertRaises(exception, callable, *args, **kwargs)
    testuje czy błąd zostanie wyrzucony. Test jest zdany czy oczekiwany blad
    zostanie podniesiony, w przeciwnym razie test jest nie zdany
"""

import unittest

def div(a, b):
    return a / b


class RaiseTest(unittest.TestCase):
    
    def test_raise(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)
        
if __name__ == '__main__':
    unittest.main()