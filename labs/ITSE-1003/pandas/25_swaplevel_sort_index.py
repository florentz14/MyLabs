import pandas as pd


ser = pd.Series(
    [10, 20, 30, 40],
    index=[
        ["A", "A", "B", "B"],
        ["one", "two", "one", "two"],
    ],
)

print("Original MultiIndex Series:")
print(ser)
print()

print("swaplevel():")
print(ser.swaplevel())
print()

print("swaplevel().sort_index():")
print(ser.swaplevel().sort_index())
