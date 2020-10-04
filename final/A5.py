from math import *
from functionlib import *
import matplotlib
import matplotlib.pyplot as plt



## Qesttion 1 ##

print('\nQesttion 1:')

## (a)

print("\n(a):")

f1 = lambda x: log(x) - sin(x)		# generating given funtion in Question 1 section a

a, b = 1.5,2.5

a,b = bracket_root(f1,a,b)		# bracketing range

print('\nBisection Method')
r = bisection(f1, a, b, key = 'Q1_a')		# Bisection Method	
print('\nBisection root = ',r)

print('\n\nRegula Falsi Method')
r = falsi(f1, a, b, key = 'Q1_a')		# Regula Falsi Method
print('\nRegula Falsi root = ',r)

print('\n\nNewton Raphson Method')		# Newton Raphson Method
r = newton_raphson(f1, 1.5, key = "Q1_a")
print('\nNewton Raphson root = ',r)



## (b)

print("\n\n(b):")

f2 = lambda x: -x - cos(x)		# generating given funtion in Question 1 section b

a, b = -pi/4, pi/4

a,b = bracket_root(f2,a,b)		# bracketing range

print('\nBisection Method')
r = bisection(f2, a, b, key = 'Q1_b')		# Bisection Method	
print('\nBisection root = ',r)

print('\n\nRegula Falsi Method')
r = falsi(f2, a, b, key = 'Q1_a')		# Regula Falsi Method
print('\nRegula Falsi root = ',r)

print('\n\nNewton Raphson Method')		# Newton Raphson Method
r = newton_raphson(f2, 0, key = "Q1_b")
print('\nNewton Raphson root = ',r)


## Qesttion 2 ##

print('\n\nQesttion 2:')


coiff =  [1, -3, -7, 27, -18]		# coeffiecients of polynomial given in Quetion 2

r = polysolver(coiff, 0)		# Synthetic division method  for finding roots of the polynomial with the given coefficients list
roots = [round(i) for i in r]		# rounding our result
print('\nThe roots are : ', roots)



###	OUTPUT ###


# Qesttion 1:

# (a):

# Bisection Method

# Iteration  Absolute error
# 0          0.5
# 1          0.25
# 2          0.125
# 3          0.0625
# 4          0.03125
# 5          0.015625
# 6          0.0078125
# 7          0.00390625
# 8          0.001953125
# 9          0.0009765625
# 10          0.00048828125
# 11          0.000244140625
# 12          0.0001220703125
# 13          6.103515625e-05
# 14          3.0517578125e-05
# 15          1.52587890625e-05
# 16          7.62939453125e-06
# 17          3.814697265625e-06
# 18          1.9073486328125e-06
# 19          9.5367431640625e-07

# Bisection root =  2.2191076278686523


# Regula Falsi Method

# Iteration  Absolute error
# 0          0.650690637448136
# 1          0.06358816982236615
# 2          0.004498957497641953
# 3          0.0003069684216292501
# 4          2.0890509801585466e-05
# 5          1.4214364827402903e-06
# 6          9.671651568510242e-08

# Regula Falsi root =  2.2191071418525734


# Newton Raphson Method

# Iteration  Absolute error
# 0          0.25868181812699165
# 1          0.015599378760597471
# 2          6.80282556468903e-05
# 3          1.2824501460784177e-09

# Newton Raphson root =  2.2191071489137464


# (b):

# Bisection Method

# Iteration  Absolute error
# 0          0.7853981633974483
# 1          0.39269908169872414
# 2          0.19634954084936207
# 3          0.09817477042468103
# 4          0.04908738521234046
# 5          0.024543692606170286
# 6          0.012271846303085199
# 7          0.006135923151542544
# 8          0.003067961575771272
# 9          0.0015339807878855805
# 10          0.0007669903939429012
# 11          0.0003834951969714506
# 12          0.0001917475984857253
# 13          9.587379924280715e-05
# 14          4.793689962134806e-05
# 15          2.396844981067403e-05
# 16          1.1984224905337015e-05
# 17          5.992112452668508e-06
# 18          2.996056226334254e-06
# 19          1.498028113222638e-06
# 20          7.490140566668302e-07

# Bisection root =  -0.7390858752647542


# Regula Falsi Method

# Iteration  Absolute error
# 0          1.4925049445839957
# 1          0.031653796217030905
# 2          0.00032131623225317707
# 3          3.207248694403475e-06
# 4          3.2007979156034594e-08

# Regula Falsi root =  -0.7390851328925051


# Newton Raphson Method

# Iteration  Absolute error
# 0          0.24963599045114615
# 1          0.011251034440497132
# 2          2.7758976825387194e-05
# 3          1.760065426736901e-10

# Newton Raphson root =  -0.7390851332151607


# Qesttion 2:

# The roots are :  [1, 2, 3, -3]
