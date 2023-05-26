from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

class YourView(APIView):
    def post(self, request):
        data = request.data  # Access the JSON payload from the request body
        print(data)
        #stockData = self.getStockData(data['startDate'], data['initialBalance'], data['stocks'])
        stockData = self.calculateStocks(data['initialBalance'], data['stocks'])
        
        return Response(stockData)
    def getStockData(self):
        stockData = {}
        
        api_result = requests.get('http://api.marketstack.com/v1/eod', params)

        api_response = api_result.json()
        print(json.dumps(api_response, indent=4))
        for stock_data in api_response['data']:
            print(u'Ticker %s has a day high of %s on %s' % (
                stock_data['symbol'],
                stock_data['high'],
                stock_data['date']
            ))
        
        return stockData   

    def calculateStocks(self, total, stocks):
        stockTotals = {}
        # percentage return = (returned amount - initial investment) / initial investment
        for stock in stocks:
            stockName = stock[0]
            stockPercentage = stock[1]
            stockTotals[stockName] = (total * (stockPercentage/100))

        return stockTotals

     