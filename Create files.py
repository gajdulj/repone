#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:11:16 2019

@author: gajdulj
"""

text = 'sample Text to save\nNew line {}!'
count = int(input("Insert number of times to create a file >> "))

while count != 0:
    count -=1
    print (count)
    save_file = open (str(count)+'file.txt','w') #a for append
    save_file.write(text)
    save_file.close()
