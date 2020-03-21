#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:18:47 2019

@author: gajdulj
"""

#To compare the prices between retailers
import requests
import bs4
import re
import pandas as pd
from datetime import datetime

retailers = ["www.electro.pl","www.komputronik.pl",
             "www.mediaexpert.pl","www.sferis.pl",
             "www.emag.pl", "www.mediamarkt.pl"]
items = []

print ("This program will download the prices of certain products for the following retailers:")
for retailer in retailers:
    print (retailer)
    
res = requests.get('https://www.electro.pl/search?query[menu_item]=&query[querystring]=beurer')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")

no_pages_raw = "body > div.c-layout.v-product.v-product_list.is-classic > div.c-layout_row.c-layout_item.is-main.is-container > div.c-layout_col.c-layout_item.is-content > div:nth-child(1) > div.c-toolbar_item.is-pagination > form > span.is-total"
no_pages = no_pages_raw.replace("nth-child", "nth-of-type")

page_info = soup.select(no_pages)
page_info = str(page_info)
print (page_info)

'''
mydivs = soup.findAll("div", {"class": "list_nav"})[0]

#Select page info by CSS
page_info = soup.select("#formPorownanie > div.list_head.list_head_top.clearfix2 > div > div.list_nav > div > input")
page_info = str(page_info)

#Using re, extract the page number from the string
m = re.search('lpage="(.+?)"', page_info)
if m:
    no_pages = int(m.group(1))
print ("Number of pages on electro: ",no_pages)


namesList = []

codeList = []

priceList = []

pageCount = int(-20) #First page starts at 0, then 20+

for page in range(1,no_pages+1): #For every page
    pageCount = page*20-20
    res = requests.get('https://www.electro.pl/produkty.html?szukaj=1&query=beurer&start={}'.format(pageCount))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    article_data = str(soup.findAll("div", class_="b-buyButtons")) #identify text to read from
    namesList.append(re.findall('data-product-name="(.+?)"', article_data)) #look for product names
    priceList.append(re.findall('data-product-price="(.+?)"', article_data)) #look for prices
    codeList.append(re.findall('data-product-id="(.+?)"', article_data)) #look for prices
    
    
    #Could also look for product id here, ex 840970
   

names = sum(namesList, []) #To change from matrix to vector
prices = sum(priceList, [])
codes = sum(codeList, [])

print (names)
#print (prices)
#print (article_data)

df = pd.DataFrame(
        {'Product': names,
         'Code':codes,
        'Price': prices,
        'updated on':datetime.today(),
        'Retailer': "Electro.pl"
        })

df.to_csv('out.csv', encoding = 'utf-8') #no polish signs, have to find a fix

'''