from rest_framework.views import APIView
from rest_framework.response import Response

class YourView(APIView):
    def post(self, request):
        data = request.data  # Access the JSON payload from the request body
        print(data)
        #stockData = self.getStockData(data['startDate'], data['initialBalance'], data['stocks'])
        stockData = self.calculateStocks(data['initialBalance'], data['stocks'])
        
        return Response(stockData)
    def getStockData(self):
        stockData = {}
        
        # TODO: Query DB
        
        return stockData   

    def calculateStocks(self, total, stocks):
        stockTotals = {}
        # percentage return = (returned amount - initial investment) / initial investment
        for stock in stocks:
            stockName = stock[0]
            stockPercentage = stock[1]
            stockTotals[stockName] = (total * (stockPercentage/100))

        return stockTotals

     