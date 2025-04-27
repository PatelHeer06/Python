# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 10:33:40 2025

@author: oener
"""

l=['heerpatel','krissa','tirthnandaniya','devaryasinh']
n=lambda x:len(x)>8
f=filter(n,l)
print(list(f))