import sqlalchemy as db
from sqlalchemy import create_engine, func, select, MetaData
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def select_spread_volume(conn):
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM ETH/BTC_spread;')
 
    rows = cur.fetchall()
 
    print(rows)
    
    
                 

def main():

    database = "/Users/maarten/binance.db"

    conn = create_connection(database)
    with conn:
        select_spread_volume(conn)

    





if __name__ == "__main__":

   main()

