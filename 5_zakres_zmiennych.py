# -*- coding: utf-8 -*-

i = 2
j = i 
i = 3

# %% 
# łapie a bo przed przypisaniem funcji 
a = 5 
def fun1():
    print(a)
fun1()

# %% 
# lakalnie jest 4 i tam tylko działa , globalna zignorowana 

a = 5 
def fun1():
    a = 4 
    print(a)
fun1()

# %% 
# bład bo a = 4 jest zdefiniowana lokalnie 

def fun():
    a = 4 
    print(a)
    
fun()

print(a)

# %% 

# nie mieszac danych lokalnych i globalnych 
tech = 'Python'

def change_tech(new_tech):
    tech = new_tech
    print(tech)
print(tech)
change_tech ('java')
print(tech)


# %% 

# status global 

tech = 'Python'

def change_tech(new_tech):
    global tech
    tech = new_tech
    
print(tech)
change_tech ('java')
print(tech)


# %% 
# zagniezdzanie funkcji 2, 1,0 
 
level = 0 
def f1():
    level = 1
    
    def f2():
        level = 2
        print('Funkcja f2:', level)
    f2()
    print('Funkcja f1:', level)
f1()
print('globalnie:', level)

# %% 
# zagniezdzanie funkcji  2,2,0
 
level = 0 
def f1():
    level = 1
    
    def f2():
        nonlocal level
        level = 2
        print('Funkcja f2:', level)
    f2()
    print('Funkcja f1:', level)
f1()
print('globalnie:', level)


# %% 
# zagniezdzanie funkcji  2,1,2
 
level = 0 
def f1():
    level = 1
    
    def f2():
        global level
        level = 2
        print('Funkcja f2:', level)
    f2()
    print('Funkcja f1:', level)
f1()
print('globalnie:', level)

 