import matplotlib
import matplotlib.pyplot as plt
from math import *
from functionlib import *


# Q.2
print('Q.2\n')

f2 = lambda x : x/(1+x)
lims = (1, 3)
N = [5, 10, 25]
a = 1.306852 # Analytical result

print('Midpoint Method:')
print('N','    Integral','             Absolute error')
for i in list(N):
    I = midpoint_integrate(f2,lims,i)
    print(i, '   ', I, '   ', abs(I-a))


print('\n\nTrapezoid method:')
print('N','    Integral','             Absolute error')
for i in list(N):
    I = trapezoidal_integrate(f2,lims,i)
    print(i, '   ', I, '   ', abs(I-a))    

    
print('\n\nSimpson method:')
print('N','    Integral','             Absolute error')
for i in list(N):
    I = simpson_integrate(f2,lims,i)
    print(i, '   ', I, '   ', abs(I-a))  



# Q.3
print('\n\nQ.3\n')

f3 = lambda x: exp(-x**2)
e = 0.001
a, b = lims = (0, 1)

# |f3''(0)| = 2, and |f3''''(0)| = 12
Nm = ceil(((b-a)**3/(24*e**2)*2)**0.5)
Nt = ceil(((b-a)**3/(12*e**2)*2)**0.5)
Ns = ceil(((b-a)**5/(180*e**4)*12)**0.25)

m = midpoint_integrate(f3, lims, Nm)
t = trapezoidal_integrate(f3, lims, Nt)
s = simpson_integrate(f3, lims, Ns)

print('Result by Midpoint Method =', m)
print('Result by Trapezoidal Method =', t)
print('Result by Simpson Method =', s)



# Q.4
print('\n\nQ.4\n')

f4 = lambda x : 4/(1+x**2)
lims = (0, 1)
n, Fn, N, sig = 10, [], [], []

while(n <= 20000):
    F , sigma =monte_carlo(f4, lims, n)
    Fn.append(F)
    N.append(n)
    sig.append(sigma)
    n +=10
print('Value of pi after 20000 iterations = ', F)
print('final sigma = ', sigma)
fig, ax = plt.subplots()
ax.plot(N, Fn)
ax.set(xlabel='N', ylabel='Pi', title='monte_carlo_plot(N vs Pi)')
ax.grid()
fig.savefig("monte_carlo_plot(N vs Pi).pdf")
fig, ax = plt.subplots()
ax.plot(N, sig)
ax.set(xlabel='N', ylabel='Sigmaf^2', title='monte_carlo_plot(N vs Sigmaf)')
ax.grid()
fig.savefig("monte_carlo_plot(N vs Sigmaf).pdf")
plt.show()


##########################################################
					## OUTPUT ##

# Q.2

# Midpoint Method:
# N     Integral              Absolute error
# 5     1.308092114284065     0.0012401142840650081
# 10     1.3071646395900398     0.00031263959003990927
# 25     1.3069028019555275     5.0801955527646214e-05


# Trapezoid method:
# N     Integral              Absolute error
# 5     1.4043650793650793     0.09751307936507936
# 10     1.3562285968245722     0.049376596824572294
# 25     1.326752839424082     0.01990083942408205


# Simpson method:
# N     Integral              Absolute error
# 5     1.433597883597884     0.12674588359788408
# 10     1.3222740910047412     0.015422091004741345
# 25     1.3332529524130519     0.02640095241305196


# Q.3

# Result by Midpoint Method = 0.7468244998655219
# Result by Trapezoidal Method = 0.7480462601714666
# Result by Simpson Method = 0.748133890507375


# Q.4

# Value of pi after 20000 iterations =  3.1433193983889267
# final sigma =  0.41728098713362805
