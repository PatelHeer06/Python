# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:16:01 2025

@author: oener
"""

n=input("Enter a string:")
def count(n):
    countdigit=0
    countalpha=0
    for ch in n:
        if(ord(ch)>=65 and ord(ch)<=90 or ord(ch)>=97 and ord(ch)<=122):
            countalpha=countalpha+1
    print("No.of alphabets:",countalpha)
    for i in n:
        if(i>='0' and i<='9'):
            countdigit=countdigit+1
    print("No.of Digits:",countdigit)
count(n)
    