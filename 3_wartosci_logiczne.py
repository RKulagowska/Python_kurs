# -*- coding: utf-8 -*-

val_1 = True 
val_2 = False

# %% 
print(val_1)
print(type(val_1))

# %% 
# koniunkcja True and False  == > False 
# alternatywa True or False == > True 
# negacja zwraca wartosc przeciwna  True ==> True , not True == > False 
# not False == > True 

# %% 
# bool pokarze prawdę jesli zawiera min 1 litere tekst, jesli pusty False 
# cyfra 0 = False, reszta true, flow 0.0 = False ale '0.0' = True, 
# pusty slownik, zbior, lista lub tupla zwraca False  

bool('python')
bool(0.1)
bool({})
bool(set())
bool(list())
bool(tuple())

bool({'key':'val'})

#####    zadanie    #####
 
print(bool(' '))
print(bool(''))
print(bool('1'))
print(bool({' ',' '}))