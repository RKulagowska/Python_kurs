# -*- coding: utf-8 -*-
# jeżeli definiujemy klasy powinnimy zostawić 2 linie puste m blokami 
# jesli deginiujemy metode to dobrzy by było zostawić jedną linie 
# __init__ - nazwa konsruktora 


class Drzewo:
    
    def __init__(self, nazwa, wiek, wysokosc):
        self.nazwa = nazwa
        self.wiek = wiek
        self.wysokosc = wysokosc
        
    def czy_chronione(self):
        if self.wiek >=20 and self.wysokosc >= 20:
            print(f'Drzewo o nazwie {self.nazwa} jest pod ochroną.')
        else:
            print(f'Drzewo o nazwie {self.nazwa} nie jest pod ochroną.')
            
    def postarz_o_rok(self):
        self.wiek += 1
        
        
# %%
drzewo_1 = Drzewo('Sosna', 35, 25)
drzewo_2 = Drzewo ('Brzoza',28,18)

print(drzewo_1.nazwa)
print(drzewo_2.nazwa)

# %% 
drzewo_1.czy_chronione()
drzewo_2.czy_chronione()

# %% 
drzewo_1.postarz_o_rok()
print(drzewo_1.wiek)
