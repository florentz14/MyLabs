import pandas as pd


io_api_pairs = [
    ("read_csv", "to_csv"),
    ("read_excel", "to_excel"),
    ("read_hdf", "to_hdf"),
    ("read_sql", "to_sql"),
    ("read_json", "to_json"),
    ("read_html", "to_html"),
    ("read_stata", "to_stata"),
    ("read_clipboard", "to_clipboard"),
    ("read_pickle", "to_pickle"),
    ("read_msgpack", "to_msgpack (experimental/legacy)"),
    ("read_gbq", "to_gbq (experimental)"),
]

print("Pandas I/O API: readers <-> writers")
print("-" * 45)
for reader, writer in io_api_pairs:
    print(f"{reader:<18} <-> {writer}")
print("-" * 45)

# Quick check that pandas is available in this environment.
print(f"pandas version: {pd.__version__}")
