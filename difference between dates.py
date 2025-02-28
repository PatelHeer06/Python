# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:13:19 2025

@author: oener
"""
from datetime import date

date1=[28,12,2024]
date2=[26,2,2025]
d1=date(date1[2],date1[1],date1[0])
d2=date(date2[2],date2[1],date2[0])
difference=abs((d2-d1).days)
print(difference)