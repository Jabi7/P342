# below command to run if matplotlib not installed
# !pip install matplotlib

import matplotlib
import matplotlib.pyplot as plt


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
    print("\nIteration  Absolute error")
    fl = open('bisection_for_'+key+'.txt', 'w+')
    fl.write('Iteration  Absolute error\n')
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
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='Iteration', ylabel='Absolute error', title='bisection_for_'+key)
    ax.grid()
    fig.savefig("bisection_for_"+key+".pdf")
    plt.show()
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
        p = lambda x : sum([coiff[len(coiff)-1-i]*x**i for i in reversed(range(len(coiff)))])   # genarating polynomial function using given coefficients list
        xi.append(Laguerre(p, coiff, al))
        coiff = deflation(p, coiff, xi[i])
        i+=1
    return xi
