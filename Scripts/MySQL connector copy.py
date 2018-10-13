
from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

connection = mysql.connector.connect(host='localhost',
                                     database='BINANCE',
                                     user='root',
                                     password='Eaststreet1', connection_timeout= 180)cursor = cnx.cursor()




DB_NAME = 'BINANCE'


data.to_sql(name='order_book', con=connection, if_exists = 'append', index=False)


cnx = mysql.connector.connect(user='root')
cursor = cnx.cursor()


def create_table():
    

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        connection.database = DB_NAME
    else:
        print(err)
        exit(1)


f

or table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()


