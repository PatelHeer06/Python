# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 15:45:19 2025

@author: oener
"""

def factors(n,i=2):
    if n==1:
        return 0
    elif n%i==0:
        print(i)
        return factors(n//i,i)
    else:
        return factors(n,i+1)
n=int(input("Enter a number:"))
print("Prime Factors are:")
factors(n)
    
    
    
    