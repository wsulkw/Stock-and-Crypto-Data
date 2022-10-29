import json
import requests


def pull_crypto_price(c):
    try:
        return round(float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={c}USDT").json()["price"]), 2)
    except KeyError:
        return None

print(pull_crypto_price(input("Crypto symbol: ")))