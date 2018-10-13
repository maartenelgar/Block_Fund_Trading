import sqlite3






def drop_table():
    try:
        con = sqlite3.connect("/Users/maarten/binance.db")
        cursor = con.cursor()
        
        cursor.execute('DROP TABLE BQX/ETH_ask_book;')
    finally:
        con.close()
        exit
    






    



if __name__ == "__main__":


 drop_table()


