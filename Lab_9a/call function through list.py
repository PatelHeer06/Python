# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 10:09:56 2025

@author: oener
"""

def func():
    print("Function")
def disp():
    print("Displaced")
def msg():
    print("Message")
l=[func,disp,msg]
for i in l:
    i()