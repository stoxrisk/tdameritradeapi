import requests
import os

class TDAmeritradeAPI:
	def __init__(self, api_key):
		self.apikey = apikey

	def getPrices(self, symbol, freqType, freqNum, endDate, startDate, extendedHours=True):
		td_ep = "https://api.tdameritrade.com/v1/marketdata/%s/pricehistory" % symbol
		history_params = {
			'apikey':self.apikey,
			'frequencyType': freqType,
			'frequency': freqNum,
			'endDate': endDate,
			'startDate': startDate,
			'needExtendedHoursData': extendedHours
		}
		response = requests.request(method="GET", url = td_ep, params = history_params)
		return response
