# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:43:00 2025

@author: oener
"""

l1=[1,2,3,4,5,6]
l2=[1,11,12,2,13,3]
l3=[i for i in l1 if i not in l2]
print(l3)

""""for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)"""
        