import requests

baseurl = 'https://bittrex.com/api/v1.1/public/'
marketsum = ['getmarketsummary?market=', 'getorderbook?market=', 'getmarkethistory?market=']
coin = ['btc', 'eth']


def btcsummary(altcoin):
    try:
        formlink = baseurl + marketsum[0] + coin[0] + '-' + altcoin
        restapi = requests.get(url=formlink)
        feed = restapi.json()
        result = feed['result'][0]
        change = (float(result['Last']) - float(result['PrevDay'])) / float(result['PrevDay'])
        btclist = result['Last'], change, result['BaseVolume'], result['Volume']
        return list(btclist)

    except TypeError:
        return ['NA', 'NA', 'NA', 'NA']


def ethsummary(altcoin):
    try:
        formlink = baseurl + marketsum[0] + coin[1] + '-' + altcoin
        restapi = requests.get(url=formlink)
        feed = restapi.json()
        result = feed['result'][0]
        change = (float(result['Last']) - float(result['PrevDay'])) / float(result['PrevDay'])
        ethlist = result['Last'], change, result['BaseVolume'], result['Volume']
        return list(ethlist)
    except TypeError:
        return ['NA', 'NA', 'NA', 'NA']

def markethistory(altcoin):
    try:
        formlink = baseurl + marketsum[2] + coin[0] + '-' + altcoin
        restapi = requests.get(url=formlink)
        feed = restapi.json()['result']
        return [tuple(x.values()) for x in feed]

    except TypeError:
        pass
