#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:34:09 2019

@author: abigailbernhardt
"""
#%%

def divisors(n): 
    divisorlist = []
    ii = 1
    while ii < n: # proper divisor so not = to n
        if (n % ii==0): 
            divisorlist.append(ii)

        ii += 1
    return divisorlist


N = 1000
amicable = []

for ii in range (1,N):
    nn = sum(divisors(ii))
    
    if sum(divisors(nn)) == ii:

        iiVal = ii in amicable
        if iiVal == False: 
            amicable.append(ii)
        nnVal = nn in amicable
        if nnVal == False: 
            amicable.append(nn)
print(amicable, 'are all of the amicable numbers found in this code')
