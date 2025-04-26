# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:27:42 2025

@author: oener
"""

price=[('Pizza',400),('Ice-Cream',40),('Pani Puri',80)]
price.sort(key=lambda x: x[1],reverse=True)
print(price)