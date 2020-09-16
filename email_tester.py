#!/usr/bin/env python

"""
Accept email address & string from the command line, then use selenium 
to log into email and send email with the string to the provided address.
"""

from selenium import webdriver
import time


# Welcome message
print('Welcome to auto emailer. Please fill out the prompts '
        'below and an email will be sent for you.\n\n')

# targetEmail = input('Target email address: ')
# messageBody = input('Enter a message body that you would like to send:\n')
# print('\nThe following message will be sent to \'{}\':\n{}\n'.format(targetEmail,messageBody))
# print('Opening browser...')

# test email: mapleskater31@yahoo.com

browser = webdriver.Firefox()
browser.get('https://www.mail.com/#.23140-header-navlogin2-1')

# Log into web browser
userElem = browser.find_element_by_id('login-email')
userElem.send_keys('rustyvox69@mail.com')
userPass = browser.find_element_by_id('login-password')
userPass.send_keys('password123!')
loginButton = browser.find_element_by_css_selector('button.btn:nth-child(11)')
loginButton.click()

# Go to inbox. Compose email
goToInbox = browser.find_element_by_css_selector('atl-menu-item.atl-actions-menu__item:nth-child(2) > '
                                                  'pos-icon-item:nth-child(1) > span:nth-child(1) > '
                                                  'pos-svg-icon:nth-child(1)')
goToInbox.click()                                                  
time.sleep(7)
composeEmail = browser.find_element_by_tag_name('a')
composeEmail.click()
# toField = browser.find_element_by_css_selector('.compose-header_to > div:nth-child(2) > div:nth-child(1) >'
#                                                'div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > '
#                                                'input:nth-child(1)')
# toField.send_keystargetEmail)

print('Exiting program.')
