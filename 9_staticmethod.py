# -*- coding: utf-8 -*-


class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.wiek = wiek 
        self.lista_studentow.append(self)   
        
    def liczba_studentow(self):
        print(len(self.lista_studentow))
        
# %% 
student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Tomasz', 'Nowak', 23)

# %% 
student_1.liczba_studentow()

# %% 
# static method 

class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.wiek = wiek 
        self.lista_studentow.append(self)   
    
    @staticmethod
    def liczba_studentow():
        print('Liczba studentów: ', len(Student.lista_studentow))
        
# %% 
student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Tomasz', 'Nowak', 23)

# %% 
Student.liczba_studentow()