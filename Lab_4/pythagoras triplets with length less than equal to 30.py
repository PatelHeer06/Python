# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:40:52 2025

@author: oener
"""

def triplets():
    total=[]
    for a in range(1,31):
        for b in range(a,31):
            c=(a**2+b**2)**0.5
            if(c.is_integer() and c<=30):
                total.append((a,b,int(c)))
    print(total)
triplets()
        