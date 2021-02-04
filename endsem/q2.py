from functionlib import *
from math import *

# Q.2
a = sin(pi/8)
f2 = lambda x: 4/sqrt(9.8*(1 - (a*sin(x))**2))
T = simpson_integrate(f2, (0, pi/2), N = 10)
print('The time period T =', T)
# output
# The time period T = 2.14871072975296