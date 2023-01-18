'''Recuperer les donnees dans un excel'''

import openpyxl

path = '/home/thenes/mqtt_raspberry/tests/data.xlsx'


wb = openpyxl.load_workbook(path) #give the full path of the file here
sh = wb.active


c1 = sh['A1']
c2 = sh['B2']
c3 = sh.cell(row=2,column=1)

print("Value of the Cell 1:",c1.value) #ligne 1 colonne 1 dans l'excel
print("Value of the Cell 2:",c2.value)
print("Value of the Cell 3:",c3.value)