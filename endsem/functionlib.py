# below command to run if matplotlib not install
# !pip install matplotlib

import matplotlib
import matplotlib.pyplot as plt
import random as rn
from math import *


'''  THE FUNTION LIBRARY functionlib CONTAINING ALL THE FUNTIONS '''


#function to read the matrix from file

def read_matrix(m,fl):
	with open ( fl , 'r') as f:
		for line in f:
			m.append( [float(n) for n in line.split(' ')] )
	return m



#function to read the vector(the constants) from file

def read_vector(v,fl):
    f = open ( fl , 'r')
    b = (f.read().split(' '))
    for i in range(len(b)):
        v.append(float(b[i]))
    return v



#function for creating m x n Zero matrix

def zero_matrix(m,n):
    z =[]
    if n == 1:
    	for i in range(m):
            z.append(0)
    else:
    	for i in range(m):
        	z.append([0 for j in range(n)])
    return z



#function for genarating m x m Identity matrix

def Identity(m):
    z =[]
    
    for i in range(m):
        z.append([1 if i==j else 0 for j in range(m)])
    return z

#function for returning Transpose of matrix

def Transpose(m):
    mt = [[round(m[j][i],3) for j in range(len(m))] for i in range(len(m))]
    return mt



#function for Partial Pivot

def p_pivot(a,b,r):
    n = len(b)
    if a[r][r]==0:
        for r1 in range(r+1,n):
            if (abs(a[r1][r])>abs(a[r][r]) and abs(a[r][r])==0):
                a[r1] ,a[r] = a[r] ,a[r1]
                b[r1] ,b[r] = b[r], b[r1]
    return a,b



#function for Gauss Jordan

def gauss_jordan(a,b):
    n = len(b)
    for r in range(n):
        p_pvt(a,b,r)
        pvt = a[r][r]
        for c in range(r,n):
            a[r][c] /= pvt
        b[r] /= pvt
        
        for r1 in range(n):
            if r1 == r or a[r1][r] == 0:
                continue
            else:
                fctr = a[r1][r]
                for c in range(r,n):
                    a[r1][c] = a[r1][c] - fctr*a[r][c]
                b[r1] -= fctr*b[r]	
                
    
    return b




#function for matrix Multiplication 

def matrix_mult(m,n):
    mn = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                mn[i][j] += m[i][k]*n[k][j] 
    return mn



def bracket_root(f,a,b, beta = 1.5):
    
    for i in range(12):
        if f(a)*f(b)>0:
            if abs(f(a)) < abs(f(b)):
                a = a - beta * (b - a)
            else:
                b = b + beta * (b - a)
    if f(a)*f(b)>0:
        print('Try different range')
    return a,b   
    
# FUNCTION FOR LU DECOMPOSITION
def LU_decomp(m,b):
    for j in range(len(m)):
        p_pivot(m,b,j)					#calling partial pivot function from funtionlib
        for i in range(len(m)):

            if i <= j:
                s = 0
                for k in range(i): 
                    s += m[i][k]*m[k][j]
                m[i][j] = m[i][j] - s
            if i>j:
                s = 0
                for k in range(j):
                    s += m[i][k]*m[k][j]
                m[i][j] = 1/m[j][j] * (m[i][j] - s)
    return m

# FUNCTION FOR FORWARD SUBSTITUTION
def for_sub(m,b):
    y = zero_matrix(len(m),1)
    for i in range(len(m)):
        s = 0
        for j in range(i): 
            s += m[i][j]*y[j]
        y[i] += b[i] - s  
    return y

# FUNCTION FOR BACKWARD SUBSTITUTION
def back_sub(m,b):
    x = zero_matrix(len(m),1)
    for i in reversed(range(len(m))):
        s = 0
        for j in reversed(range(len(m))): 
            if i<j:
                s += m[i][j]*x[j]
        x[i] += 1/m[i][i] * (b[i] - s)  
    return x


### ASSIGNMENT 5 ###


# fuction to find derivative of f(x)

def der(f, x, h = 10**-10):
    return ((f(x + h) - f(x - h))/(2*h))


# fuction to find 2nd derivative of f(x)

def double_der(f, x, h = 10**-6):
    return ((f(x + h) - 2*f(x) + f(x - h))/(2*h*h))



# Bisection method for finding root of f(x)

def bisection(f, a, b, epsilon = 10**-6, key = "0"):
    i = 0
    e = abs(a-b)
    x, y = [], []
#     print("\nIteration  Absolute error")
#     fl = open('bisection_for_'+key+'.txt', 'w+')
#     fl.write('Iteration  Absolute error\n')
    while(e>epsilon and i<100):
        c = (a+b)/2
        if f(a)*f(c) < 0:
            e = abs(b-c)
            b = c
        else:
            e = abs(a-c)
            a = c
        fl.write(str(i)+'          '+str(e)+'\n')
        x.append(i)
        y.append(abs(b-a))
        print(i,'        ', e)
        i +=1
