# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 10:20:18 2025

@author: oener
"""

import random
l=[]
for i in range(0,10):
    l.append(random.randint(-15,15))
print(l)
square=lambda x:x**2
m=map(square,l)
print(list(m))