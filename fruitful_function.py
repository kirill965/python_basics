#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as ppl

def ryad(n):
    r = np.arange(0,n,0.1)
    return r

def sin_list(n):
    sin_a_list = np.sin(np.radians(np.arange(0,n,0.1)))
    return sin_a_list 

def cos_list(n):
    cos_a_list = np.cos(np.radians(np.arange(0,n,0.1)))
    return cos_a_list 

n = float(input("Please input value: "))
angles = ryad(n)
sin_a_list = sin_list(n)
cos_a_list = cos_list(n)

ppl.plot(angles, sin_a_list)
ppl.plot(angles, cos_a_list)
ppl.show()
