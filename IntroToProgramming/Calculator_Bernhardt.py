#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:27:13 2019

@author: abigailbernhardt
"""

x = 1
y = 2
z = 3

mylist = [x+y,(y*z)+(3*x)]
mylist.append(mylist[0]**2)
mylist.append((2*mylist[1]-(x/2))/(mylist[0]))
mylist.append(7%3)

mylist[2] += 3
mylist[4] = mylist[4] * (3/4)

mysum = mylist[0] + mylist[1] + mylist[2] + mylist[3] + mylist[4]

print('The sum of all the values in my list is ', mysum)