#     fig, ax = plt.subplots()
#     ax.plot(x, y)
#     ax.set(xlabel='Iteration', ylabel='Absolute error', title='bisection_for_'+key)
#     ax.grid()
#     fig.savefig("bisection_for_"+key+".pdf")
#     plt.show()
    return c



# Regula Falsi method for finding root of f(x)

def falsi(f, a, b, epsilon = 10**-6, key = "0"):
	    i = 0
	    x, y, e = [], [], abs(a-b)
	    fl = open('Regula_Falsi_for_'+key+'.txt', 'w+')
	    fl.write('Iteration  Absolute error\n')
	    print("\nIteration  Absolute error")
	   
	    while(e>=epsilon):
	        
	        c = b - ((b-a)*f(b))/(f(b) - f(a))
	        
	        if f(a)*f(c) < 0:
	            e = abs(b-c)
	            b = c
	        else:
	            e = abs(a-c)
	            a = c
	        fl.write(str(i)+'          '+str(e)+'\n')
	        x.append(i)
	        y.append(e)
	        print(i,'        ',e)
	        i +=1
	    fl.close()
	    fig, ax = plt.subplots()
	    ax.plot(x, y)
	    ax.set(xlabel='Iteration', ylabel='Absolute error', title='Regula Falsi_for_'+key)
	    ax.grid()
	    fig.savefig("Regula Falsi_for_"+key+".pdf")
	    plt.show()
	    return c



# Newton Raphson method for finding root of f(x)

def newton_raphson(f, x0, epsilon = 10**-6, key = "0"):
    
    xn, i, x, y, ec = x0 - f(x0)/der(f, x0) , 0, [], [], True
    fl = open('Newton_Raphson_for_'+key+'.txt', 'w+')
    fl.write('Iteration  Absolute error\n')
    print("\nIteration  Absolute error")
    while(ec):
        l = xn
        xn = l - f(l)/der(f, l)
        e = abs(l - xn)
        ec = e >= epsilon
         
        fl.write(str(i)+'          '+str(e)+'\n')
        x.append(i)
        y.append(e)
        print(i,'        ',e)
        i +=1
    fl.close()
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='Iteration', ylabel='Absolute error', title='Newton_Raphson_for_'+key)
    ax.grid()
    fig.savefig("Newton_Raphson_for_"+key+".pdf")
    plt.show()
    return xn


# Laguerre's method for finding one root of polynomial p(x)

def Laguerre(p, coiff, al, epsilon = 10**-6):
    
    if p(al) == 0: 
        return al
    else:
        n, e = len(coiff)-1, True

        while(e):
            al0 = al
            g = der(p, al)/p(al)
            h = g*g - double_der(p, al)/p(al)
            d1 = g + ((n - 1)*(n*h - g*g))**(1/2)
            d2 = g - ((n - 1)*(n*h - g*g))**(1/2)
            
            a = n/d1 if abs(d1) > abs(d2) else n/d2
            al -= a
            e = abs(al - al0) >= epsilon
        return al   


# Deflation method for reducing the degree of polynomial p(x)

def deflation(p, coiff, xi):
    nc = [coiff[0]]
    for i in range(len(coiff)-1):
        nc.append(coiff[i+1]+nc[i]*xi)
    nc.pop(len(coiff)-1)
    return nc



# Synthetic division method  for finding roots of a polynomial with given coefficients list

def polysolver(coiff, al):
    
    xi, i = [], 0
    while(len(coiff)>1):
        p = lambda x : sum([coiff[len(coiff)-1-i]*x**i for i in reversed(range(len(coiff)))])	# genarating polynomial function using given coefficients list
        xi.append(Laguerre(p, coiff, al))
        coiff = deflation(p, coiff, xi[i])
        i+=1
    return xi



    ################################################################
                    ##### ASSIGNMENT 6 #####


# Midpoint Integration method

def midpoint_integrate(f, lims, N):
    
    a, b = lims
    h = (b - a)/N
    s = 0
    for i in range(N):
        x = (a + i*h + a + (i+1)*h)/2
        s += h*f(x)
    return s


# Trapezoidal Integration method

def trapezoidal_integrate(f, lims, N):
    
    a, b = lims
    h = (b - a)/N
    s = 0
    for i in range(N+1):
        x = a + i*h
        s += h*f(x)/2 if i == (0 or N) else  h*f(x) 
    return s


# Simpson's Integration method

