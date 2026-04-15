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
