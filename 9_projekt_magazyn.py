# -*- coding: utf-8 -*-

# tworzenie magazynu , wyswietlenie dostepnych produktów, usuniecie 
# dodanie produktów
# tworzenie listy za pomoca konstruktora 
# >>> znak zachęty ? :) 
# żeby skorzystać z funcki exit musisz zaimportować sys

import sys

class Magazyn:
    
    def __init__(self, lista_prod):
        self.lista_prod = lista_prod
        
    def wyswietl_prod(self):
        print('Dostepne profukty:')
        for produkt in self.lista_prod:
            print(produkt)
            
    def dodaj_prod(self):
        self.nazwa_prod = input('Podaj nazwe produktu: >>>')
        if self.nazwa_prod not in self.lista_prod:
            self.lista_prod.append(self.nazwa_prod)
        print(f'Produkr {self.nazwa_prod} został dodany do Magazynu')
      
        
    def usun_prod(self):
        self.nazwa_prod = input('Podaj nazwe produktu, który chcesz usunąc: '
                                '>>>')
        if self.nazwa_prod in self.lista_prod:
            self.lista_prod.remove(self.nazwa_prod)
            print('Usunięto produkt z magazynu.')
        else:
            print('Podanego produktu nie ma na magazyne.')
            
# %%
magazyn = Magazyn(['mleko','woda','jajka'])

while True:
    print('Wprowadź 1 żeby wyswietlić stan magazynu.')
    print('Wprowadź 2 żeby dodać produkt.')
    print('Wprowadź 3 żeby usunac produkt.')   
    print('Wprowadź 4 żeby zakończyć. ')
    
    wyb_uzyt = int(input('>>>'))
    if wyb_uzyt is 1:
        magazyn.wyswietl_prod()
    elif wyb_uzyt is 2:
        magazyn.dodaj_prod()
    elif wyb_uzyt is 3:
        magazyn.usun_prod()
    elif wyb_uzyt is 4:
        sys.exit()
    

        
            

        
    

