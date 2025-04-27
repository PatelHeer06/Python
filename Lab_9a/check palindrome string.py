# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 10:23:23 2025

@author: oener
"""

def palindrome(s):
    if type(s)==str:
        for i in range(0,len(s)):
            if s[i]==s[len(s)-1-i]:
                return s
l=['madam','python',12321]
f=filter(palindrome,l)
print(list(f))
   