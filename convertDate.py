import pandas as pd
from datetime import datetime

df = pd.read_csv('ARK_Log_3.csv', index_col=0)
df = df.drop_duplicates()

print(df)

