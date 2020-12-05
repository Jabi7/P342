from functionlib import exp_euler

import matplotlib
import matplotlib.pyplot as plt
from math import log
e = 2.71828

dx = [0.02, 0.05, 0.25, 0.5]


# Q1, a

y1, x1 = [], []

t1 = lambda y, x: y*log(y)/x

fig, ax = plt.subplots()
for i in range(4):
    y, x = exp_euler(t1, e, 2, dx[i])
    y1.append(y)
    x1.append(x)
    ax.plot(x1[i], y1[i], label ='dx = '+str(dx[i]))

ay = [e**(x1[0][i]/2) for i in range(len(x1[0]))]

ax.plot(x1[0], ay, dashes = [3,1], label = ' y =  $ e^{x/2}$ ')
ax.legend()
ax.set(xlabel='x', ylabel='y(x)', title='Q1. dy/dx = y*log(y)/x')
ax.grid()
fig.savefig("Q1.a.pdf")


# Q1, b

y2, x2 = [], []

t2 = lambda y, x: 6 - 2*y/x

fig, ax = plt.subplots()
for i in range(4):
    y, x = exp_euler(t2, 1, 3, dx[i], 5)
    y2.append(y)
    x2.append(x)
    ax.plot(x2[i], y2[i], label ='dx = '+str(dx[i]))

ay = [2*x2[0][i] - 45/(x2[0][i]**2) for i in range(len(x2[0]))]

ax.plot(x2[0], ay, dashes = [3,1], label = ' y =  $ 2x - 45/x^2$ ')
ax.legend()
ax.set(xlabel='x', ylabel='y(x)', title='Q1. dy/dx = 6 - 2*y/x')
ax.grid()
fig.savefig("Q1.b.pdf")
