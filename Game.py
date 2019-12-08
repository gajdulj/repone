#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:11:16 2019

@author: gajdulj
"""

text = 'Hello World \nNew line !'
count = int(input("Insert any number between 1 and 99 >> "))
while count != 0:
    count -=1
    print (count)
    save_file = open (str(count)+'Hello.txt','w') 
    save_file.write(text)
    save_file.close()
