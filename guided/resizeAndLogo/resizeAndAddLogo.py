#! /usr/bin/env python

# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((50, 50))
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory
for filename in os.listdir('.'):
    # skip files that don't end with [.jpg, .png, .bmp, or .gif in lowercase]; skip logo
    if not (filename.lower().endswith('.gif') or filename.lower().endswith('.jpg') \
        or filename.lower().endswith('.bmp') or filename.lower().endswith('.png')) \
            or filename == LOGO_FILENAME or filename == 'withLogo':
                continue

    im = Image.open(filename)
    width, height = im.size

    # Check if the image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height: 
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else: 
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image
        print('Resizing %s ...' % (filename))
        im = im.resize((width, height))

    if width < SQUARE_FIT_SIZE and height < SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        print('Image resolution smaller than 300 on longest side.')
        logoIm = logoIm.resize((15, 15))
        SQUARE_FIT_SIZE = 100
        # Calculate the new width and height to resize to
        if width > height: 
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else: 
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image
        print('Resizing %s ...' % (filename))
        im = im.resize((width, height))

    # Add the logo
    print('Adding logo to %s ...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes
    im.save(os.path.join('withLogo', filename))