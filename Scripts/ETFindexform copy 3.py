from binance.client import Client
import time
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
import save_historical_data_Roibal
from BinanceKeys import BinanceKey1

api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

client = Client(api_key, api_secret)

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')

def run_CTF_index():
    list_of_symbols_ETF = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT','BNBBTC', 'ETHBTC', 'LTCBTC']
    #time_horizon = "Short"
    #Risk = "High"
    time.sleep(1)
    print(list_of_symbols_ETF)
    aggregated_index_data_list(list_of_symbols_ETF)

def aggregated_index_data_list(CTF):
    prices = client.get_all_tickers()
    print("\nSelected (CTF) Ticker Prices: ")
    for symbol in prices
    if 
    CTF_index = list( prices )
    print(CTF_index)
    return CTF_index












def convert_time_binance(gt):
    #Converts from Binance Time Format (milliseconds) to time-struct
    #From Binance-Trader Comment Section Code
    #gt = client.get_server_time()
    print("Binance Time: ", gt)
    print(time.localtime())
    aa = str(gt)
    bb = aa.replace("{'serverTime': ","")
    aa = bb.replace("}","")
    gg=int(aa)
    ff=gg-10799260
    uu=ff/1000
    yy=int(uu)
    tt=time.localtime(yy)
    #print(tt)
    return tt


def coin_prices(CTF):
    #Will print to screen, prices of coins on 'watch list'
    #returns all prices
    prices = client.get_all_tickers()
    print("\nSelected (CTF) Ticker Prices: ")
    for price in prices:
        if price['symbol'] in CTF:
            print(price)
    return prices


def coin_tickers(CTF):
    # Prints to screen tickers for 'CTF' coins
    # Returns list of all price tickers
    tickers = client.get_orderbook_tickers()
    print("\nCTF Order Tickers: \n")
    for tick in tickers:
        if tick['symbol'] in CTF:
            print(tick)
    return tickers





if __name__ == "__main__":
    run_CTF_index()

