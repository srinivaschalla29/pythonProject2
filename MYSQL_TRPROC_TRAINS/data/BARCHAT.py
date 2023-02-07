from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference
wb=Workbook()
sheet=wb.active
salesdata=[["products","online","store"],
           [58,86,49],
           [43,57,65],
           [76,68,56],
           [75,66,43],
           ]
for row in salesdata:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("..//data/book.xlsx")