# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:21:54 2025

@author: oener
"""
import random
ODD=[]
EVEN=[]
for i in range(0,5):
    a=random.randrange(1,100,2)
    ODD.append(a)
print("List of Odd numbers",ODD)
for i in range(0,4):
    b=random.randrange(0,100,2)
    EVEN.append(b)
print("List of Even numbers",EVEN)
c=2 
for i in EVEN:
    ODD.insert(c,i)
    c+=1   
print(ODD)