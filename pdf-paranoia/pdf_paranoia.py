#!/usr/bin/env python

# # PDFparanoia
# Use os walk to encrypt or decrypt all PDFs in a tree structure and save as a new file

import os, PyPDF2
import EncryptPDF

def PDF_Encrypt(filename,password):
    '''
    Accept filename parameter and create new PDF file as encrypted version of given file.
    '''

    print('Attempting to encrypt PDF file: {}'.format(filename))

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
        print('PDF file successfully encrypted!')
    except Exception as e: 
        print('ERROR! PDF file was not encrypted.\n Error: {}'.format(e))


def PDF_Decrypt(filename, password):
    '''
    Accept filename and password as parameters to decrypt PDF file. 
    '''

    print('Attempting to decrypt PDF file: {}'.format(filename))

    try: 
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfReader.decrypt(password)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))

        newFileName = filename[:-14] + "_decrypted.pdf"
        resultPdf = open(newFileName, 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()
        print('PDF file successfully decrypted!')

    except Exception as e: 
        print('ERROR! PDF file was not decrypted.\n Error: {}'.format(e))


def OS_Walk_Encrypt(password):
    '''
    From the current working dir, perform a tree walk & encrypt all encountered PDF files with password parameter.
    '''

    print('\n\nScanning folders and sub-folders for PDF files...')
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        # print('The current folder is ' + folderName)
        for filename in filenames:
            if filename.endswith('.pdf') and 'encrypt' not in filename:
                print('PDF found!\nFilename: {}'.format(filename))
                filepath = folderName + '/' + filename
                PDF_Encrypt(filepath,password)
                print('')
                

def OS_Walk_Decrypt(password):
    '''
    From the current working dir, perform a tree walk & decrypt all encountered PDF files with password parameter.
    '''


    print('\n\nScanning folders and sub-folders for PDF files...')
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        # print('The current folder is ' + folderName)
        for filename in filenames:
            if filename.endswith('.pdf') and 'encrypt' in filename:
                print('PDF found!\nFilename: {}'.format(filename))
                filepath = folderName + '/' + filename
                PDF_Decrypt(filepath,password)
                print('')


# Ecrypt PDFs: 
# dirName = '/home/ross/All Things Python/ATBS/PracticeProjects/PDFparanoia/'
# os.chdir(dirName)
# print('Encrypting all PDF files in the following directory:\n{}'.format(dirName))
# password = input('\nPlease enter a password to encrypt PDF files with: ')
# OS_Walk_Encrypt(password)


# Decrypt encrypted PDFs: 
# dirName = '/home/ross/All Things Python/ATBS/PracticeProjects/PDFparanoia/'
# os.chdir(dirName)
# print('Decrypting all PDF files in the following directory:\n{}'.format(dirName))
# password = input('\nPlease enter password for encrypted PDF files: ')
# OS_Walk_Decrypt(password)