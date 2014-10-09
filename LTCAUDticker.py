#!/usr/bin/env python3

import requests
import time

from config import domain
uri = "/market/LTC/AUD/tick"
url = domain + uri

r = requests.get(url, verify=True)

ask = str(r.json()["bestAsk"])
bid = str(r.json()["bestBid"])
last = str(r.json()["lastPrice"])
tstamp = r.json()["timestamp"]
ltime = time.ctime(tstamp)
utime = time.asctime(time.gmtime(tstamp))

p = """
    BTC Markets most recent LTC trade data:

    Best ask price (buy at):   {0} AUD
    Best bid price (sell at):  {1} AUD

    Last trade price:  {2} AUD

    Accurate at:

    {3} (local time)
    {4} UTC

    Source:  {5}
    
    """.format(ask, bid, last, ltime, utime, r.url)

print(p)
