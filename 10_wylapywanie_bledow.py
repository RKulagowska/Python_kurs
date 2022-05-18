# -*- coding: utf-8 -*-

# %%
# ZeroDivisionError: division by zero

1/0

# %% 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

4 + '4'

# %%
# ValueError: invalid literal for int() with base 10: 'f'

int('f')


# %%
# ValueError: could not convert string to float: 'sd'

float('sd')

# %% 
# kontrola błedów 
try:
    1 / 0
except:
    print('nie dzieli się przez 0')
    
# %% 
# jesłi ne wiemy jaki bład może się pojawić 

try:
    1 / 0
except ZeroDivisionError:
    print('Nie dzieli się przez 0.')
except TypeError:
    print('Zły kod.')
    
# %% 

try:
    4 + '4'
except:
    print('Nie można dodawać tekstu do liczby.')
    
# %% 

try:
    4 + '4'
except TypeError:
    print('Nie można dodawać tekstu do liczby.')
    
# %% 
try:
    int('s')
except ValueError:
    print('Zły tekst.')
    
    
# %%
# jesli podamy liczbę zamiast cyfry to pokarze bład 

while True:
    x = int(input('Podaj liczbę: '))
    break

    

# %%
# poprawienie kodu 

while True:
    try:
        x = int(input('Podaj liczbę: '))
        break
    except ValueError:
        print('To nie cyfra')
        
# %%
# otwieranie pliku który nie istnieje - 
# FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'

with open('text.txt', 'r') as file:
    for line in file :
        print(line)
    
# %%
# otwieranie pliku który nie istnieje - 
# poprawienie kodu 
try:
    with open('text.txt', 'r') as file:
        for line in file :
            print(line)
except FileNotFoundError:
    print('Plik nie istnieje.')
    
    
# %%
# dodawanie podnzenia błędów 

raise TypeError('Błąd')

# %%
raise ValueError('Błąd wartosci')

# %%
def divine(x,y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('Dzielenie przez zero')
    except ValueError:
        print('Musisz wprowa')
        
divine(3,0)
divine('1','2')
divine('a','b')
