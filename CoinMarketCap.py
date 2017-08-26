import requests
# price_usd
# price_btc
# 24h_volume_usd
# market_cap_usd
# available_supply
# total_supply
# percent_change_1h
# percent_change_24h
# percent_change_7d

baseurl = 'https://api.coinmarketcap.com/v1'
getmethod = ['/ticker/','/global/']

def getglobalcap():
    formlink = baseurl + getmethod[1]
    restapi = requests.get(url=formlink)
    result = restapi.json()
    return result['total_market_cap_usd']

def marketcapsort(min, max):
    formlink = baseurl + getmethod[0]
    restapi = requests.get(url=formlink)
    result = restapi.json()
    for a in result:
        if a['market_cap_usd'] != None and float(a['market_cap_usd']) >= min * 1000000.0 and float(a['market_cap_usd']) <= max * 1000000.0:
            print(a['name'], a['market_cap_usd'])
