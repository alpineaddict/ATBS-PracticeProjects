#!/usr/bin/env python

"""
Brute force PDF password breaker
Application that attempts password guesses at random from the english dictionary in 
order to guess a random password that was used to encrypt a PDF file
Password: glimmering
"""

import random
import os
import PyPDF2
import time
import pyinputplus as pyip

DICTIONARY_FILE = (
    '/home/ross/AllThingsPython/ATBS/automate_online-materials/dictionary.txt'
)

def getInfo():
    '''
    Get input from user for path, filename and password. Return values. 
    '''

    print('Please fill out the following prompts to locate PDF file for decryption.')
    path     = pyip.inputStr('File path: ') 
    filename = pyip.inputStr('File name: ')

    # Validate path and filename
    print('\nValidating file path and whether specified filename exists...')    
    try: 
        os.chdir(path)
    except Exception as e1:
        print('\nERROR! Path is not valid. Exiting program.')
        print('Error: {}'.format(e1))
    try:
        os.stat(filename)
    except Exception as e2:
        print('\nERROR! Specified file is not valid. Exiting program.')
        print('Error: {}'.format(e2))
    else: 
        print('Success! Path and filename OK.')
    return(path, filename)


def buildWordDatabase(dictionary_item):
    '''
    Accept dictionary item as parameter and return object that contains all
    words in English language as individual strings within list. 
    '''

    word_list_1 = []
    word_list_2 = []
    new_dict   = open(dictionary_item, 'r')
    counter   = 0

    for word in new_dict:
        word_list_1.append(word.lower())
    for word in word_list_1:
        word = word_list_1[counter][:-1]
        word_list_2.append(word)
        counter += 1

    return(word_list_2)


def decryptPdf(path, filename, dictionary_words):
    '''
    Accept path to PDF and words database file as parameters.
    Iterate through word database and attempt to decrypt PDF file with each word. 
    Print time to complete operation, password that was successful in decrypting PDF.
    '''

    print('\nAttempting to decrypt PDF file: {}'.format(filename))
    print('Please standby. This may take a few minutes...')
    start = time.time()
    os.chdir(path)
    pdf_file = open(filename, 'rb')
    pdf_reader = PyPDF2.pdf_fileReader(pdf_file)
    counter = 1

    for word in dictionary_words:
        if pdf_reader.decrypt(word) == 1:
            pdf_writer = PyPDF2.pdf_fileWriter()
            for page_num in range(pdf_reader.num_pages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            new_filename = filename[:-14] + "_decrypted.pdf"
            result_pdf = open(new_filename, 'wb')
            pdf_writer.write(result_pdf)
            result_pdf.close()
            print('\n\nPDF file successfully decrypted!')
            print('It took {} different word attempts to decrypt PDF.'.format(counter))
            print('Decryption password: {}'.format(word))
            end = time.time()
            time_in_seconds = str(end - start)[:4]
            print('Completion time: {} seconds'.format(time_in_seconds))
            print('Terminating program. Goodbye!')
            break
        else:
            counter += 1


if __name__ == '__main__':
    
    dictionary_words = buildWordDatabase(DICTIONARY_FILE)
    path, filename = getInfo()
    decryptPdf(path, filename, dictionary_words)
