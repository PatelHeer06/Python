# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:26:50 2025

@author: oener
"""

import random
s=set()
a=set()
while(len(s)<10):
    n=random.randint(15,45)
    s.add(n)
print(s)
count=0
for i in s:
    if(i<30):
        count=count+1
    if not(i>35):
        a.add(i)
print(count)
print(a)
        
    