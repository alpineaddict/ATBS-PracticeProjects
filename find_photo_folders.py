#! python3

"""
Find folders that have more than 50 image files in them. If found, print out
location in a text file
"""

import os
import time
from PIL import Image

print('Scanning entire hard drive looking for photo folders.')
print('Photo folders are defined where at least half of the file \n' \
      'contents are image files that are at least 500px in width/height.')
print('The scan may take some time...\n')      

for folder_name, sub_folders, filenames in os.walk('/'):
    num_of_photo_files = 0
    num_of_non_photo_files = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith('.png') or 
                filename.lower().endswith('.jpg')):
            num_of_non_photo_files += 1
            continue    # skip to next filename

        # Open image file using Pillow.\
        try: 
            img = Image.open(os.path.join(folder_name, filename))
            width, height = img.size
        except OSError:
            print('Unable to open up the following file. Ignoring...\n' \
                'Filename: {}'.format(filename))

        # Check if width & height are larger than 500. 
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            num_of_photo_files += 1
        else:
            # Image is too small to be a photo. 
            num_of_non_photo_files += 1

    # If more than half of files were photos, print the absolute path of the folder
    total_files = num_of_photo_files + num_of_non_photo_files
    if num_of_photo_files > (total_files / 2):
        print('Photo folder found! Path: {}\nNumber of photo files: {} \n' \
            .format(os.path.join(folder_name),num_of_photo_files))