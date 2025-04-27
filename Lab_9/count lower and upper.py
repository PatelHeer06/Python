# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 14:48:52 2025

@author: oener
"""

def count_lower_upper(n):
    countL=0
    countU=0
    d={}
    for i in n:
        if(i>='a' and i<='z'):
            countL+=1
        elif(i>='A' and i<='Z'):
            countU+=1
    d={'Lower':countL,'Upper':countU}
    print(d)
n=input("Enter a string:")
count_lower_upper(n)
