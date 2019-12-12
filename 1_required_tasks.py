#---------------------------------------------------------------------
# 1. Read the data from the spreadsheet

import csv

def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)

        for row in spreadsheet:
            data.append(row)

    return data

print('Sales data: {}'.format(read_data()))

#---------------------------------------------------------------------
# 2. Collect all of the sales from each month into a single list

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    sales = []

    for row in spreadsheet:
        sales_list = row['sales']
        sales.append(sales_list)

print('Sales from each month: {}'.format(sales))

#---------------------------------------------------------------------
# 3. Output the total sales across all months

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    sales = []

    for row in spreadsheet:
        sales_list = row['sales']
        sales.append(sales_list)

total_sales = 0
for sale in sales:
    total_sales += int(sale)

print('Total year sales: {}'.format(total_sales))


