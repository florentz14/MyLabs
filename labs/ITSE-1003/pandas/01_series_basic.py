# ------------------------------------------------------------ #
# File: 01_series_basic.py
# Date: 2026-04-15
# Author: Florentino
# Description: 01 series basic script.
# Explanation: It explains 01 series basic script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


ser = pd.Series([2, 5, 7, 4], index=["one", "two", "three", "four"])

print("Basic pandas Series:")
print(ser)
