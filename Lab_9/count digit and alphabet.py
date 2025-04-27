# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 11:16:23 2025

@author: oener
"""

def count_alpha_digits(s):
    countD=0
    countA=0
    for i in s:
        if(i.isalpha()):
            countA=countA+1
        elif(i.isdigit()):
             countD=countD+1
    d={"Digits":countD,"Alphabet":countA}
    print(d)
s=input("Enter a string containing digits:")
count_alpha_digits(s)