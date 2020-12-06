from functionlib import RK4

import matplotlib
import matplotlib.pyplot as plt
from math import log
e = 2.71828

dy  = lambda u, y, x : u
ddy = lambda u, y, x : 1 - x - u


# Q2, a
# for x in range[-5, 5]

fig, ax = plt.subplots()

y1, x1 = RK4(ddy, dy, 1, 2, 0, -0.02)
y1.reverse()
x1.reverse()
y2, x2 = RK4(ddy, dy, 1, 2, 0, 0.02)
x = x1 + x2
y = y1 + y2
ax.plot(x, y, label = 'numerical')

ay = [1 + e**(-x[i]) - x[i]**2/2 + 2*x[i] for i in range(len(x))]

ax.plot(x, ay, dashes = [3,2], label = ' y =  $1 + e^{-x} - x^2/2 + 2x $ ')
ax.legend()
ax.set(xlabel='x', ylabel='y(x)', title='Q2.a $d^2y/dx^2 + dy/dx  = 1 - x$')
ax.grid()
fig.savefig("Q2.a.pdf")


# Q2, b
# for y in range[-5, 5]

fig, ax = plt.subplots()

y1, x1 = RK4(ddy, dy, 1, 2, 0, -0.02, axis = 'y')
y1.reverse()
x1.reverse()
y2, x2 = RK4(ddy, dy, 1, 2, 0, 0.02, axis = 'y')
x = x1 + x2
y = y1 + y2
ax.plot(x, y, label = 'numerical')

ay = [1 + e**(-x[i]) - x[i]**2/2 + 2*x[i] for i in range(len(x))]

ax.plot(x, ay, dashes = [3,2], label = ' y =  $1 + e^{-x} - x^2/2 + 2x $ ')
ax.legend()
ax.set(xlabel='x', ylabel='y(x)', title='Q2.b $d^2y/dx^2 + dy/dx  = 1 - x$')
ax.grid()
fig.savefig("Q2.b.pdf")
