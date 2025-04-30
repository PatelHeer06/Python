# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 13:21:36 2025

@author: oener
"""

f=open('vcard.vcf','w+')
name=input("Enter name:")
number=int(input("Enter phone number:"))
email=input("Enter E-mail id:")
vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{name};
FN:{name}
TEL;TYPE=CELL:{number}
EMAIL;TYPE=INTERNET:{email}
END:VCARD
"""
f.write(vcard)
f.close()
