#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:59:24 2019

@author: abigailbernhardt
"""

#%%
Orgin = 8
CollNum = Orgin #number you change 
CollSeq = [CollNum]


Lim = 10000
Runs = 2

for ii in range (0, Lim-1):
    if CollNum % 2 ==0:
        CollNum = CollNum/2
    else:
        CollNum = (3*CollNum) + 1
#    CollSeq.append(CollNum)

    if CollNum ==1: 
        Runs +=1
        break
    
    else:
        Runs +=1
        
#print(CollSeq)
#print(len(CollSeq))
#print(Runs)
print("The starting number for this Collatz sequence is", Orgin,".")
if CollNum == 1:
    print("The Collatz sequence ended after", Runs, "terms.")
else: 
    print("The Collats failed within ", Lim,"terms.")