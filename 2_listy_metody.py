# -*- coding: utf-8 -*-

techs = []
print()


# %%
techs.append('python')
print(techs)

# %% 
techs.append('java')
print(techs)

# %% 
# doklejanie zagnieżdzonej listy 

techs.append(['hadoop', 'spark'])
print(techs)

# %% 

# dodaje na pierwszym poziomie 
techs.extend(['sql', 'sas'])
print(techs)

# %%

# potrzebuje wartoc na którym miejscyu musi wstawić daną wartosc - techs.insert('go')
# powoduje error TypeError: insert expected 2 arguments, got 1

techs.insert(0, 'go')
print(techs)

# %%
techs.insert(2,'r')
print(techs)

# %% 
# pop - daje output ostatnią wartoć i usuwa ją z listy 

techs.pop()


# %%
# usuwa konkretną pozycję 
techs.pop(0)

# %%
techs = ['python', 'java', 'r']
techs.index('r')

# %% 
# ile razy występuje dany element 
techs = ['python', 'java', 'r', 'python']
techs.count('python')

# %% 
# sortuje listę alfabetycznie
techs = ['python', 'java', 'r', 'angular', 'php']
techs.sort()

# %% 
# sortuje listę alfabetycznie od końca 
techs = ['python', 'java', 'r', 'angular', 'php']
techs.sort(reverse = True)

# %%
# odwracanie kolejnosci - 2 rozne metody 

techs = ['python', 'java', 'r', 'angular', 'php']

techs[::-1]
techs.reverse()

# %% 

# podmiana na konkretnej pozycji 
techs = ['python', 'java', 'r', 'angular', 'php']
techs[1]= 'c++'



 ##### zadanie ######
 
a = [4, 5, 3, 3]
b = [9, 7]
a.extend(b)
print(a)



##### zadanie 2 

a = ['Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber']
a.extend(['Amazon', 'Google'])
print(a)

#### rozwiązanie podane przez prowadzącego 

companies = ['Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber']
companies.append('Amazon')
companies.append('Google')
 
print(companies)


