# ------------------------------------------------------------ #
# File: 25_swaplevel_sort_index.py
# Date: 2026-04-15
# Author: Florentino
# Description: 25 swaplevel sort index script.
# Explanation: It explains 25 swaplevel sort index script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


ser = pd.Series(
    [10, 20, 30, 40],
    index=[
        ["A", "A", "B", "B"],
        ["one", "two", "one", "two"],
    ],
)

print("Original MultiIndex Series:")
print(ser)
print()

print("swaplevel():")
print(ser.swaplevel())
print()

print("swaplevel().sort_index():")
print(ser.swaplevel().sort_index())
