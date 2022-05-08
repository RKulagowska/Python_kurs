# -*- coding: utf-8 -*-

# zastąpi ! przecinkiem

raw_data = '345!23!2344!3334455'
clean_data = ''
for char in raw_data:
    if char != '!':
        clean_data = clean_data + char
    else:
        clean_data = clean_data + ','
        
print(clean_data)

# %%
# ulepszenie poprzedniego zapisu 

raw_data = '345!23!2344!3334455'
clean_data = ''
for char in raw_data:
    if char != '!':
        clean_data += char
    else:
        clean_data += ','
        
print(clean_data)

# %%

suma = 0
for i in range(10):
    suma += i
print(suma)

# %%
# wyciag bankowy :)

saldo = 450
print('Saldo początkowe {}'.format(saldo))
for kwota in range(10,60,10):
    print('Wypłacona kwota {}'.format(kwota))
    saldo -= kwota
    print('Saldo:{}'.format(saldo))
print('Saldo koncowe: {}'.format(saldo))

# %%
# sprawdzenie czy kod jest ważny - 4 znaki i same cyfry

print('Witaj w systemie logowania')
print('*'*30)
nick = input("podaj twój nick: ")
pin = input('Podaj Pin: ')
if len(pin) == 4:
    for char in pin:
        if char not in '0123456789':
            print('Pin niepoprawny')
            break
    else:
        print('kod pin ok')
        
else:
    print('Niepoprawny pin')

    