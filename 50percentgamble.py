#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:19:39 2019

@author: gajdulj
"""

import random as rn

def bet():
    cash = 1000
    round_count = 0
    stake = 3
    for i in range (100):
        outcome = rn.randint(0,1) #50% chance gamble
        print ("Round number:",round_count)
        print ("Current cash: £{}".format(cash))
        print ("Current stake: £{}".format(stake))
        
        if outcome == 0:
            print ("Round Lost")
            cash = (cash - stake)
            
            if cash > 0:
                stake = stake * 2
                print ("Current cash: £{}".format(cash))
                print ("Betting £{}".format(stake))
                round_count +=1
                print("\n")
                outcome = rn.randint(0,1)
            else:
                print ("Game over")
                print("\n")
                break
            
        elif outcome == 1:
            print ("Round won")
            cash = (cash + stake)
            stake = 3
            print ("Current cash: £{}".format(cash))
            print ("Betting £{}".format(stake))
            round_count +=1
            print("\n")
            
        print ("Survived ",round_count, " rounds")

bet()

