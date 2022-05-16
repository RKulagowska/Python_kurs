# -*- coding: utf-8 -*-
# nazwa z dużej litery. Kazdy kolejny wyraz z dużej litery też
# obiekty z małej liter 
# w consoli drzewo_1

class Drzewo:
    nazwa = 'Sosna'
    wiek = 40
    wysokosc = 25
    
drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

# %% 

# zwraca nr Id obiektu 

print(id(drzewo_1))
print(id(drzewo_2))

# %% 
# atrybuty to nazwa . dostajemy się tam za pomoca .
dir(drzewo_1)

drzewo_1.nazwa
drzewo_1.wiek
drzewo_1.wysokosc

# %% 
# atrybuty klasy 
# atrybuty instancji można podawać przy okacji jak poniżej 
# instancja klasy = obiekt 

drzewo_1.stan = 'dobry'


# %%

Drzewo.miejsce = 'las'

# %% 
print(dir(drzewo_1))
print(dir(drzewo_2))


# %% 
# zmiana atrybutu 

drzewo_2.miejsce = 'park'
print(drzewo_2.miejsce)


# %% 
# pass nic nie robi ?przeskakuje :)
# f oznacza że będzie formatowany 
# self 

class Drzewo:
    def info_drzewo(self):
        self.nazwa = 'Sosna'
        self.wiek = 40
        print(f'Drzewo {self.nazwa} ma {self.wiek} lat.')
    
drzewo = Drzewo()
drzewo.info_drzewo()

# %%
# równoważny zapis 

drzewo.info_drzewo()

# %%
# równoważny zapis 

Drzewo.info_drzewo(drzewo)