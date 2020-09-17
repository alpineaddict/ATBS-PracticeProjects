#!/usr/bin/env python

"""
Small program that requests input from a user, then opens a file and replaces
particular string matches with user input. Saves the content to a new file.
"""

import re
from pathlib import Path
import pyinputplus as pyip

FILEPATH = "/home/ross/AllThingsPython/ATBS/Testing/"
FILENAME = "string_file.txt"

print('===== MAD LIB =====\n')
print('Please enter words appropriately for the following prompts:')
user_adj   = pyip.inputStr('Adjective: ')
user_noun1 = pyip.inputStr('Noun: ')
user_verb  = pyip.inputStr('Verb: ')
user_noun2 = pyip.inputStr('Noun: ')

# Create variable from reading lines in file
string_file = open(FILEPATH, 'r')
content = string_file.read()

# replace text with user input any time one of the following words are encountered:
    # ADJECTIVE
    # NOUN
    # ADVERB
    # VERB
adjRepl = re.compile(r'ADJECTIVE')
replaced = re.sub(adjRepl, user_adj, content)
nounRepl1 = re.compile(r'NOUN')
replaced = re.sub(nounRepl1, user_noun1, replaced, count=1)
verbRepl = re.compile(r'VERB')
replaced = re.sub(verbRepl, user_verb, replaced)
nounRepl2 = re.compile(r'NOUN')
replaced = re.sub(nounRepl2, user_noun2, replaced)

# print results to screen
print('Your new sentence is as follows:')
print(replaced)

# save to a new text file with a unique name
print('\nSaving file...\n')
newfile = open(F"{FILEPATH}newfile.txt", 'w')
newfile.write('\n' + replaced)
print('File was saved at the following location:)
print(f"{FILEPATH}+/newfile.txt')
print('Have a nice day.')