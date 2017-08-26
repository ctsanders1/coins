import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials


class Googlespread:

    def __init__(self, keypath, book, sheet):
        self.keypath = keypath
        self.book = book
        self.sheet = sheet
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.keypath, scope)
        client = gspread.authorize(creds)
        monitorcoins = client.open(self.book)
        self.worksheet = monitorcoins.worksheet(self.sheet)

    # def rowfind(gfeed):
    #     try:
    #         start = gfeed.index('R') + len('R')
    #         end = gfeed.index('C',start)
    #         return gfeed[start:end]
    #     except ValueError:
    #         return ""

    def batchupdate(self, cellrange, data):
        cell_list = self.worksheet.range(cellrange)
        for index, item in enumerate(cell_list):
            item.value = data[index]
        self.worksheet.update_cells(cell_list)

    def searchcoin(self):
        raw = self.worksheet.col_values(1)
        tar = [x for x in raw if x != "" and x != 'Coin']
        altcoin = tar[0:len(tar)]
        return altcoin

    def maxrow(self):
        raw = self.worksheet.col_values(1)
        tar = [x for x in raw if x != ""]
        return len(tar) + 1

