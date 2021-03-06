import csv

#---------------------------------------------------------------------
#5. Output the average
with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    sales = []

    for row in spreadsheet:
        sales_list = row['sales']
        sales.append(sales_list)

total_sales = 0
for sale in sales:
    total_sales += int(sale)
print('Sale average: {}'.format((total_sales) / 12))

#---------------------------------------------------------------------
#6. Output total sales for summer

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    summer_sales = []

    for row in spreadsheet:
        summer_months = row['sales']
        summer_sales.append(summer_months)

total_summer_sales = 0
for summer_sale in summer_sales:
    total_summer_sales = (int(summer_sales[5])) + (int(summer_sales[6])) + (int(summer_sales[7]))

print('Total summer sales: {}'.format(total_summer_sales))

#---------------------------------------------------------------------
#7. Output total sales for winter

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    winter_sales = []

    for row in spreadsheet:
        winter_months = row['sales']
        winter_sales.append(winter_months)

total_winter_sales = 0
for winter_sale in winter_sales:
    total_winter_sales = (int(winter_sales[11])) + (int(winter_sales[2])) + (int(winter_sales[3]))

print('Total winter sales: {}'.format(total_winter_sales))

#---------------------------------------------------------------------
#8. Months with the highest and lowest sales
with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    highest_sale = []
    for row in spreadsheet:
        find_sale_max = row['sales']
        highest_sale.append(find_sale_max)

find_highest_sale = max(highest_sale)
print('Highest sale: {}'.format(find_highest_sale))

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    lowest_sale = []
    for row in spreadsheet:
        find_sale_min = row['sales']
        lowest_sale.append(find_sale_min)

find_lowest_sale = min(lowest_sale)
print('Lowest sale: {}'.format(find_lowest_sale))

