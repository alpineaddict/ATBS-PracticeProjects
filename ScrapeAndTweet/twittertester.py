#!/usr/bin/env python

#tweepy tester

import os, random, tweepy, datetime, time

APIkey              = "n3OnnJI7TxduhzwKQ4V3bVvuJ"
APIsecretKey        = "WkdBaUaSihqpmevegIwW6gkxSXgsBPxsJRrKkx87Bc8WFLuN8S"
AccessToken         = "1265659823015686150-2csYn38Hau6Waie2plt0TAkCrZ2haQ"
AccessTokenSecret   = "VStLKeCdcpcypbLd2Yd5gtbPZwi7rCEgeR9nRiJoAYPae"

auth = tweepy.OAuthHandler(APIkey, APIsecretKey)
auth.set_access_token(AccessToken, AccessTokenSecret)

api = tweepy.API(auth)
try: 
    api.verify_credentials()
    print('Attempting authentication...')
    print("Authentication OK")
except: 
    print("Error during authentication.")


def image_upload_test(api):
    filePath = "/home/ross/All Things Python/ATBS/PracticeProjects/ImageDownloader/ImageDump/"
    fileName = "depositphotos_102333710-stock-photo-back-and-white-sad-pug.jpg"
    fullPath = "/home/ross/All Things Python/ATBS/PracticeProjects/ImageDownloader/ImageDump/depositphotos_102333710-stock-photo-back-and-white-sad-pug.jpg"

    try:
        print('\n\nAttempting image tweet...')
        os.chdir(filePath)
        api.update_with_media(fileName,status="Via Tweepy API for Python.")
        time.sleep(15)
        print("Image '{}' tweeted successfully.".format(fileName))
    except Exception as e:
        print("ERROR! Media image file was not uploaded. Error message:\n%s" % (e))

image_upload_test(api)


def tweet_test(api):
    dateTime = str(datetime.date.today()) + " " + time.strftime("%H:%M:%S", time.localtime())
    try: 
        api.update_status("Test tweet via Tweepy API for Python.\nTimestamp: {}".format(dateTime))
        print('\n\nTest tweet sent. Text:\n\"Test tweet via Tweepy API for Python.\n Timestamp: {}\"'.format(dateTime))
    except Exception as e:
        print("Tweet failure.")

# tweet_test(api)



