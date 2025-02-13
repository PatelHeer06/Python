# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:22:42 2025

@author: oener
"""

def day():
    hour=int(input("Enter hour:"))
    if(hour==0):
        print("MIDNIGHT")
    elif(hour==12):
        print("NOON")
    elif(hour>0 and hour<12):
        print(hour,"AM")
    elif(hour>12 and hour<24):
        print(hour-12,"PM")
day()