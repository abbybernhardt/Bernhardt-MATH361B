#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:20:58 2019

@author: abigailbernhardt
"""
#%%

N = 10 # represents number of units of black tiles, change this number 
red = 2
green = 3 
blue = 4

def tiles (NewColor, N): # NewColor = number of black tiles covered by a new color and N is total black tiles 
    number = [1] * NewColor + [0] * (N-NewColor+1) #number is the total number of ways which the NewColors block can cover N black coloured tiles
    
    
    for ii in range (NewColor, N+1):
        number[ii] += number[ii - 1] + number[ii - NewColor]
    return number[N] - 1

All = tiles (red, N) + tiles( green, N) + tiles (blue, N)

print ('There are', All , 'different ways to place all the colored tiles seperately on', N, 'blank squares.')
print ('Within the', All , 'different ways, there are', tiles(red, N), 'red tiles', tiles(green, N), 'green tiles', tiles(blue, N), 'blue tiles')
