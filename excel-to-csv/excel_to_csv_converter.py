#! /usr/bin/env python

# ExcelToCSVconverter - A simple program that converts all excel files in working directory to CSV files
# If an excel file has more than 1 sheet, then each sheet will be it's own CSV file

import os, openpyxl, csv, shutil

def xlsx_to_csv(targetDirectory):
    os.chdir(targetDirectory)
    os.makedirs('Converted_Files', exist_ok=True)
    targetDir = 'Converted_Files/'
    print('Converting .xlsx files to .csv in the following directory:\n{}\n\n'.format(targetDirectory))

    try:
        for excelFile in os.listdir('.'):
            # Skip non-xlsx files, load the workbook object
            if excelFile.endswith('xlsx') and '~lock' not in excelFile:
                wb = openpyxl.load_workbook(excelFile)

                # Loop through every sheet in the workbook
                for sheetName in wb.sheetnames:
                    sheet = wb[sheetName] 

                    # Create the CSV filename from the Excel filename and sheet title
                    csvFileName = excelFile[:-5] + '_' + sheetName + '.csv'

                    # Create the csv.writer object for this CSV file
                    with open(csvFileName, 'w') as csvFile:
                        outputWriter = csv.writer(csvFile)

                        rangeData = []
                        for c in sheet.iter_cols(sheet.min_column, sheet.max_column, sheet.min_row, sheet.max_row):
                            columnData = []
                            for r in c:
                                columnData.append(r.value)
                            rangeData.append(columnData)

                        for row in rangeData:
                            outputWriter.writerow(row)

                    # Print conversion message and move CSV to Converted_Files repository
                    print('File converted: \n{}\t==>\t{}\n'.format(excelFile + '_' + sheetName, csvFileName))
                    shutil.move(csvFileName, targetDir)
        print('Conversion operations completed!\nExiting application. Goodbye!')

    except Exception as e:
        print('ERROR!\nError message: {}'.format(e))


# Running the application
# Change directory to excel file dump: 
# path = '/home/ross/AllThingsPython/ATBS/PracticeProjects/ExcelToCSV/ExcelFiles/'
xlsx_to_csv('/home/ross/AllThingsPython/ATBS/PracticeProjects/ExcelToCSV/ExcelFiles/')