# -*- coding: utf-8 -*-

"""
unittest.skip(reason) - pomija test 
unittest.skipIf(condition,reason)- pomija jesli spełniony warunek 
unittest.skipUnless(condition,reason)- pomija chyba że warunek jest prawdziwy
unittest.expectedFailure()- oznacza test jako oczekiwany błąd, jeżeli test ma 
                            błąd , błąd nie zostanie policzony 
                            
"""

import unittest 


class SimpleTest(unittest.TestCase):
    
    x = 6
    y = 2
    
    @unittest.skip('pomin')
    def test_add(self):
        wynik = self.x + self.y
        self.assertEqual(wynik, 8)
        
    @unittest.skipIf(x < y,'pomin')    
    def test_sub(self):
        wynik = self.x - self.y
        self.assertEqual(wynik, 4)
        
    @unittest.skipUnless(y == 0, 'pomin')
    def test_div(self):
        wynik = self.x / self.y
        self.assertEqual(wynik, 3.0)
        
    @unittest.expectedFailure
    def test_mul(self):
        wynik = self.x * self.y
        self.assertEqual(wynik, 12)


if __name__ == '__main__':
    unittest.main()
