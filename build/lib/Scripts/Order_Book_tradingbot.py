
from binance.client import Client
import time
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
import save_historical_data_Roibal
from BinanceKeys import BinanceKey1
import numpy as np
import pandas as pd



api_key = BinanceKey1['OfBLqIoRvQCloLCSc5lmrN5ikapHhDul27yn6TrsM5X7l0dkw64ME0ESkEkBatNL']
api_secret = BinanceKey1['9Jwb6sR6z8N4jWlK9n0bZrHAeipA8FaYibl5VFnBoE0t3CmnY1CyVWKCekOmpg2r']

client = Client(api_key, api_secret)

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')

sym = 'ETHBTC'

pd.set_option('display.max_row', 1000)

pd.set_option('display.max_columns', 50)

sym = ['ETHBTC']



def ticker_orderbook_information(sym):
    tickers = client.get_orderbook_tickers()
    for tick in tickers:
        if tick['symbol'] in sym:
            best_bid_price = float(tick['bidPrice'])
            best_bid_volume = float(tick['bidQty'])
            best_ask_price = float(tick['askPrice'])
            best_ask_volume = float(tick['askQty'])
            data = {'bidprice': best_bid_price, 'bidqty' : best_bid_volume, 'askprice' : best_ask_price, 'askqty' : best_ask_volume }
            df = pd.DataFrame(data, index=range(0,1)),
            print(df),
            Pa = best_ask_price
            Pb = best_bid_price
            Qa = best_ask_volume
            Qb = best_bid_volume
            midprice = (Pa + Pb) / 2
            print('MidPrice :', midprice)
            microprice = (Qb*Pb + Qa*Pa) / (Qb+Qa)
            print('MicroPrice :', microprice)
    return tick, best_bid_price, best_ask_price, best_bid_volume, best_ask_volume, midprice, microprice

def microprice(sym):
    depth = stream_orders(sym, num_entries=20)
    return depth
        
        
    

def stream_orders(sym, num_entries=20):
    i=0     #Used as a counter for number of entries
    print("Order Book: ", convert_time_binance(client.get_server_time()))
    depth = client.get_order_book(symbol=sym)
    time.sleep(5)
    print('/n ASK Orders')
    for ask in depth['asks']:
        print(ask)
    print('/n BID Orders')
    for bid in depth['bids']:
        print(bid)
    return bid, ask



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


def market_depth(sym, num_entries=20):
    #Get market depth
    #Retrieve and format market depth (order book) including time-stamp
    i=0     #Used as a counter for number of entries
    print("Order Book: ", convert_time_binance(client.get_server_time()))
    depth = client.get_order_book(symbol=sym)
    print(depth)
    print(depth['asks'][0])
    ask_tot=0.0
    ask_price =[]
    ask_quantity = []
    bid_price = []
    bid_quantity = []
    bid_tot = 0.0
    place_order_ask_price = 0
    place_order_bid_price = 0
    max_order_ask = 0
    max_order_bid = 0
    print("\n", sym, "\nDepth     ASKS:\n")
    print("Price     Amount")
    for ask in depth['asks']:
        if i<num_entries:
            if float(ask[1])>float(max_order_ask):
                #Determine Price to place ask order based on highest volume
                max_order_ask=ask[1]
                place_order_ask_price=round(float(ask[0]),5)-0.0001
            #ask_list.append([ask[0], ask[1]])
            ask_price.append(float(ask[0]))
            ask_tot+=float(ask[1])
            ask_quantity.append(ask_tot)
            #print(ask)
            i+=1
    j=0     #Secondary Counter for Bids
    print("\n", sym, "\nDepth     BIDS:\n")
    print("Price     Amount")
    for bid in depth['bids']:
        if j<num_entries:
            if float(bid[1])>float(max_order_bid):
                #Determine Price to place ask order based on highest volume
                max_order_bid=bid[1]
                place_order_bid_price=round(float(bid[0]),5)+0.0001
            bid_price.append(float(bid[0]))
            bid_tot += float(bid[1])
            bid_quantity.append(bid_tot)
            #print(bid)
            j+=1
    return ask_price, ask_quantity, bid_price, bid_quantity, place_order_ask_price, place_order_bid_price

def scalping_orders(coin, wait=1, tot_time=1):
    #Function for placing 'scalp orders'
    #Calls on Visualizing Scalping Orders Function
    ap, aq, bp, bq, place_ask_order, place_bid_order, spread, proj_spread, max_bid, min_ask = visualize_market_depth(wait, tot_time, coin)
    print("Coin: {}\nPrice to Place Ask Order: {}\nPrice to place Bid Order: {}".format(coin, place_ask_order, place_bid_order))
    print("Spread: {} % Projected Spread {} %".format(spread, proj_spread))
    print("Max Bid: {} Min Ask: {}".format(max_bid, min_ask))
    #Place Orders based on calculated bid-ask orders if projected > 0.05% (transaction fee)
    #Documentation: http://python-binance.readthedocs.io/en/latest/account.html#orders
    """
    if proj_spread > 0.05:
        quant1=100          #Determine Code Required to calculate 'minimum' quantity
        #Place Bid Order:
        bid_order1 = client.order_limit_buy(
            symbol=coin,
            quantity=quant1,
            price=place_bid_order)
        #Place Ask Order
        ask_order1 = client.order_limit_sell(
            symbol=coin,
            quantity=quant1,
            price=place_ask_order)


    #Place second order if current spread > 0.05% (transaction fee)

    """


