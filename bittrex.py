import json
import requests
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
monitorcoins = client.open("test")
worksheet = monitorcoins.worksheet('Sheet1')
# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()


# /public/getmarkets
# /public/getcurrencies
# /public/getticker
# /public/getmarketsummaries
# /public/getmarketsummary
# para ?market=eth/btc-coin
# /public/getorderbook
# para ?market=eth/btc-coin&type=both/buy/both
# /public/getmarkethistory
# para ?market=eth/btc-coin

baseurl = 'https://bittrex.com/api/v1.1/public/'
marketsum = ['getmarketsummary?market=','getorderbook?market=','getmarkethistory?market=']


def bittrexfeed(coin, altcoin):
    formlink = baseurl + marketsum[0] + coin + '-' + altcoin
    restapi = requests.get(url = formlink)
    feed = restapi.json()
    return feed['result'][0]


def rowfind(gfeed):
    try:
        start = gfeed.index('R') + len('R')
        end = gfeed.index('C',start)
        return gfeed[start:end]
    except ValueError:
        return ""


def colfind(gfeed):
    try:
        start = gfeed.index('C') + len('C')
        end = gfeed.index(' ',start)
        return gfeed[start:end]
    except ValueError:
        return ""


def marketinfo(coin, altcoin):
    try:
        name = bittrexfeed(str.upper(coin), str.upper(altcoin))['MarketName']
        currentprice = bittrexfeed(coin, altcoin)['Last']
        prevdayprice = bittrexfeed(coin, altcoin)['PrevDay']
        change = (currentprice - prevdayprice) / prevdayprice
        vol = bittrexfeed(coin, altcoin)['Volume']
        basevol = bittrexfeed(coin, altcoin)['BaseVolume']

        # data = [currentprice, change, basevol, vol]

        row = rowfind(str(worksheet.find(name)))
        # label = 'D' + row + ':G' + row
        # cell_list = worksheet.range(str(label))
        # for cell in cell_list:
        #     cell.value = [x for x in data]
        #     print(cell)
        worksheet.update_cell(row, 4, currentprice)
        worksheet.update_cell(row, 5, change)
        worksheet.update_cell(row, 6, basevol)
        worksheet.update_cell(row, 7, vol)
    except TypeError:
        name = str(coin) + "-" + str(altcoin)
        row = rowfind(str(worksheet.find(name)))
        print(name)
        worksheet.update_cell(row, 4, 'Trade Not Found')
    except gspread.exceptions.CellNotFound:
        pass


def scan():
    raw1 = worksheet.col_values(1)
    raw2 = worksheet.col_values(2)
    tar1 = [x for x in raw1 if x != ""]
    tar2 = [x for x in raw2 if x != ""]
    coin = tar1[1:len(tar1)]
    altcoin = tar2[1:len(tar2)]
    return [marketinfo(a, b) for a, b in zip(coin, altcoin)]





