import os
import operator
import requests
import urllib.parse
import textwrap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime
import time
import mplcursors
import json
import warnings
import pandas as pd
import webbrowser

warnings.filterwarnings("ignore")

STOCK_API_URL = "https://api.twelvedata.com/"
STOCK_API_KEY = "e763a45b79a14e99983d22e08b10331a"
DATE_FORMAT = "%Y-%m-%d"
TODAY = datetime.datetime.today()
STOCK_START_DATE = (TODAY - datetime.timedelta(days=540)).strftime(DATE_FORMAT)
STOCK_END_DATE = (TODAY + datetime.timedelta(days=1)).strftime(DATE_FORMAT)
df = pd.read_csv('ARK_Log.csv')
df = df.drop_duplicates()
df = df.sort_values(by=['date'])

def getStockData(symbol, interval, start, end):
    apiParams = {
        'format':"JSON",
        'symbol':symbol,
        'apikey':STOCK_API_KEY,
        'interval':interval,
        'end_date':end
    }

    if start is not None:
        apiParams['start_date'] = start
    
    apiURL = STOCK_API_URL + "time_series?"
    resp = requests.get(url=apiURL, params=apiParams, verify=False);
    stockResp = resp.json()

    stockClose = []
    stockDate = []
    if stockResp['status'] == 'ok':
        for values in stockResp['values']:
            stockClose.insert(0, float(values['close']))
            stockDate.insert(0, datetime.datetime.strptime(values['datetime'], DATE_FORMAT))

    return  stockClose, stockDate

def drawGraph(symbol, newStock):
    stockValues, stockDate = (getStockData(symbol, "1day", (None if newStock else STOCK_START_DATE), STOCK_END_DATE))
    
    tmpDF = df[df['stock'] == symbol]

    fig, ax, = plt.subplots()
    fig.set_size_inches(17,8)
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    ax.set_xlabel('Time', fontsize=13)
    ax.set_ylabel('Price', fontsize=13)
    ax.set_title(symbol + ' Stock Market', fontsize=20)
    ax.plot_date(stockDate, stockValues, 'r-')

    for index, row in tmpDF.iterrows():
        operation = row['operation']
        annotate_date = datetime.datetime.strptime(row['date'], DATE_FORMAT)
        if annotate_date not in stockDate:
            continue
        index = stockDate.index(annotate_date)
        annotate_value = stockValues[index]
        ax.annotate(operation, (
            annotate_date, annotate_value),
            xytext=(15, 15), 
            textcoords='offset points',
            bbox=dict(boxstyle="round", edgecolor='green' if operation == 'Buy' else 'red', fc="0.8"),
            arrowprops=dict(arrowstyle='-|>'))
     
    fig.autofmt_xdate()
    fmt = mplcursors.cursor(hover=True)
    plt.show()

if __name__ == "__main__":
    while True:
        userInput = input("@:")
        userInput = userInput.split(' ')
        
        if userInput[0] == 'list':
            tmpDf = df[df['operation'] == 'Buy']
            
            if len(userInput) == 2:
                print(tmpDf[tmpDf['date'] == userInput[1]].stock.unique())
            else:
                print(tmpDf.stock.unique())

        elif userInput[0] == 'date':
            print(df.date.unique()[-10:])
        
        elif userInput[0] == 'stock':
            if userInput[1].upper() in df.stock.unique():
                drawGraph(userInput[1].upper(), False)
            else:
                print('Stock not found!')

        elif userInput[0] == 'new':
            if userInput[1].upper() in df.stock.unique():
                drawGraph(userInput[1].upper(), True)
            else:
                print('Stock not found!')
                
        elif userInput[0] == 'web':
            if userInput[1].upper() in df.stock.unique():
                webbrowser.open("https://finance.yahoo.com/quote/" + userInput[1].upper())
            else:
                print('Stock not found!')
            
        elif userInput[0] == 'q':
            break
    
    
    


    
