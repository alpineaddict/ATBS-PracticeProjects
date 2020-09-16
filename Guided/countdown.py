#!/usr/bin/env python

# countdown.py - A simple countdown script

import time, subprocess

timeLeft = 5

while timeLeft > 0: 
    print('Timeleft: {}'.format(timeLeft))
    #print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file
subprocess.Popen(['see', '/home/ross/AllThingsPython/ATBS/PracticeProjects/Guided/alarm.wav'])
