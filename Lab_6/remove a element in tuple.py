# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:56:01 2025

@author: oener
"""

tpl=(10,20,30,40)
l1=list(tpl)
l1.remove(20)
tpl=tuple(l1)
print(tpl)