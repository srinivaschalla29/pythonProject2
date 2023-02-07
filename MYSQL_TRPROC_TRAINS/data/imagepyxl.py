from openpyxl import load_workbook
from openpyxl.drawing.image import Image
#let's use the hello_world spreadsheet since it has less data
workbook=load_workbook(filename="..//data/Book1.xlsx")
sheet=workbook.active
logo=Image("..//data/hcl.png")
logo.height =150
logo.width =150
sheet.add_image(logo,"D10")
workbook.save(filename="..//data//Book.xlsx")