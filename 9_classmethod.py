# -*- coding: utf-8 -*-

# dekorator class method podobny do static method ale odnosi się do klasy  


class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.wiek = wiek 
        self.lista_studentow.append(self)   
    
    @classmethod
    def liczba_studentow(cls):
        print('Liczba studentów: ', len(Student.lista_studentow))
        
# %% 
student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Tomasz', 'Nowak', 23)

# %% 
Student.liczba_studentow()