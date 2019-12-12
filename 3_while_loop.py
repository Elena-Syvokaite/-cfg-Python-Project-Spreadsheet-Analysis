import csv
#---------------------------------------------------------------------
# Read data

def read_data():
        data = []
        with open ('sales.csv', 'r') as sales_csv:
                spreadsheet = csv.DictReader(sales_csv)
                for row in spreadsheet:
                        data.append(row)
        return data
#---------------------------------------------------------------------
# Total sales

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    sales = []

    for row in spreadsheet:
        sales_list = row['sales']
        sales.append(sales_list)

total_sales = 0
for sale in sales:
    total_sales += int(sale)
#---------------------------------------------------------------------
# Summer sales

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    summer_sales = []

    for row in spreadsheet:
        summer_months = row['sales']
        summer_sales.append(summer_months)

total_summer_sales = 0
for summer_sale in summer_sales:
    total_summer_sales = (int(summer_sales[5])) + (int(summer_sales[6])) + (int(summer_sales[7]))

#---------------------------------------------------------------------
# Winter sales
with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    winter_sales = []

    for row in spreadsheet:
        winter_months = row['sales']
        winter_sales.append(winter_months)

total_winter_sales = 0
for winter_sale in winter_sales:
    total_winter_sales = (int(winter_sales[11])) + (int(winter_sales[2])) + (int(winter_sales[3]))

#---------------------------------------------------------------------
# Higest and lowest sales

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    highest_sale = []
    for row in spreadsheet:
        find_sale_max = row['sales']
        highest_sale.append(find_sale_max)

find_highest_sale = max(highest_sale)

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    lowest_sale = []
    for row in spreadsheet:
        find_sale_min = row['sales']
        lowest_sale.append(find_sale_min)

find_lowest_sale = min(lowest_sale)


while True:
    print('See sales data - 1')
    print('See total year sales - 2')
    print('See sales average - 3')
    print('See total summer sales - 4')
    print('See total winter sales - 5')
    print('See highest sale - 6')
    print('See lowest sale - 7')

    user_input = input('Choose between 1-7')

    if user_input == '1':
        print('Sales data: {}'.format(read_data()))
        break
    elif user_input == '2':
        print('Total year sales: {}'.format(total_sales))
        break
    elif user_input == '3':
        print('Sale average: {}'.format((total_sales) / 12))
        break
    elif user_input == '4':
        print('Total summer sales: {}'.format(total_summer_sales))
        break
    elif user_input == '5':
        print('Total winter sales: {}'.format(total_winter_sales))
        break
    elif user_input == '6':
        print('Highest sale: {}'.format(find_highest_sale))
        break
    elif user_input == '7':
        print('Lowest sale: {}'.format(find_lowest_sale))
        break




