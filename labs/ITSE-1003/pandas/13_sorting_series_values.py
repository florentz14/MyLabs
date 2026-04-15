# ------------------------------------------------------------ #
# File: 13_sorting_series_values.py
# Date: 2026-04-15
# Author: Florentino
# Description: 13 sorting series values script.
# Explanation: It explains 13 sorting series values script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


ser = pd.Series([5, 0, 3, 8, 4], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

# Old pandas books may show ser.order(); modern equivalent is sort_values().
print("ser.sort_values():")
print(ser.sort_values())
