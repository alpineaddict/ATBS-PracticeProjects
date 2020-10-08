#!/usr/bin/env python

"""
Stopwatch program that tracks elapsed time, creates laps 
and returns output to clipboard
"""

import time
import pyperclip

def track_time():
    print('Press ENTER to begin. Afterwards, press ENTER to start stopwatch.')
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
            lap_time   = str(round(time.time() - lastTime, 2))
            total_time = str(round(time.time() - startTime, 2))
            lap_num_str  = 'Lap # {}:'.format(lapNum)
            lap_timeStr = '({})'.format(lap_time)
            print(lap_num_str.ljust(8), total_time.center(6), lap_timeStr.rjust(7), end='')
            output_str = lap_num_str.ljust(8) + total_time.center(6) + lap_timeStr.rjust(7) + '\n'
            output.append(output_str)
            lapNum += 1
            lastTime = time.time()      # reset the last lap time

    except KeyboardInterrupt:
        print('\nDone!')

    print('Terminating application.')
    return(output)


if __name__ == '__main__':
    output = '\n'.join(track_time())
    pyperclip.copy(output)
