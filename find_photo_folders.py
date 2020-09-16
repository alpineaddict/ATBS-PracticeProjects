#! python3

# findPhotoFolders.py - find folders that have more than 50 image files in them, and if so
# then print out location to a text file

# Import modules and write comments to describe this program.
import os, time
from PIL import Image

print('Scanning entire hard drive looking for photo folders.')
print('Photo folders are defined where at least half of the file \n' \
      'contents are image files that are at least 500px in width/height.')
print('The scan may take some time...\n')      

for foldername, subfolders, filenames in os.walk('/'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.\
        try: 
            img = Image.open(os.path.join(foldername, filename))
            width, height = img.size
        except OSError:
            print('Unable to open up the following file. Ignoring...\n' \
                'Filename: {}'.format(filename))

        # Check if width & height are larger than 500. 
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo. 
            numNonPhotoFiles += 1

    # If more than half of files were photos, print the absolute path of the folder. 
    totalFiles = numPhotoFiles + numNonPhotoFiles
    if numPhotoFiles > (totalFiles / 2):
        print('Photo folder found! Path: {}\nNumber of photo files: {} \n' \
            .format(os.path.join(foldername),numPhotoFiles))