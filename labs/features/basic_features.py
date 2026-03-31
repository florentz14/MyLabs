# Basic feature engineering
import pandas as pd

df = pd.DataFrame({'first_name': ['Ana', 'Bob'], 'city': ['Austin', 'Boston']})
df['name_length'] = df['first_name'].str.len()
print(df)