def visualize_market_depth(wait_time_sec='1', tot_time='1', sym='ICXBNB', precision=5):
    cycles = int(tot_time)/int(wait_time_sec)
    start_time = time.asctime()
    fig, ax = plt.subplots()
    for i in range(1,int(cycles)+1):
        ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order = market_depth(sym)

        #print(ask_price)
        plt.plot(ask_pri, ask_quan, color = 'red', label='asks-cycle: {}'.format(i))
        plt.plot(bid_pri, bid_quan, color = 'blue', label = 'bids-cycle: {}'.format(i))

        #ax.plot(depth['bids'][0], depth['bids'][1])
        max_bid = max(bid_pri)
        min_ask = min(ask_pri)
        max_quant = max(ask_quan[-1], bid_quan[-1])
        spread = round(((min_ask-max_bid)/min_ask)*100,5)   #Spread based on market
        proj_order_spread = round(((ask_order-bid_order)/ask_order)*100, precision)
        price=round(((max_bid+min_ask)/2), precision)
        plt.plot([price, price],[0, max_quant], color = 'green', label = 'Price - Cycle: {}'.format(i)) #Vertical Line for Price
        plt.plot([ask_order, ask_order],[0, max_quant], color = 'black', label = 'Ask - Cycle: {}'.format(i))
        plt.plot([bid_order, bid_order],[0, max_quant], color = 'black', label = 'Buy - Cycle: {}'.format(i))
        #plt.plot([min_ask, min_ask],[0, max_quant], color = 'grey', label = 'Min Ask - Cycle: {}'.format(i))
        #plt.plot([max_bid, max_bid],[0, max_quant], color = 'grey', label = 'Max Buy - Cycle: {}'.format(i))
        ax.annotate("Max Bid: {} \nMin Ask: {}\nSpread: {} %\nCycle: {}\nPrice: {}"
                    "\nPlace Bid: {} \nPlace Ask: {}\n Projected Spread: {} %".format(max_bid, min_ask, spread, i, price, bid_order, ask_order, proj_order_spread),
                    xy=(max_bid, ask_quan[-1]), xytext=(max_bid, ask_quan[0]))
        if i==(cycles+1):
            break
        else:
            time.sleep(int(wait_time_sec))
    #end_time = time.asctime()
    ax.set(xlabel='Price', ylabel='Quantity',
       title='Binance Order Book: {} \n {}\n Cycle Time: {} seconds - Num Cycles: {}'.format(sym, start_time, wait_time_sec, cycles))
    plt.legend()
    plt.show()
    return ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order, spread, proj_order_spread, max_bid, min_ask


def coin_prices(watch_list):
    #Will print to screen, prices of coins on 'watch list'
    #returns all prices
    prices = client.get_all_tickers()
    print("\nSelected (watch list) Ticker Prices: ")
    for price in prices:
        if price['symbol'] in watch_list:
            print(price)
    return prices


def coin_tickers(watch_list):
    # Prints to screen tickers for 'watch list' coins
    # Returns list of all price tickers
    tickers = client.get_orderbook_tickers()
    print("\nWatch List Order Tickers: \n")
    for tick in tickers:
        if tick['symbol'] in watch_list:
            print(tick)
    return tickers

def portfolio_management(deposit = '10000', withdraw=0, portfolio_amt = '0', portfolio_type='USDT', test_acct='True'):
    """The Portfolio Management Function will be used to track profit/loss of Portfolio in Any Particular Currency (Default: USDT)"""
    #Maintain Portfolio Statistics (Total Profit/Loss) in a file
    pass

def Bollinger_Bands():
    #This Function will calculate Bollinger Bands for Given Time Period
    #EDIT: Will use Crypto-Signal for this functionality
    #https://github.com/CryptoSignal/crypto-signal
    pass

def buy_sell_bot():
    pass

def position_sizing():
    pass

def trailing_stop_loss():
    pass







#Place Limit Order
"""
order = client.order_limit_buy(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')

order = client.order_limit_sell(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')
"""




"""
#trade aggregator (generator)
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')
# iterate over the trade iterator
for trade in agg_trades:
    pass
    #print(trade)
    # do something with the trade data

# convert the iterator to a list
# note: generators can only be iterated over once so we need to call it again
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')
agg_trade_list = list(agg_trades)

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
#for kline in klines:
    #print(kline)
"""

#place an order on Binance
"""
order = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')
"""

if __name__ == "__main__":
        ticker_orderbook_information(sym)
