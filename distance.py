#!/usr/bin/python3
from math import sqrt
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = round(sqrt(dsquared), 2)
    return result 
result = distance(1, 2, 3, 4)
print("The result of calculation is ({}).".format(result))
