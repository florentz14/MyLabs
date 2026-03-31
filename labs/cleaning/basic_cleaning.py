# Basic pandas cleaning example
import pandas as pd

df = pd.DataFrame({'name': ['Ana', 'Ana', None], 'age': [20, 20, None]})
clean = df.drop_duplicates().fillna({'name': 'Unknown', 'age': 0})
print(clean)
