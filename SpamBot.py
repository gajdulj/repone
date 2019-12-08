# -*- coding: utf-8 -*-

import time
import pyautogui

#Use this to spam people
def spam_messages():
    time.sleep(3)
    for i in range (10):
        pyautogui.typewrite('Hello world count:{} !'.format(i))  
        pyautogui.press('enter') 

#Use this to determine the location of coursor to use for other actions
def displaypos():
    while True:
        time.sleep(1)
        pointing_at = pyautogui.position()
        print (pointing_at)

#Use this to keep the mouse active
def movearound():
    time.sleep(1)
    while True:
        pyautogui.moveTo(x=100, y=80, duration=0.5)
        time.sleep(3)
        pyautogui.moveTo(x=900, y=80, duration=0.5)
        time.sleep(3)
    

#displaypos()
movearound()