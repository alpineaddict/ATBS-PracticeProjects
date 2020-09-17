#!/usr/bin/env python

"""
Use os walk to encrypt or decrypt all PDFs in a tree structure and save as
new file.
"""

import os
import PyPDF2
import EncryptPDF

def pdfEncrypt(filename, password):
    '''
    Accept filename parameter and create new PDF file as encrypted version 
    of given file.
    '''

    print('Attempting to encrypt PDF file: {}'.format(filename))

    try:
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.pdf_fileReader(pdf_file)
        pdf_writer = PyPDF2.pdf_fileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))


        pdf_writer.encrypt(password)
        newFileName = filename[:-4] + '_encrypted.pdf'
        resultPdf = open(newFileName, 'wb')
        pdf_writer.write(resultPdf)
        resultPdf.close()
        print('PDF file successfully encrypted!')
    except Exception as e: 
        print('ERROR! PDF file was not encrypted.\n Error: {}'.format(e))


def pdfDecrypt(filename, password):
    '''
    Accept filename and password as parameters to decrypt PDF file. 
    '''

    print('Attempting to decrypt PDF file: {}'.format(filename))

    try: 
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.pdf_fileReader(pdf_file)
        pdf_reader.decrypt(password)
        pdf_writer = PyPDF2.pdf_fileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        newFileName = filename[:-14] + "_decrypted.pdf"
        resultPdf = open(newFileName, 'wb')
        pdf_writer.write(resultPdf)
        resultPdf.close()
        print('PDF file successfully decrypted!')

    except Exception as e: 
        print('ERROR! PDF file was not decrypted.\n Error: {}'.format(e))


def osWalkEncrypt(password):
    '''
    From the current working dir, perform a tree walk & encrypt all 
    encountered PDF files with password parameter.
    '''

    print('\n\nScanning folders and sub-folders for PDF files...')
    for folder_name, sub_folders, filenames in os.walk(os.getcwd()):
        # print('The current folder is ' + folder_name)
        for filename in filenames:
            if filename.endswith('.pdf') and 'encrypt' not in filename:
                print('PDF found!\nFilename: {}'.format(filename))
                filepath = folder_name + '/' + filename
                pdfEncrypt(filepath,password)
                print('')
                

def osWalkDecrypt(password):
    '''
    From the current working dir, perform a tree walk & decrypt all
    encountered PDF files with password parameter.
    '''


    print('\n\nScanning folders and sub-folders for PDF files...')
    for folder_name, sub_folders, filenames in os.walk(os.getcwd()):
        # print('The current folder is ' + folder_name)
        for filename in filenames:
            if filename.endswith('.pdf') and 'encrypt' in filename:
                print('PDF found!\nFilename: {}'.format(filename))
                filepath = folder_name + '/' + filename
                pdfDecrypt(filepath,password)
                print('')


# Ecrypt PDFs: 
# dir_name = '/home/ross/AllThingsPython/ATBS/PracticeProjects/PDFparanoia/'
# os.chdir(dir_name)
# print(f'Encrypting all PDF files in the following directory:\n{dir_name}')
# password = input('\nPlease enter a password to encrypt PDF files with: ')
# osWalkEncrypt(password)


# Decrypt encrypted PDFs: 
# dir_name = '/home/ross/AllThingsPython/ATBS/PracticeProjects/PDFparanoia/'
# os.chdir(dir_name)
# print(f'Decrypting all PDF files in the following directory:\n{dir_name}'
# password = input('\nPlease enter password for encrypted PDF files: ')
# osWalkDecrypt(password)