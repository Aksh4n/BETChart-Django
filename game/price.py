# Import libraries
import json
import requests

# defining key/request url
key = "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT"

# requesting data from url
data = requests.get(key)
data = data.json()
price = (data["data"]["price"])
