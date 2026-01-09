# salesdataanalysis
A Python program that analyzes sales, product, and return transaction data from CSV files to generate insights such as top-selling products, total revenue, discounts, returns, and weekday transaction trends.
📌 Overview

This repository contains Assignment 1, a Python program that analyzes sales, product, and return transaction data stored in CSV files.
The script processes the data to generate sales insights such as top-selling products, total revenue, discounts, returns, and weekly transaction trends.

📂 Project Structure
.
├── assignment1.py
├── transactions_Sales.csv
├── transactions_Products.csv
├── transactions_Returns.csv
└── README.md

⚙️ Features

The program performs the following tasks:

Top Products by Units Sold
Identifies the top 3 products with the highest number of units sold.

Top Products by Sales Revenue
Identifies the top 3 products with the highest total sales value.

Detailed Sales Report
Displays:

Total units sold per product

Total sales amount

Average discount

Total discount amount

Overall turnover

Transactions per Weekday
Counts how many transactions occurred on each weekday (Monday–Friday).

Returned Products Summary
Lists all products and the number of times each was returned.

Export Sales Units File
Writes a text file (transactions_units.txt) containing product IDs and total units sold.

🧠 How It Works

Reads CSV files using custom file-handling functions

Stores sales, product, and return data in dictionaries

Excludes returned transactions from sales calculations

Uses Python’s built-in libraries (datetime) for date handling

Outputs results directly to the console and to a text file

▶️ How to Run

Make sure you have Python 3.x installed

Place all CSV files in the same directory as assignment1.py

Run the script:

python assignment1.py

🛠️ Requirements

Python 3.x

No external libraries required

📄 Output

Console output answering all assignment questions

A generated file:

transactions_units.txt

✍️ Author

Rayan Ahmed
