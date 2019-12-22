#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program sends randomly generated data to a fake goverment website.

SMS:
HMRC Have determined that you are eligible for a tax rebate of £228.88. 
Press the link to get started. 
https://gov.uk-auth-c58.com/account
"""

url= 'https://gov.uk-auth-c58.com/account/Finish.php?ssl_id=GfAlwBJ3gtIq17F6jurP3d9sHYPoGJCnYcIvOrz4VhvWpa3IEuyIIIapG0OnJqKICsdqUNvP40MubPcQkLy3uIsbJgysGjajMoJGbfwgfiKq8XhsJPvdyYohfXJWgUf2jZ'

import requests 
import random
import csv

def rand_x_digit_num(x):
    return random.randint(10**(x-1), 10**x-1)  

        
with open('names.csv', 'r') as f:
  reader = csv.reader(f)
  names = list(reader)
names = names[1:]

for name in names:
    fullname = ''.join(random.choice(names))
    card = rand_x_digit_num(16)
    exp =  str('0')+(str(random.randint(1,9)))+' '+'/'+ ' ' + str(random.randint(20,22))
    scode = random.randint(150,750)
    acc = rand_x_digit_num(8)
    sortcode = str('0')+str(random.randint(3,8))+'-'+str(random.randint(3,8))+ str('0')+'-'+str(random.randint(11,55))
    print (str(names.index(name))+': '+fullname,card,exp,scode,acc,sortcode)
    requests.post(url,allow_redirects = False, data ={
        'tes': r'csrfToken,user_id,password,profile:6180403181099740681::Z7PJmvIbwqpEkYXuwErxkhl6/47IiqWuUIG089Fk/n9Rs34jIFTbTGzC3cNDsii8GVso7bwbKSw3KI/uEjS7Ag==',
        'csrfToken': r'60e95235e20c5eed27a06f25a9f99e782833a652\\-1553630837725-185ce4b4a7e1ecf38c2b8b1a',
        'ccname': fullname,
        'ccno': card,
        'ccexp': exp,
        'secode': scode,
        'account': acc,
        'sortcode': sortcode
    })