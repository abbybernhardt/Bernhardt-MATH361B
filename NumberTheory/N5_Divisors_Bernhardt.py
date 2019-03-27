#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:00:32 2019

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

mylist = divisors(500)
print('Here is a list of all proper divisors:', mylist)
