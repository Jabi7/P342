from functionlib import *
from math import *

# Q.3 
t = [round(i*0.3,2) for i in range(12) ]
# (i)
print('\n(i):')
v = [2.2, 1.96, 1.72, 1.53, 1.36, 1.22, 1.1, 1.0, 0.86, 0.75, 0.65, 0.6]
w, sigx, sigy, sigxy  = LSF(t, v, 2)
r1 = sigxy**2/(sigx*sigy)
print('\nW0 = ', w[0])
print('\nWc = ', w[1])
print('\nPearsons r = ', r1)
lv = [log(v[i]) for i in range(12) ]

## Plotting
y = [w[1]*t[i] + w[0] for i in range(len(t))]
fig = plt.figure()
plt.xlabel('time $N$')
plt.ylabel('angular velocity')
a1 = fig.add_subplot()
a1.scatter(t, v, label='data')
a2 = fig.add_subplot()
a2.plot(t, y, label='fitted data')
plt.legend()
fig.savefig("time vs. angular velocity.pdf")
plt.show()


# (ii)
print('\n(ii):')
lv = [log(v[i]) for i in range(12) ]
lw, lsigx, lsigy, lsigxy  = LSF(t, lv, 2)
r1 = lsigxy**2/(lsigx*lsigy)
print('\nW0 = ', lw[0])
print('\nWc = ', -lw[1])
print('\nPearsons r = ', r1)


## Plotting
y = [lw[1]*t[i] + lw[0] for i in range(len(t))]
fig = plt.figure()
plt.xlabel('time $N$')
plt.ylabel('log(angular velocity)')
a1 = fig.add_subplot()
a1.scatter(t, lv, label='data')
a2 = fig.add_subplot()
a2.plot(t, y, label='fitted data')
plt.legend()
fig.savefig("time vs. log(angular velocity).pdf")
plt.show()

## output ##

# (i):

# W0 =  2.0291025641025637

# Wc =  -0.4747086247086245

# Pearsons r =  1.100423417188293

# (ii):

# W0 =  0.7902775293458719

# Wc =  0.3955961745485566

# Pearsons r =  7.392606746388487