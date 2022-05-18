# -*- coding: utf-8 -*-

def add(x,y):
    """
    Zwraca sumę 2 liczb
    
    >>> add(3,4)
    6
    
     """
    return x + y
 
if __name__ == '__main__':
    import doctest
    doctest.testfile('test.txt')