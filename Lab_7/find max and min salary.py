# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:31:03 2025

@author: oener
"""

d={(1,1):40000,(1,2):35000,(2,1):50000,(2,2):60000}
d1={}
for k,v in d.items():
    print(k[0],v)
    if k[0] not in d1:
        d1[k[0]]={'Max':v,'Min':v,'Total':v}
    else:
        if v>d1[k[0]]['Max']:
            d1[k[0]]['Max']=v
        elif v<d1[k[0]]['Min']:
            d1[k[0]]['Min']=v
        d1[k[0]]['Total']+=v
print(d1)        
