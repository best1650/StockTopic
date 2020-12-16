import pandas as pd
import datetime

df = pd.read_excel('ARK.xlsx', index_col=None)

date = []
stock = []
operation = []

for index, row in df.iterrows():
    dateObj = datetime.datetime.strptime(row['Date'], "%m/%d/%Y")
    dateString = dateObj.strftime("%Y-%m-%d")
    ticker = row['Ticker']
    direction = row['Direction']
    
    operation.append(direction)
    date.append(dateString)
    stock.append(ticker)
    
df_1 = pd.DataFrame(data={'date':date, 'stock':stock, 'operation':operation})
df_1.drop_duplicates()
print(df_1)


df_2 = pd.read_csv('ARK_Log.csv', index_col=None)

df_3 = pd.concat([df_1, df_2])

df_3.to_csv('ARK_Log_1.csv', index=False)


