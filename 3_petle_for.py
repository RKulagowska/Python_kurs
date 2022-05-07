# -*- coding: utf-8 -*-
# 
for i in 'python':
    print(i)

# %% 

name = 'python'
index = 0 

for char in name:
    print(index,char)
    index = index + 1

# %%
# zwraca od 0 do 9 

for index in range(10):
    print(index)

# %%
range(len(name))
list(range(len(name)))

for index in range(len(name)):
    print('Nr indeksu: ', index,'Litera:', name[index])
    
# %%
# enumerate dzieli tekst i zwraca nr indeksu i pierwszy element
for i in enumerate(name):
    print(i)
    
for indeks, character in enumerate(name):
    print(indeks, character)
    
# %%
for i in [4, 5, 6, 7, 8]:
    print(i)

# %%
for i, value in enumerate([4, 5, 6, 7, 8]):
        print(i, value)
        
# %%
for i in range(10,20):
    print(i)  
            
# %%
for i in range(10,20,2):
    print(i)    

# %%
for i in range(10,0,-1):
    print(i)    

# %%
for i in range(10,100,10):
    print(i)    
    
# %%
x = 'java'
for i in range(len(x)):
    print(i,x[i])
    
# %%
string = 'python course'
for char in string:
    print(char)
    
# %%
# tylko do 6 indeksu
string = 'python course'
for char in string[:6]:
    print(char)
# %%
# od końca
string = 'python course'
for char in string[::-1]:
    print(char)
    
# %%
hashtags= '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)
        
# %% 
# zipuje elementy - i łaczy w tuple

for char in zip('abcde', '12345'):
    print(char)
    
# %% 
# zipuje elementy - i łaczy w tuple. Obcina do najkrutszego elementy jesli
# rózne dlugosci 

for char, number in zip('python', '12345'):
    print(char, number)
    
# %%
# nie załapie fitness bo na końcu nie ma #

hashtags= '#sport#gym#fitness'

result = ''

for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''
        
        
####  zadanie    ####

for i in range(21):
    print(i)  
    
# %%
### zadanie 2  ###

hashtags = '#weekend#good#time#'
x = ''
for char in hashtags:
    if char not in '#':
        x = x + char
    else:
        if x:
            print(x)
            x = ''


