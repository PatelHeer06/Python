# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:09:30 2025

@author: oener
"""

def upper():
    str=input("Enter a string:")
    str1=''
    for ch in str:
        if(ch>='a' and ch<='z'):     #a=97 and A=65
            str1=str1+chr(ord(ch)-32)
        else:
            str1=str1+ch
    print(str1)
def lower():
    str=input("Enter a string:")
    str1=''
    for ch in str:
        if(ch>='A' and ch<='Z'):
            str1=str1+chr(ord(ch)+32)
        else:
            str1=str1+ch
    print(str1)
upper()
lower()