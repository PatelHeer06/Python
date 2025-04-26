# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:46:21 2025

@author: oener
"""
alpha='abcdefghighijklmnopqrstuvwxyz'
def lower(alpha):
    for char in alpha:
        print(char.lower(),end='')
print("Lower Case:")
lower(alpha)  
def upper(alpha):
    for char in alpha:
        print(char.upper(),end='')
print("\nUpper Case:")
upper(alpha)