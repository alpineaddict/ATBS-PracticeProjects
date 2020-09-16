#!/usr/bin/env python


# petrifiedstopwatch.py - Stopwatch program that tracks elapsed time, creates laps 
# and returns output to clipboard

import time, pyperclip

def Track_Time():
    # display the program's instructions
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.')
    print('Press Ctrl-C to quit.')
    input()                             # press Enter to begin
    print('Started.')
    startTime = time.time()   # get the first lap's start time
    lastTime  = startTime
    lapNum    = 1
    output    = []

    # Start tracking the lap times
    try:
        while True: 
            input()
            lapTime   = str(round(time.time() - lastTime, 2))
            totalTime = str(round(time.time() - startTime, 2))
            lapNumStr  = 'Lap # {}:'.format(lapNum)
            lapTimeStr = '({})'.format(lapTime)
            print(lapNumStr.ljust(8), totalTime.center(6), lapTimeStr.rjust(7), end='')
            outputString = lapNumStr.ljust(8) + totalTime.center(6) + lapTimeStr.rjust(7) + '\n'
            output.append(outputString)
            lapNum += 1
            lastTime = time.time()      # reset the last lap time

    except KeyboardInterrupt:
        # Handle the Ctrl-C exception to keep its error message from displaying
        print('\nDone!')

    print('Terminating application.')
    return(output)


# Run application
output = '\n'.join(Track_Time())
pyperclip.copy(output)