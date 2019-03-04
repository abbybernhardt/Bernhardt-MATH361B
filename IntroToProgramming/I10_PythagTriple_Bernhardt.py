#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:03:31 2019

@author: abigailbernhardt
"""
#%%
import numpy as np
import math
N = 1026

my_array = np.zeros([0,4])

for ii in range (290,310):
    for jj in range (ii, 310):
        c = math.sqrt(ii**2 + jj**2)
        if c.is_integer() == True:
            my_array = np.vstack([my_array, np.array([ii,jj,c,ii+jj+c])])
            break
print(my_array)



