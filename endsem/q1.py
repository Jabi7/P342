from functionlib import *
from math import *

# Q.1
f1 =  lambda x: (x - 5)*exp(x) + 5
print('\n\nNewton Raphson Method')		# Newton Raphson Method
r = newton_raphson(f1, 6, key = "Q1_a")
print('\nNewton Raphson root = ',r)
b = 6.626*3*10**(-3)/(1.381*r)
print('\nfrom lamda_m*T = b and x = hc/(lamda_m*k*T) we have:\n b = ', b)

# output
# Newton Raphson root =  4.9651142317448285

# from lamda_m*T = b and x = hc/(lamda_m*k*T) we have:
#  b =  0.0028990103307379696