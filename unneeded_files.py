#!/usr/bin/env python

# Undeeded Files
# Small program that accepts a directory and a file size, then walks said directory
# looking for files larger than the file size specified and deletes them. 

import os
from pathlib import Path

def UnneededFiles(directory, filesize):
    '''
    Accept directory path and file size as parameters.
    Perform tree walk starting at specified directory looking for files larger
    than the specified file size and delete them. 
    '''

    path = Path(directory)
    convertToBytes = filesize * 1024 * 1024
    filesDeleted = []

    while True: 
        # Check validity of directory specified
        if not path.exists():
            print('ERROR! Path does not exist. Please specify valid file path.')
            break

        # Perform tree walk
        for foldername, subfolders, filenames in os.walk(path):
            print(f'Scanning files in {foldername} ...')
            
            # List matching files and copy to target directory 
            for filename in filenames:
                if os.path.getsize(os.path.join(foldername, filename)) > convertToBytes:
                    print(f'File over {filesize} MB found: ' + filename)
                    filesDeleted.append(filename)
                    os.unlink(os.path.join(foldername, filename))
            print()     # print blank line for readability

        # Show files deleted:
        print("Scan finished. Here is a list of files deleted:")
        for file in filesDeleted: 
            print(file)

        break

UnneededFiles('/home/ross/All Things Python/ATBS/', 99)

# file size: 104000000 or 100M
# 99 converted:  103809024
# 100 converted: 104857600
