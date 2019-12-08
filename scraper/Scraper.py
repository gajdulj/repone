#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:26:04 2018

@author: Kuba

for item in items and retailer in retailers
search for product on the websites search engine
parse the price, make note on no. other prices
export to CSV where columns = "Item", "Price", "note
schedule the thing to run weekly, email CSV to MD

To parse prices, currency (PLN) straight after a float
Or numbers separated by comma/ dot (May not work because of different formats)
For numbers use floats instead of int so its more accurate
If more than one on the page, make note on len(prices)

All Beurer products name is in format (XX ## or XX ###)
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

print ("This program will compare the prices of certain products for the following retailers:")
for retailer in retailers:
    print (retailer)

# Queries list where PRODUCTNAME is what we are looking for
    
# https://www.electro.pl/produkty.html?szukaj=1&query=PRODUCTNAME
# https://www.komputronik.pl/search/category/1?query=PRODUCTNAME
# https://www.mediaexpert.pl/produkty.html?query=PRODUCTNAME&szukaj=1
# https://www.sferis.pl/szukaj?q=PRODUCTNAME
# https://www.emag.pl/search/PRODUCTNAME?ref=effective_search
# https://mediamarkt.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D=PRODUCTNAME

#Electro price reader
'''
res = requests.get('https://www.electro.pl/produkty.html?szukaj=1&query=HK+47+To+Go')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
electroPrice = soup.find(itemprop="price").get("content")
print (electroPrice,"zł")


#Komputronik price reader
res2 = requests.get('https://www.komputronik.pl/search/category/1?query=HK%2047%20to%20go')
res2.raise_for_status()
soup2 = bs4.BeautifulSoup(res2.text,"html.parser")

#next item will have price-1 but first result is the product we are looking for
spans = soup2.find_all('span', attrs={'at-gross-price-0'}) 
for span in spans:
    price = span.string
    print (price.replace(" ", ""))

#Mediaexpert price reader 
res = requests.get('https://www.mediaexpert.pl/produkty.html?query=HK+47+to+go&szukaj=1')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
mediaPrice = soup.find(itemprop="price").get("content")
print (mediaPrice)

#Sferis price reader
res = requests.get('https://www.sferis.pl/szukaj?q=HK+47+to+go')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
spans = soup.find_all('span', attrs={'price__part price__part--regular'}) 
lines = [span.get_text() for span in spans]
sferis_price = lines[0].replace(" ","")
print (sferis_price)

#Emag price reader
res = requests.get('https://www.emag.pl/search/HK%2047%20to%20go?ref=effective_search')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
#not found

#Media price reader
res = requests.get('https://mediamarkt.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D=HK+47+to+go')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
#Not found
'''



#Electro price reader- all Beurer


#identify the number of pages and open each of them as per patter below
#identify where to look for :
#full description
#product codes
#price

'''
res = requests.get('https://www.electro.pl/produkty.html?szukaj=1&query=beurer')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
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

# !!! With soup, use nth-of-type instead of nth-child!!!


kompPrices = []
kompHeads = []
variant_entries = []
min_prices = []
min_prices_raw = []

from requests_html import HTMLSession
session = HTMLSession()

#Open the first page to identify how many pages are there
r = session.get('https://www.komputronik.pl/producer/1181/beurer.html?showProducts=1&showBuyActiveOnly=1&p=1')
jsPage = r.html.render()

#Select an element that returns a list where last element is no pages
pageText = r.html.find('#products-list > div:nth-of-type(2) > div.col-xs-30.col-slg-9.text-xs-center.text-slg-right.product-list-top-pagination.sp-top-grey-md', first=True).text
KompnoPages = pageText.split("\n")
KompnoPages = KompnoPages[-1]
KompnoPages = int(KompnoPages)  

#Have to identify a pattern for products that are multi color
#Pop codes of the multi- color products from the main list (can put them in a new list)
#Go through all the pages, collect prices for multi-col

#Strip any list to hold unique values only
def unique_values(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

for page in range (1,KompnoPages+1): #For every page (1 to 15)
    res = requests.get('https://www.komputronik.pl/producer/1181/beurer.html?showProducts=1&p={}&showBuyActiveOnly=1'.format(page))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"lxml")
    
    #identify text to parse the codes from
    head_data = str(soup.findAll("div", class_="pe2-head"))
    price_data = str(soup.findAll("div", class_="ps4-price")) 
    variant_text = soup.findAll("li", {"class": "product-entry2 variant-entry"})
    
    #Look for codes in the data, append them to a list
    kompHeads.append(re.findall('beurer-(.+?).html', head_data))
    
    #Look for codes in the data, append them to a list
    for value in variant_text:
        variant_entries.append(re.findall('beurer-(.+?).html', str(variant_text)))


    # Below will find prices with corrupted discounted prices in format'1\xa0899'
    for product in range(21):
        spans = soup.find_all('span', attrs={"at-gross-price-{}".format(product)})  
        for span in spans:
            price = span.string
            p = (price.replace(" ", "")[1:-2])
            
            #Append each price to list, replace if corrupted
            kompPrices.append(p.replace('\xa0',','))
        
        #Look for varying prices minimum
        min_prices_text = soup.find("div", class_="ps4-price at-min-price-{}".format(product))
        if min_prices_text:
            min_prices_raw.append(re.sub(r'<div class="ps4-price at-min-price-{{}}">(.+?)<'.format(product), '', min_prices_text.string))
 
#Delete spaces, newlines and currency           
for min_price in min_prices_raw:
    min_price = (min_price.replace(" ", ""))
    min_price = (min_price.replace("\n", ""))
    min_price = (min_price.replace("zł", ""))
    
    min_prices.append(min_price)
    
#To change from matrix to vector
kompHeads = sum(kompHeads, [])

#Change from matrix to a vector and remove duplicates
variant_entries = sum(variant_entries, [])
variant_entries = unique_values(variant_entries)

#Substract variant entries codes from the main list, call it a new array
variant_entries = set(variant_entries)
new_array = [x for x in kompHeads if x not in variant_entries]

new_array = list(new_array)

final_codes = new_array + list(variant_entries)
final_prices = kompPrices + min_prices

print('Number of codes collected: {}'.format(len(final_codes))) 
print('Number of prices collected: {}'.format(len(final_prices)))     


df2 = pd.DataFrame(
        {'Product': final_codes,
         'Code': final_codes,
        'Price': final_prices,
        'updated on':datetime.today(),
        'Retailer': "Komputronik.pl"
        })
print(df2.head())



