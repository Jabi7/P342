from functionlib import *
from math import *

# Q.4
dy  = lambda u, y, x : u
ddy = lambda u, y, x : -9.8
a, b = 0, 5
y, x = shooting_method(ddy, dy, 2, 0, 45, 0.02)

print('the final velocity = 47.89999999999995')

## output ##
# Guess the 1st value of slope: 40
# Guess the 2nd value of slope: 50
# The obtained solution for z is : 47.89999999999995
# the velocity = 47.89999999999995 
