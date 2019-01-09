# -*- coding: utf-8 -*-
"""
Author: M. Can Kandemir
Contact: cnkndmr@gmail.com
"""

import sys
sys.path.insert(0, '../src/')

from physics_lib import *

problems=["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "2.10", "2.11", "2.12", "2.13", "2.14", "2.15", "2.16", "2.17", "2.18", "2.19"]
problems=problems[9]

# TODO 2.6, 2.8(wrong result)

if "2.1" in problems:
    print("Problem 2.1")
    Vavx = 6.25*meter/second
    deltat = (25*meter)/Vavx
    deltax = Vavx*deltat
    A = Vavx*deltat
    pprints("A:\n", A)
    
if "2.2" in problems:
    print("Problem 2.2")
    x1 = 0
    x2 = 5.15*10**6*meter
    t1 = 0
    t2 = 1.166*10**6*second
    deltat = t2-t1
    deltax = x2-x1
    Vavx = deltax/deltat
    A = convert_to(Vavx, kilometer/hour)
#    A = vavx
    pprints("A:\n", A)

if "2.3" in problems:
    print("Problem 2.3")
    Vavx = 105*kilometer/hour
    deltat = 140*minute
    deltax = Vavx*deltat
    Vavx2 = 70*kilometer/hour
    pprints("A:\n", deltax/Vavx2)
    
if "2.4" in problems:
    print("Problem 2.4")
    eDeltax = 200*meter
    eVav = 5*meter/second
    eT = eDeltax/eVav
    wDeltax = 280*meter
    wVav = 4*meter/second
    wT = wDeltax/wVav
    tTotal = eT+wT
    Vav = (eDeltax+wDeltax)/tTotal
    deltax = eDeltax-wDeltax
    wVav = deltax/tTotal
    pprints("A:\na)\n", Vav, 
           "b)\n", wVav)
    
if "2.5" in problems:
    print("Problem 2.5")
    x1 = 40*meter
    x2 = 60*meter
    deltax = x2-x1
    t1 = 28*second
    t2 = 36*second
    deltat = t1+t2
    Vavx = deltax/deltat
    sumX = x1+x2
    Vav = sumX/deltat
    pprints("A:\na)\n", Vavx, 
           "b)\n", Vav)
    
if "2.6" in problems:
    print("Problem 2.6")
    def x(t):
        alpha = 1.5*meter/second**2
        beta = -0.05*meter/second**3
        return alpha*t**2+beta*t**3
    t0 = 0
    t1 = 2*second
    t2 = 4*second
    Vavx1 = (x(t1)-0)/(t1)
    Vavx2 = (x(t2)-0)/(t2)
    Vavx21 = (x(t2)-x(t1))/(t2-t1)
    pprints("A:\na)\n", Vavx1, 
           "b)\n", Vavx2,
            "c)\n", Vavx21)
        
if "2.7" in problems:
    print("Problem 2.7")
    b = 2.4*meter/second**2
    c = 0.12*meter/second**3
    def x(t):
        return b*t**2 - c*t**3
    def v(t):
        return 2*b*t - 3*c*t**2
    t0 = 0
    t1 = 5*second
    t2 = 10*second
    Vavx20 = (x(t2)-x(t0))/(t2-t0)
    Vt0 = v(t0)
    Vt1 = v(t1)
    Vt2 = v(t2)
    t = Symbol('t')
    t3 = solve(2*b*t - 3*c*t**2, t)[1]
    t30 = t3-t0
    pprints("A:\na)\n", Vavx20,
            "b1)\n", Vt0,
            "b2)\n", Vt1,
            "b3)\n", Vt2,
            "c)\n", t30)
    
if "2.8" in problems:
    print("Problem 2.8")
    t = Symbol('t')
    def x(t):
        return 28*meter + 12.4*meter/second*t - 0.045*meter/second**3*t**3
    def v(t):
        return 12.4*meter/second*diff(t,t) - 0.045*meter/second**3*diff(t**3, t)
    pprints("A:\na)\n", v(8*second))
    
if "2.9" in problems:
    print("Problem 2.9")
    t0 = 0
    t1 = 2*second
    t2 = 3*second
    v1 = 2*meter/second
    v2 = 3*meter/second
    x1 = v1*(t1-t0)
    x2 = v2*(t2-t1)
    Vavx = (x1+x2)/(t2)
    x3 = -(v2)*(t2-t1)
    Vavx2 = (x1+x3)/(t2)
    pprints("A:\na)\n", Vavx,
           "\nb)", Vavx2)

if "2.10" in problems:
    print("Problem 2.10")
    x = Symbol('x')
    f01 = (50*x - 0)/(1 - 0)
    f12 = (100*x - f01)/(2 - 1)
    f23 = (350*x - f12)/(3.5 - 2)
    f34 = (400*x - f23)/(5.5 - 3.5)
    f45 = (200*x - f34)/(7 - 5.5)
    function = [f01, f12, f23, f34, f45]
        
    