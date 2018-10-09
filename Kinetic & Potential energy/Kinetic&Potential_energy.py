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
    plt.show()
    
# In[2]
pe = []
height = 60

for i in range(height+1):
    temp_tuple = ()
    temp_tuple += (potential_energy(i),i)
    pe.append(temp_tuple) 

potential_energy = []
pe_time = []

for i in pe:
    potential_energy.append(i[0])
    pe_time.append(i[1])
    
plot_print(pe_time,potential_energy)

# In[3]
ke = []
velocity = 100

for i in range(velocity+1):
    temp_tuple = ()
    temp_tuple += (kinetic_energy(i),i)
    ke.append(temp_tuple)

kinetic_energy = []
ke_time = []

for i in ke:
    kinetic_energy.append(i[0])
    ke_time.append(i[1])

plot_print(ke_time,kinetic_energy)