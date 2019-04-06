#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:09:46 2019

@author: abigailbernhardt
"""
#%%
import numpy as np

residues = np.zeros([0,2])
minus1 = np.zeros ([0,2])
P = 15

def prime_check (N):

    if N == 1:
        return False
    
    for nn in range(2,N):
        if N % nn == 0:
            return False #false indicates composite 
            break 
    else:
            return True
            
        
primelist=[]



for pp in range (2, P+1):
    if prime_check(pp) == True:
         primelist.append(pp)
        
    
    
    

for p in primelist:
    number = []
    for ii in range(0,p):
        for d in range(0,ii+1):
            if ii==(d**2)%p:
                i = ii in number
                if i == False:
                    number.append(ii)
                dd = d in number
                if dd == False:
                    number.append(d)
               
                
    residues = np.vstack( [residues, np.array( [p,len(number)] )] )
print("Below are lists of the quadratic residues.")
print(residues)





for p in primelist:
    quadratic = "False"
    for ii in range(0,p):
        if (p-1)==(ii**2)%p:
            quadratic = "True"
         
    minus1 = np.vstack( [minus1, np.array([p, quadratic])])

print("Below are lists of -1 when a quadratic residue.")
print(minus1)        