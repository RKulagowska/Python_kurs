# -*- coding: utf-8 -*-

# słowniki {} zmienna typu dict, struktura nieuporządkowana, 
# zawiera pary:klucz i wartosć, klucze nie mogą się powtarzać 
# wydobywanie danych za pomocą klucza 
# dict = {'key1': 'value1', key2': 'value2'}


empty_dict = dict()
print(empty_dict)

d = {}

e = set()

# %%

pol_to_eng = {'jeden':'one', 'dwa':'two', 'trzy':'three'}

name_to_digit = {'jeden':1, 'dwa':2, 'trzy':3}

len(name_to_digit)

# %% 
# dodawanie do do słownika
pol_to_eng['cztery'] = 'four'

# %% 
# clear wyczysci cały słownik

pol_to_eng.clear()

# %%
# wydobywanie kluczy ze słownika 

pol_to_eng.keys()

# wydobywanie klucz z przekonwertowaniem na liste 
list(pol_to_eng.keys())

# %% 
# wydobywnaie wartosci z przkonwertowaniem na liste 

list(pol_to_eng.values())

# %% 
# i klucze i wartosci z przekonwertowaniem na liste 
list(pol_to_eng.items())

# %% 
# wyciągniecie wartosci dla konkretnego klucza 

pol_to_eng['jeden']

# wyd wartosc po kluczu. Na 2 miejscu podajemy co chcemy otrzymać gdy wartosci
# brak. Nie generuje się bład

pol_to_eng.get('zero', 'N/A')

# %% 
# pop - musimy podać wartoć klucza dla zestawu który chcemy usunąc 
pol_to_eng.pop('dwa')

# dowalna do skasowania 
pol_to_eng.popitem()

# %% 
# dodawanie pary 
pol_to_eng.update({'dwa':2})


 #### zadanie    ####
 
new = {1:1, 2:4, 3:9, 4:16, 5:25}
print(new)

#### zadanie 2 ######

# do podanego słownika dodaj Włochy:Rzym, utwórz listę stolic posotowaną od A do Z 

capitals = {'Polska': 'Warszawa', 'Niemcy': 'Berlin', 'Czechy': 'Praga'}
capitals['Włochy'] = 'Rzym'
x = sorted(list(capitals.values()))
print(x)

 
 
 
