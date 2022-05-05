# -*- coding: utf-8 -*-

name = 'Python'

# %%
print(name)
print(name[0])


# numerowanie od końca zaczyna się od -1 
# numerowanie ciągu jest prawostronnie otwarte

print(name[-1])

print(name[1:3])
print(name[:4])
print(name[2:])
print(name[::-1])

name[:]

# %%
name[-3:]
name[-3:-1]

# indeksacje podajemy w nawiasie kwadratowym 

# %%
full = 'Python Programming'

print(full[7:])


# co druga literę  name[start:stop:step]
print(full[::2])

# %% 
sample = '#stop#this#flow'
print(sample[::5])

# %%
numbers = '8,9,7,4'
print(numbers[::2])


# wycinanie od końca [::-1] 4,7,9,8  , [::-2]4798
# %% 
numbers = '8,9,7,4'
print(numbers[::-1])
print(numbers[::-2])

# %%
# sprawdznie czy dane są ciągu - daje true albo false 
name = 'Python'
'p' in name
'Py'in name

