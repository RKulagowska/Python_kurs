# -*- coding: utf-8 -*-

# wyrzucenie wszystkich atrybutów i metody obiektu tekstowych

string = 'Python'

print(dir(string))

# %%

a= 10 
print(dir(a))

# %%
string = 'Python'
type(a)
type(string)



# %%

##### zadanie  ####

x = '12333'
y = 1234 
z = '0'

print('x: ' +str(type(x)), '\ny: ' +str(type(y)),'\nz: ' +str(type(z)))

print('x: {0}\ny: {1}\nz: {2}'.format(type(x), type(y), type(z)))