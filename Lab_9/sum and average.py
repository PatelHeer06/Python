# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:13:43 2025

@author: oener
"""

def sum_avg(a,b,c,d,e):
    sum=a+b+c+d+e
    avg=sum/5
    return sum,avg
a=int(input("Enter marks 1:"))
b=int(input("Enter marks 2:"))
c=int(input("Enter marks 3:"))
d=int(input("Enter marks 4:"))
e=int(input("Enter marks 5:"))
print(sum_avg(a,b,c,d,e))