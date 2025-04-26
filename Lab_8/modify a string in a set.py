# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:33:21 2025

@author: oener
"""

s=set()
while(len(s)<5):
    a=input("Enter a string:")
    s.add(a)
print(s)
n=input("Enter a string which you want to delete")
if n in s:
    new=input("Enter a new string")
    s.remove(n)
    s.add(new)
else:
    print(n,"not in s")
print(s)