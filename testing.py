import GoogleSheets as gs
import bittrexAPI as bit
import BTCmarkets as btcmkt
import datastorage as db
import sqlite3

### GoogleSheet data placement
book = gs.Googlespread('C:\\client_secret.json', 'test', 'Sheet1')
btccellrange ='C3:F' + str(book.maxrow())
ethcellrange ='G3:J' + str(book.maxrow())
btcfiatcellrange = "C1"
ethfiatcellrange = "G1"

### Data Sets
btcdata = []
ethdata = []

### Instances

### Forming list to update table
for a in book.searchcoin():
    for x in bit.ethsummary(a):
        ethdata.append(x)

for a in book.searchcoin():
    db.create_table(a)
    for x in bit.btcsummary(a):
        btcdata.append(x)
    for y in bit.markethistory(a):
        db.data_entry(a, y)

### Uploading to Google Sheets
book.batchupdate(btcfiatcellrange, [btcmkt.btcsummary('aud')])
book.batchupdate(ethfiatcellrange, [btcmkt.ethsummary('aud')])
book.batchupdate(btccellrange, btcdata)
book.batchupdate(ethcellrange, ethdata)
