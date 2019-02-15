#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:06:01 2019

@author: abigailbernhardt
"""
#%%
f0=0
f1=1
N=10000
m=2
multiples=[]

fibseq=[f0,f1]

for i in range (N-2):
    fibseq.append(fibseq[-1]+fibseq[-2])


for ii in (fibseq):
    if ii%m==0:
        multiples.append(ii)
print('Number of terms divisible by m ' , len(multiples))
#print((multiples))

percentage= len(multiples)/N
print(percentage*100)

#%% this is the code for the conjecture
for k in range(len(fibseq)):
    if fibseq[k]%m==0:
        print(k)
#every third number is even