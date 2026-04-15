# ------------------------------------------------------------ #
# File: 06_arithmetic_data_alignment.py
# Date: 2026-04-15
# Author: Florentino
# Description: 06 arithmetic data alignment script.
# Explanation: It explains 06 arithmetic data alignment script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


# Arithmetic methods align labels automatically.
s1 = pd.Series([2, 5, 7, 4], index=["one", "two", "three", "four"])
s2 = pd.Series([1, 3, 2, 8], index=["three", "four", "five", "one"])

print("Series s1:")
print(s1)
print()

print("Series s2:")
print(s2)
print()

print("s1.add(s2):")
print(s1.add(s2))
print()

print("s1.sub(s2):")
print(s1.sub(s2))
print()

print("s1.mul(s2):")
print(s1.mul(s2))
print()

print("s1.div(s2):")
print(s1.div(s2))
print()

print("s1.add(s2, fill_value=0):")
print(s1.add(s2, fill_value=0))
print()

df1 = pd.DataFrame(
    {"A": [1, 2], "B": [3, 4]},
    index=["row1", "row2"],
)
df2 = pd.DataFrame(
    {"B": [10, 20], "C": [30, 40]},
    index=["row2", "row3"],
)

print("DataFrame df1:")
print(df1)
print()

print("DataFrame df2:")
print(df2)
print()

print("df1.add(df2):")
print(df1.add(df2))
print()

print("df1.sub(df2, fill_value=0):")
print(df1.sub(df2, fill_value=0))
