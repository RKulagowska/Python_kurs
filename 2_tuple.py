# -*- coding: utf-8 -*-

# tuple struktura którą nie można zmieniać , uporządkowane

empty_tuple= tuple()
print(empty_tuple)

# %%
# mozemy definiować za pomocą ()

amazon = ('amazon', 'USA', 'Technology', '1')
google = ('Google', 'USA', 'Technology', '2')


# %%
name_google = google[0]
 # google[0] = 'Google Company'da TypeError: 'tuple' object does not support item assignment
 
# %%
# łączenie 2 tupli
data = (amazon, google)

# %%
a = ('Renata', 'Kułagowska') 

# %%
imie = 'Renata'
nazwisko = ' Kułagowska '

imie, nazwisko, id_user = ('Renata',  'Kułagowska', '001')

# %%
# rozpakowywanie tupli do poszczególnych zmiennych 
amazon_name, country, sector, rank = amazon

# %%
# tuple możemy definiować bez nawiasu okrągłego 

stocks = 'Amazon', 'Apple', 'IBM'

# %%
# tuple zagnieżdzone

nested = 'Europa', 'Polska', ('Warszawa', 'Kraków')

# %% 
# zamienianie wartosci 

a = 12
b = 14

c = b 
b = a 
a = c 
print(a,b)

# %% 
x, y = 10, 15
x, y = y, x 
print(x, y)


#### zadanie   #####

x = 'Python'
y = 3.7

tupla = (x, y)
print(tupla)



