# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:52:27 2025

@author: oener
"""

def factorial():
    n=int(input("Enter a number:"))
    a=1
    for i in range(1,n+1):
        a=a*i
    print("Factorial is:",a)
factorial()
    