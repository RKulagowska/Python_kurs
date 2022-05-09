# -*- coding: utf-8 -*-

# zmienna r - odczytywanie plików do odczytu, zwr bład jesli nie istnieje 
# pokazuje z odstępami między linijkami 

file = open('simple.txt', 'r')
for line in file:
    print(line)
file.close()

# %%
# żeby zlikwidować linijki 

file = open('simple.txt', 'r')
for line in file:
    print(line, end = '')
file.close()

# %% 
# with otwiera przypisujemy do zmiennej file 
# już zamkniete nie zamykamy 
with open('simple.txt', 'r') as file:
    for line in file:
        print(line, end='')
        
# 'a' - append - otwiera plik do dopisania , tworzy plik
# jełi nie istnieje 
# 'w' -write-otwiera plik do zapisu, tworzy jesli nie istnieje 


# %%
###### zadanie 1  #####
#otworz plik o nazwie dane.txt i wydrukuj dane 
file = open('dane.txt', 'r')
for line in file:
    print(line, end = '')
file.close()

# %%
## rozw instruktora 
with open('dane.txt', 'r') as file:
    for line in file:
        print(line, end='')
        
# %% 
# odczytuje pierwszą listę 
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)

# %% 
# odczytuje wszystkie linie 
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    
# %% 
# odczytuje wszystkie linie  end ='' - kasuje puste linie 
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end ='')
        
# %% 
# while line: - jeżeli linia - tzn w pierwszej lini będzie cokolwiek 
# wtedy w str wartoć True 
# readline()czyta kolejną linie

with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end = '')
        line = file.readline()
        
# %% 
        
with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)

# %%
# wczytaj dane.txt i pokaż w postaci listy 

with open('dane.txt', 'r') as file:
    line = file.readlines()
    print(line)

   

