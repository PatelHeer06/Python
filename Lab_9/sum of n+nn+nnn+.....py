# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:01:10 2025

@author: oener
"""

def sum(n):
    sum=n
    check=n
    for i in range(1,n):
        check=check*10+n
        sum=sum+check
    print(sum)
n=int(input("Enter a number:"))
sum(n)