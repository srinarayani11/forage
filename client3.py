# client3.py

import server3

def getDataPoint(quote):
    """ Returns the stock name, bid price, ask price, and price (average of bid and ask). """
    stock_name = quote['stock']
    bid_price = quote['top_bid']['price']
    ask_price = quote['top_ask']['price']
    price = (bid_price + ask_price) / 2  # Calculate the average price
    return stock_name, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Returns the ratio of the two stock prices. """
    return price_a / price_b  # Calculate the ratio of stock prices

def main():
    """ Outputs correct stock info, prices, and ratio. """
    quotes = server3.getQuotes()  # Fetch quotes from the server

    for quote in quotes:
        stock_name, bid_price, ask_price, price = getDataPoint(quote)
        print(f"Stock: {stock_name}, Bid Price: {bid_price}, Ask Price: {ask_price}, Price: {price}")

    # Calculate and print the correct ratio of stock prices
    price_a = quotes[0]['top_bid']['price']  # Use bid price for stock A
    price_b = quotes[1]['top_bid']['price']  # Use bid price for stock B
    ratio = getRatio(price_a, price_b)
    print(f"Ratio of stock prices: {ratio}")

if __name__ == "__main__":
    main()
