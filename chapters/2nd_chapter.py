# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../src/')

from physics_lib import *

problems=dict(ch2=["2.1", "2.2", "2.3"])
problems=problems["ch2"][0]


if "2.1" in problems:
    m, s= symbols('m s')
    Q="A car travels in the x-direction on a straight and level road. For the first 4.00 s of its motion, the average velocity of the car is v av-x = 6.25 m/s . How far does the car travel in 4.00 s?"
    
    A=((6.25*m/s)*4*s)
    
    pprints("Q:", Q,
            "A:", A)
    
if "2.2" in problems:
    
    Q="In an experiment, a shearwater (a seabird) was taken from its nest, flown 5150 km away, and released. The bird found its way back to its nest 13.5 days after release. If we place the origin in the nest and extend the +x-axis to the release point, what was the bird’s average velocity in m/s (a) for the return flight, and (b) for the whole episode, from leaving the nest to returning?"
    
    pprint("Q:\n", Q, 
          "\nA:\n", A)
    
if "2.3" in problems:
    
    A=kinetic_energy(4,7)
    
    B=potential_energy(8,9)
    
    pprints(A,B)