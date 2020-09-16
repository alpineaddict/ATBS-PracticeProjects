#! /usr/bin/env python

# ChoreAssigner.py - Program that goes through a list of email addresses and list of chores
# and assigns chores out randomly via emails.

import random, ezgmail, os

# Welcome message
print('Welcome to chore assigner! \nChore assigner will assign a random choice from a list of '
      'predetermined choices to an email address in the available email list.')

# Create variables for list of emails, list of chores, subject line and email body
emails  = ['photo.rossthompson@gmail.com', 'mapleskater31@yahoo.com', 'rossthompson89@gmail.com']
chores  = ['dishes', 'walk_dog', 'cleaning', 'laundry']
subject = 'Chore assignment'
msgBody = 'Hello,\n\nYou have been assigned the following chore via ChoreAssigner.py:\n'

print('\nEmail addresses:')
for email in emails: 
    print('- ' + email)
print('\nChores:')
for chore in chores:
    print('- ' + chore)

# Log into gmail via ezgmail API
print('\nAttempting to log into gmail API...')
os.chdir('/home/ross/AllThingsPython/ATBS/PracticeProjects/ChoreAssigner')
try:
    initialize = ezgmail.init()
    print('Login successful!')
except Exception as e:
    print('ERROR! Unable to log into gmail API.\nError Message: {}'.format(e))

# Assign chore to an email address, send email, update lists appropriately
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
        # emails.remove(email)
    print('\nEmails have been successfully sent! Exiting application')
except Exception as e:
    print('ERROR! Unable to send email.\nError Message: {}'.format(e))
