import requests

API_KEY = "5ORRI6BLX3RVSMGN"  # Step 1 get the API key

API_URL = "https://www.alphavantage.co/"  # Step 2 get the API URL


# print(API_URL + query)


def get_stock_market_data(symbol, is_timeseries):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=API_URL + query)
    for key, value in response.json().items():
        if is_timeseries:
            print(key, value)
        else:
            if key == "Time Series (Daily)":
                continue


symbol = input(
    "Enter the symbol you want for the Stock Market Data eg. (GOGL,AMZN,IBM,AAPL): "
)
is_timeseries = True
get_stock_market_data(symbol, is_timeseries)
