#!/usr/bin/env python

"""
Encrypt PDF at specified location with specified password.
"""

import os
import PyPDF2
import time
import pyinputplus as pyip

def get_info():
    '''
    Get input from user for path, filename and password. Return values. 
    '''

    print('Please fill out the following prompts, which will be the info used '
          'to encrypt your PDF file.')
    path     = pyip.inputStr     ('File path: ') 
    filename = pyip.inputStr     ('File name: ')
    password = pyip.inputPassword(' Password: ')

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

    return(path, filename, password)


def encrypt_pdf(path, filename, password):
    '''
    Accept PDF path, filename and password as parameters. Encrypt PDF with given
    password.
    '''

    print('\n\nAttempting to encrypt PDF...')
    os.chdir(path)

    # Attempt encryption:
    try:
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.pdf_fileReader(pdf_file)
        pdf_writer = PyPDF2.pdf_fileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        pdf_writer.encrypt(password)
        new_file_name = filename[:-4] + '_encrypted.pdf'
        result_pdf = open(new_file_name, 'wb')
        pdf_writer.write(result_pdf)
        result_pdf.close()
    except Exception as e: 
        print('ERROR! PDF file was not encryped.\n Error: {}'.format(e))
    else: 
        print('\nPDF was successfully encrypted! '
            'Please write down the password below in a safe space!'
            '\nPassword: {}'.format(password))
        print('\nTerminating program.')


# Run program
path, filename, password = get_info()
encrypt_pdf(path, filename, password)