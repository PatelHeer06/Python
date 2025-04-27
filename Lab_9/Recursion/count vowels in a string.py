# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:04:45 2025

@author: oener
"""

def count_vowels(n,i,count):
    l=['a','e','i','o','u']
    if i==len(n):
        return count
    elif n[i] in l:
        count=count+1
        return count_vowels(n,i+1,count)
    else:
        return count_vowels(n,i+1,count)
n=input("Enter a string:")
print("Vowels are:",count_vowels(n,0,0))
    