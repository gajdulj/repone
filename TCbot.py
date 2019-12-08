# -*- coding: utf-8 -*-

import time
import pyautogui

#Use this to send messages
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
        pyautogui.moveTo(x=300, y=300, duration=0.5)
        time.sleep(3)
        pyautogui.moveTo(x=700, y=300, duration=0.5)
        time.sleep(3)
 

# TC bot  
#Password
#9f09536b1c17
    
print ("""\n************************
Welcome to The Crims bot
************************
\n""")

import subprocess
import pyperclip
import re

applescript = """
display dialog "Task completed" ¬
with title "Success" ¬
with icon caution ¬
buttons {"OK"}


"""
#Pop-up when process complete (will only work on Mac)
def completion_alert():
    subprocess.call("osascript -e '{}'".format(applescript), shell=True)


qneeded = 0

def check_stamina():
    # Loop used to prevent Value error when unexpected event interupts stamina check
    result = None 
    while result is None:
        try:
            time.sleep(1)
            pyautogui.moveTo(x=1002, y=261, duration=0.5)
            pyautogui.dragTo(981, 263, duration=1)
            pyautogui.rightClick()
            pyautogui.moveTo(x=988, y=303, duration=0.5) #This will copy the value selected with a mouse drag
            pyautogui.click()
            time.sleep(1) #This pause was critical as it takes time to process clipboard content
            stamina = str(pyperclip.paste())
            global m
            m = re.findall(r'\d+', stamina) #Look for percentage in what was copied
            m = "".join(m)
            print ("Identified ",m, "% of health")
            
            global qneeded
            qneeded = str((101-float(m))/2)
            result = qneeded
        except:
            pass #Try to get the value again

def group_robbery(): 
    pyautogui.moveTo(x=323, y=232, duration=0.5)
    pyautogui.click()

    check_stamina()
    # Loop untill no stamina to attack
    while float(m) > 24 :
        pyautogui.moveTo(x=628, y=706, duration=0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        check_stamina()
  
def rob_museum():
    pyautogui.moveTo(x=323, y=232, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(x=460, y=445, duration=0.5)   
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=495, y=559, duration=0.5) 
    time.sleep(2)
    pyautogui.click()
    
def single_robbery():
    pyautogui.moveTo(x=323, y=232, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(x=480, y=446, duration=0.5)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=460, y=579, duration=0.5)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    
def party_and_detox():    
    pyautogui.moveTo(x=310, y=269, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    
    check_stamina()
    
    pyautogui.moveTo(x=843, y=489, duration=0.5)
    pyautogui.click()
    
    pyautogui.moveTo(x=803, y=449, duration=0.3)
    pyautogui.click()
    pyautogui.typewrite(qneeded)
    pyautogui.moveTo(x=853, y=447, duration=0.3)
    pyautogui.click()
    print ("Bought ", qneeded, "booze...")
 
    #Go hospital and detox
    print ("Detoxing...")
    pyautogui.moveTo(x=300, y=584, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(x=802, y=561, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    pyautogui.typewrite(str(1))
    pyautogui.moveTo(x=846, y=564, duration=0.5)
    pyautogui.click()
    print ("Cycle complete.")
    
def train_strength():
   time.sleep(1)
   pyautogui.moveTo(x=967, y=726, duration=0.5) 
   pyautogui.click()
   pyautogui.moveTo(x=834, y=573, duration=0.5)
   pyautogui.click()
   print ("Starting strength training.")

# Core function
def rob_and_party():
    rob_museum()
    #group_robbery()
    party_and_detox()


def rob_and_partytwo():
    group_robbery()
    party_and_detox()



def delay(tcminutes):
    real_time = (tcminutes / 4*60)
    print ("Delay set for ", tcminutes, "TC minutes, equal to ", real_time, "seconds/", (real_time/60), 
           "minutes in real life")
    timer = 0
    while timer != real_time:
        time.sleep(1)
        timer +=1   
        print (timer)

print ("Starting the routine...")
before = time.time() #Time before the operations start

#Insert number below for script delay by TC minutes
delay(0)
     
#Insert value below for number of iterations through the cycle
cycles = 150

for i in range(1,cycles+1):
    print ("\nPerforming robbery cylce #{} \n".format(i))
    rob_and_party()

for i in range(1,cycles+1):
    print ("\nPerforming robbery cylce #{} \n".format(i))
    rob_and_partytwo()
after = time.time() #Time after it finished

print("It took: ", (after - before), " seconds or ", ((after - before)/60), "minutes to complete this task") 


#completion_alert()

#Use the function below for adjustments:
#displaypos()