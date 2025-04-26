# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:22:42 2025

@author: oener
"""

def day():
    for i in range(0,25):
        if(i==0):
            print("MIDNIGHT")
        elif(i==12):
            print("NOON")
        elif(i>0 and i<12):
            print(i,"AM")
        elif(i>12 and i<24):
            print(i-12,"PM")
day()