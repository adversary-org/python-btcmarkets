#!/usr/bin/env python3

import requests
import time
import hashlib
import hmac

from config import apikey_secret
from config import apikey_public
from config import domain
uri = "/account/balance"
url = domain + uri
skey = apikey_secret.encode("utf-8")
pkey = apikey_public.encode("utf-8")

ctstamp = int(time.time() * 1000)
sctstamp = str(ctstamp)
sbody = uri + "\n" + sctstamp + "\n"
rbody = sbody.encode("utf-8")

rsig = hmac.new(skey, rbody, hashlib.sha512)

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
            "Accept": "application/json",
            "Accept-Charset": "UTF-8",
            "Content-Type": "application/json",
            "apikey": pkey,
            "timestamp": sctstamp,
            "signature": rsig.digest()
          }

r = requests.get(url, headers=headers, verify=True)

audbal = r.json()[0]
btcbal = r.json()[1]
ltcbal = r.json()[2]

print(audbal)
print(btcbal)
print(ltcbal)

