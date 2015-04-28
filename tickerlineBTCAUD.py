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
# indicate which it is.  The utcdiff value is used to determine the +
# or - later in the script.  Specific TZ names must still be
# specified.
offset = str(abs((datetime.datetime.now() - datetime.datetime.utcnow()) / 3600 * 3600))
utcdiff = round((datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds())
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
    # oset = "".join(offset[0:5].split(":"))  # standard format without colon
    oset = offset[0:5]  # standard format with colon
elif len(offset) == 7:
    # oset = "".join(offset[0:4].split(":"))  # standard format without colon
    oset = "0{0}".format(offset[0:4])  # standard format with colon
else:
    oset = offset

utcdiff = round((datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds())

if utcdiff > 0:
    p = "BTCMarkets BTCAUD | Best bid: {0}, Best ask: {1}, Bid-Ask spread: {2}, last trade: {3} | valid at: {4} UTC | {5} {6} (UTC+{7}) | {8}".format(bid, ask, spread, last, utime, ltime, localtz, oset, since)
elif utcdiff < 0:
    p = "BTCMarkets BTCAUD | Best bid: {0}, Best ask: {1}, Bid-Ask spread: {2}, last trade: {3} | valid at: {4} UTC | {5} {6} (UTC-{7}) | {8}".format(bid, ask, spread, last, utime, ltime, localtz, oset, since)
elif utcdiff == 0:
    p = "BTCMarkets BTCAUD | Best bid: {0}, Best ask: {1}, Bid-Ask spread: {2}, last trade: {3} | valid at: {4} UTC | {8}".format(bid, ask, spread, last, utime, since)
else:
    p = "BTCMarkets BTCAUD | Best bid: {0}, Best ask: {1}, Bid-Ask spread: {2}, last trade: {3} | valid at: {4} UTC | {8}".format(bid, ask, spread, last, utime, since)

print(p)
