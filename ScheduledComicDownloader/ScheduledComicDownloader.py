#! /usr/bin/evn python

# ScheduledComicDownloader.py - Script program that checks a comic webpage and
# downloads currently displayed image if image has not already been downloaded

import requests, bs4, os, logging, time

# Toggle logging: 
# logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')

# Check for comic image and download if it doesn't exist:
def main(siteURL):
    '''
    Accept website URL as parameter. Get website via requests and retrieve image file.
    Create image repository if it does not already exist, then check for image.
    Download image if it does not exist.
    '''
    print('Checking {} few new image.'.format(siteURL))

    try:
        # Get website, check for errors:
        website = requests.get(siteURL)
        website.raise_for_status()
        print('Website validity: Successful\n')
    except Exception as e:
        print('ERROR ENCOUNTERED! \nError message: {}'.format(e))    

    try:
        # Create beautiful soup object, find image tag and create image object:
        # imageName* && imageURL* vars will need to be modified if site != XKCD @ www.xkcd.com
        soup = bs4.BeautifulSoup(website.text, 'html.parser')
        images = soup.findAll('img')
        for image in images:
            if 'comics' in (image['src']):
                imageURL = 'http:' + image['src']
                imageName = image['src'].split('/')[4]
                # # Show daily image:
                print('Daily image file: {}'.format(imageName))
                print('Image URL: {}'.format(imageURL))

        # Create repository if it doesn't exist & chdir:
        path = '/home/ross/AllThingsPython/ATBS/PracticeProjects/ScheduledComicDownloader/Images/'
        os.makedirs(path, exist_ok=True); os.chdir(path)
        print('Image target repository: {}\n'.format(path))

        # Check if image exists. If not, download it:
        print('Checking if image file is in directory...'.format(imageName))
        if imageName not in os.listdir():
            print('Image does not exist.')
            print('Standby... ', )
            with open(os.path.basename(imageName), "wb") as f:
                f.write(requests.get(imageURL).content)
            print('Image did not previously exist. Image successfully downloaded!',
                    '\nFilename: {}'.format(imageName))
            print('Exiting application.')                
        else: 
            print('Image \'{}\' already existed; no need for download.'.format(imageName))
            print('Exiting application.')
    except Exception as e:
        print('ERROR ENCOUNTERED! \nError message: {}'.format(e))

# Running the program:
if __name__ == "__main__":
    siteURL = 'http://www.xkcd.com'
    main(siteURL)