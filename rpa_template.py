# -*- coding: utf-8 -*-
"""
This script is a template for creating simple RPA apps.
"""
import time
import pyautogui
import sys
import random

def type_messages():
    time.sleep(3)
    for i in range (10):
        pyautogui.typewrite("Hello world")  
        pyautogui.press('enter') 

def displaypos():
    while True:
        time.sleep(1)
        pointing_at = pyautogui.position()
        print (pointing_at)

def keep_active():
    time.sleep(1)
    while True:
        noise=random.randint(-20, 20)
        pyautogui.click(clicks=3,interval=1)
        pyautogui.move(noise,-50, duration=0.5)
        time.sleep(3)
        pyautogui.click(clicks=3,interval=1)
        pyautogui.move(-(noise),50, duration=0.5)
        time.sleep(3)

# This will prevent screen from locking    
print('Press Ctrl-C to quit.')
try:
    while True:
        keep_active()
except KeyboardInterrupt:
    print ('\n')

# To see current mouse position use below
# displaypos()


