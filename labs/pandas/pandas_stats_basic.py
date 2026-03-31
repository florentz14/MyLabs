# Basic pandas statistics example
import pandas as pd

from settings import EXCEL_PATH


df = pd.read_csv(EXCEL_PATH / "people.csv")

print("Mean age:", round(df["age"].mean(), 2))
print("Median salary:", round(df["salary"].median(), 2))
print("Department counts:")
print(df["department"].value_counts().head())
