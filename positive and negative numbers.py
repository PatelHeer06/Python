# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:31:10 2025

@author: oener
"""

import random
l=[]
positive=[]
negative=[]
for i in range(0,30):
    a=random.randrange(-100,100)
    l.append(a)
print(l)
for i in l:
    if(i>=0):
        positive.append(i)
    else:
        negative.append(i)
print("List of positive number is:",positive)
print("List of negative number is:",negative)
    