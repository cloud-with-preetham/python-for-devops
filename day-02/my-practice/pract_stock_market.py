import requests

api_key = "I6ZGOEU7P5VARH9O"  # Step 1 to add API Key

api_url = "https://www.alphavantage.co/" # Step 2 add url and move the query

symbol = "AMZN"

# print(api_url + query)

def get_stock_market_data(symbol):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    responses = requests.get(url=api_url + query)
    # print(responses.json())
    for key,value in responses.json().items():
        if is_timeseries:
            print(key,value)
            if key == "Time Series (Daily)":
                continue

symbol = input("Enter the symbol you want for Stock Market API. eg. (AMZN, GOGL, AAPL, IBM): ")
is_timeseries = True
get_stock_market_data(symbol)
