# -*- coding: utf-8 -*-

text =  'Witaj na kursie Pythona.\nPython jest wspaniały.'
print(text)

# %%

dir(text)

# pomoc co dana formuła robi 

help(str.count)

# %%
# zwraca dużą literę tylko na początku

text.capitalize()

# %%
# zwaca dużą litere na początku każdego wyrazy

text.title()

# zwraca ile razy ciąg wystąpił w tekscie 

text.count('Python')

# %% 
# od jakiego ciągu ma się zaczynać - zwraca true lub False 

text.startswith('Wi')

# %% 

'python'.startswith('py')
text.endswith('y.')

# %%
# zwraca nr indeksu a potem możemy wrzucić do wycinania 

text.find('Python')
text[text.find('Python'):]

# %%
# wyciagniecie indexu 1-go # i wrzucenie do wycinania 

hashtags = 'sport#gym#'
idx = hashtags.find('#')
hashtags[:idx]

# %%
# sprawdza czy wszystkie znaki sa alfanumeryczne 

'pawel33 '.isalnum()

# %%

'2333445'.isdigit()
# %%

'pyThon'.islower()
'pyThon'.isupper()

# %%
# łączenie - listy podajemy w nawiasach kwadratowych 

' '.join(['python', '3.7'])
','.join(['1','2','3'])
'#'.join(['sport','gym', 'fit'])


# %%

'#good#time#mood'.replace('#', ' ')

# %%

'column name'.replace(' ', '_')
# %%
# wycinanie białych znaków w odrębie tekstu 

' python    '.strip()
' python    '.rstrip()
' python    '.lstrip()

# %% 

'1,2,3,4,5,6'.split(',')
'python java php sql sas'.split()
'#gym#fit#mood'.split('#')

# %%
# dobija do cyfry (x) literowej - dodaje 0 na początku 

'12'.zfill(4)


######    zadanie 1   #####

x = '#'.join(['sport','python','free','time'])
print(x)

####   zadanie 2 ######

x= '123,785,45,5'
print(x.split(','))



