# -*- coding: utf-8 -*-

empty_set= set()
print(empty_set)
print(type(empty_set))

# %%
# {} zbiory są nieuporządkowane
# len podaje długoc znbioru 

techs = {'python' , 'java', 'sql'}
print(techs)
print(len(techs))

# %%
# set daje tylko unikalne wartosc: p y t h o n , ale set('aaaleeerrtt')= a l e r t 

set('python')
set('aaaleeerrtt')

# %%
'python'in techs
'go' in techs
'yt' in techs

# %% 
print(dir(set))

# %%
techs.add('sas')
print(techs)

# %%
techs.remove('sql')
print(techs)

# %%
# usuwa po 1 dowolnym elemencie 
techs.pop()

# %%
techs.clear()
print(techs)

# %%
# czy zbior zqawiera się w innym zbiorze 
# nadzbiór zawiera 
# suma zbiorów - union - nie dubluje tych samych 
# intersection - współne
# symetric_difference(b) odejmowanie częci wspólnej

a = {1, 2, 3, 4, 5, 6, 7}
b = {5, 6, 7, 8, 9}
c = {5, 6}

c.issubset(a)
c.issubset({5, 7})
c.issuperset(c)
a.union(b)
a.intersection(b)
a.symmetric_difference(b)
a.copy()



#### zadanie ####
# wszystko małymiliterami,zamienić '-' i ' ' na '', zamiana polskich liter 
# podaj zbior unikalnych znaków a nastepnie ilosc unikalnych znaków 

x = 'Programowanie w języku Python - od A do Z'
x = x.lower()
x = x.replace('-','')
x = x.replace(' ','')
x = x.replace('ę','e')
print(len(set(x)))

#### inne rozwiazanie instruktora 

x = 'Programowanie w języku Python - od A do Z'
x = x.lower().replace('ę', 'e').replace(' ', '').replace('-', '')
 
print(len(set(x)))
