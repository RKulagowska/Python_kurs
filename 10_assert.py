# -*- coding: utf-8 -*-

assert 1 == 1 

# %% 

assert 1 == 2

# %% 

def test_sum():
    assert sum([1,2,3]) == 6
test_sum()

# %% 

def test_sum():
    assert sum([1,2,3]) == 6, "Powinno być 6"

def test_min():
    assert min([1,2,3]) ==1, 'Powinno być 1'
    
if __name__ == '__main__':
    test_min()
    test_sum()
    print ('ok')