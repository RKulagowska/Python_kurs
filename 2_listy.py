# -*- coding: utf-8 -*-

# listy są zmienne , uporządkowane, magą być zduplikowane [], można miksować typy, możemy zagnieżdzać 

empty_list = list()

# %%
# zmiana listy 
techs = ['Python', 'java', 'go', 'sql']
techs[0] = 'Python 3.7'
print(techs)

# %%
numbers = [3, 4, 5, 56]
print(numbers)
print(type(numbers))

# %%
mixed = ['python', 3.7, 4, True]
print(mixed)

# %% 
nested = [[1, 2, [3, 'sql']], ['python', 'java', 'go'],3]

# %%
first = ['mleko', 'ziemniaki', 'makaron']
second = ['woda', 'jajka']

bucked = [first, second]

# %%
len(bucked)

# %% 
techs = ['Python', 'java', 'go', 'sql']
techs += ['javascript']
print(techs)

# %%
print(dir(list))

#####    zadanie    ####

numbers = [1, 4, 2, 5]
letters = ['d', 's', 't']
new = numbers + letters 
print(new)

### rozwiązanie instruktora 
numbers = [1, 4, 2, 5]
letters = ['d', 's', 't']
 
print(numbers + letters)