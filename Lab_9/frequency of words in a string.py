# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 11:45:50 2025

@author: oener
"""
def frequency(s):
    s1=sorted(s.split())
    print(s1)
    l=[]
    d={}
    for i in s1:
        if i not in l:
            l.append(i)
            c=s1.count(i)
            d.update({i:c})
    print(d)
s="Krissa Heer Krissa"
frequency(s)