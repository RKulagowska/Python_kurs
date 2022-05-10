# -*- coding: utf-8 -*-

# abs zwraca wartosc bezwzgledna, funkcje mozna łaczyć

abs(-10)
print(abs(-10))

# %%
# bool testuje logige daje albo prawda albo falsz, Falsz- pusta lista, słownik
# 0 - fałsz 

bool([])
bool({})
bool(False)
bool(' ')

# %%
# dir zwraca wszystkie możliwe atrybuty i metody obiektu ( formuly)
# te ktore zaczynaja się od __ są bardziej zaawansowane

dir(list)
dir(tuple)

# %%
# enumerate tworzy liste tupli i zwraca indeks + wartosc

list(enumerate(['pawel','python', 'one' ]))

# %%
# eval liczy 

eval('1+1')
x = 10 
eval ('x+13')

# %% 
# zwarca wartosci prawdziwe czyli wyrzuci 0 

list(filter(abs, [-2,-1, 0, 1, 2]))

# %% 
# wyrzuci ''

list(filter(bool,['python', '', 'java']))

# %% 
# pozwala konwertowac liczbe lub wartosc tekstową podana jako liczbe
# na wartosc zmienna przecinkowa
float(1)
float('1')
float(1.3)

# %% 
# type zwraca typ danego elementu 
type(1)
type('1')
type([1, 2,])

# %% 
# jak działa dana funkcja 
help(float)
help(int)

# %% 
# czy dany obiekt jest instancja naszej klasy - czy 1 jest cyfra
# '' to string
isinstance(1,int)
isinstance(1, float)
isinstance(1.0, float)
isinstance('text', str)
isinstance('', str)

# %% 
# długoc elementy 
len('python')
len('')
len(' ')
len([])

# w przypadku zagnieżdzonych podaje tylko najwyższy rząd poniżej  2 

len([[3,4], [4,5,6,7,[5,5]]])
# %% 
#list rozdziela na znaki 

list('python')
list(range(10))

# %% 
# map składnia (funkcja, obiekt literowalny)
# zwraca liste po zastosowaniu abs

list(map(abs,[-2,-1,0,1,2]))

# %%
# zmienia na pierwsza duza litere  . title
# 
name= ['pawel', 'renata', 'jan']
list(map(str.title,name))

# %%
# max zwraca w literach najdalsza od a , min na odwrot
max([1,2,3,6])
max('renata')

min('renata')

# %% 
# podniesienie do potegi (baza, wykładnik) to samo co **

pow(2,4)
2**4

# %%
list(reversed([5,3,1]))
list(reversed('python'))

# %%
# skraca miejsca po przecinku ( wartosc, ile miejs po przecinku 

round(3.45678889889,2)

# %% 
# przekztałca liczbe na text
str(1)
str(34.44)

# %%
# sumowanie elementow 

sum([3,4,5])

# %% 
# iterowanie po kilku listach na raz i łaczy w tuple, ucina dłuższa liste
# czyli wyrzuci 10 

l1 = [1,2,3]
l2 = [4,5,9,10]
list(zip(l1,l2))

list(zip('puthon','course'))


# %%
### zadanie ####
# sprawdz typy obiektów

print(type((1,2,3)))
print(type({1,2,3}))
print(type([1,2,3]))
print(type({1:1,2:2,3:3}))
print(type('123'))
print(type(123))

