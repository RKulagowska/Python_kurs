# -*- coding: utf-8 -*-
# pozwala tworzyc klasę a potem je rozszerzać


class Czlowiek:
    
    def __init__(self, imie, nazwisko):
        self.imie = imie 
        self.nazwisko = nazwisko
        
    def info(self):
        print(f'{self.imie} {self.nazwisko}')
        
class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, klub):
        super().__init__(imie, nazwisko)
        self.klub = klub
        
    def info_o_zawodn(self):
        print(f'Klub: {self.klub}')
        
# %% 

pilkarz_1 = Pilkarz('Robert', 'Lewandowski', 'Bayern')
pilkarz_2 = Pilkarz('Krzysztof', 'Piątek', 'AC Milan')

# %% 
pilkarz_1.info()

# %% 
pilkarz_1.info_o_zawodn()

# %% 
# jesli chemy pokazać info z grupy człowiek i pilkarz razem 


class Czlowiek:
    
    def __init__(self, imie, nazwisko):
        self.imie = imie 
        self.nazwisko = nazwisko
        
    def info(self):
        print(f'{self.imie} {self.nazwisko}')
        
class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, klub):
        super().__init__(imie, nazwisko)
        self.klub = klub
        
    def info_o_zawodn(self):
        super().info()
        print(f'Klub: {self.klub}')
        
# %% 
pilkarz_1 = Pilkarz('Robert', 'Lewandowski', 'Bayern')
pilkarz_2 = Pilkarz('Krzysztof', 'Piątek', 'AC Milan')

# %% 
pilkarz_1.info_o_zawodn()
