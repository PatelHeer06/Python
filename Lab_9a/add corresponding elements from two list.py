# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 10:12:55 2025

@author: oener
"""

l1=[1,2,3,4,5,6]
l2=[6,5,4,3,2,1]
l=lambda a,b:a+b
m=map(l,l1,l2)
print(list(m))
