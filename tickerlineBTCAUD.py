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
# Note, offset only works for positive TZ offsets, use + or - to
# indicate which it is.
offset = str(abs((datetime.datetime.now() - datetime.datetime.utcnow()) / 3600 * 3600))
age = str(datetime.timedelta(seconds=abs(time.time() - tstamp))).split(':')

# This must be changed if TZ is at +1000, +1100, -1100 or -1000 UTC
# and not in Australia (in the first two cases):
if offset == "10:00:00":
    localtz = "AEST"
elif offset == "11:00:00":
    localtz = "AEDT"
else:
    localtz = "local time"

p = "BTCMarkets | BTCAUD | Best bid: {0}, Best ask: {1}, Bid-Ask spread: {2}, last trade: {3} | valid at: {4} UTC | {5} {6} (+{7} UTC) | {8} hours, {9} minutes and {10} seconds ago.".format(bid, ask, spread, last, utime, ltime, localtz, offset, age[0], age[1], age[2])

print(p)
