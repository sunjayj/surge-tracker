from api_header import client
import json, time

def getsurge(product, start_latitude, start_longitude, end_latitude, end_longitude):
	response = client.get_price_estimates(start_latitude, start_longitude, end_latitude, end_longitude)
	data = response.json
	prices = data.get('prices')

	#print json.dumps(prices,indent=2)

	for i in prices:
		if i['display_name'] == product:
			surge = i['surge_multiplier']

	return surge

#Seattle - Belltown

while True:
	print getsurge('uberX', 47.618417, -122.347950, 47.618034, -122.338940)
	time.sleep(60)