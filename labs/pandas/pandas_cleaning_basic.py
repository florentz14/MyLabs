# Basic pandas cleaning example
import pandas as pd

from settings import EXCEL_PATH


df = pd.read_csv(EXCEL_PATH / "hospital_patients_dirty.csv")

# Keep only one row per patient_id and fill simple missing values.
df = df.drop_duplicates(subset=["patient_id"])
df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(0)

print(df[["patient_id", "age", "city"]].head())
