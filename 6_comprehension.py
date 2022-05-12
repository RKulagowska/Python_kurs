# -*- coding: utf-8 -*-

# przeliterować i zwrócić do list kwadrat 

results = []
for i in range(100):
    results.append(i**2)
print(results)


# %%
# przeliterować i zwrócić do list kwadrat 
results2 = [i**2 for i in range(100)]

# %% 
lista = [i for i in range(100)]

# %%
# podzielne przez 5 + podniesione do kwadratu

results3 = []
for i in range(100):
    if i % 5 == 0: 
        results3.append(i**2)
print(results3)

# %% 
result4 = [i ** 2 for i in range(100) if i % 5 == 0]

# %% 
# 2 petle for + list comprehentions

letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

result5 = []
for letter in letters :
    for number in numbers:
        result5.append(letter + number)
        
# %% 
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

results6 = [letter + number for letter in letters for number in numbers]

# %% 
let1 = ['a', 'b', 'c']
let2 = ['a', 'b', 'c']

result7 = [l1 + l2 for l1 in let1 for l2 in let2]

# %% 
# jak połaczyć literki które są rózne 

let1 = ['a', 'b', 'c']
let2 = ['a', 'b', 'c']

result8 = [l1 + l2 for l1 in let1 for l2 in let2 if l1 != l2]

# %%
# układ 0,1,2,... w 10 linijkach 

[ [j for j in range(10)] for i in range(10)]

# 0 do 4 w 10 linijkach 
[ [j for j in range(5)] for i in range(10)]

[ [j for j in range(10)] for i in range(5)]


# dające 3 tuple 

[ [(i,j) for j in range(10)] for i in range(3)]


# %%
# ala tabliczka mnożenia 
[ [i * j for j in range(10)] for i in range(10)]

# %%
# alista 5 list w pierszej linijce wszystkie kombinacje z 1 potem 2..
[ [l1 + l2 for l2 in 'abcde'] for l1 in '12345']

# %% 

def silnia(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * silnia(n-1)
[silnia(i) for i in range(10)]

#### zadanie ####
# wydrukuj podzielne przez 4 z listy od 1 do 30 

print([i for i in range(30) if i % 4 == 0])
###### zadanie ######
# wydrukuj list com od 0 30 30 podzilene przez 4 



x = [ i for i in range(30) if i % 4 == 0]