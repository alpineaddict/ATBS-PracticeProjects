#!/usr/bin/env python

# Mind the Gaps
# Write a program that finds all files with a given suffix, such as spam001.txt, spam002.txt, and so on, 
# in a single folder and locates any gaps in the num- bering (such as if there is a spam001.txt and spam003.txt
# but no spam002.txt). Have the program rename all the later files to close this gap.

import os
from pathlib import Path

def MindTheGaps(path):
    '''
    Accept path as parameter. Within the path specified, iterate through the files
    and check suffixes to see if there are any missing gaps in the filename endings.
    Example: spam001.txt, spam003.txt. This would be considered to be a gap. 
    '''

    path = Path(path)
    filesInDir = []

    while True: 
        # Check validity of directory specified
        if not path.exists():
            print('ERROR! Path does not exist. Please specify valid file path.')
            break        

        for file in os.listdir(path):
            Path(file).suffix
            print(file)

        break

MindTheGaps("/home/ross/All Things Python/ATBS", 0)