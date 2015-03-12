import base64, hashlib, hmac, urllib2, time, urllib, json

base = 'https://api.btcmarkets.net'

def post_request(key, secret, path, postData):
     
    nowInMilisecond = str(int(time.time() * 1000))
    stringToSign = path + "\n" + nowInMilisecond + "\n" + postData  

    signature = base64.b64encode(hmac.new(secret, stringToSign, digestmod=hashlib.sha512).digest())

    header = {
        'accept': 'application/json', 
        'Content-Type': 'application/json',
        'User-Agent': 'btc markets python client',
        'accept-charset': 'utf-8',  
        'apikey': key,
        'signature': signature,
        'timestamp': nowInMilisecond,
    }

    request = urllib2.Request(base + path, postData, header)
    response = urllib2.urlopen(request, postData)
    return json.load(response)


class BTCMarkets:

    def __init__(self, key, secret):
        self.key = key
        self.secret = base64.b64decode(secret)

    def request(self, path, params={}):

     	postData = '{"currency":"AUD","instrument":"BTC","limit":10,"since":1}'

        result = post_request(self.key, self.secret, path, postData)
        print result
