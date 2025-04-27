# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:27:21 2025

@author: oener
"""

def tuple(n):
    tuple=()
    l=[]
    for i in range(1,n+1):
        tuple=(i,i**2,i**3)
        l.append(tuple)
    print(l)
n=int(input("Enter a number:"))
tuple(n)
        