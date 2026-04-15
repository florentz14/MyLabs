import numpy as np
import pandas as pd


ser = pd.Series([0, 1, 2, np.nan, 9], index=["red", "blue", "yellow", "white", "green"])

print("Original series with np.nan:")
print(ser)
print()

ser["white"] = None

print("After ser['white'] = None (still NaN in pandas):")
print(ser)
