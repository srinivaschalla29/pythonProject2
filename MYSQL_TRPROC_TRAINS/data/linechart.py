from openpyxl import Workbook
from openpyxl.chart import PieChart,Reference
wb=Workbook()
sheet=wb.active
salesdata=[["year","sales"],
           [2000,10000],
           [2001,20650],
           [2002,30560],
           [2003,40000],
           [2004,30000],
           [2005,1000]
           ]
for row in salesdata:
    sheet.append(row)
chart=PieChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("..//data/book1.xlsx")