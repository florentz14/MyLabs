from pathlib import Path

import pandas as pd


out_dir = Path(__file__).parent / "output_io"
out_dir.mkdir(exist_ok=True)

df = pd.DataFrame(
    {
        "product": ["ball", "pen", "pencil"],
        "price": [1.2, 1.0, 0.6],
    }
)

csv_path = out_dir / "products.csv"
json_path = out_dir / "products.json"
pickle_path = out_dir / "products.pkl"

# Writers
df.to_csv(csv_path, index=False)
df.to_json(json_path, orient="records", indent=2)
df.to_pickle(pickle_path)

# Readers
df_csv = pd.read_csv(csv_path)
df_json = pd.read_json(json_path)
df_pickle = pd.read_pickle(pickle_path)

print("Original DataFrame:")
print(df)
print()

print("Loaded with read_csv:")
print(df_csv)
print()

print("Loaded with read_json:")
print(df_json)
print()

print("Loaded with read_pickle:")
print(df_pickle)
