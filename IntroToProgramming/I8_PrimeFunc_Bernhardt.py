#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:59:10 2019

@author: abigailbernhardt
"""
#%%
def prime_check (N):

    if N == 1:
        return False
    
    for nn in range(2,N):
        if N % nn == 0:
            return False #false indicates composite 
            break 
    else:
            return True
            
primelist=[]
numofprime=100 #checking 5 numbers
check=2 #is the first number

while len(primelist) < numofprime:
    prime = False
    while prime == False:
        prime=prime_check(check)
        check += 1
    
    primelist.append(check -1)

prime_check(N)

print("The {}th prime number is: {}".format(numofprime,primelist[-1]))