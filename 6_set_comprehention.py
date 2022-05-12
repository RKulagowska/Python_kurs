# -*- coding: utf-8 -*-

# split dzieli po np spacji , ale wtedy pojawiają się również słowa z "."
# dlatego też musimy replace 
# w unic wybieramy unikalne wyrazy 

text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi.'

words = text.lower().replace('.', '').split()

unic = {word for word in words}

# pozbyci się słowek = mniejszych niż 4 liter 

Unic_2 = {word for word in words if len(word) > 4}


# %% 
# napisać dużą literą jesli zaczyna się od pyt 
{word.capitalize() if word.startswith('pyt') else word for word in words}


##### zadanie ######
# stwórz zbiór zawierający unikalne znaki 

text = 'python jest popularny w uczeniu maszynowym'
print(len({letter for letter in text})) 


