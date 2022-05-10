# -*- coding: utf-8 -*-

# funkcja_1()- uruchamia funkcje a nie print

def funkcja_1():
    print('pierwsza funcja uruchomiona')
    
funkcja_1()
    
# %%
def funk_2(x, y):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funk_2(2,10)

# %%
# odwraca kolejnosc printowania 

def funk_2(x, y):
    print('Podane argumenty to: {1}, {0}'.format(x, y))
    
funk_2(2,10)

# %% 
# mozna jedna przypisac na stałe

def funk_2(x, y=10):
    print('Podane argumenty to: {1}, {0}'.format(x, y))
    
funk_2(2)

# %% 
# mozna przypisac na stałe, ale jesli na koncu przypiszemy inna ona priorytetowa

def funk_2(x, y=10):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funk_2(2, 8)

funk_2(2)

# %% 
# jesli brak argumentu błąd-unk_2() missing 1 required positional argument: 'x'

def funk_2(x, y=10):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funk_2()

# %% 
# na koncu wazniejsze i te beda wyswietlane 

def funk_2(x = 3, y=10):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funk_2(y=3, x=5)

# %% 
# import bibliotek

import math

math.sqrt(9)
math.exp(1)
math.sin(0)

# %%
def fun_3():
    print('Uruchomiono')
fun_3()
print(type(fun_3))

# %%
# tworzenie funkcji - zwraca sume

def add(x, y):
    return x + y
add(2, 6)

# x= add(2,6)

# %%
def subtract(x: int, y: int):
    """
    odejmuje od siebie 2 liczby.
    """
    return x - y
subtract(10, 6)


# %%
# """ zachowuje ukłąd tekstu jak przekazano pomiedzy """
def print_menu():
    print('Start ...')
    print('#'* 30)
    print("""Wybierz jedna z opcji:
          0 - logowanie 
          1 - wyjscie""")
    print('#'* 30)
    print('Koniec programu.')
print_menu()

# %%
#### zadanie 1  ####
def policz_srednia(x, y, z):
        return (x+y+z)/3
print(policz_srednia(10,30,50))


# %% 
# wyprintuje liczby parzyste 
# + 1 spowoduje że oststnia będzie właczona 

def print_even(maximum):
    for i in range(maximum + 1):
        if i % 2 == 0 :
            print(i)
print_even(10)
            

# %% 
# funkcja zapisujaca text do pliku 

def write_f(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file = file)
write_f('sample3.txt', '1 linia.\n2 linia.')
        

# %% 
# zysk na lokacie przy danej stopie % i liczbie okresów 

def cal_pr(pv,rate,n):
    return pv * (1+rate)**n-pv
cal_pr(1000, 0.02, 3)

# %% 
# zysk na lokacie przy danej stopie % i liczbie okresów 
# jesli zmieniamy dane w ostatniej linijce przy wywołaniu to one są aktualne 

def cal_pr(pv = 1000, rate= 0.02, n= 3):
    return pv * (1+rate)**n-pv
cal_pr(rate = 0.05)


# %%
### zadanie 2 ####

# drukuj nieparzyste od 0 do 20 

def nieparzyste(x):
    for i in range(x + 1):
        if i % 2 == 1:
            print(i)
nieparzyste(20)
            
### rozwiazanie instrukrora 
def drukuj_nieparzyste():
    wynik = []
    for i in range(20):
        if i % 2 != 0:
            wynik.append(i)
    return wynik


