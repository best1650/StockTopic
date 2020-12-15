import PyPDF2
import pandas as pd
import re

pdfFile = open('ARK_Trades.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
date = []
stock = []
operation = []

for i in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    text = pageObj.extractText().split('\n')
    for line in text:
        if 'Buy' in line:
            stockData = line.split('Buy')
            operation.append('Buy')
            date.append(stockData[0])
            stock.append(stockData[1])
            
        elif 'Sell' in line:
            stockData = line.split('Sell')
            operation.append('Sell')
            date.append(stockData[0])
            stock.append(stockData[1])
            
df = pd.DataFrame(data={'date':date, 'stock':stock, 'operation':operation})
df.to_csv(path_or_buf='./ARK_Log.csv', index=False)

print('Done')
    
