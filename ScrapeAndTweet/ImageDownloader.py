#!/usr/bin/env python

# ImageDownloader
# Navigate to a photo search site and search for a particular set of photos
# Download all search results as images to sub-directory

# TODO: Check for images that are zero bytes in size and delete them

from selenium import webdriver
import requests, os, bs4, random, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# toggle logging on/off
logging.disable(logging.CRITICAL)

# search functionality test
# browser = webdriver.Firefox()
# browser.get('https://depositphotos.com/stock-photos/{}.html'.format(imageSearch))

def Image_Download(website):
    '''
    Accept URL as parameter and download images (100) from search results page.
    '''
    res = requests.get(website)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Scrape 100 images (different source tags). Add objects to list
    images  = soup.find_all('img', attrs={'class':'file-container__image _file-image'})
    images2 = soup.find_all('img', attrs={'class':'file-container__image _file-image lazyload'})

    all_images = []
    for image in images:
        all_images.append(image.get('src'))
    for image in images2:
        all_images.append(image.get('data-src'))

    # Download objects from list as images to image dump directory
    for image in all_images:
        if "http" in image: 
            with open(os.path.basename(image), "wb") as f:
                logging.debug('Downloading {}.\n'.format(os.path.basename(image)))
                f.write(requests.get(image).content)


# Welcome user. Request input for search
print('\n\nWelcome to Image Downloader!\nImage search engine: depositphotos.com')
print('Image Downloader will download 4 pages of images from the search of your choice.')
imageSearch = input('\nWhat do you want to search for?\nImage search: ')

# Create image repository if it does not exist
path = '/home/ross/AllThingsPython/ATBS/PracticeProjects/ScrapeAndTweet/ImageDump/'
os.makedirs(path, exist_ok=True); os.chdir(path)

# Create website variable and plug into function to download images
print('Downloading images. This may take a few minutes...')
counter = 0
for iter in range(4):
    website = 'https://depositphotos.com/stock-photos/{}.html?offset={}'.format(imageSearch, counter)
    Image_Download(website)
    counter += 100

print('\nDownload finished! Exiting program.')