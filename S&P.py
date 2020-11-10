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

warnings.filterwarnings("ignore")

STOCK_API_URL = "https://api.twelvedata.com/"
STOCK_API_KEY = "e763a45b79a14e99983d22e08b10331a"

def getStockData(symbol, interval, start, end):
    apiParams = {'format':"JSON", 'symbol':symbol,'apikey':STOCK_API_KEY, 'interval':interval, 'start_date':start, 'end_date':end}    
    apiURL = STOCK_API_URL + "time_series?"
    resp = requests.get(url=apiURL, params=apiParams, verify=False);
    stockResp = resp.json()

    stockData = []
    stockVol = []
    if stockResp['status'] == 'ok':
        for values in stockResp['values']:
            stockData.insert(0, float(values['close']))
            stockVol.insert(0, int(values['volume']))

    return  stockData, stockVol

def drawGraph(title, data, vol):
    '''
    fig, ax = plt.subplots(1)
    fig.set_size_inches(15,8)
    
    plt.title(title, fontsize=24)
    plt.xlabel("Time", fontsize=18)
    plt.ylabel("Stock Price", fontsize=18)
    
    ax.plot(list(range(0, len(data))), data, 'r-')
    fmt = mplcursors.cursor(hover=True)

    plt.show()
    '''
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(17,8)

    ax1.plot(list(range(0, len(data))), data, 'r-')
    ax2.set_xlabel('Day')
    ax2.set_ylabel('Price')
    
    ax2.plot(list(range(0, len(vol))), vol, 'g-')
    ax2.set_xlabel('Day')
    ax2.set_ylabel('Volume')
    
    fmt = mplcursors.cursor(hover=True)
    plt.show()
    

    

if __name__ == "__main__":
    # baseSymbol = "SPX"
    # baseData, baseVol = (getStockData(baseSymbol, "1day", "2020-08-10", "2020-11-10"))
    # time.sleep(2)
    
    compareSymbol = "AMD"
    compareData, compareVol = (getStockData(compareSymbol, "1day", "2020-06-10", "2020-11-10"))
    drawGraph(compareSymbol + ' Graph', compareData, compareVol)
    


    
