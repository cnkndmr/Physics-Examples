# -*- coding: utf-8 -*-
# Author: M. Can Kandemir
# Contact: cnkndmr@gmail.com

import matplotlib.pyplot as plt
#from sympy import pprint
#from IPython import get_ipython
#from IPython.display import display, HTML, Latex, Math
#from sympy.interactive import printing
#from sympy import symbols
from sympy.physics.units import *
from sympy import * # Added for import units

def potential_energy(h, m=1*kilogram, g=9.81*meter/second**2):
    res = m*g*h
    return convert_to(res, joule)

def kinetic_energy(v, m=1*kilogram):
    res = (1/2)*m*v**2
    return convert_to(res, joule)

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