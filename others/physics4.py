from sympy import *
import numpy as np
import matplotlib.pyplot as plt
init_printing(use_latex=True)

e = 0
for n in range(18):
    e += 1/factorial(n)
    display("For e{} = {}".format(n,1/factorial(n)), float(e))

e = 0
for n in range(0, 100001, 10000):
    e = (1 + 1/(n+1))**n
    display("For n = {}".format(n), float(e))

x = np.arange(0,10,0.001)
eq1 = 5*(np.exp(x) - 1)
eq2 = x*np.exp(x)
plt.plot(x, eq1, label=r'$5(e^{x}-1])$')
plt.plot(x, eq2, label=r'$xe^{x}$')
plt.axis([4.955, 4.975, 705, 720])
plt.legend()
plt.grid()
plt.show()

x = Symbol('x')
eq1 = 5*(exp(x) - 1)
eq2 = x*exp(x)
display(eq2 - eq1,
       solve(eq1 - eq2, x))

