# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:42:06 2025

@author: oener
"""

def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
def sinx(x,terms):
    result=0
    for i in range(0,terms):
        sign=i**(2*(i+1))
        result=result+sign*(x**(2*(i+1)))/factorial(2*(i+1))
    print(result)
x=float(input("Enter radians:"))
terms=int(input("Enter total terms:"))
sinx(x,terms)