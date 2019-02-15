#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:35:58 2019

@author: abigailbernhardt
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

# the last number in coordinate indicated the number inbetween. This is how many points will be graphed. 
xval = np.linspace(-3, 3, 20)


def f(x):
    mypoints=[]
    for n in x:
        if (n<-2):
            mypoints.append(-3*((n+2)**2)+1)
        elif (n>=-2 and n<-1):
            mypoints.append(1)
        elif (n>=-1 and n<=1):
            mypoints.append(((n-1)**3)+3)
        elif (n>1 and n<2):
            mypoints.append(np.sin(n*np.pi)+3)
        else:
            mypoints.append(3*np.sqrt(n-2)+4)
    return mypoints


plt.scatter(xval, f(xval))