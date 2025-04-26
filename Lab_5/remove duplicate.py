# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:21:28 2025

@author: oener
"""

import random
l=[]
l2=[]
for i in range(0,50):
    a=random.randrange(1,30)
    l.append(a)
print(l)
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
