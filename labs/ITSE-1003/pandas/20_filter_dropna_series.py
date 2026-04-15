import numpy as np
import pandas as pd


ser = pd.Series([0, 1, 2, np.nan, 9], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

print("ser.dropna():")
print(ser.dropna())
print()

print("ser[ser.notnull()]:")
print(ser[ser.notnull()])
