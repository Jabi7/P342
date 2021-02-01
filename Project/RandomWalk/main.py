from math import *
import random
import matplotlib
import matplotlib.pyplot as plt
random.seed(1028)
#importing our random wal library
from randomWalk import *


# a)
N = [250, 500, 750, 1000, 1500]
RMS = []
SN = []

# func. to plot and print for each item in set N
def plotandprint(N):
    w, r, rms, av_x, av_y = rand_walk_set(N, 100)
    RMS.append(rms)
    SN.append(sqrt(N))

    # b)
    # plotting random walk for totel steps N
    fig = plt.figure()
    for i in range(5):
        a = fig.add_subplot()
        a.plot(w[i][0], w[i][1])
    plt.title('n = ' + str(N),
              fontsize=14, fontweight='bold')
    plt.show()
    fig.savefig(str(N) + ".pdf")

    # c)
    # printing the calculated results
    print("N = ", N)
    print("radial distance R = ", r)
    print("R.M.S =", rms)
    print("average displacement in the x = ", av_x)
    print("average displacement in the y = ", av_y)
    print('\n\n')

# calling plotandprint for each item in N
for i in N:
    plotandprint(i)

# d)
# plotting r.m.s vs root N
fig, ax = plt.subplots()
ax.plot(RMS, SN)
ax.set(xlabel='$\sqrt{N}$', ylabel='R.M.S', title='R.M.S vs $\sqrt{N}$')
ax.grid()
plt.show()
fig.savefig("R.M.S vs sqrt{N}.pdf")



###  output  ###

# N =  250
# radial distance R =  13.568082163347322
# R.M.S = 15.277404936374062
# average displacement in the x =  0.14267727880486314
# average displacement in the y =  -1.8799733079018548
#
# N =  500
# radial distance R =  18.58340527604839
# R.M.S = 20.814134980571566
# average displacement in the x =  -1.3631885612695078
# average displacement in the y =  -1.3719597678758295
#
# N =  750
# radial distance R =  22.796672872636535
# R.M.S = 25.637338046578307
# average displacement in the x =  -1.4527476956681953
# average displacement in the y =  2.7077605544787047
#
# N =  1000
# radial distance R =  26.33496120007577
# R.M.S = 29.8786493870571
# average displacement in the x =  -2.9029187321318375
# average displacement in the y =  -1.598860652433084
#
# N =  1500
# radial distance R =  34.760680642775
# R.M.S = 39.58062217433793
# average displacement in the x =  2.124834184258501
# average displacement in the y =  -0.0789879358660659