import pandas as pd

df = pd.read_excel('ARK.xlsx', index_col=None)

date = []
stock = []
operation = []

print(df.head())

'''
for index, row in df.iterrows():
    opText = row['Observation for period']
    if 'Bought' in opText or 'Entered new position' in opText:
        operation.append('Buy')
        date.append('2020-11-25')
        stock.append(row['Ticker'])
    elif 'Sold' in opText or 'Exited position' in opText:
        operation.append('Sell')
        date.append('2020-11-25')
        stock.append(row['Ticker'])

df_1 = pd.DataFrame(data={'date':date, 'stock':stock, 'operation':operation})
df_1.drop_duplicates()

df_2 = pd.read_csv('ARK_Log.csv', index_col=None)

df_3 = pd.concat([df_1, df_2])

df_3.to_csv('ARK_Log_1.csv', index=False)
'''

