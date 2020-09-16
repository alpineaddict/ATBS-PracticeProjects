#!/usr/bin/env python


# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = '9d7c32bf4a234db1747b7a1c3bc31447'

import json, requests, sys

def Get_Weather():
    '''
    Accept sys.arg arguments from cmd line and generate a weather report based off location.
    '''

    # Compute location from command line arguments
    # if len(sys.argv) < 2: 
    #     print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    #     sys.exit()
    # location = ' '.join(sys.argv[1:])
    location = 'Pittsburgh'

    # Download the JSON data from OpenWeatherMap.org's API
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Pittsburgh&cnt=3&appid=9d7c32bf4a234db1747b7a1c3bc31447'
    # url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=%s' % (location, APPID)
    response = requests.get(url)
    response.raise_for_status()

    # View raw JSON text: 
    print(response.text)

    # Load JSON data into a Python variable
    weatherData = json.loads(response.text)

    # Print weather descriptions
    w = weatherData['list']
    print('Current weather in %s:' % (location))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


Get_Weather()