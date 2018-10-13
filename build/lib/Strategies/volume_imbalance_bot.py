import time
from binance.enums import *
import numpy as np
import pandas as pd
from pandas.io import sql
import sqlite3
from binance.client import Client
from BinanceKeys import BinanceKey1


sym = ['ETHBTC']

api_key = BinanceKey1['OfBLqIoRvQCloLCSc5lmrN5ikapHhDul27yn6TrsM5X7l0dkw64ME0ESkEkBatNL']
api_secret = BinanceKey1['9Jwb6sR6z8N4jWlK9n0bZrHAeipA8FaYibl5VFnBoE0t3CmnY1CyVWKCekOmpg2r']

client = Client(api_key, api_secret)


def simple_ticker_orderbook_information(sym):

    server_time = client.get_server_time()
    aa = str(server_time)
    bb = aa.replace("{'serverTime': ","")
    aa = bb.replace("}","")
    timestamp = int(aa)
    tickers = client.get_orderbook_tickers()

    best_bid_price_list =[]
    best_bid_volume_list =[]
    best_ask_price_list =[]
    best_ask_volume_list =[]

    

   
    
    for tick in tickers:
     if tick['symbol'] in sym:
        best_bid_price = float(tick['bidPrice'])
        best_bid_volume = float(tick['bidQty'])
        best_ask_price = float(tick['askPrice'])
        best_ask_volume = float(tick['askQty'])

        best_bid_price_list.append(best_bid_price)
        best_bid_volume_list.append(best_bid_volume)
        best_ask_price_list.append(best_ask_price)
        best_ask_volume_list.append(best_ask_volume)

        Pa = best_ask_price
        Pb = best_bid_price
        Qa = best_ask_volume
        Qb = best_bid_volume
        
        midprice = (Pa + Pb) / 2
        midprice_list = []
        midprice_list.append(midprice)
        microprice = (Qb*Pb + Qa*Pa) / (Qb+Qa)
        microprice_list = []
        microprice_list.append(microprice)
        

        df = pd.DataFrame(dict(timestamp = timestamp, best_bid_price = best_bid_price_list, best_bid_volume = best_bid_volume_list, best_ask_price = best_ask_price_list, best_ask_volume = best_ask_volume_list, midprice = midprice_list, microprice = microprice_list ))
        print(df)
    try:
        con = sqlite3.connect("/Users/maarten/binance.db")
        print('SQLite connection is open')

        df.to_sql("order_book_statistics", con , if_exists = 'append', index = False,)

    finally:
       con.close()
       print('SQLite connection is closed')

    return df




#defining variables


#the exact time the snapshot was taken

update_time = []

#volume is the total transaction volume since market open. There is no open so we set to 00:00 
Volume = []

#turnover is the  quantity  calculated by number of contracts × price × tick value since 00:00

Turnover = []

# the number of contracts traded that create an open position
Open_interest = []

if __name__ == "__main__":


 simple_ticker_orderbook_information(sym)
