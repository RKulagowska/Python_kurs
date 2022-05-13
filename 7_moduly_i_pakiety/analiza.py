# -*- coding: utf-8 -*-

import rocket_science

# %%
dir(rocket_science)

# %% 
rocket_science.calculate_mean([3,4])
rocket_science.calculate_min([3,4])
rocket_science.calculate_max([3,4])

# %% 
# import tylko jednej formuły 
from rocket_science import calculate_max
calculate_max([2,3])


# importowanie wszystkich 
from rocket_science import *
calculate_max([4,5])

# %% 
# wyciagniecie tylko 2 

from rocket_science import calculate_mean, calculate_min
calculate_mean([4,5])