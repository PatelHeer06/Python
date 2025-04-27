# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:19:31 2025

@author: oener
"""

def reverse_list(l,l1):
    if len(l)==0:
        return l1
    else:
        l1.append(l[len(l)-1])
        return reverse_list(l[:len(l)-1],l1)
l=[1,2,3,4,5]
l1=[]
print("List:",l)
print("Reversed list:",reverse_list(l,l1))