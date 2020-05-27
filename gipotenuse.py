#!/usr/bin/python3

import math
def hypotenuse(len_a, len_b):
    return math.sqrt(len_a ** 2 + len_b ** 2)
a = hypotenuse(3,4)
print("Hypotenuse of the right triangle is {} mm.".format(a))
