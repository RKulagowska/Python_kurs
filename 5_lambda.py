# -*- coding: utf-8 -*-

def parabola(x):
    return x**2 + 3
print(type(parabola))
print(parabola(30))

# %% 
funkcja_1 = parabola
funkcja_1(30)

# %%
f = lambda x: x**2 +3
f(30)

# %%
# zwraca duże litery 
f_2 = lambda word: word.upper()
f_2('python')
    
# %%
f_3 = lambda x, y: x + y
add(3,5)

# %%
# skleja tekst 

f_4 = lambda word_1, word_2: word_1 + ' '+ word_2
f_4('Hello', 'World')


# %% 
# map? - hdziała jak help 

lista = ['python', 'java', 'r', 'sql']
list(map(lambda word: word.upper(), lista))

# %% 
def make_upper(word):
    return word.upper()
list(map(make_upper, lista))

# %%
list(map(lambda word: word.title(), lista))

# %%
# zwraca liste i mapuje włowo i długosc teksty 

list(map(lambda word: (word, len(word)),lista))

# %% 

def apply_fun(x,fn):
    return fn(x)
apply_fun(5,lambda x: x**2)
apply_fun([12,42],lambda x:sum(x))

# %% 
# sortowanie 
num = [5, 7, 8, 2, 4, 6, 9]
sorted(num)

# %% 
# sortowanie z kluczem po moduje z liczby: [0, -1, 1, -2, 2, -3, 3]

num = [-3, -2, -1, 0, 1, 2, 3]
sorted(num, key = lambda x: abs(x))

# %% 
# sortuje po pierwszym 
lista = [('jeden', 'one'), ('dwa', 'two'), ('trzy', 'three')]
sorted(lista)

# %% 
# sortuje po drugim
lista = [('jeden', 'one'), ('dwa', 'two'), ('trzy', 'three')]
sorted(lista, key = lambda x:[1])


 #### zadanie ######
 # podana jest lista, używajac map() i lambda uzyskaj 3 pierwsze litery 
 # każdego miasta 
 
city = ['Warsaw', 'London', 'Berlin', 'New York']
print(list(map(lambda word: word[:3], city)))
 
 