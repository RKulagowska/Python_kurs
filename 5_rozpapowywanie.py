# -*- coding: utf-8 -*-

# tylko jeden argument

def test_args(x, *args):
    print('Pierwszy parametr: ', x)
    for arg in args:
        print('Kolejny parametr *args:', arg)
test_args(4)

# %%
# jeden obowiązkowy reszta nie  ( bo *args)

def test_args(x, *args):
    print('Pierwszy parametr: ', x)
    for arg in args:
        print('Kolejny parametr *args:', arg)
test_args(4,3,4,5,6,)

# %% 

def fun_1(x, y, *args):
    print('x =', x)
    print('y =', y )
    print('*args =', args)
fun_1(1, 2)
fun_1(1, 2, 3)
fun_1(1, 2, 3, 4)

# %% 
def suma(x, y):
    return x + y

suma(1,2)

# %% 
# sumuje dow liczbe argumentow 
def sum_dow(*args):
    return sum(args)
sum_dow(1,2,3,4,5)

#### zadanie  #### 
# policz srednią która wyciąga z dowolnej liczby arg 

def aver(*args):
    return sum(args)/ len(args)
print(aver(1,2,3,4,5,6,7,8,9,10))


# %% 
# zwraca nazwy argumentów
def fun_2(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
fun_2(**{'a':1,'b':2})

# %% 
def fun(**kwargs):
    print(kwargs)
fun(a=1,b=2)

# %% 
# args - nienazwanie  zapisane do listy 
# kwargs - nazwane np  a= 1 dopisane do słownika 

def fun_2(*args,**kwargs):
    print(args)
    print(kwargs)
    
fun_2(1, 2, 4, a = 7,b = 10)


# %% 
# suma arg bez nazwy 
# wartoć danych w słowniku 

def fun_2(*args,**kwargs):
    print(sum(args))
    print(kwargs.values())
    
fun_2(1, 2, 4, a = 7,b = 10)

# %% 
#### zadanie ##### 
# napisz funkcję zwracająca liczbę przekazanych 'keyworld arg'

def policz_kwargs(*args,**kwargs):
    return len(kwargs)
policz_kwargs(10, b = 2, c = 3)


  