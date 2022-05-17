# -*- coding: utf-8 -*-
# poszukiwania Pythona 

class A :
    
    def metoda(self):
        print('Metoda z klasy A')
 
class B(A):
    
    def metoda(self):
        print('Metoda z klasy B')
            
class C(A): 
    
    def metoda(self):
        print('Metoda z klasy C')
        
class D(B,C):
    
    def metoda(self):
        print('Metoda z klasy D')
        
# %%
d = D()
d.metoda()

# %% 
#  wywołano D więc sprawdza class D(B,C):jesli nie ma D szuka dalej w kolejnoci 
# B i na końcu w C
# jesli i tam nie ma porednio przejdzie do A  class B(A):

class A :
    
    def metoda(self):
        print('Metoda z klasy A')
 
class B(A):
    
   pass
            
class C(A): 
    
    pass
        
class D(B,C):
    
    pass
        
# %%
d = D()
d.metoda()