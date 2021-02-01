## Library of relevant funtion ##

from math import *
import random
import matplotlib
import matplotlib.pyplot as plt
random.seed(1028)


# funtion for estimating volume of a 3D shape by monte carlo method
def monte_carlo_vol(shape, a, b, c, N):
    x, y, z = [], [], []    # cordinates inside the cuboid
    xs, ys, zs = [], [], [] # cordinates inside the volume of shape
    in_points = 0
    for i in range(N):
        x.append(random.uniform(-a, a))
        y.append(random.uniform(-b, b))
        z.append(random.uniform(-c, c))

        if shape(x[i], y[i], z[i], a, b, c) <= 0:
            in_points += 1
            xs.append(x[i])
            ys.append(y[i])
            zs.append(z[i])

    vol = 8 * a * b * c * in_points / N

    return vol, xs, ys, zs

# funtion for generating volume set for a set of step number and calculating fractional error
def volume_set(shape, a, b, c, N, av):
    vol, err = [], []
    for n in N:
        v, X, Y, Z = monte_carlo_vol(shape, a, b, c, n)
        vol.append(v)
        err.append(abs(av - v)/av)

    return vol, err