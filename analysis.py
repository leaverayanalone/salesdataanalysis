#----------------------------------------------------
# ASSIGNMENT 1
# Date of Submission: 16th February, 2024
#
# Author: Rayan Ahmed
# Collaborators/references:
#----------------------------------------------------

from datetime import datetime

def read_csvFile(filename):
    """Reads a CSV file and returns its contents as a list of lists."""
    data = []
    with open(filename, "r") as f:
        next(f)
        for dt in f:
            data.append(dt.strip().split(','))
    return data

def writeFile(filename, data):
    """Writes data to a file."""
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def sales_data():
    """Processes sales data and returns it as a dictionary."""
    sales_data = {}
    data = read_csvFile("transactions_Sales.csv")
    for dt in data:
        sales_data[dt[0]] = tuple(dt[0:5])
    return sales_data

def products_data():
    """Processes products data and returns it as a dictionary."""
    products_data = {}
    data = read_csvFile("transactions_Products.csv")
    for dt in data:
        products_data[dt[0]] = tuple(dt[1:])
    return products_data

def returns_data():
    """Processes returns data and returns it as a dictionary."""
    returns_data = {}
    data = read_csvFile("transactions_Returns.csv")
    for dt in data:
        returns_data[dt[0]] = dt[1]
    return returns_data

def product_sales(sales_data, products_data, returns_data):
    """Processes product sales data and returns it as a dictionary of total quantity, price and discounts."""
    product_sales = {}
    for key, value in sales_data.items():
        transaction_id, date, product_id, quantity, discount = value
        if transaction_id not in returns_data:
            quantity = int(quantity)
            price = float(products_data[product_id][1])
            discount_amount = price * float(discount)
            total_amount = (price - discount_amount) * quantity
            if product_id not in product_sales:
                product_sales[product_id] = [quantity, total_amount, [float(discount)], [discount_amount]]
            else:
                product_sales[product_id][0] += quantity
                product_sales[product_id][1] += total_amount
                product_sales[product_id][2].append(float(discount))
                product_sales[product_id][3].append(discount_amount)
    return product_sales

def returns(sales_data, returns_data):
    """Processes sales and return data and returns it as a dictionary."""
    pdt_returns = {}
    for transaction_id, date in returns_data.items():
        product_id = sales_data[transaction_id][2]
        if product_id not in pdt_returns:
            pdt_returns[product_id] = 1
        else:
            pdt_returns[product_id] = pdt_returns[product_id] + 1
    return pdt_returns

def formatting_currency(amt):
    return '{:,.2f}'.format(amt)
def formatting_percentage(pct):
    return '{:0>5.2f}%'.format(pct*100)

def task_1(sales_data, products_data, returns_data):
    """Performs task 1."""
    product_saless = product_sales(sales_data, products_data, returns_data)
    top_units = sorted(product_saless.items(), key=lambda x: x[1][0], reverse=True)[:3]
    print("Question 1: ")
    print("The product that led to the larger number of sales in units: ")
    for product_id, dt in top_units:
        product_name = products_data[product_id][0]
        quantity_sold = dt[0]
        print(f"{product_name:>20} {quantity_sold:>3}")

def task_2(sales_data, products_data, returns_data):
    """Performs task 2."""
    product_saless = product_sales(sales_data, products_data, returns_data)
    top_sold = sorted(product_saless.items(), key=lambda x: x[1][1], reverse=True)[:3]
    print("\nQuestion 2: ")
    print("The product that led to the larger number of sales in dollars: ")
    for product_id, dt in top_sold:
        product_name = products_data[product_id][0]
        amount_sold = dt[1]
        print(f"{product_name:>20} {formatting_currency(amount_sold):>10}")
        
def task_3(sales_data, products_data, returns_data):
    """Performs task 3."""
    product_saless = product_sales(sales_data, products_data, returns_data)
    product_salesss = sorted(product_saless.items(), key=lambda x: x[1][1],reverse=True)
    turnovr = 0
    print("\nQuestion 3:")
    print("+---+--------------------+---+-----------+------+-----------+")
    print("|ID |      Product       |Qty|   Amount  | Disc | Disc Amt  |")
    print("+---+--------------------+---+-----------+------+-----------+") 
    for product_id, dt in product_salesss:
        product_name = products_data[product_id][0]
        total_units = dt[0]
        total_amount = dt[1]
        average_disc = (sum(dt[2])/len(dt[2]))
        total_disc = dt[1] - dt[1] * (1 - average_disc)
        print(f"|{product_id:3}|{product_name:^20}|{total_units:3}|${formatting_currency(total_amount):>10}|{formatting_percentage(average_disc):5}|${formatting_currency(total_disc):>10}|")
        turnovr += total_amount
    print("+---+--------------------+---+-----------+------+-----------+")
    print(f"Total Turnover: {formatting_currency(turnovr)}")    
 
def task_4(sales_data):
    """Performs task 4."""
    weekly_sales = {}
    for transaction_id, dt in sales_data.items():
        date = dt[1]
        date = datetime.strptime(date, "%Y-%m-%d")
        dig = date.weekday()
        if dig<5:
            weekday = {
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
            }.get(dig+1) 
            
            if weekday not in weekly_sales:
                weekly_sales[weekday] = 1
            else:
                weekly_sales[weekday] += 1
    print("\nQuestion 4: ")
    print("The number of transactions per weekday: ")
    for weekday, dt in weekly_sales.items():
        print(f"{weekday:9}:{dt:3}")

def task_5(sales_data, products_data, returns_data):
    """Performs task 5."""
    pdt_returns = returns(sales_data, returns_data)
    print("\nQuestion 5: ")
    print("A list of all the products and the number of times they were returned")
    for product_id, dt in pdt_returns.items():
        if product_id in products_data.keys():
            product_name = products_data[product_id][0]
            print(f"{product_id:3} {product_name:<20} {dt:>3}")
        
def task_6(sales_data, products_data, returns_data):
    """Performs task 6."""
    product_saless = product_sales(sales_data, products_data, returns_data)
    information = []
    information_s = []
    for product_id, dt in product_saless.items():
        infos = (product_id, str(dt[0]))
        information.append(infos)
    for data in information:
        data_s = ",".join(data)
        information_s.append(data_s)
    writeFile("transactions_units.txt", information_s)
    
def main():
    sales_datas = sales_data()
    products_datas = products_data()
    returns_datas = returns_data()
    
    task_1(sales_datas, products_datas, returns_datas)
    task_2(sales_datas, products_datas, returns_datas)
    task_3(sales_datas, products_datas, returns_datas)
    task_4(sales_datas)
    task_5(sales_datas, products_datas, returns_datas)
    task_6(sales_datas, products_datas, returns_datas)
    
if __name__ == '__main__':
    main()