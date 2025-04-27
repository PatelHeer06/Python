# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:29:31 2025

@author: oener
"""

def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
a=int(input("Enter base:"))
b=int(input("Enter power"))
print(a,"power",b,"is",power(a,b))