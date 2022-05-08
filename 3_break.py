# -*- coding: utf-8 -*-
# wydrukuje tylko 6 
for i in '0123456789':
    i = int(i)
    if i == 6:
        print(i)
        break

# %%
# będzie w pętli do 6 
for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break
print('koniec')
    
# %%
sample = 'Python course'
for char in sample:
    if char == ' ':
        break
    print(char)
print('koniec')

# %%
for char in 'kowalskij@gmail.com':
    if char == '@':
        print('adres email zweryfikowany')
        break
else:
    print('Adres nie jest poprawny')

print('koniec')

# %%
##### zadanie #####

# sprawdz czy podane hasło ma min 10 znaków, zawiera !

ps = 'jnhvsoics!vd'

x = int(len(ps))
if int(x) > 10 and '!' in ps:
    print('Hasło poprawne')
else:
    print('Hasło niepoprane')

### rozwiązanie instruktora 
ps = 'jnhvsoics!vd'
if len(ps) > 10:
    for i in ps:
        if '!' in ps:
            print('Hasło poprawne')
            break
    else:
        print('Hasło niepoprawne')
else:
    print('Hasło niepoprawne')

    