# -*- coding: utf-8 -*-

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