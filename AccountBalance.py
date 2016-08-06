#!/usr/bin/env python3

import requests
import time
import hashlib
import hmac
import base64
import json

from collections import OrderedDict
from config import apikey_secret
from config import apikey_public
from config import domain

# Define Global Vars
uri = "/account/balance"
url = domain + uri
askey = apikey_secret.encode("utf-8")
pkey = apikey_public.encode("utf-8")
skey = base64.standard_b64decode(askey)

def build_headers(URL, PUBKEY, PRIVKEY):
    """Build timestamp, format and encode everything,  and construct string to 
    sign with api key. Use HmacSHA512 algorithm in order to sign.
    
    Lastly build the headers to send... In order to ensure the correct order 
    of key value pairs in the JSON payload, build an ordered dictionary out
    of a list of tuples.
    """
    # Build timestamp
    tstamp = time.time()
    ctstamp = int(tstamp * 1000)  # or int(tstamp * 1000) or round(tstamp * 1000)
    sctstamp = str(ctstamp)
    
    # Optional timestamping method, not recommended as ticker results may
    # be cached beyond the authentication window.
    #
    #urt = "/market/BTC/AUD/tick"
    #turl = domain + urt
    #rt = requests.get(turl, verify=True)
    #tstamp = r.json()["timestamp"]
    #ctstamp = tstamp * 1000

   
    # Build and sign to construct body
    sbody = uri + "\n" + sctstamp + "\n"
    rbody = sbody.encode("utf-8")
    rsig = hmac.new(skey, rbody, hashlib.sha512)
    bsig = base64.standard_b64encode(rsig.digest()).decode("utf-8")
    
    # Construct header list of key value pairs
    headers_list = OrderedDict([("Accept", "application/json"),
                     ("Accept-Charset", "UTF-8"),
                     ("Content-Type", "application/json"),
                     ("apikey", pkey),
                     ("timestamp", sctstamp),
                     ("signature", bsig)])
    # Load list into dictionary
    headers = dict(headers_list)
    
    return headers


def main():
    """ Build the request body by invoking header function with config
    params specified as global variables at top and return the balances for 
    AUD, BTC and LTC. 
    
    TODO: Add in functionality to pass options for the CLI.
    """

    res = build_headers(url, pkey, skey)
    r = requests.get(url, headers=res, verify=True)

    audbal = r.json()[0]
    btcbal = r.json()[1]
    ltcbal = r.json()[2]

    print(audbal)
    print(btcbal)
    print(ltcbal)

if __name__ == "__main__":
    main()
