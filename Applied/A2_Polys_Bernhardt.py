#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:01:50 2019

@author: abigailbernhardt
"""
p = [2,4,0,-6] # 2 is the coefficent that represents the lowest exponential

a = 0
b = 10
c = 2 

def polynomial (p,point):
    answer = 0
    for i in range (len(p)):
        answer = answer + (p[i]*point**i)
    return answer


def prettyprint(p):
    values = ''
    for i in range(len(p)):
        if i == 0:
            values = values + '+(' + str(p[i]) + ')'
        elif p[i] == 0:
            values = values
        else:
            values = values+ '+(' + str(p[i]) + 'x^' + str(i) + ')'
    return values




def deriv(p):
    derivative = []
    for i in range(1,len(p)):
            derivative.append(p[i]*i)
    return derivative




def integrate(p,x,y): 
    integral = []
    integral.append(0)
    for i in range(len(p)):
            integral.append((p[i]/(i+1)))
    return polynomial(integral, y) - polynomial(integral, x)


print('The original polynoimal is f(x) =',prettyprint(p))
print('This function was evaluated at f(' + str(c) + '), which equals: '+ str(polynomial(p,c)))
print('The derivative of this function is f`(' + str(c) + ') = ' + str(polynomial(deriv(p),c)))
print('The integral of this fucntion f(x) from '+str(a)+ ' to ' + str(b) + ' equals: ' + str(integrate(p,a,b)))
