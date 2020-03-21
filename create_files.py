#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:11:16 2019

@author: gajdulj
"""

text = 'sample Text to save\nNew line!'

count = int(input("Insert number of times to create a file >> "))

for i in range(count):
    print (f"Creating file #{i+1}")
    save_file = open(f"file{str(i+1)}.txt",'w') #w for write, a for append
    save_file.write(text)
    save_file.close()
