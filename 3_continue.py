# -*- coding: utf-8 -*-

# pozwala ominąć tylko 1 iteracje i kontunuować 
# poniżej pokaże od 0 do 5 omija 6 i kontynuuje do konca

for i in range(10):
    if i == 6: 
        continue
    print(i)

# %%
# użyto modulo % pokazuje ile reszty , pokaże 0,2,4,6,...
for i in range(20):
    if i % 2 == 0:
        print(i)
    
# %%
# użyto modulo % pokazuje ile reszty pokaże 1,3,5,7
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)
    
# %%
# wyprintuje wszystkie znaki pomijając spacje
sample = 'Python course'
for char in sample:
    if char == ' ':
        continue 
    print(char)
    
# %%
# znowu da tylko summer i holiday a ominie free

hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result = result+ char
    
# %%
# znowu da tylko summer i holiday a ominie free wiec dodajemy print(result)
# co rozwiązuje sprawę 

hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result = result+ char
print(result)    

# %%
##### zadanie ####
# z podanej listy wyprintuj wszystkie oprócz 99 
lista = [1, 2, 99, 4, 5]
for i in lista:
    if i == 99:
        continue
    print(i)

