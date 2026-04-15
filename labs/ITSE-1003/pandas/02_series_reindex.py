# ------------------------------------------------------------ #
# File: 02_series_reindex.py
# Date: 2026-04-15
# Author: Florentino
# Description: 02 series reindex script.
# Explanation: It explains 02 series reindex script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


ser = pd.Series([2, 5, 7, 4], index=["one", "two", "three", "four"])
ser = ser.reindex(["three", "four", "five", "one"])

print(ser)
