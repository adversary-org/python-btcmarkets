#!/usr/bin/env python3

import requests
import time
import hashlib
import hmac
import base64

from config import apikey_secret
from config import apikey_public
from config import domain
uri = "/account/balance"
url = domain + uri
askey = apikey_secret.encode("utf-8")
apkey = apikey_public.encode("utf-8")
skey = base64.standard_b64decode(askey)
pkey = base64.standard_b64decode(apkey)

# Optional timestamping method, not recommended as ticker results may
# be cached beyond the authentication window.
#
#urt = "/market/BTC/AUD/tick"
#turl = domain + urt
#rt = requests.get(turl, verify=True)
#tstamp = r.json()["timestamp"]
#ctstamp = tstamp * 1000

tstamp = time.time()
ctstamp = int(tstamp * 1000)  # or int(tstamp * 1000) or round(tstamp * 1000)
sctstamp = str(ctstamp)

sbody = uri + "\n" + sctstamp + "\n"
rbody = sbody.encode("utf-8")

rsig = hmac.new(skey, rbody, hashlib.sha512)
# bsig = base64.standard_b64encode(rsig.digest())
bsig = base64.standard_b64encode(rsig.digest()).decode("utf-8")

headers = { #"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
            "Accept": "application/json",
            "Accept-Charset": "UTF-8",
            "Content-Type": "application/json",
            "apikey": pkey,
            "timestamp": sctstamp,
            "signature": bsig
          }

r = requests.get(url, headers=headers, verify=True)

#audbal = r.json()[0]
#btcbal = r.json()[1]
#ltcbal = r.json()[2]

#print(audbal)
#print(btcbal)
#print(ltcbal)

# Use this output for testing until we succeed with authentication:

print(r.request.headers)
print(r.headers)
print(" ")
print(time.asctime(time.gmtime(tstamp)) + " UTC")
print(time.ctime(tstamp) + " local time")
print(" ")
print(sctstamp)
print(r.content)
print(bsig)
