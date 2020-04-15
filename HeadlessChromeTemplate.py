#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:42:54 2018
@author: Kuba
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)  # Optional argument, if not specified will search path.
driver.get("https://secure.tesco.com/account/en-GB/login?from=/")

innerHTML = driver.execute_script("return document.body.innerHTML")
print (innerHTML)
print ("Headless Chrome Initialized")

driver.quit()