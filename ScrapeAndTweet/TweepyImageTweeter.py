#!/usr/bin/env python

# PugTweepy
# When executed, log into twitter via API and tweet a random
# picture of a pug from image repository. Delete selected image.

# API key             : n3OnnJI7TxduhzwKQ4V3bVvuJ
# API secret key      : WkdBaUaSihqpmevegIwW6gkxSXgsBPxsJRrKkx87Bc8WFLuN8S
# Access token        : 1265659823015686150-2csYn38Hau6Waie2plt0TAkCrZ2haQ
# Access token secret : VStLKeCdcpcypbLd2Yd5gtbPZwi7rCEgeR9nRiJoAYPae

import tweepy, os, random, time, shutil, send2trash

class Tweepy_API():
    '''
    Build out API object to interact with Twitter Tweepy API.
    '''
    def __init__(self, APIkey, APIsecretKey, AccessToken, AccessTokenSecret):
        self.APIkey            = APIkey
        self.APIsecretKey      = APIsecretKey
        self.AccessToken       = AccessToken
        self.AccessTokenSecret = AccessTokenSecret


    # Authenticate to Twitter via Tweepy API
    def Twitter_Authenticate(self):
        '''
        Accept parameters for twitter API keys & access tokens and then attempt authentication. 
        '''
        auth = tweepy.OAuthHandler(self.APIkey, self.APIsecretKey)
        auth.set_access_token(self.AccessToken, self.AccessTokenSecret)
        self.api = tweepy.API(auth)
        
        try: 
            print('Attempting authentication...')
            result = self.api.verify_credentials()
            print("Authentication: OK")
            # return(api)    maybe put this back? 
        except Exception as e: 
            print("Error during authentication. Error:\n{}".format(e))

    # Select random image file and upload it to a tweet
    def Tweet_Image(self):
        '''
        Choose a picture at random from photo repository and tweet the photo. Return image file name. 
        '''
        # Change dir to image dump repository. Add image files to list
        filePath = '/home/ross/AllThingsPython/ATBS/PracticeProjects/ScrapeAndTweet/ImageDump/'
        os.chdir(filePath)
        self.imageList = []
        for image in os.listdir():
            self.imageList.append(image)

        # Acquire random image file from list
        self.imageNum = random.randrange(len(self.imageList))
        self.fileName = self.imageList[self.imageNum]

        # Attempt tweet
        try:
            print('\n\nAttempting image tweet...')
            self.api.update_with_media(self.fileName,status="Via Tweepy API for Python.")
            time.sleep(5)
            print("Image '{}' tweeted successfully.".format(self.fileName))
        except Exception as e:
            print("ERROR! Media image file was not uploaded. Error message:\n{}".format(e))

    # Delete image from repository (first move to new dir as test)
    def Delete_Image(self):
        '''
        Accept filename as parameter. Delete file.
        '''
        # Change dir to image dump repository
        os.chdir('/home/ross/AllThingsPython/ATBS/PracticeProjects/ScrapeAndTweet/ImageDump/')
        print('\n\nDeleting \'{}\' ...'.format(self.fileName))
        
        # Delete image
        try: 
            send2trash.send2trash(self.fileName)
            print('\nFile deleted.')
        except Exception as e:
            print('Error! File not deleted.\nError Message: {}'.format(e))


def main():   
    # Variables
    APIkey              = "n3OnnJI7TxduhzwKQ4V3bVvuJ"
    APIsecretKey        = "WkdBaUaSihqpmevegIwW6gkxSXgsBPxsJRrKkx87Bc8WFLuN8S"
    AccessToken         = "1265659823015686150-2csYn38Hau6Waie2plt0TAkCrZ2haQ"
    AccessTokenSecret   = "VStLKeCdcpcypbLd2Yd5gtbPZwi7rCEgeR9nRiJoAYPae"

    # Create API object
    api = Tweepy_API(APIkey, APIsecretKey, AccessToken, AccessTokenSecret)

    # Authenticate, tweet image and then delete image
    api.Twitter_Authenticate()
    api.Tweet_Image()
    api.Delete_Image()

    # Exit Program
    input('\nPress any key to exit program... ')

if __name__ == '__main__':
    main()