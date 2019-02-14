#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 23:12:20 2019

@author: abigailbernhardt
"""
#%%
my_list=[]
F0=int(input("First term "))
F1=int(input("Second term "))
N=int(input("How many terms? "))
my_list.append(F0)
my_list.append(F1)
#I'm still not completely sure I understand what Rosie was talking about when she was explaining the placeholder to me and helping me work out this problem in class. 
placeholder=0

# Need to start at 2 because 1 would give 0
for nn in range(2,N):
    my_list.append(my_list[nn-1]+my_list[nn-2])
for terms in range(1,N-1):
    if (((my_list[terms]**2)-(my_list[terms-1])*(my_list[terms+1]))==((-1)**(nn-1))):
        placeholder=1
if placeholder==1:
#true if identity applies
    print("True")
else:
#false if identity does not apply
    print("Fasle")

print("Here are the last 10 terms  ",my_list[-10:N])