#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:32:27 2019

@author: gajdulj
"""
'''
import re
m = re.findall(r'\d+', '5Need47forSpeed 2')
m = "".join(m)
print (m)
'''



def solution(A):
    # write your code in Python 3.6
    B = range(1,max(A))
    difference = set(A)-set(B)
    print (difference)
    
solution(A)