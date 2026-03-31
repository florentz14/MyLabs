# Basic pandas feature engineering example
import pandas as pd

from settings import EXCEL_PATH


df = pd.read_csv(EXCEL_PATH / "people.csv")

# Two simple derived features.
df["is_senior"] = df["age"] >= 30
df["salary_k"] = df["salary"] / 1000

print(df[["name", "age", "is_senior", "salary_k"]].head())
