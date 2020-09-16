#!/usr/bin/env python

"""
Script which walks through a folder tree and searches for files with a certain
file extension (such as .pdf or .jpg). Copy these files from whatever location
they are in to a new folder.
"""

import shutil, os
from pathlib import Path

def fileTypeCopy(source_path, target_path, file_extension):
    '''
    Accept absolute file path, target path and file extension as parameter. 
    Perform a tree walk at the absolute path and copy files of specified type to target destination.
    '''

    source = Path(source_path)
    target = Path(target_path)
    filesCopied = []

    if not target.exists():
        os.makedirs(target)
        print('\'{}\' did not exist. Directory created.\n'.format(target))

    while True:
        # Check for valid absolute path and if it is a directory
        if not source.exists():
            print("ERROR! Source directory path does not exist. Terminating program.")
            break
        if source.is_file():
            print("ERROR! Source directory specified is a file. Terminating program.")
            break 

        # Perform tree walk. Print out matching file type results. Copy matches to target
        for foldername, subfolders, filenames in os.walk(source):
            print(f'Scanning files in {foldername} ...')
            
            # List matching files and copy to target directory 
            for filename in filenames:
                if filename.endswith(file_extension):
                    print('File found: ' + filename)
                    if filename in os.listdir(target):
                        print('{} already exists in {}. Skipping copy.'.format(filename,target))
                    if filename not in os.listdir(target):
                        shutil.copy(os.path.join(foldername, filename), target)
                        filesCopied.append(filename)
            print()     # print blank line for readability

        # Print files copied
        if len(filesCopied) == 0: 
            print('Zero files copied. ')
        else: 
            print('Files copied:')
            for file in filesCopied:
                print(file)

        # Print listing of target directory
        print('\nTarget directory listing: ')
        for file in os.listdir(target):
            print(file)

        break

if __name__ == '__main__'"
    FILEPATH   = '/home/ross/AllThingsPython/ATBS'
    TARGET_DIR = '/home/ross/Dump2/'
    FILETYPE   = 'pdf'

    fileTypeCopy(FILEPATH, TARGET_DIR, FILETYPE)
