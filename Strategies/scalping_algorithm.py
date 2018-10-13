from binance.client import Client
import time
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
from BinanceKeys import BinanceKey1
import math


api_key = BinanceKey1['OfBLqIoRvQCloLCSc5lmrN5ikapHhDul27yn6TrsM5X7l0dkw64ME0ESkEkBatNL']
api_secret = BinanceKey1['9Jwb6sR6z8N4jWlK9n0bZrHAeipA8FaYibl5VFnBoE0t3CmnY1CyVWKCekOmpg2r']

client = Client(api_key, api_secret)

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')

coin = []
   #weighted Asymmetrical Logarithmic Error (ALE)
    #for 20 days thus N = 20

class Strategy_Statistics(object):

    def __init__(self):
        self.GMLE = GMLE



def scalping_run():
    



def 20_day_geometric_mean_estimator():
    #for 20 days thus N = 20
    #we need to add appropriate len functions and change the sql table to day
    try:
        con = sqlite3.connect("/Users/maarten/binance.db")
        cursor = con.cursor()
        
        cursor.execute('SELECT Volume from historical_market_data ORDER BY Volume DESC LIMIT 20;')  
        recent_N_volume = cursor.fetchall()
        recent_N_volume = list(recent_N_volume)
        recent_N_volume = [i for (i,) in recent_N_volume]
        #we need to create a volume function
        N = 20
        log_volume20_list = []

        for values in recent_N_volume:
            log_volume20 = math.log1p(values)
            log_volume20_list.append(log_volume20)

        summation_log_volume = sum(log_volume20_list)
        q = summation_log_volume
        MLV = q / N
        GMLV = math.exp(MLV)
        print(GMLE)

    finally:
        con.close()
        exit
    return GMLE
       


def projected_yield_stats():
    try:
        con = sqlite3.connect("/Users/maarten/binance.db")
        cursor = con.cursor()
        
        cursor.execute('SELECT askprices, askvolumes FROM ask_book WHERE  askprices=(SELECT MAX(askprices) FROM ask_book);')

        max_ask_price_info = cursor.fetchone()
        max_ask_price_info = list(max_ask_price_info)
        max_ask_price_info = [float(i) for i in max_ask_price_info]
        print(max_ask_price_info)

        #still need to convert into list / object
    
        cursor.execute('SELECT bidprices, bidvolumes FROM bid_book WHERE bidprices=(SELECT MAX(bidprices) FROM bid_book);')
        max_bid_price_info = cursor.fetchone()
        max_bid_price_info = list(max_bid_price_info)
        max_bid_price_info =  [float(i) for i in max_bid_price_info]
        print(max_bid_price_info)
    finally:
        con.close()
        exit
    return max_ask_price_info, max_bid_price_info


def projected_yield():
    #return a true statement 
    pass
    

def scalping_order_excecutor(coin, wait=1, tot_time=1):

    #Function for placing 'scalp orders'

 
    #Place Orders based on calculated bid-ask orders if projected > 0.05% (transaction fee)
    
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






if __name__ == "__main__":
       daily_volume_estimation()
