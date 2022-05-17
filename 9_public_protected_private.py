# -*- coding: utf-8 -*-

# public: zmienna 
# dostepna z poziomu klasy, klasy pochodnej i wszedzie poza klasa pochodną 
# protected: _zmienna - z jednym podkrelnikiem 
# dostepna z poziomu klasy i klasy pochodnej 
# private: __zmienna - z dwoma podkreslnikami 
# dostepna tyylko z poziomu klasy 

# AttributeError: 'Spolka' object has no attribute '__gielda' - prywatna 

# %%
class Spolka:
    
    def __init__(self,rodzaj, rynek, gielda):
        self.rodzaj = rodzaj 
        self._rynek = rynek
        self.__gielda = gielda
        
class KGHM(Spolka):
    
    def __init__(self, rodzaj, rynek, gielda, nazwa):
        super().__init__(rodzaj,rynek, gielda)
        self.nazwa = nazwa
        print(f'Atrubut publiczny: {self.rodzaj}')
        print(f'Atrubut chroniony: {self._rynek}')
        # print(f'Atrubut prywatny: {self.__gielda}')
        
# %% 

spolka = Spolka('SA','Główny','GPW w Warszawie')
print(f'Atrubut publiczny: {spolka.rodzaj}')
print(f'Atrubut chroniony: {spolka._rynek}')
# print(f'Atrubut prywatny: {spolka.__gielda}')


# %% 
# dobieranie się na siłe do wartosci prywatnej, nie powinnismy tego robić :) 

kghm = KGHM('SA','Główny','GPW w Warszawie','KGHM')

print(f'Atrubut prywatny: {kghm._Spolka__gielda}')
