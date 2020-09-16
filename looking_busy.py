#! /usr/bin/env python

# lookingBusy.py - Move move slightly every 25 seconds to prevent computer from going idle/sleeping

import pyautogui, time, os, sys
print('lookingBusy is running! \nYour mouse will be moved every 25 seconds to ensure' \
        ' your computer doesn\'t go idle.\n\nPress Ctrl+c to quit...')
time.sleep(3)

distance  = 25
changeVar = 0

while True:
    try: 
        if changeVar == 0:
            pyautogui.move(100, 0, duration=0.25)   # move mouse 100px to the right
            changeVar = 1
            time.sleep(5)
        else: 
            pyautogui.move(-100, 0, duration=0.25)   # move mouse 100px to the left
            changeVar = 0
            time.sleep(5)
            continue
    except KeyboardInterrupt: 
        print('\nCtrl+c registered! Exiting program.')
        os._exit(1)