import os

import openpyxl


def change_directory():
    path = "/Users/Maitrey/Documents"
    print(os.getcwd())
    change_path = os.chdir(path)
    lists = os.listdir(path)
    print(os.getcwd())
    print(lists)


change_directory()
excelFile = "Bashers_Batting.xlsx"
wb = openpyxl.load_workbook(excelFile)
sheet = wb.get_sheet_by_name('Sheet1')
sheetValue = sheet.columns[8]

for values in sheetValue:
    try:
        print(values.value)
    except:
        pass
