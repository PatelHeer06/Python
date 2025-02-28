# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:52:15 2025

@author: oener
"""

a=input("Enter a string:")
d1={}
d2={}
for i in a:
    fre=a.count(i)
    d1={i:fre}
    d2={**d2,**d1}
print(d2)
