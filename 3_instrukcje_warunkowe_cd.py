# -*- coding: utf-8 -*-

# dane z input daja stringa dlatego w if ''

print('Program uruchiomiony...')

print("""Włam się do systemu, zgadując dwucyfrowy kod pin.
Numer pin składa się z cyfr 0,1,2. """)
pin = input('Wprowadź numer pin: ')

if pin == '21':
    print('Brawo. Złamałes system!')
elif pin =='20':
    print('Byłes blisko')
else:
    print('Nie zgadłes') 

# aby input byl czytany jak cyfry dodajemy int i podajemy w if bez ''

pin = int(input('Wprowadź numer pin: '))

if pin == 21:
    print('Brawo. Złamałes system!')
elif pin ==20:
    print('Byłes blisko')
else:
    print('Nie zgadłes') 
# %%

# if true , else - False , spacja to też True 

string = ''
if string:
    print('Niepusty ciag znakow')
else:
    print('Pusty ciag znakow')
    
# %%
number = ''
if number:
    print('Liczba niezerowa')
else:
    print('zero') 
    
# %%

default_flag = True

if not default_flag:
    print('Nie doszlo do defaultu')
else:
    print('Doszlo do defaultu')

# %%
#### zadanie 1 #####
v = 55 
if v > 50 :
    print('Zwolnij')
else:
    print('Tak trzymaj!')
    
    
# %%
# koniunkcja (and = oba warunki musza być spełnione)
saldo = 1222
klient_zweryfikowany = False 

if saldo > 0 and klient_zweryfikowany:
    print('Możesz wypłacić gotowkę')
else:
    print('Nie możesz wypłacić')
    
# %%

saldo = 1000
klient_zweryfikowany = True
amount = int(input('Ile chcesz wyplacic: '))

if saldo > 0 and klient_zweryfikowany and (saldo - amount) >= 0 :
    print('Możesz wypłacić gotowkę')
else:
    print('Nie możesz wypłacić')
    
# %%
# abs - absolute - wartosć bezwzgledna
saldo = 1000
klient_zweryfikowany = True
amount = int(input('Ile chcesz wyplacic: '))

if saldo > 0 and klient_zweryfikowany and (saldo - amount) >= 0 :
    print('Możesz wypłacić gotowkę')
else:
    print('Nie możesz wypłacić. '
          'Brak wystarczajacej kwoty {} '.format(abs(saldo - amount)))

# %%
##### zadanie 2 #####

# stworz liste wszystkich znaków => unikalny zbiór = > czy długosć jest >20 
# wydrukuj instrukcje 

fakt = 'python jest łatwy i przyjemny'
x = list(fakt)
y = len(set(x))

if y > 20:
    print('Liczba unikalnych znaków jest większa lub równa 20.')
else:
    print('Mniej niż 20 unikalnych znakow.')
    
    
# %% 

'a' in 'python'
'p' in 'python'

# %%
name = 'python'
if 'p' in name:
    print('Znaleziono')
else:
    print('Brak')
    
# %%
tech = 'python'
if tech == 'python':
    flag = 'ok'
else:
    flag = 'niedobrze'
    
# %%
# x if [warunek] else y

tech = 'python'
flag = 'ok'if tech =='python' else 'niedobrze'
    
# %%
tech = 'sas'
'ok'if tech =='python' else 'niedobrze'

# %%
### zadanie 3 ###

text = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'
if 'q' in text:
    print('Zawiera')
else:
    print('Nie zawiera')









    
    