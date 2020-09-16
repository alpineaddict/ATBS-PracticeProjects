#!/usr/bin/env python

# Small program that requests input from a user, then opens a file and replaces particular string matches with user input. Saves the content to a new file.

import re
from pathlib import Path
import pyinputplus as pyip


# mad lib
print('===== MAD LIB =====\n')

# ask user for a string of the following:
    # adjective
    # noun
    # verb
    # noun
print('Please enter words appropriately for the following prompts:')
userAdj   = pyip.inputStr('Adjective: ')
userNoun1 = pyip.inputStr('     Noun: ')
userVerb  = pyip.inputStr('     Verb: ')
userNoun2 = pyip.inputStr('     Noun: ')

# Create variable from reading lines in file
# path: "/home/ross/All Things Python/ATBS/Testing/stringfile.txt"
stringfile = open("/home/ross/All Things Python/ATBS/Testing/stringfile.txt", 'r')
content = stringfile.read()

# replace text with user input any time one of the following words are encountered:
    # ADJECTIVE
    # NOUN
    # ADVERB
    # VERB
adjRepl = re.compile(r'ADJECTIVE')
replaced = re.sub(adjRepl, userAdj, content)
nounRepl1 = re.compile(r'NOUN')
replaced = re.sub(nounRepl1, userNoun1, replaced, count=1)
verbRepl = re.compile(r'VERB')
replaced = re.sub(verbRepl, userVerb, replaced)
nounRepl2 = re.compile(r'NOUN')
replaced = re.sub(nounRepl2, userNoun2, replaced)

# print results to screen
print('Your new sentence is as follows:')
print(replaced)

# save to a new text file with a unique name
print('\nSaving file...\n')
newfile = open("/home/ross/All Things Python/ATBS/Testing/newfile.txt", 'w')
newfile.write('\n' + replaced)
print('File was saved at the following location:\n/home/ross/All Things Python/ATBS/Testing/newfile.txt')
print('Have a nice day.')