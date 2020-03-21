# -*- coding: utf-8 -*-
"""
This script is a template for creating simple RPA apps.
"""
import time
import pyautogui

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
        pyautogui.moveTo(x=300, y=300, duration=0.5)
        time.sleep(3)
        pyautogui.moveTo(x=700, y=300, duration=0.5)
        time.sleep(3)

# This will prevent screen from locking    
keep_active()

# To see current mouse position use below
# displaypos()


