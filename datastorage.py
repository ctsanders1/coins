import sqlite3
import GoogleSheets as gs
import bittrexAPI as bit
import BTCmarkets as btcmkt



book = gs.Googlespread('C:\\client_secret.json', 'test', 'Sheet1')
conn = sqlite3.connect('coins.db')
c = conn.cursor()


def create_table(name):
    c.execute("CREATE TABLE IF NOT EXISTS " + str(name) + """ (ID INT, TimeStamp TEXT, 
                            Quantity REAL, Price REAL, Total REAL, FillType TEXT, OrderType TEXT, unique (ID))""")


def data_entry(name, x):
    with conn:
        c.execute("INSERT OR IGNORE INTO " + str(name) + " VALUES (?, ?, ?, ?, ?, ?, ?)", x)


def buysell(name):
    with conn:
        c.execute("SELECT count(OrderType) FROM " + str(name) + " WHERE OrderType='SELL'")
        sellrow = [a for a in c.fetchall()]
        c.execute("SELECT count(OrderType) FROM " + str(name) + " WHERE OrderType='BUY'")
        buyrow = [b for b in c.fetchall()]
        print (sellrow, buyrow)

