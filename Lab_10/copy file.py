# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 18:13:29 2025

@author: oener
"""


f=open('C:\\Users\\oener\\Desktop\\Name,Roll no.,Marks.csv','r')
a=f.read()
print(a)
f1=open('‪New file.csv','w')
f1.write(a)
f.close()
f1.close()
    
    