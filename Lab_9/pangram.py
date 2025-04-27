# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:20:23 2025

@author: oener
"""

def pangram(n):
    alpha={chr(i) for i in range(65,91)}
    a=set(n.upper())
    if alpha.issubset(a):
        print("Pangram")
    else:
        print("Not Pangram")
n=input("Enter a string:")
pangram(n)