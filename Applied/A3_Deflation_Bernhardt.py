#%%
import numpy as np 

f = [3,4,5,6] 
g = [2,1] 

def poly(f,g):
    q = [0]
    r = f
    while r != 0 and len(g) <= len(r):
        nn = divide(r,g)
        q = addition(q,nn)
        rnn = multiply(g,nn)
        r = subtraction(r,rnn)
        clean_poly(r)
    return q,r


def clean_poly(p):
    highest_deg = len(p) - 1   
    for ii in range(len(p)-1,-1,-1):
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1
    
    
    del p[highest_deg+1:]
    
    
    return p


def multiply(r, N):
    mult = [0]*(len(r)+len(N)-1)
    last = N[-1]
    for ii in range(len(r)):
        index = ii + len(N)-1
        mult[index] = last*r[ii]
    return mult


def divide(x1,x2):
    N = (x1[-1]/x2[-1])
    deg = (len(x1)-len(x2))
    div = [0]*(deg + 1)
    div[deg] = N
    return div


def subtraction(r,g):
    if len(r) > len(g):
        sub = list(r)
        for ii in range(len(g)):
            sub[ii] = r[ii]-g[ii]
    else:
        sub = [0]*len(g)
        for ii in range(len(r)):
            sub[ii] = r[ii]-g[ii]
        for jj in range(len(r),len(g)):
            sub[jj] = 0-g[jj]
    return sub


def addition(x1,x2):
    if len(x1) > len(x2):
        add = list(x1)
        for ii in range(len(x2)):
            add[ii] = x1[ii]+x2[ii]
    else:
        add = list(x2)
        for jj in range(len(x1)):
            add[jj] = x1[jj]+x2[jj]
    return add




print('f = ', f)
print('g = ', g)
print('q = ', q)
print('r = ', r)

#%%