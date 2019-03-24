#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:17:29 2019

@author: abigailbernhardt
"""

#%%

import math 
import numpy as np
number = 5
primenumbers = []

def prime_check (N): #this code came from I8

    if N == 1:
        return False
    
    for nn in range(2, math.floor(np.sqrt(N))+1):
        if N % nn == 0:
            return False #false indicates composite 
            break 
    else:
            return True
            
while True:
    if prime_check(number):
        primenumbers.append(number)
    else:
        for ii in primenumbers:
            x = np.sqrt(((number-ii)/2))
            if x.is_integer() == True:
                break
        else:
            print(number, "is the first odd composite number for which this conjecture does not hold true.")
            break
    number += 2