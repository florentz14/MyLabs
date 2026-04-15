# ------------------------------------------------------------ #
# File: 11_sorting_series_index.py
# Date: 2026-04-15
# Author: Florentino
# Description: 11 sorting series index script.
# Explanation: It explains 11 sorting series index script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


ser = pd.Series([5, 0, 3, 8, 4], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

print("ser.sort_index():")
print(ser.sort_index())
print()

print("ser.sort_index(ascending=False):")
print(ser.sort_index(ascending=False))
