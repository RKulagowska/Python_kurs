# -*- coding: utf-8 -*-

"""
tworzenie testu jednostkowego 
1. zaimportowanie unittest
2. zdefiniowanie funkcji do testowania 
3. stworzenie przypadku testowego używając klasy inittest.TestCase
4. zdefiniowanie testu jako metody klasy TestCase
    metoda musi zaczynać się od słowa test
5. call assert function
6. assert function wywoła błąd assertionError jeżeli otrzymany błąd
7. wywołaj funkcje main() z modułu unittest                    
"""

import unittest

def add(x,y):
    return x + y


class SimpleTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(3,4), 6, msg='powinno być 7')
        
if __name__ == '__main__':
    unittest.main()
