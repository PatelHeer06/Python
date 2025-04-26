# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:19:05 2025

@author: oener
"""
def compare():
    str1=input("Enter string 1:")
    str2=input("Enter string 2:")
    if(str1 in str2):
        print("String 1 is a substring of string 2")
    elif(str2 in str1):
        print("String 2 is a substring of string 1")
compare()

