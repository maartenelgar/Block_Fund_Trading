import sqlite3


sqlite_file = '/Users/maarten/binance.sqlite'


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

