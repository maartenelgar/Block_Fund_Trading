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


def run_CTF_portfolio_asset_balances():
    CTF_asset_information = client.get_account()
    print (CTF_asset_information)
    return CTF_asset_information






if __name__ == "__main__":
    run_CTF_portfolio_asset_balances()
