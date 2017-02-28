'''
Created on Mar 28, 2017

@author: Austin Dillinger
'''

import openpyxl as openxl

def getabv(beername):
    """Returns the ABV value in the specificied column for the request beer"""
    ##This is a static fileS
    workbook = openxl.load_workbook("D:\Documents\Brewing.xlsx")
    sheet = workbook.get_sheet_by_name(beername)
    beerabv = round(sheet['b49'].value * 100, 3)
    beerabv = str(beerabv) + "% ABV"
    return beerabv
