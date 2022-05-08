# -*- coding: utf-8 -*-
# 

i = 0
while i < 5:
    print(i)
    i = i + 1

# %%
# wywietla z 11 

n = 0 
while True:
    print(n)
    if n > 10:
        break
    n = n + 1

# %%
while True:
    name = input('Podaj imie: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Czessc {}'.format(name))

 
# %%
n = 0
while n < 20:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# %% 
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False

idx = 0 
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1
    
 
# %% 
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 63 

idx = 0 
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania == wartosc:
        flaga = True 
        break
    idx += 1
if flaga:
    print('jest{}'.format(wartosc))
    
# %% 

lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 50

idx = 0 
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania == wartosc:
        flaga = True 
        break
    idx += 1
if not flaga:
   lista_do_przeszukania.append(wartosc)
   
#### zadanie 1   #####E#

numbers = [23, 12, 53, 13, 65, 1, 45]
x = 13
idx = 0 
while idx < len(numbers):
    if numbers[idx] == x :
        flaga = True 
        break
    idx += 1
if flaga:
     print('Znaleziono')
     
     
# %% 
# WARTOSCI STAŁE DRUKOWANYMI PODAJEMY 

KOD_PIN = '0000'

pin = input('Podaj kod pin: ')
while pin != KOD_PIN:
    pin = input('sprobuj jeszcze raz: ')
print('Zalogowany')

# %% 
# PO 3 próbach wyrzuca 

KOD_PIN = '0000'
pin = ''
counter = 0 

while pin != KOD_PIN and counter < 3:
    pin = input('Podaj kod pin: ')
    if pin == KOD_PIN:
        print('zalogowany')
        break
    counter += 1 
else:
    print('Zbyt dużo prób')
