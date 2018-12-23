# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sympy import pprint
from IPython import get_ipython
from IPython.display import display, HTML, Latex, Math
from sympy.interactive import printing

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



def pprints(func, *funcs, **kwargs):
    """Reference: https://butterflyofdream.wordpress.com/
    
    Parameters
    ==========
    **kwargs
    output_style : display, pprint, print, latex
    
    Examples
    ========
    pprints("f(x)",f,
            "collect(f,x)=",collect(f,x),
            output_style="pprint")
    """
    output_style=kwargs.get("output_style","pprint")
    if output_style=="display":
        display(func)
        if funcs is None: return
        for f in funcs:
            display(f)
    elif output_style=="pprint":
        pprint(func)
        if funcs is None: return
        for f in funcs:
            pprint(f)
    elif output_style=="print":
        print(func)
        if funcs is None: return
        for f in funcs:
            print(f)
    elif output_style=="latex":
        print(func)
        if funcs is None: return
        for f in funcs:
            print(latex(f))