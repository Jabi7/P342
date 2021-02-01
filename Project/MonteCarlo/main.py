from math import *
import random
import matplotlib
import matplotlib.pyplot as plt
random.seed(1028)
from mpl_toolkits import mplot3d
from MCvolume import *


# a)

# ellipsoid funtion
ellipsoid = lambda x, y, z, a, b, c: x**2/a**2 + y**2/b**2 + z**2/c**2 - 1
# analytical Volume
a_vol = lambda a, b, c: 4*pi*a*b*c/3

# given parameters
a, b, c = 1, 1.5, 2
av = a_vol(a, b, c)

N = [n for n in range(100, 50000, 500)]

# call for ~100 trials
vol, err = volume_set(ellipsoid, a, b, c, N, av)

# b)

# plotting for volume for each N to compare with analytical volume
fig = plt.figure()
plt.xlabel('step numbers $N$')
plt.ylabel('volume of ellipsoid $V$')
a1 = fig.add_subplot()
a1.plot(N, vol, label='Estimated volume')
a2 = fig.add_subplot()
a2.plot([0, N[-1]], [av, av], label='Analytical volume = 12.566 units$^3$')
plt.legend()
fig.savefig("Volume vs. step numbers.pdf")
plt.show()


# c)

# plotting for frac error
fig, ax = plt.subplots()
ax.plot(N, err)
ax.set(xlabel='step numbers $N$', ylabel='fractional error', title='fractional error vs. step numbers.')
ax.grid()
fig.savefig("fractional error vs. step numbers.pdf")
plt.show()

# d)

# plotting 3-D plot of the ellipsoid Monte Carlo data for N = 10000
v, X, Y, Z = monte_carlo_vol(ellipsoid, a, b, c, 10000)

fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection='3d')
ax.scatter(X, Y, Z,s=1, c=Y, cmap='viridis', linewidth=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3-D plot of the ellipsoid Monte Carlo data for N = 10000")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
ax.view_init(19, 54)
fig.savefig("3-D plot of the ellipsoid Monte Carlo data for N = 10000.pdf")
plt.show()