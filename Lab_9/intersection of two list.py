# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 12:13:43 2025

@author: oener
"""

def create_list(l1,l2):
    s1=set(l1)
    s2=set(l2)
    print(s1&s2)
l1=[1,2,3,4]
l2=[1,3]
create_list(l1,l2)