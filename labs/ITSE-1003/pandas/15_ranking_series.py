# ------------------------------------------------------------ #
# File: 15_ranking_series.py
# Date: 2026-04-15
# Author: Florentino
# Description: 15 ranking series script.
# Explanation: It explains 15 ranking series script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


ser = pd.Series([5, 0, 3, 8, 4], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

print("ser.rank():")
print(ser.rank())
print()

print("ser.rank(method='first'):")
print(ser.rank(method="first"))
print()

print("ser.rank(ascending=False):")
print(ser.rank(ascending=False))
