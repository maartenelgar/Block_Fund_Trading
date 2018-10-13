import sqlite3
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
from pandas.io import sql





    


def store_historical_trades(symbol, num_entries = 500):


    
    trade_id =[]
    trade_price =[]
    trade_quantity =[]
    trade_timestamp =[]
    trade_maker_status =[]
    trade_best_match_status =[]
    
    


    try:

        con = sqlite3.connect("/Users/maarten/binance.db")
        print('SQLite connection is open')

        df.to_sql("historical_trades", con, if_exists = 'append', index = False,)


    finally:
        con.close()
        print('SQLite connection is closed')

    return df
   
class Position:
    """
    Position main class
    """

    def __init__(self, number, entry_price, size, exit_price, stop_loss):
        self.number = number
        self.type_ = "None"
        self.entry_price = float(entry_price)
        self.size = float(size)
        self.exit_price = float(exit_price)
        self.stop_loss = float(stop_loss)

    def show(self):
        """
        Print position info
        :return:
        """
        print("No. {0}".format(self.number))
        print("Type:   {0}".format(self.type_))
        print("Entry:  {0}".format(self.entry_price))
        print("Size: {0}".format(self.size))
        print("Exit:   {0}".format(self.exit_price))
        print("Stop:   {0}\n".format(self.stop_loss))

    def __str__(self):
        return "{} {}x{}".format(self.type_, self.size, self.entry_price)











