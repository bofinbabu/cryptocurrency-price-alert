#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import requests
import schedule
import time

btc_usd = 'https://api.cryptonator.com/api/full/btc-usd'
eth_usd = 'https://api.cryptonator.com/api/full/eth-usd'
ltc_usd = 'https://api.cryptonator.com/api/full/ltc-usd'

ALERT_INTERVAL = 30

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


def get_btc_usd():
    try:
        r = requests.get(btc_usd).json()
        price = int(float(r['ticker']['price']))
        return unicode(price)
    except:
        return '??'


def get_eth_usd():
    try:
        r = requests.get(eth_usd).json()
        price = round(float(float(r['ticker']['price'])), 1)
        return unicode(price)
    except:
        return '??'


def get_ltc_usd():
    try:
        r = requests.get(ltc_usd).json()
        price = round(float(float(r['ticker']['price'])), 2)
        return unicode(price)
    except:
        return '??'


def send_notification():
    message = 'BTC: '+get_btc_usd()+'  | '+'ETH: '+get_eth_usd()+'  |  '+'LTC: '+get_ltc_usd()
    sendmessage(message)

if __name__ == '__main__':
    schedule.every(ALERT_INTERVAL).minutes.do(send_notification)
    while True:
        schedule.run_pending()
        time.sleep(1)

