#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:43:54 2018

@author: cnkndmr
"""
# In[1]
import matplotlib.pyplot as plt

def potential_energy(h, m=1, g=9.81):
    return m*g*h

def kinetic_energy(v, m=1):
    return (1/2)*m*v**2

def plot_print(x, y):
    plt.plot(x, y)
    return plt.show()
    
def tuple_to_list(a,b,c):
    for i in a:
        b.append(i[0])
        c.append(i[1])
    return

def append_tuple_to_list(a,b,c):
    for i in range(a+1):
        temp_tuple = ()
        temp_tuple += (b(i),i)
        c.append(temp_tuple)
    return
    
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