from functionlib import shooting_method

import matplotlib
import matplotlib.pyplot as plt
from math import log
e = 2.71828

dx = [0.02, 0.05, 0.25, 0.5]


# Q1, a

y1, x1 = [], []

dy  = lambda u, y, x : u
ddy = lambda u, y, x : u + 1

yn = 2*(e-1)

fig, ax = plt.subplots()
for i in range(4):
    print('For dx = ', dx[i])
    y, x = shooting_method(ddy, dy, 1, 0, yn, dx[i])
    y1.append(y)
    x1.append(x)
    ax.plot(x1[i], y1[i], dashes =[6-i, 2+i] , label ='dx = '+str(dx[i]))


ax.legend()
ax.set(xlabel='x', ylabel='y(x)', title='Q3. $d^2y/dx^2 = dy/dx + 1$')
ax.grid()
fig.savefig("Q3.pdf")

# OutPut

# For dx =  0.02
# Guess the 1st value of slope: 0.8
# Guess the 2nd value of slope: 1.3
# The obtained solution for z is : 0.9999978759077413
# For dx =  0.05
# Guess the 1st value of slope: 0.7
# Guess the 2nd value of slope: 1.5
# The obtained solution for z is : 0.9999980298267261
# For dx =  0.25
# Guess the 1st value of slope: 0.3
# Guess the 2nd value of slope: 1.7
# The obtained solution for z is : 0.4804108827345731
# For dx =  0.5
# Guess the 1st value of slope: 0.1
# Guess the 2nd value of slope: 1.8
# The obtained solution for z is : 0.1313984810448554
