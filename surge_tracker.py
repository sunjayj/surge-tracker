from api_header import client
import json

def getprice(product, start_latitude, start_longitude, end_latitude, end_longitude):
	response = client.get_price_estimates(start_latitude, start_longitude, end_latitude, end_longitude)
	data = response.json
	prices = data.get('prices')

	print json.dumps(prices,indent=2)

	for i in prices:
		if i['display_name'] == product:
			low_price = i['low_estimate']
			high_price = i['high_estimate']
			surge = i['surge_multiplier']

	return (low_price, high_price, surge)

#Seattle - Belltown
low_price, high_price, surge = getprice('uberX', 47.618417, -122.347950, 47.618034, -122.338940)

#Seattle - Capitol Hill
#low_price, high_price, surge = getprice('uberX',47.615035, -122.322938, 47.618034, -122.338940)