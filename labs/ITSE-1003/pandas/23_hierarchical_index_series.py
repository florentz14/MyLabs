import pandas as pd


ser = pd.Series(
    [10, 20, 30, 40, 50, 60],
    index=[
        ["A", "A", "A", "B", "B", "B"],
        ["one", "two", "three", "one", "two", "three"],
    ],
)

print("Hierarchical Series:")
print(ser)
print()

print("Select first level 'A':")
print(ser["A"])
print()

print("Select tuple ('B', 'two'):")
print(ser[("B", "two")])
