import pandas as pd


df = pd.DataFrame(
    {
        "class": ["A", "A", "B", "B"],
        "student": ["Ana", "Luis", "Mia", "Noah"],
        "score": [95, 88, 91, 84],
    }
)

print("Original DataFrame:")
print(df)
print()

df_idx = df.set_index(["class", "student"])
print("set_index(['class', 'student']):")
print(df_idx)
print()

print("reset_index():")
print(df_idx.reset_index())
