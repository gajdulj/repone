#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:47:04 2018

@author: Kuba
"""
import requests
import bs4
from requests_html import HTMLSession
import re

session = HTMLSession()

def unique_values(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]




#Open the first page to identify how many pages are there
r = session.get('https://www.mediaexpert.pl/produkty.html?query=beurer&szukaj=1')
jsPage = r.html.render()

#Select an element that returns a list where last element is no pages
pageText = r.html.find('#formPorownanie > div.list_head.b-offer_filters.clearfix2 > div:nth-child(2) > div.view_on_desktop > div.list_nav > div > span', first=True).text
medex_pages = pageText.split(" ")
medex_pages = medex_pages[-1]
medex_pages = int(medex_pages)  
print (medex_pages)

codes = []
prices = []

start_page = -2
# every next page will have 2 more and then 0 (20>40>60...)
# will keep the second digit constant and vary the first.
for page in range (1,medex_pages+1): #For every page (1 to 15):
    start_page += 2
    res = requests.get('https://www.mediaexpert.pl/produkty.html?query=beurer&szukaj=1&start={}0'.format(start_page))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"lxml")
    codes_data = str(soup.findAll("div", class_="m-product_desc"))  
    price_data = str(soup.findAll("div", class_="product_prices")) 
    codes.append(re.findall('-beurer-(.+?),id-', str(codes_data)))
    
    price_data = str(soup.findAll("div", class_="m-product_price"))
    prices.append(re.findall('data-atat="price">(.+?)<', str(price_data)))
    
    print ("Number of codes on page {}:".format(page))
    print (len(codes[page-1]))
    print ("Number of unique codes on page {}:".format(page))
    print (len(unique_values(codes[page-1])))
    print ("Number of prices on page {}:".format(page))
    print (len(prices[page-1]))
    print (codes[page-1])
    print (prices[page-1])
    
codes = sum(codes, [])
print ("all codes: ")
print (len(codes))
codes = unique_values(codes)

print ("no duplicates codes: ")
print (len(codes))
prices = sum(prices, [])   
 
print ("all prices: ")
print (len(prices))

# Identify outlet products, allow to keep their duplicates
#Append links to the list>delete duplicates>add outlet to code where relevant 

#Too many codes being downloaded
'''
codes = []
res = requests.get('https://www.mediaexpert.pl/produkty.html?query=beurer&szukaj=1&start=60')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"lxml")
codes_data = str(soup.findAll("div", class_="m-product_desc"))  
codes.append(re.findall('-beurer-(.+?),id-', str(codes_data)))
print (codes) 
codes = sum(codes, [])
print (len(codes))
''' 






