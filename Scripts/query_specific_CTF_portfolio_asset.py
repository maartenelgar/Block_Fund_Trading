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


def run__query_specific_CTF_portfolio_asset():
    asset = input("Asset information to be requested")
    type(asset)
    CTF_asset_information = client.get_asset_balance(asset)
    print (CTF_asset_information)
    return CTF_asset_information






if __name__ == "__main__":
    run__query_specific_CTF_portfolio_asset()
