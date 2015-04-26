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

if int(age[0]) == 0 and int(age[1]) == 0:
    secs = str(float(age[2]))
    since = "{0} seconds ago.".format(secs)
elif int(age[0]) == 0 and int(age[1]) > 0:
    mins = str(int(age[1]))
    secs = str(float(age[2]))
    since = "{0} minutes and {1} seconds ago.".format(mins, secs)
elif int(age[0]) > 0 and int(age[1]) > 0:
    hours = str(int(age[0]))
    mins = str(int(age[1]))
    secs = str(float(age[2]))
    since = "{0} hours, {1} minutes and {2} seconds ago.".format(hours, mins, secs)
else:
    hours = str(int(age[0]))
    mins = str(int(age[1]))
    secs = str(float(age[2]))
    since = "{0} hours, {1} minutes and {2} seconds ago.".format(hours, mins, secs)

# This must be changed if TZ is at +1000, +1100, -1100 or -1000 UTC
# and not in Australia (in the first two cases):
if offset == "10:00:00":
    localtz = "AEST"
elif offset == "11:00:00":
    localtz = "AEDT"
else:
    localtz = "local time"

if len(offset) == 8:
    # oset = "".join(offset[0:5].split(":"))  # correct format
    oset = offset[0:5]  # easy to read format
elif len(offset) == 7:
    # oset = "".join(offset[0:4].split(":"))  # correct format
    oset = offset[0:4]  # easy to read format
else:
    oset = offset

p = "BTCMarkets BTCAUD | Best bid: {0}, Best ask: {1}, Bid-Ask spread: {2}, last trade: {3} | valid at: {4} UTC | {5} {6} (+{7} UTC) | {8}".format(bid, ask, spread, last, utime, ltime, localtz, oset, since)

print(p)
