# -*- coding: utf-8 -*-


from sympy import symbols

problems=dict(ch2=["2.1", "2.2"])
problems=problems["ch2"][0]


if "2.1" in problems:
    
    m, s= symbols('m s')
    
    Q="A car travels in the x-direction on a straight and level road. For the first 4.00 s of its motion, the average velocity of the car is v av-x = 6.25 m/s . How far does the car travel in 4.00 s?"
    
    A=((6.25*m/s)*4*s)
    
    print("Q:\n", Q, 
          "\nA:\n", A)
    
if "2.2" in problems:
    
    print("Q:\n", Q, 
          "\nA:\n", A)