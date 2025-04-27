# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:47:36 2025

@author: oener
"""

def ispalindrome(s):
    s1="".join(s.split()).lower()
    a=s1[::-1]
    if(s1==a):
        print("Palindrome")
    else:
        print("Not Palindrome")
    
s=input("Enter a string")
ispalindrome(s)
