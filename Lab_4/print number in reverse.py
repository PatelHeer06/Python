# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:56:55 2025

@author: oener
"""
n=int(input("Enter a number:"))
def reverse(n):
    for i in range(n,0,-1):
        print(i,end=' ')
reverse(n)