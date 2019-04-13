#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:39:08 2019

@author: abigailbernhardt
"""
#%%
import numpy as np
import math as m 


N = 100
TOL = 1e-4
tol = 2
z0 = 1.5
process = 0
applied = np.zeros([0,2])


#fz = lambda x: 1/100 * ( x**4 + (np.exp(1)-2-np.sqrt(2))*x**3 + (2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*x**2 + (2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1))*x + 3*np.sqrt(2)*np.exp(1) )
#primefz = lambda x: 1/100 * ( 4*x**3 + 3*(np.exp(1)-2-np.sqrt(2))*x**2 + 2*(2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*x + (2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1)))

fz = lambda x: m.tan(x) - x - 2
primefz = lambda x: (1/m.cos(x))**2 - 1



while tol > TOL and process < N:
    z1 = z0 - (fz(z0) / primefz(z0))
    tol = abs(z1 - z0)
    process = +1
    applied = np.vstack([applied, np.array([z1,tol])])
    if tol < TOL:
        print('Stopped due to reaching tolerance.')
        break
    z0 = z1
    
if tol > TOL and process == N:
    print ('Stopped due to maximum number.')
 
print('Iterations and differences between them:', applied)
