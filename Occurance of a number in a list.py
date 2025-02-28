# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:11:01 2025

@author: oener
"""

import random
l=[]
for i in range(0,20):
    a=random.randrange(1,100)
    l.append(a)
print(l)
n=int(input("Enter a number whose index is needed:"))
for i,j in enumerate(l):
    if (j==n):
        print("Index is",i)