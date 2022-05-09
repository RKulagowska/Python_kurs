# -*- coding: utf-8 -*-

# otwiera plik techs.txt jesli istnieje i zapisuje dane do pliku 

techs = ['python', 'java', 'sql', 'scala']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file = file)

# %% 
# chcemy przypisać do pliku wszystkie parzyste mniejsze od 100 
# TypeError: write() argument must be str, not int dlatego w ostatniej linijce 
# przekształcamy liczbę na stringa
# + '\n'pozwala przekształcic ciąg liczb w liczny w osobnych linijkach 

even_number = list(range(100))[::2]

with open('numbers.txt','w') as file:
    for number in even_number:
        file.write(str(number) + '\n')
        
# %%
# 'a' dodaje dane 

techs = ['python', 'java', 'sql', 'scala']

with open('techs.txt', 'a') as file:
    for tech in techs:
        print(tech, file = file)
        
# %%
# wszystkie w stringu z wyjątkiem ostatniego tzn bez białych znaków \n

technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
print(technologies)

# %%
##### zadanie 1
techs2 = ['python', 'java', 'sql', 'sas']

with open('techs2.txt', 'w') as file:
    for x in techs2:
        print(x, file = file)
        
        
# %%
# zbudować choinkę za pomocą pętli 
# ta częsc kodu buduje prawą strone choinki

for i in range(10):
    print('*'*i)
    
# %%
# ta częsc kodu buduje lewa strone choinki
# prawy i lewy daje baładan
for i in range(10):
    print('{:>9}'.format('*'*i))
    print('{}'.format('*'*i))
        
# %%

# prawy i lewy daje baładan end='' - rozwiązuje sprawe 
for i in range(10):
    print('{:>9}'.format('*'*i), end='')
    print('{}'.format('*'*i))
    
# %%
# ta częsc kodu buduje choinke i zapisujemy do tree.txt
# pamietaj że file= file zapisuje do pliku , jełi tego nie dodamy pokaże 
# tylko w konsoli 

with open('tree.txt', 'w') as file:
    for j in range(2):   
        for i in range(10):
            print('{:>9}'.format('*' * i ), end = '', file = file)
            print('{}'.format('*'*i), file = file)
        