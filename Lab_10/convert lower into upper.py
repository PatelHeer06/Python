# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 18:41:49 2025

@author: oener
"""

f=open('C:\\Users\\oener\\Desktop\\Name,Roll no.,Marks.csv','r')
a=f.read()
print(a)
f1=open('File 1.csv','w')
for i in a:
    f1.write(i.upper())
f.close()
f1.close()
