'''
Created on Mar 29, 2017

@author: Austin Dillinger
'''

import openpyxl as openxl
#import datetime
#import time

def getbeerdate(beername):
    """Returns the target beer's brew date."""
    workbook = openxl.load_workbook("D:\Documents\Brewing.xlsx")
    sheet = workbook.get_sheet_by_name(beername)
    date = sheet['b1'].value
    date = date.strftime('%m/%d/%Y')
    return date
