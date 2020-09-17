#!/usr/bin/env python

"""
Move move slightly every 25 seconds to prevent computer from going idle/sleeping
"""

import pyautogui
import os
import sys
import time

print("looking_busy is running!")
print("Your mouse will be moved every 25 seconds to ensure your computer does "
    "not go idle.")
print("Press Ctrl+c to quit...")
time.sleep(3)

distance  = 0.25
change_var = 0

while True:
    try: 
        if change_var == 0:
            pyautogui.move(100, 0, duration=distance)   # move mouse 100px to the right
            change_var = 1
            time.sleep(25)
        else: 
            pyautogui.move(-100, 0, duration=distance)   # move mouse 100px to the left
            change_var = 0
            time.sleep(25)
            continue
    except KeyboardInterrupt: 
        print('\nCtrl+c registered! Exiting program.')
        os._exit(1)