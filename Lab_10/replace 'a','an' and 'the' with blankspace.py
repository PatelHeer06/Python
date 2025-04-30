# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 19:17:38 2025

@author: oener
"""
remove_words = ['a', 'an', 'the']


with open('C:\\Users\\oener\\Desktop\\python codes\\file handling\\file 1.txt', 'r') as infile:
    content = infile.read()


words = content.split()  
filtered_words = [word for word in words if word.lower() not in remove_words]  


cleaned_text = ' '.join(filtered_words)


with open('destination.txt', 'w') as outfile:
    outfile.write(cleaned_text)

print("File processed successfully! Cleaned content saved in 'destination.txt'.")