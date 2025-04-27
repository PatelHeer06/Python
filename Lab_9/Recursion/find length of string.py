# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:46:30 2025

@author: oener
"""

def length(s):
    if not s:
        return 0
    else:
        return 1+length(s[1:])
s=input("Enter a string:")
print("Length",length(s))