# -*- coding: utf-8 -*-

import os

# %% 
dir(os)

# %% 
# current working directory 
os.getcwd()

# %% 
# zmiana folderu roboczego, wejscie o 1 stopień wyżej 

os.chdir('..')

# %% 
os.getcwd()

# %% 
# utworzenie folderu 
os.chdir('C:\\Users\\ZenBook\\Desktop\\rozwój osob\\24.Python')
os.system('mkdir dir1 dir2') 

# %% 
# usunięcie utworzonego foleru 
os.rmdir('dir1')

# %% 
# wylistowanie plików 

os.listdir()

# %% 
#wylistowanie plików z koncówką .txt

for item in os.listdir():
    if item.endswith('.txt'):
        print(item)

# %% 

# walk zwraca katalog głowny potem komendy moga wyciągnąć katalogi, pliki 

for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
    
# %% 
# łączy nazwy scieżek 
# r oznacza row text, brak naraża na błędy znakami bialymi typu \n \t

os.path.join(r'home\user\bin', 'python')


