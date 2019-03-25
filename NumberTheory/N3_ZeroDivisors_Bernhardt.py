#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:34:56 2019

@author: abigailbernhardt
"""
#%%
inputnum = 10

zerodiv=[]
for ii in range(1,inputnum):
    for nn in range(1,inputnum):
        if (ii*nn)%inputnum==0:
           zerodiv.append(ii)
print(set(zerodiv), 'are all of the zero divisors')
print('There are' , len(set(zerodiv)), 'zero divisors total.')

