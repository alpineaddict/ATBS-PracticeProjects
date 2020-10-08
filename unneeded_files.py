#!/usr/bin/env python

"""
Small program that accepts a directory and a file size, then walks said directory
looking for files larger than the file size specified and deletes them. 
"""

import os
from pathlib import Path

FILEPATH = '/home/ross/Desktop/TestDirectory'

def unneeded_files(directory, file_size):
    '''
    Accept directory path and file size as parameters.
    Perform tree walk starting at specified directory looking for files larger
    than the specified file size and delete them. 
    '''

    path = Path(directory)
    convert_to_bytes = file_size * 1024 * 1024
    files_deleted = []

    while True: 
        # Check validity of directory specified
        if not path.exists():
            print('ERROR! Path does not exist. Please specify valid file path.')
            break

        # Perform tree walk
        for folder_name, sub_folders, filenames in os.walk(path):
            print(f'Scanning files in {folder_name} ...')
            
            # List matching files and copy to target directory 
            for filename in filenames:
                if os.path.getsize(os.path.join(folder_name, filename)) > convert_to_bytes:
                    print(f'File over {file_size} MB found: ' + filename)
                    files_deleted.append(filename)
                    os.unlink(os.path.join(folder_name, filename))

        # Show files deleted:
        print("Scan finished. Here is a list of files deleted:")
        for file in files_deleted: 
            print(file)

        break

unneeded_files(FILEPATH, 99)

# file size: 104000000 or 100M
# 99 converted:  103809024
# 100 converted: 104857600
