from btcmarkets import BTCMarkets 

client = BTCMarkets('your api key', 'your private key') 

print client.request('/order/trade/history', {})
 
