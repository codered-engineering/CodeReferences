import numpy as np
import pandas as pd

# saves the wanted columns from a sheet as .txt
def getSheet(filename, sheetname, columns):
        dataframe = pd.read_excel(filename, sheet_name=sheetname)
        # Rename column-Header
        dataframe.set_axis(dataframe.iloc[0].tolist(), axis=1, inplace=True)
        # Delete unnecessary row
        dataframe.drop(index=dataframe.index[1], axis=0, inplace=True)

        # Get only wanted columns, if columns==[] then get all columns
        if columns != []:
           dataframe = dataframe[columns]

        # save as .txt
        np.savetxt(sheetname+'.txt', dataframe.to_numpy(), fmt='%s', delimiter='; ')

# saves the wanted columns from every sheet as .txt
def getAllSheets(filename, columns):
    excel_Sheet_names = pd.ExcelFile(filename).sheet_names
    for name in excel_Sheet_names:
        getSheet(filename, name, columns)

# saves the wanted columns from every sheet as .txt starting with the i-th sheet
def getSomeSheets(filename, columns, startnumber):
    excel_Sheet_names = pd.ExcelFile(filename).sheet_names
    i = startnumber - 1
    while i < len(excel_Sheet_names):
        getSheet(filename, excel_Sheet_names[i], columns)
        i += 1

file = "values.xlsx"
columns = ["Spalte A", "Spalte C"]
getAllSheets(file, columns)
#getSomeSheets(file, columns, 2)

