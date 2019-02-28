#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:45:24 2019

@author: abigailbernhardt
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

#lambda is one simple line of code 
f_n = lambda n: n**5+1
g_n = lambda n: n**4+n**2.0+1

def mainfunc():
    z = 40 #change these numbers
    b = 1 #change these numbers
    divlist = [1]
    bList = [1]
    for ii in range (1,z):
        divlist.append(((1+(f_n(ii)/(g_n(ii)))))*(divlist[ii-1]))
        bList.append((1+b**ii)*bList[ii-1])
        
    listx = np.linspace(1,len(divlist), len(divlist))
    
    print("The first 15 terms of the sequence are: \n ", divlist[:15])
    print()
    print("The last 15 terms of the sequence are: \n ", divlist[-15:])
    print()
    print("The first 15 terms of the sequence are: \n ", bList[:15])
    print()
    print("The last 15 terms of the sequence are: \n ", bList[-15:])  

mainfunc()