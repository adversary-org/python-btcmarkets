#!/usr/bin/env python3

import datetime
import requests
import time

domain = "https://api.btcmarkets.net"
uri = "/market/BTC/AUD/tick"
url = domain + uri

r = requests.get(url, verify=True)

ask = str(r.json()["bestAsk"])
bid = str(r.json()["bestBid"])
last = str(r.json()["lastPrice"])
spread = str(round(r.json()["bestAsk"] - r.json()["bestBid"], 2))
tstamp = r.json()["timestamp"]
ltime = time.ctime(tstamp)
utime = time.asctime(time.gmtime(tstamp))
age = str(datetime.timedelta(seconds=abs(time.time() - tstamp))).split(':')

p = "BTCMarkets | BTCAUD | Best bid: {0}, Best ask: {1}, Bid-Ask spread: {2}, last trade: {3} | valid at: {4} UTC | {5} hours, {6} minutes and {7} seconds ago.".format(bid, ask, spread, last, utime, age[0], age[1], age[2])

print(p)
