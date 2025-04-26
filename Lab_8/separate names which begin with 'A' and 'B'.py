# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:39:12 2025

@author: oener
"""

s=("Aryan","Bob","Arti","Bhavya","Bhumi","Ashika")
a=set()
b=set()
for i in s:
    if i.startswith('A'):
        a.add(i)
    else:
        b.add(i)
print(a)
print(b)
    