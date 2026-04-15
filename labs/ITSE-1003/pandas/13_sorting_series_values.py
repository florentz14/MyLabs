import pandas as pd


ser = pd.Series([5, 0, 3, 8, 4], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

# Old pandas books may show ser.order(); modern equivalent is sort_values().
print("ser.sort_values():")
print(ser.sort_values())
