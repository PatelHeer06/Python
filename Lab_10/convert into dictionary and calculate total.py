# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 11:41:35 2025

@author: oener
"""

f=open('C:\\Users\\oener\\Desktop\\Name,Roll no.,Marks.csv','r')
a=f.readlines()
print(a)
print('\n')
l=[]
d={}
for i in a:
    l.append(i.strip().split(','))
print(l)
print('\n')
for i in range(len(l[0])): 
    d.update({l[0][i]:[l[1][i],l[2][i]]})            
print(d)       
f.close()

    