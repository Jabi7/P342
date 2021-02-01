## Library of relevant funtion ##

from math import *
import random
import matplotlib
import matplotlib.pyplot as plt
random.seed(1028)

# funtion for generating the set of coordinates in random walk
def rand_walk(N):
    x, y = [0], [0]
    for i in range(N):
        x.append(x[i] + cos(2*pi*random.random()))
        y.append(y[i] + sin(2*pi*random.random()))
    return x,y

# funtion for generating set of walks for given total steps n
def rand_walk_set(N, n):
    walks = []
    r = 0  # radial distance
    rs = 0  # for r.m.s
    av_x, av_y = 0, 0  # average displacement

    for i in range(n):
        x, y = rand_walk(N)
        walks.append([x, y])
        xf, yf = x[-1], y[-1]  # final position
        r += sqrt(xf ** 2 + yf ** 2) / n
        rs += xf ** 2 + yf ** 2
        av_x += xf / n
        av_y += yf / n
    rms = sqrt(rs / n)
    return walks, r, rms, av_x, av_y
