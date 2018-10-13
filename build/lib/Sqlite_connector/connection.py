import sqlite3



api_key = BinanceKey1['OfBLqIoRvQCloLCSc5lmrN5ikapHhDul27yn6TrsM5X7l0dkw64ME0ESkEkBatNL']
api_secret = BinanceKey1['9Jwb6sR6z8N4jWlK9n0bZrHAeipA8FaYibl5VFnBoE0t3CmnY1CyVWKCekOmpg2r']

client = Client(api_key, api_secret)

class sqlitedb(object):
    def __init__(self, ):
        self.


    try:
        con = sqlite3.connect("/Users/maarten/binance.db")
        cur = con.cursor()
        df.to_sql("historical_market_data", con , if_exists = 'replace', index = False,)


    finally:
        con.close()
        print('SQLite connection is closed')

            






