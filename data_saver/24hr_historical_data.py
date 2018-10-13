import sqlite3
import time
import dateparser
import pytz
import json


from datetime import datetime
from binance.client import Client
from BinanceKeys import BinanceKey1

import numpy as np
import pandas as pd
from pandas.io import sql


api_key = BinanceKey1['OfBLqIoRvQCloLCSc5lmrN5ikapHhDul27yn6TrsM5X7l0dkw64ME0ESkEkBatNL']
api_secret = BinanceKey1['9Jwb6sR6z8N4jWlK9n0bZrHAeipA8FaYibl5VFnBoE0t3CmnY1CyVWKCekOmpg2r']

client = Client(api_key, api_secret)

symbol = 'ETHBTC'

start = "1 Sep, 2018"

end = "7 Oct, 2018"

interval = Client.KLINE_INTERVAL_1DAY




def get_historical_klines(symbol, interval, start_str, end_str=None):
    """Get Historical Klines from Binance

    See dateparse docs for valid start and end string formats http://dateparser.readthedocs.io/en/latest/

    If using offset strings for dates add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

    :param symbol: Name of symbol pair e.g BNBBTC
    :type symbol: str
    :param interval: Biannce Kline interval
    :type interval: str
    :param start_str: Start date string in UTC format
    :type start_str: str
    :param end_str: optional - end date string in UTC format
    :type end_str: str

    :return: list of OHLCV values

    """
    # create the Binance client, no need for api key
    client = Client("", "")

    # init our list
    output_data = []

    # setup the max limit
    limit = 500

    # convert interval to useful value in seconds
    timeframe = interval_to_milliseconds(interval)

    # convert our date strings to milliseconds
    start_ts = date_to_milliseconds(start_str)

    # if an end time was passed convert it
    end_ts = None
    if end_str:
        end_ts = date_to_milliseconds(end_str)

    idx = 0
    # it can be difficult to know when a symbol was listed on Binance so allow start time to be before list date
    symbol_existed = False
    while True:
        # fetch the klines from start_ts up to max 500 entries or the end_ts if set
        temp_data = client.get_klines(
            symbol=symbol,
            interval=interval,
            limit=limit,
            startTime=start_ts,
            endTime=end_ts
        )

        # handle the case where our start date is before the symbol pair listed on Binance
        if not symbol_existed and len(temp_data):
            symbol_existed = True

        if symbol_existed:
            # append this loops data to our output data
            output_data += temp_data

            # update our start timestamp using the last value in the array and add the interval timeframe
            start_ts = temp_data[len(temp_data) - 1][0] + timeframe
        else:
            # it wasn't listed yet, increment our start date
            start_ts += timeframe

        idx += 1
        # check if we received less than the required limit and exit the loop
        if len(temp_data) < limit:
            # exit the while loop
            break

        # sleep after every 3rd call to be kind to the API
        if idx % 3 == 0:
            time.sleep(1)

    return output_data


def date_to_milliseconds(date_str):
    """Convert UTC date to milliseconds

    If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

    See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/

    :param date_str: date in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
    :type date_str: str
    """
    # get epoch value in UTC
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # parse our date string
    d = dateparser.parse(date_str)
    # if the date is not timezone aware apply UTC timezone
    if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
        d = d.replace(tzinfo=pytz.utc)

    # return the difference in time
    return int((d - epoch).total_seconds() * 1000.0)


def interval_to_milliseconds(interval):
    """Convert a Binance interval string to milliseconds

    :param interval: Binance interval string 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    :type interval: str

    :return:
         None if unit not one of m, h, d or w
         None if string not in correct format
         int value of interval in milliseconds
    """
    ms = None
    seconds_per_unit = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60
    }

    unit = interval[-1]
    if unit in seconds_per_unit:
        try:
            ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
        except ValueError:
            pass
    return ms



def migrate_historic_klines_sqlite(symbol, start, end, interval):
    klines = get_historical_klines(symbol, interval, start, end)
    list_of_open_prices = []
    list_of_close_prices = []
    list_of_high_prices = []
    list_of_low_prices = []
    list_of_volume_prices = []
    list_of_time_prices = []


    three_period_moving_ave = []
    time3=[]
    five_period_moving_ave = []
    ten_period_moving_ave = []
    time10=[]
    for kline in klines:

        time = int(kline[0])
        Open = float(kline[1])
        Low = float(kline[2])
        High = float(kline[3])
        Close = float(kline[4])
        Volume = float(kline[5])

        #track opening prices, use for calculating moving averages
        list_of_open_prices.append(Open)
        list_of_close_prices.append(Close)
        list_of_high_prices.append(High)
        list_of_low_prices.append(Low)
        list_of_volume_prices.append(Volume)
        list_of_time_prices.append(time)

        #Calculate three 'period' moving average - Based on Candlestick duration
        if len(list_of_open_prices)>2:
            price3=0
            for price in list_of_open_prices[-3:]:
                price3+=price
            three_period_moving_ave.append(float(price3/3))
            time3.append(time)
        #Perform Moving Average Calculation for 10 periods
        if len(list_of_open_prices)>9:
            price10=0
            for price in list_of_open_prices[-10:]:
                price10+=price
            ten_period_moving_ave.append(float(price10/10))
            time10.append(time)

    try:
        con = sqlite3.connect("/Users/maarten/binance.db")
        cur = con.cursor()

        column_values_time = pd.Series(list_of_time_prices)
        column_values_open = pd.Series(list_of_open_prices)
        column_values_close = pd.Series(list_of_close_prices)
        column_values_high = pd.Series(list_of_high_prices)
        column_values_low= pd.Series(list_of_low_prices)
        column_values_volume = pd.Series(list_of_volume_prices)

        df = pd.DataFrame(dict(OpenTime = column_values_time, Open = column_values_open, Close = column_values_close, High = column_values_high, Low = column_values_low, Volume = column_values_volume), index = None)

        df.to_sql("historical_market_data", con , if_exists = 'replace', index = False,)


    finally:
        con.close()
        print('SQLite connection is closed')

            








if __name__ == "__main__":
            
    migrate_historic_klines_sqlite(symbol, start, end, interval )
