#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:43:54 2018

@author: cnkndmr
"""
# In[1]

from phys_lib import *
    
# In[2]
pe = []
height = 60

append_tuple_to_list(height, potential_energy, pe)

potential_energy = []
pe_time = []

tuple_to_list(pe,potential_energy,pe_time)
    
plot_print(pe_time,potential_energy)

# In[3]
ke = []
velocity = 100

append_tuple_to_list(velocity, kinetic_energy, ke)

kinetic_energy = []
ke_time = []

tuple_to_list(ke,kinetic_energy,ke_time)

plot_print(ke_time,kinetic_energy)