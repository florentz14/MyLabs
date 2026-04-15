# ------------------------------------------------------------ #
# File: Coffee_sales.py
# Date: 2026-04-15
# Author: Florentino
# Description: Build and print a simple coffee sales DataFrame.
# Explanation: It explains build and print a simple coffee sales dataframe and why it is useful in basic data analysis.
# ------------------------------------------------------------ #


import pandas as pd


my_data = {
    "Type of Coffee": ["Espresso", "Latte", "Cappuccino", "Americano"],
    "Price": [1.50, 2.50, 3.00, 1.00],
    "Quantity": [100, 200, 150, 250],
    "Pounds of Coffee": [10, 20, 15, 25],
    "Total Revenue": [150, 500, 450, 250],
}

df = pd.DataFrame(my_data)

print(df)
