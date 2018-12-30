# -*- coding: utf-8 -*-
# Author: M. Can Kandemir
# Contact: cnkndmr@gmail.com

import sys
sys.path.insert(0, '../src/')

from physics_lib import *

problems=dict(ch2=["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "2.10", "2.11", "2.12", "2.13", "2.14", "2.15", "2.16", "2.17", "2.18", "2.19"])
problems=problems["ch2"][3]

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
    A = deltat2 = deltax/Vavx2
    pprints("A:\n", A)
    
if "2.4" in problems:
    print("Problem 2.4")
    erDeltax = 200*meter
    erVav = 5*meter/second
    erT = erDeltax/erVav
    wrDeltax = 280*meter
    wrVav = 4*meter/second
    wrT = wrDeltax/wrVav
    tTotal = erT+wrT
    Vav = (erDeltax+wrDeltax)/tTotal
    A = Vav
    deltax = erDeltax-wrDeltax
    wrVav = deltax/tTotal
    B = wrVav
    
    pprints("A:\na)\n", A, 
           "b)\n", B)