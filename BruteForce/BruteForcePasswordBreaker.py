#!/usr/bin/env python

# Brute force PDF password breaker
# Application that attempts password guesses at random from the english dictionary in 
# order to guess a random password that was used to encrypt a PDF file
# Password: glimmering


import random, os, PyPDF2, time, pyinputplus as pyip

def Get_Info():
    '''
    Get input from user for path, filename and password. Return values. 
    '''

    # Get input
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
        # return(True)                                                                                              # program logic

    return(path, filename)


def Build_Word_Database(dictionary_item):
    '''
    Accept dictionary item as parameter and return object that contains all
    words in English language as individual strings within list. 
    '''

    wordList1 = []
    wordList2 = []
    newDict   = open(dictionary_item, 'r')
    counter   = 0

    for word in newDict:
        wordList1.append(word.lower())
    for word in wordList1:
        word = wordList1[counter][:-1]
        wordList2.append(word)
        counter += 1

    return(wordList2)


def Decrypt_PDF(path, filename, dictionary_words):
    '''
    Accept path to PDF and words database file as parameters.
    Iterate through word database and attempt to decrypt PDF file with each word. 
    Print time to complete operation, password that was successful in decrypting PDF.
    '''

    print('\nAttempting to decrypt PDF file: {}'.format(filename))
    print('Please standby. This may take a few minutes...')
    start = time.time()
    os.chdir(path)
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    counter = 1

    for word in dictionary_words:
        if pdfReader.decrypt(word) == 1:
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            newFileName = filename[:-14] + "_decrypted.pdf"
            resultPdf = open(newFileName, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            print('\n\nPDF file successfully decrypted!')
            print('It took {} different word attempts to decrypt PDF.'.format(counter))
            print('Decryption password: {}'.format(word))
            end = time.time()
            timeInSeconds = str(end - start)[:4]
            print('Completion time: {} seconds'.format(timeInSeconds))
            print('Terminating program. Goodbye!')
            break
        else:
            counter += 1


# Running program
dictionaryFile   = '/home/ross/All Things Python/ATBS/automate_online-materials/dictionary.txt'
dictionaryWords  = Build_Word_Database(dictionaryFile)
path, filename   = Get_Info()
Decrypt_PDF(path, filename, dictionaryWords)

