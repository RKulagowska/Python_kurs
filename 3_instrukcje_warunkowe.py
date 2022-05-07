# -*- coding: utf-8 -*-

version = 3.7
print(version)

# %% 
version > 3 
version <= 3 

# %% 
# znak porównania == - sprawdzanie równosci 2 wartosci 
# znak róznosci != - sprawdzanie czy rózne 2 wartosci 
number = 1200 
number > 1000
number == 1200

number != 1200

# %% 
# Pamiętaj o tab ! 
# if [warunek]:
#     [instrukcja]

# %% 

if 8 < 10:
    print('tak')
    
# %%
a = 5
if a > 10:
    print('a > 10')
else:
    print('a <= 10')
    
# %% 
age = 17
if age < 18:
    print('Nie masz uprawnien')
else:
    print('Dostęp przyznany')

# %%
age = 15
if age == 18:
    print('Masz 18 lat')
elif age < 18:
    print('Nie masz uprawnien')
else:
    print('Dostęp przyznany')
    
# %%
age = 15
if age == 18:
    print('Masz 18 lat')
elif age < 18:
    print('Nie masz uprawnien')
elif age > 18:
    print('Dostęp przyznany')  
    
# %%
# age = input('Podaj swoj wiek: ')
# analizuje warunki na podstawie input. Input daje stringa 
# TypeError: '<' not supported between instances of 'str' and 'int'
# dlatego dodajemy int 

age = int(input('Podaj swoj wiek: '))
if age == 18:
    print('Masz 18 lat')
elif age < 18:
    print('Nie masz uprawnien')
elif age > 18:
    print('Dostęp przyznany')  
    
# %%    
##### zadanie ######

x = 10 
if x > 0:
    print('Zmienna x wieksza od zera')
    