# -*- coding: utf-8 -*-

# komentarz 
# %%

print(2 + 2)

# %%
print(3 * 3)

print(3 + 2 * 2)

# %%
10 / 3

#%%
10 // 3

# %%
2 ** 5

# %%

10 % 3

#$$

( 10 - 2 ** 3 ) * 10

#%%

a = 10
b = 20

c = a * b
print(c)

# %%
'love python'
"love python"

# %%
"It's the best"
'It\'s the best'

# %%
print('Python\n3.7')
print("""Python
3.7""")

# %%
print('\tPython')

# %%
print('c:\path\to\something\new')
print('c:\path\\to\something\\new')
print('c:\\path\\to\\something\\new')
print(r'c:\path\to\something\new')

# %%
import os
os.getcwd()

# %%
print("""
Instrukcja uruchamiania pliku przyklad.py:
    
    -- file [nazwa pliku]
        zapisuje output do pliku 
        
    -- quiet
        wycisza logi w konsoli 
        
koniec.""")

# %% 
text = ' I love Python. '
print(text)
print (text * 3)
print('* ' * 10 )

# %%

'Python'
'Py'  'thon'
print('Py'    'thon')

# %%

url = 'https://www.google.pl/maps/place/Narwik,+01-471+Warszawa/@52.2420203,20.8939667,17z/data=!3m1!4b1!4m5!3m4!1s0x471ecaef64a49c77:0x8120444a2b2255c7!8m2!3d52.2420203!4d20.8961554 '

url2= ('https://www.google.pl/maps/place/Narwik,+01-471+Warszawa/'
      '@52.2420203,20.8939667,17z/data=!3m1!4b1!4m5!3m4!1s0x471ecaef64a49c77:'
      '0x8120444a2b2255c7!8m2!3d52.2420203!4d20.8961554 ')

# %% 
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')


# łączenie liczby z tekstem . Musimy przekonwertować liczbę na tekst -'
#    'TypeError: can only concatenate str (not "int") to str
    
# indeksowanie zaczyna się od 0 

# %%
age = 27 
imie = 'Paweł'
print( imie + ' ' +str(age) )
print(imie,age)
print('{} ma {} lat.'.format(imie,age))
print('{0} ma {1} lat.'.format(imie,age))

# %%
saldo = 40 
   # saldo = saldo = 30 
saldo += 30
saldo -= 10
print(saldo)

# %% 
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata  * czynnik_akumulacyjny
print('Wartosc lokaty po roku: ', lokata_po_roku)

# standaryzowanie wartosci (podzielic przez max wartoć jaką może przyjąć )
# %%
pixel = 150 
 #pixel = pixel / 255
pixel /= 255
print(pixel)

# %% 
base = 2
base **= 5
print(base)

# modulo - reszta 
# %%
x = 103
 # x = x % 10
x %= 10
print(x)

# %%
imie = 'Renata '
nazwisko = 'Kułagowska'
  #nazwa = imie + nazwisko
imie += nazwisko

# %%
name = 'Python '
version = '3.7'
name += version
print(name) 

# zadanie 1

kwota_poczatkowa = 1000
stopa_procentowa = 0.05
okres_trwania = 2 
fv = kwota_poczatkowa * (1 + stopa_procentowa) ** okres_trwania
print(fv)




 











