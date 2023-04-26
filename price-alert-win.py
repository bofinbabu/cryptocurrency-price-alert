#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import schedule
import time
from plyer import notification

COINGECKO_API = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin&vs_currencies=usd'

ALERT_INTERVAL = 60

def sendmessage(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def get_crypto_prices():
    try:
        r = requests.get(COINGECKO_API).json()
        btc_price = int(float(r['bitcoin']['usd']))
        eth_price = round(float(r['ethereum']['usd']), 1)
        ltc_price = round(float(r['litecoin']['usd']), 2)
        return btc_price, eth_price, ltc_price
    except:
        return '??', '??', '??'

def send_notification():
    btc, eth, ltc = get_crypto_prices()
    message = f'BTC: {btc}  |  ETH: {eth}  |  LTC: {ltc}'
    sendmessage("Crypto Prices", message)

if __name__ == '__main__':
    schedule.every(ALERT_INTERVAL).seconds.do(send_notification)
    while True:
        schedule.run_pending()
        time.sleep(1)
