import requests
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY':'87a3588f-647b-4b1d-bd0f-a85fb1d80c0e',
}

json = requests.get(url, params=parameters, headers=headers).json()
coins = json["data"]
for x in coins:
  if x['symbol']=='BTC':
    x['quote']['USD']['price']
    print(x['symbol'],x['quote']['USD']['price'])

