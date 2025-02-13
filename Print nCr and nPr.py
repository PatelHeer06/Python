# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:30:54 2025

@author: oener
"""

def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
def nCr(n,r):
    ncr=factorial(n)/(factorial(r)*factorial(n-r))
    print("nCr:",ncr)
def nPr(n,r):
    npr=factorial(n)/factorial(n-r)
    print("nPr:",npr)
n=int(input("Enter n:"))
r=int(input("Enter r:"))
nCr(n,r)
nPr(n,r)
    