# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:42:02 2025

@author: oener
"""

l1=[('Tirth','Prince'),'Heer',('Aryan','Devarya'),'Krissa','Vruti']
countgirls=0
countboys=0
for ele in l1:
    if isinstance(ele,tuple):
        for i in ele:
            countboys=countboys+1
    else:
        countgirls=countgirls+1 
print("Total Girls are:",countgirls)
print("Total Boys are:",countboys)
        