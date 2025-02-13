# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:12:50 2025

@author: oener
"""

def fibo():
    n=int(input("Enter a number:"))
    a=1
    b=1
    for i in range(0,n+1):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
fibo()
        