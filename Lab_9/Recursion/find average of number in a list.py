# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:36:04 2025

@author: oener
"""

def sum(l,i):
    if i==len(l):
        return 0
    else:
        s=l[i]+sum(l,i+1)
        return s
l=[1,2,3,4,5]
print("Average:",(sum(l,0))/len(l))
    