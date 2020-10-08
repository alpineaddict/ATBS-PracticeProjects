#! /usr/bin/env python

"""
Script that will go through a list of given email addresses and list of chores
and assigns chores out randomly through emails with gmail via ezgmail module.
"""

import random
import ezgmail
import os
import emails

FILEPATH = '/home/ross/AllThingsPython/ATBS/PracticeProjects/ChoreAssigner'

print(
    'Welcome to chore assigner! \nChore assigner will assign a random choice'
    'from a list of predetermined choices to an email address in the'
    'available email list.'
)

emails  = emails.email_list
chores  = ['dishes', 'walk_dog', 'cleaning', 'laundry']
subject = 'Chore assignment'
msgBody = 'Hello,\n\nYou have been assigned the following chore via ChoreAssigner.py:\n'

print('\nEmail addresses:')
for email in emails: 
    print('- ' + email)
print('\nChores:')
for chore in chores:
    print('- ' + chore)

print('\nAttempting to log into gmail API...')
os.chdir(FILEPATH)
try:
    initialize = ezgmail.init()
    print('Login successful!')
except Exception as e:
    print('ERROR! Unable to log into gmail API.\nError Message: {}'.format(e))

try: 
    print('\nDelegating tasks...')
    # print('\n\nemail list TEST')
    # for email in emails: 
    #     print('- ' + email)
    for email in emails:
        randomChoice = random.choice(chores)
        print('Sending email to {} for the following task: {}'.format(email, randomChoice))
        ezgmail.send(email, subject, msgBody + randomChoice)
        chores.remove(randomChoice)
    print('\nEmails have been successfully sent! Exiting application')
except Exception as e:
    print('ERROR! Unable to send email.\nError Message: {}'.format(e))
