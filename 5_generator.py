# -*- coding: utf-8 -*-

def generator():
    yield 4
    yield 5
    
# %%
gen = generator()

# %%
next(gen)


# %%
def gen2(word):
    letters = list(word)
    for letter in letters:
        yield letter
        
gen2= gen2('python')

# %%
next(gen2)

# %% 
files = ['script_1.py', 'geny.txt', 'new.py']

def gen_files(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item
            
gen = gen_files(files)

# %% 
next(gen)


# %%
#### zadanie ###
# stwórz generator który zrawca tylko pliki .py

files = ['run_me.py', 'README.md', 'help.txt.', 'script.py', 'menu.py', 'main.py', 'py']

def generator_py(lista):
    for item in lista :
        if item.endswith('.py'):
            yield item
gen = generator_py(files)
# %% 
next(gen)


### rozw instruktora 
files = ['run_me.py', 'README.md', 'help.txt.', 'script.py', 'menu.py', 'main.py', 'py']
 
def generator_py(files):
    for file in files:
        if file.endswith('.py'):
            yield file

