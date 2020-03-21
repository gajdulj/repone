#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:41:52 2018

@author: Jakub Gajdul
"""
import random as rd
import time
import numpy as np

opening_price = int(100) #initial price
noise = np.linspace (-0.5 , 0.5, 20) #np array or possible changes
current_price = opening_price #set them equal (only initially)

while True:
    time.sleep(0.5)
    n= rd.randint(1,19) # random for array position
    random_noise = noise[n] # random from list
    current_price += random_noise # price change
    clock = time.asctime()
    print (clock)
    print (current_price)
    
