import requests

baseurl = 'https://api.btcmarkets.net/'
marketsum = ['/market/']
coin = ['BTC','ETH']

def btcsummary(altcoin):
    try:
        formlink = baseurl + marketsum[0] + coin[0] + '/' + str.upper(altcoin) + '/tick'
        restapi = requests.get(url=formlink)
        feed = restapi.json()
        result = feed['lastPrice']
        return result
    except TypeError:
        return ['NA', 'NA', 'NA', 'NA']
def ethsummary(altcoin):
    try:
        formlink = baseurl + marketsum[0] + coin[1] + '/' + str.upper(altcoin) + '/tick'
        restapi = requests.get(url=formlink)
        feed = restapi.json()
        result = feed['lastPrice']
        return result
    except TypeError:
        return ['NA', 'NA', 'NA', 'NA']
