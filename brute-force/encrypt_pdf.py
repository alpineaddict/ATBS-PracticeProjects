#!/usr/bin/env python

# PDF Encrypter
# Encrypt PDF at specified path with specified password

import os, PyPDF2, time, pyinputplus as pyip
# TODO: Figure out logic to only run Encrypt_PDF() if path & filename is valid

def Get_Info():
    '''
    Get input from user for path, filename and password. Return values. 
    '''

    # Get input
    print('Please fill out the following prompts, which will be the info used to encrypt'
          'your PDF file.')
    path     = pyip.inputStr     ('File path: ') 
    filename = pyip.inputStr     ('File name: ')
    password = pyip.inputPassword(' Password: ')

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
        # return(True)                                # program logic

    return(path, filename, password)


def Encrypt_PDF(path, filename, password):
    '''
    Accept PDF path, filename and password as parameters. Encrypt PDF with given password.
    '''

    print('\n\nAttempting to encrypt PDF...')
    os.chdir(path)

    # Attempt encryption:
    try:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))


        pdfWriter.encrypt(password)
        newFileName = filename[:-4] + '_encrypted.pdf'
        resultPdf = open(newFileName, 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()
        # print('PDF file successfully encrypted!')                                                 # Temp Removed. Relocated to else
    except Exception as e: 
        print('ERROR! PDF file was not encryped.\n Error: {}'.format(e))
    else: 
        print('\nPDF was successfully encrypted! '
            'Please write down the password below in a safe space!'
            '\nPassword: {}'.format(password))
        print('\nTerminating program.')


# Run program
path, filename, password = Get_Info()
Encrypt_PDF(path, filename, password)