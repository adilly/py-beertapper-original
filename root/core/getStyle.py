'''
Created on Mar 26, 2017

@author: Austin Dillinger
'''

import openpyxl as openxl

def getstyle(beername):
    """Returns the target beer's style."""
    workbook = openxl.load_workbook("D:\Documents\Brewing.xlsx")
    sheet = workbook.get_sheet_by_name(beername)
    style = sheet['b3'].value
    return style
