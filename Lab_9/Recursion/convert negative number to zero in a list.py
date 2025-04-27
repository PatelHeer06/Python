# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:37:59 2025

@author: oener
"""

def sanitize(l,l1,i):
    if len(l1)==len(l):
        return l1
    else:
        if l[i]>=0:
            l1.append(l[i])
        else:
            l1.append(0)
        return sanitize(l,l1,i+1)
l=[1,-1,2,0,-2,3,4]
l1=[]
print(l)
print(sanitize(l,l1,0))