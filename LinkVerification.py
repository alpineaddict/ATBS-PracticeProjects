#!/usr/bin/env python

# LinkVerification
# Request input from user to acquire a website URL
# Retrieve all links from the page and check their validity

import requests, bs4, pyinputplus as pyip
from urllib.request import Request, urlopen

def URL_Validity(url):
    '''
    Custom function used for URL input validation.
    '''
    if 'https://' not in url:
        raise Exception('\nURL must contain \'https://\'. Please enter a valid URL.'
                        '\nWebsite URL:')


def Get_Website(url):
    '''
    Take URL as parameter and check for validity. 
    If link is not valid, return error and prompt again.
    '''
    try: 
        print('\nChecking website validity...')
        website = requests.get(url)
        status  = website.raise_for_status()
        if status == None:
            print('Website validation check has passed.')

        return(True)

    except Exception as e: 
        print('Unable to load website. Error:\n{}'.format(e))


def Check_Links(url):
    '''
    Accept website as parameter. Crawl website for links, and then check validity of each link.
    Return link validity for all links found on website. 
    '''
    print('\nBelow is a list of links of page and their validity.\n')
    
    # Create beautifulsoup object: 
    req       = Request(url)
    html_page = urlopen(req)
    soup = bs4.BeautifulSoup(html_page, "html.parser")

    # Find all links on page, add to a list
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
        #print(link.get('href'))

    # Iterate through list and return validity for each link
    for link in links:
        try:
            validity = requests.get(link)
            validity.raise_for_status()
            print('\nLink:\n', link, '\nStatus: Valid')
        except Exception as e:
            print('\nLink:\n', link, '\nStatus: ERROR! 404 - Link is not a valid website.')
            print('Exception: {}'.format(e))


# Running the program
print('Welcome to LinkVerification. This app will crawl a website of your choice and check ',
      'all links for validity. An error will be presented if a link is not valid.')
print('\nPlease enter a website URL: ')

basePage     = pyip.inputCustom(URL_Validity)
pageValidity = Get_Website(basePage)

if pageValidity:
    # Find every link on website
    Check_Links(basePage)
else: 
    print('Terminating program.')

