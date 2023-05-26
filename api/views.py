from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
import os

class YourView(APIView):
    def post(self, request):
        data = request.data  # Access the JSON payload from the request body
        print(data)
        stocks = []
        for stock in data['stocks']:
            stocks.append(stock[0])
        stockData = self.getStockData(data['startDate'], stocks)
        #stockTotals = self.calculateStocks(data['initialBalance'], data['stocks'])
            
        return Response(stockData)
    
    def getStockData(self, startDate, stocks):
        params = {
            'access_key': os.environ.get("access_key"),
            'symbols': stocks,
            'date_from': startDate,
        }
        api_result = requests.get('http://api.marketstack.com/v1/eod', params)

        api_response = api_result.json()
        print(json.dumps(api_response, indent=4))
        for stock_data in api_response['data']:
            print(u'Ticker %s has a day high of %s on %s' % (
                stock_data['symbol'],
                stock_data['high'],
                stock_data['date']
            ))
        
        return api_response   

    def calculateStocks(self, total, stocks):
        stockTotals = {}
        # percentage return = (returned amount - initial investment) / initial investment
        for stock in stocks:
            stockName = stock[0]
            stockPercentage = stock[1]
            stockTotals[stockName] = (total * (stockPercentage/100))

        return stockTotals

     