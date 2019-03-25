#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:37:24 2019

@author: abigailbernhardt
"""
#%%
inputnum = 25

inv=[]
for ii in range(0,inputnum):
    for nn in range(0,inputnum):
        if (ii*nn)%inputnum==1:
            inv.append(ii)
print(inv, 'are all the elements that have a multiplicative inverse.')
print('There are', len(inv), 'such elements.')