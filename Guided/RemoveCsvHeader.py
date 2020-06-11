#!/usr/bin/env python

# RemoveCsvHeader.py
# Remove header of all CSV files in a directory and re-write file

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue 
    
    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row)
    csvRows    = []
    csvFileObj = open(csvFilename)
    readerObj  = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue   # skip the first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                      newline='')
    csvWriter = csv.writer(csvFileObj)                      
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
