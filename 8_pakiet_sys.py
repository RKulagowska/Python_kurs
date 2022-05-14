# -*- coding: utf-8 -*-

# power Shell  i git bash 
# pwd - scieżka 
# ls - lista plików 
# python hello.py - otwiera zawartosć hello.py 
# interpreter pythona - komenda  python 
# cd - change directory 


import sys
# zwraca liste nazwę pliku + argumenty
# komenda ls w consoli 

print(sys.argv)

args = sys.argv
print("nazwa pliku:", args.pop(0))

i = 1
while args:
    print('arg nr {}: {}'.format(i, args.pop(0)))
    i += 1
    
