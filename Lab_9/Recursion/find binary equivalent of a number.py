# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:33:11 2025

@author: oener
"""

def binary(n):
    if n==1:
        return '1'
    else:
        return binary(n//2)+str(n%2)
n=int(input("Enter a number"))
print("Binary equivalent of",n,"is",binary(n))