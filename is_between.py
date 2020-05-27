#!/usr/bin/python3

def is_between(a,b,c):
    return a <= b <= c
a,b,c = 1,2,3
if is_between(a,b,c):
    print("{} is between {} and {}.".format(b,a,c))
else:
    print("{} is not between {} and {}.".format(b,a,c))
    
