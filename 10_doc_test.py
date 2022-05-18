# -*- coding: utf-8 -*-

# sprawdzanie dokumentacji 

def add(x,y):
    """
    Zwraca sumę 2 liczb
    
    >>> add(3,4)
    6
    
     """
    return x + y
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()


# testowanie z pliku 

def add(x,y):
    """
    Zwraca sumę 2 liczb
    
    >>> add(3,4)
    6
    
     """
    return x + y
 
if __name__ == '__main__':
    import doctest
    doctest.testfile('10_test.txt')