# -*- coding: utf-8 -*-

stocks = {'AMZN.US':'AMAZON.COM', 'MSFT.US':'MISCROSOFT', \
          'UBER.US':'UBER TECHNOLOGIES'}

# %% 
# 8 to osiem miejsc dla pierwszego elementu

stocks.keys()
stocks.values()
stocks.items()

for key, value in stocks.items():
    print('{:8}: {}'.format(key,value))

# %% 
# (key,value) - nawias żeby tupla ( typ x to dict)
x = {key: value for(key,value) in stocks.items()}


# %% 
# zbiór tupli ( typ y to set )

y = {(key, value) for (key, value) in stocks.items()}

# %% 
# slownik odwrocony 
{value:key for (key,value) in stocks.items()}

# %% 
# słownik key małymi literami 

{key.lower():value for (key, value) in stocks.items()}

# %% 
# w wartoci nazwa i długoć nazwy 
# key i valalue możemy zastepowac np k i v 

c = {key:len(value) for (key, value) in stocks.items()}

b = {key:value + ' : ' + str(len(value)) for (key, value) in stocks.items()}
b = {k:v + ' : ' + str(len(v)) for (k, v) in stocks.items()}

# %% 

def replace_c(name):
    name = name.replace('COM', '0')
    name = name.replace('inc', '1')
    return name 

f = {k:replace_c(v) for (k,v) in stocks.items()}

# %% 
# pokaże tylko te które mają com w value 
g = {k:v for (k,v) in stocks.items() if 'COM'in v}

# %%
# pokaże value zaczynające się na M 
h = {k:v for (k,v) in stocks.items() if v.startswith('M')}

# %%
# pokaże value zaczynające się na M i znaków mniej niz 10
h1 = {k:v for (k,v) in stocks.items()\
     if v.startswith('M') if len(v)<10}
    
    
#### zadanie #### 
# zamien wartoci z kluczmi 


dicts = {'jeden':1, 'dwa':2, 'trzy':3}

l = {v:k for (k,v) in dicts.items()}


# %% 

k = {key: 'COM' if 'COM' in value else 'INC'for (key,value) in stocks.items()}


# %% 
# słownik jezeli parzysta to jej kwadrat 

number  = range(20)
number_dict = {}

for n in number:
    if n % 2 == 0 :
        number_dict[n] = n **2
        
print(number_dict)

# %% 
# słownik jezeli parzysta to jej kwadrat 
q = {key: key **2 for key in number if key % 2 == 0}

# %%
nest_dic = {'001':{'price':100},'002':{'price':40}, '003':{'price':60}}

for key, val in nest_dic.items():
    print(key,val)
    
# %% 
{key:val for (key,val) in nest_dic.items()}
    

# %% 
# mapowanie produktu do ceny 
{key:val['price'] for (key,val) in nest_dic.items()}
    

# %% 
nest_dic2 = {'001':{'price':100, 'items':4},'002':{'price':40, 'items':9},\
             '003':{'price':60, 'items':8}}

for key, val in nest_dic2.items():
    print(key,val)
    
# %% 
# mapowanie produktu do ceny 
{key:val['price'] for (key,val) in nest_dic.items()}

# %%
{key: val['price']*val['items'] for (key, val)in nest_dic2.items()}