def simpson_integrate(f, lims, N):
    
    a, b = lims
    h = (b - a)/N
    s = 0
    for i in range(N+1):
        x = a + i*h
        s += (h*f(x) if i == (0 or N) else  (4*h*f(x) if i%2 == 0 else 2*h*f(x) ))/3 
    return s


# Monte Carlo method

def monte_carlo(f,lims, N):
    a, b = lims
    x, s1, s2 = [], 0, 0
    for i in range(N):
        x.append(rn.uniform(a,b))
        s1 += f(x[i])
        s2 += f(x[i])**2
    F = (b - a)*s1/N
    sig = s2/N - (s1/N)**2
    return F, sig
    
    
    ################################################################
                    ##### ASSIGNMENT 7 #####    
    

def exp_euler(t, y0, x0, h = 0.05, n = 20):
    
    Y, X = [y0], [x0]

    x, y= x0, y0
    while x < n:
        y += t(y, x) * h
        x += h
        Y.append(y)
        X.append(x)
    return Y, X
    

def RK4(ddy, dy, u, y, x, h=0.05, n = 5, axis = 'x'):
    Y, X = [y], [x]
    
    while(abs(y) <= n if axis == 'y' else abs(x) <= n):
        k1 = h * dy(u, y, x)
        l1 = h * ddy(u, y, x)
        
        k2 = h * dy(u + l1/2, y + k1/2, x + h/2)
        l2 = h * ddy(u + l1/2, y + k1/2, x + h/2)
        
        k3 = h * dy(u + l2/2, y + k2/2, x + h/2)
        l3 = h * ddy(u + l2/2, y + k2/2, x + h/2)
        
        k4 = h * dy(u + l3, y + k3, x + h)
        l4 = h * ddy(u + l3, y + k3, x + h)
        
        u += (l1 + 2*l2 + 2*l3 + l4)/6
        y += (k1 + 2*k2 + 2*k3 + k4)/6
        x += h
        X.append(x)
        Y.append(y)
    return Y, X 
    
   
def shooting_method(ddy, dy, y0,x0, yn, h, tol = 0.01):
    
    # estimation
    flag = True
    while flag:
        zl = float(input("Guess the 1st value of slope: "))
        zh = float(input("Guess the 2nd value of slope: "))
        y1, x1 = RK4(ddy, dy, zl, y0, x0, h, 1)
        y2, x2 = RK4(ddy, dy, zh, y0, x0, h, 1)
        if (y2[-1]>yn and y1[-1]>yn) or (y2[-1]<yn and y1[-1]<yn):
            print("\nPlease try another set")
            
        else:
            flag = False
            
    flag = True
    while flag:
        
        if abs(y1[-1]-yn) < tol:
            print("The solution for z is :", zl)
            return y1,x1
            flag = False
        if abs(y2[-1]-yn) < tol:
            print("The solution for z is :", zh)
            return y2,x2
            flag = False
        
        if y1[-1]>yn and y2[-1]<yn:
            z = zh + (zl-zh)/(y1[-1]-y2[-1])*(yn - y2[-1])
            y, x = RK4(ddy, dy, z, y0, x0, h, 1)
            if abs(y[-1]-yn) < tol:
                print("The obtained solution for z is :", z)
                return y, x
                flag = False
            elif z<yn:
                zh=z
            else:
                zl=z
        
        if y2[-1]>yn and y1[-1]<yn:
            z = zl + (zh-zl)/(y2[-1]-y1[-1])*(yn - y1[-1])
            y,x = RK4(ddy, dy, z, y0, x0, h, 1)
            if abs(y[-1]-yn) < tol:
                print("The obtained solution for z is :",z)
                return y, x
                flag = False
            elif z<yn:
                zl=z
            else:
                zh=z 
    
##### Least squar fitting   #####

def ksum(x, k):
    s = 0
    for i in range(len(x)):
        s += x[i]**k
    return s

def xkysum(x, y ,k):
    s = 0
    for i in range(len(x)):
        s += y[i]*(x[i]**k)
    return s

# Leniar equation solver
def LES(m, b):
    LU_decomp(m,b)
    y = for_sub(m,b)     
    x = back_sub(m,y)
    return x

# general least squar fitting for polynomial funtion
def LSF(x, y, k):
    n = len(x)
    m = [[ksum(x, j+i) for j in range(k)] for i in range(k)]
    b = [xkysum(x, y, j) for j in range(k)]
    c = LES(m, b)
    if k ==2:
        Sxx= ksum(x, 2) - ksum(x, 1)**2
        Syy= ksum(y, 2) - ksum(y, 1)**2
        Sxy= xkysum(x, y, 1) - ksum(x, 1)*ksum(y, 1)
        sigx = Sxx/n
        sigy = Syy/n
        sigxy = Sxy/n
        return c, sigx, sigy, sigxy
    else:
        return c    