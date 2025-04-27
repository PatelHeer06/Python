# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 11:05:54 2025

@author: oener
"""

def convert(s):
    s1=s.split()
    print(s1)
    s2=set(s1)
    print(s2)
    s3=sorted(list(s2))
    print(s3)
s="Heer Tirth Heer"
convert(s)    